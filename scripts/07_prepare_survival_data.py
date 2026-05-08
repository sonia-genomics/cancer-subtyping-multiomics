import pandas as pd

clusters = pd.read_csv("./results/pca_clusters.csv", index_col=0)
mapping = pd.read_csv("data/sample_ref_data/id_mapping.csv")
clinical = pd.read_csv("data/sample_ref_data/clinical.tsv", sep="\t", low_memory=False)

print("Files loaded")
clusters_ids = set(clusters.index)
mapping_ids = set(mapping["UUID"])

print("Clusters UUID example:", list(clusters_ids)[:5])
print("Mapping UUID example:", list(mapping_ids)[:5])

print("Common UUIDs:", len(clusters_ids & mapping_ids))
# Prepare clusters
clusters = clusters.reset_index()
clusters = clusters[["index", "Cluster"]]
clusters.columns = ["UUID", "Cluster"]

# Normalize TCGA IDs
mapping["TCGA_ID"] = mapping["TCGA_ID"].str.strip()
clinical["cases.submitter_id"] = clinical["cases.submitter_id"].str.strip()

# Clean clinical
clinical_clean = clinical[[
    "cases.submitter_id",
    "demographic.vital_status",
    "demographic.days_to_death",
    "diagnoses.days_to_last_follow_up",
    "diagnoses.ajcc_pathologic_stage"
]].copy()

clinical_clean.columns = [
    "TCGA_ID",
    "vital_status",
    "days_to_death",
    "days_to_followup",
    "stage"
]

print("Clinical cleaned:", clinical_clean.shape)

# Merge step 1 (UUID)
df = clusters.merge(mapping, on="UUID", how="inner")
print("After UUID merge:", df.shape)

# Merge step 2 (TCGA)
df = df.merge(clinical_clean, on="TCGA_ID", how="inner")
print("After TCGA merge:", df.shape)

# Survival variables
df["time"] = df["days_to_death"].fillna(df["days_to_followup"])
df["event"] = df["vital_status"].map({"Dead": 1, "Alive": 0})

df = df.dropna(subset=["time", "event"])

# Subtype labels
label_map = {
    0: "Basal-like",
    1: "Luminal B",
    2: "Luminal A"
}
df["Subtype"] = df["Cluster"].map(label_map)

df.to_csv("./results/survival_data.csv", index=False)


print("\nFINAL DATASET SAVED")
print("Final shape:", df.shape)
print("\nEvent distribution:")
print(df["event"].value_counts())
print("\nSubtype distribution:")
print(df["Subtype"].value_counts())
print("\nPreview:")
print(df.head())