import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


expr = pd.read_csv(
    "./data/processed/final_expression.csv",
    index_col=0
)

clusters = pd.read_csv(
    "./results/pca_clusters.csv",
    index_col=0
)

# SUBTYPE LABELS
label_map = {
    0: "Basal-like",
    1: "Luminal B",
    2: "Luminal A"
}

clusters["Subtype"] = clusters["Cluster"].map(label_map)

# SELECT IMPORTANT MARKERS
markers = [
    "ESR1",
    "PGR",
    "ERBB2",
    "MKI67",
    "KRT5",
    "EGFR",
    "FOXA1",
    "GATA3",
    "TP53"
]

markers_found = [g for g in markers if g in expr.columns]

print("Markers found:")
print(markers_found)

# COMBINE DATA
heatmap_df = expr[markers_found].copy()

heatmap_df["Subtype"] = clusters["Subtype"]

# subtype averages
heatmap_avg = heatmap_df.groupby("Subtype").mean()

print("\nHeatmap matrix:")
print(heatmap_avg)


# PLOT
plt.figure(figsize=(10,6))

sns.heatmap(
    heatmap_avg,
    cmap="coolwarm",
    annot=True,
    fmt=".2f",
    linewidths=0.5
)

plt.title(
    "Breast Cancer Subtype Marker Expression",
    fontsize=15,
    weight="bold"
)

plt.xlabel("Genes")
plt.ylabel("Subtype")

plt.tight_layout()

plt.savefig(
    "./results/marker_heatmap.png",
    dpi=300,
    bbox_inches="tight"
)

#plt.show()

print("\nPublication heatmap saved")