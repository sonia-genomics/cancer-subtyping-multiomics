import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(
    "./results/pca_clusters.csv",
    index_col=0
)

print(df.head())

# MAP CLUSTERS TO SUBTYPES
label_map = {
    0: "Basal-like",
    1: "Luminal B",
    2: "Luminal A"
}

df["Subtype"] = df["Cluster"].map(label_map)

print("\nSubtype counts:")
print(df["Subtype"].value_counts())

# PLOT
plt.figure(figsize=(10,8))

sns.scatterplot(
    data=df,
    x="PC1",
    y="PC2",
    hue="Subtype",
    s=70,
    alpha=0.8
)

# CENTROIDS
centroids = df.groupby("Subtype")[["PC1","PC2"]].mean()

for subtype, row in centroids.iterrows():

    plt.text(
        row["PC1"],
        row["PC2"],
        subtype,
        fontsize=14,
        weight="bold"
    )

plt.title(
    "PCA-Based Molecular Subtyping of TCGA-BRCA",
    fontsize=16,
    weight="bold"
)

plt.xlabel("Principal Component 1", fontsize=13)
plt.ylabel("Principal Component 2", fontsize=13)

plt.grid(True)

plt.legend(title="Subtype")

plt.tight_layout()

plt.savefig(
    "./results/pca_subtypes.png",
    dpi=300,
    bbox_inches="tight"
)

#plt.show()

print("\n PCA subtype plot saved")