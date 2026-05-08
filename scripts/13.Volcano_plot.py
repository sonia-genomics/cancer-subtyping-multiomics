import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

deg = pd.read_csv(
    "./results/differential_expression.csv"
)

# Create significance column
deg["significant"] = (
    (deg["pvalue"] < 0.05) &
    (abs(deg["logFC"]) > 1)
)

# -log10 pvalue
deg["minus_log10_p"] = -np.log10(deg["pvalue"] + 1e-10)

# Plot
plt.figure(figsize=(10,8))

# Non-significant
plt.scatter(
    deg.loc[~deg["significant"], "logFC"],
    deg.loc[~deg["significant"], "minus_log10_p"],
    alpha=0.5,
    s=10
)

# Significant
plt.scatter(
    deg.loc[deg["significant"], "logFC"],
    deg.loc[deg["significant"], "minus_log10_p"],
    alpha=0.8,
    s=12
)

# Threshold lines
plt.axvline(-1, linestyle="--")
plt.axvline(1, linestyle="--")
plt.axhline(-np.log10(0.05), linestyle="--")

plt.xlabel("log2 Fold Change")
plt.ylabel("-log10 Adjusted P-value")
plt.title("Differential Expression Volcano Plot")

# Save
plt.savefig(
    "./results/volcano_plot.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Volcano plot saved")