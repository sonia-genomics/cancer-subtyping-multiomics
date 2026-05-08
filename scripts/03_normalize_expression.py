import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

data = pd.read_csv(
    "./data/processed/expression_cleaned.tsv",
    sep="\t",
    index_col=0
)

print("Raw shape:", data.shape)

data = np.log2(data + 1)

# Transpose → samples × genes
data = data.T

print("After transpose:", data.shape)


top_genes = data.var().sort_values(ascending=False).head(5000).index
data = data[top_genes]

print("After gene selection:", data.shape)


scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

data_scaled = pd.DataFrame(data_scaled, index=data.index, columns=data.columns)

# Save
data_scaled.to_csv(
    "./data/processed/final_expression.csv"
)

print("FINAL DATA READY:", data_scaled.shape)