import pandas as pd

clusters = pd.read_csv("./results/pca_clusters.csv",index_col=0)

mapping = pd.read_csv("data/sample_ref_data/id_mapping.csv")
clinical = pd.read_csv("./data/processed/clinical_cleaned.csv")


mapping["TCGA_short"] = mapping["TCGA_ID"].str[:12]
clinical["TCGA_short"] = clinical["TCGA_ID"].str[:12]

clusters = clusters.reset_index()

clusters = clusters[["index", "Cluster"]]

clusters.columns = ["UUID", "Cluster"]

print("Clusters:", clusters.shape)
print("Mapping:", mapping.shape)
print("Clinical:", clinical.shape)

df = clusters.merge(mapping, on="UUID")

print("After UUID merge:", df.shape)

df = df.merge(clinical, on="TCGA_short")

print("After clinical merge:", df.shape)

print("\nStage distribution:\n")

print(
    df.groupby("Cluster")["Stage"]
    .value_counts()
)

df.to_csv("data/sample_ref_data//stage_analysis.csv", index=False)

print("\nStage analysis saved")