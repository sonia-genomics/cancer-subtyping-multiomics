import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

expr = pd.read_csv(
    "./data/processed/final_expression.csv",
    index_col=0
)

clusters = pd.read_csv(
    "./results/pca_clusters.csv",
    index_col=0
)

# MAP SUBTYPES
label_map = {
    0: "Basal-like",
    1: "Luminal B",
    2: "Luminal A"
}

clusters["Subtype"] = clusters["Cluster"].map(label_map)

# ALIGN SAMPLES
expr["Subtype"] = clusters["Subtype"]

# SPLIT GROUPS
group1 = expr[expr["Subtype"] == "Basal-like"]
group2 = expr[expr["Subtype"] == "Luminal A"]

print("Basal-like:", group1.shape)
print("Luminal A:", group2.shape)

# remove subtype column
group1 = group1.drop(columns=["Subtype"])
group2 = group2.drop(columns=["Subtype"])


# DIFFERENTIAL EXPRESSION
results = []

for gene in group1.columns:

    vals1 = group1[gene]
    vals2 = group2[gene]

    # t-test
    stat, pval = ttest_ind(
        vals1,
        vals2,
        equal_var=False,
        nan_policy="omit"
    )

    # log fold change
    logfc = vals1.mean() - vals2.mean()

    results.append([
        gene,
        logfc,
        pval
    ])

# RESULTS TABLE
de = pd.DataFrame(
    results,
    columns=["Gene", "logFC", "pvalue"]
)

# sort by significance
de = de.sort_values("pvalue")


de.to_csv(
    "./results/differential_expression.csv",
    index=False
)

print("\nTop DE genes:")
print(de.head(20))

print("\nDifferential expression completed")