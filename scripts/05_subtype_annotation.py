import pandas as pd
import numpy as np

full_data = pd.read_csv("./data/processed/expression_cleaned.tsv", sep="\t", index_col=0)
full_data = np.log2(full_data + 1)
full_data = full_data.T

clusters = pd.read_csv("./results/pca_clusters.csv", index_col=0)

full_data["Cluster"] = clusters["Cluster"]

# Marker genes for breast cancer subtypes
markers = ["ESR1", "PGR", "ERBB2", "TP53", "MKI67", "KRT5", "FOXA1", "GATA3", "EGFR"]

available_markers = [m for m in markers if m in full_data.columns]

print("Using markers:", available_markers)
result = full_data.groupby("Cluster")[available_markers].mean()

print(result)
result.to_csv("./results/subtype_markers.csv")


