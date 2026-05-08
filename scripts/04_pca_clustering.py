import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = pd.read_csv(
    "./data/processed/final_expression.csv",
    index_col=0
)

# PCA
pca = PCA(n_components=2)
pca_result = pca.fit_transform(data)

# K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
labels = kmeans.fit_predict(data)

pca_df = pd.DataFrame(pca_result, columns=["PC1", "PC2"], index=data.index)
pca_df["Cluster"] = labels
pca_df.to_csv("./results/pca_clusters.csv")

# Plot
plt.figure()
plt.scatter(pca_df["PC1"], pca_df["PC2"], c=labels)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("TCGA-BRCA Subtypes (PCA + KMeans)")
plt.savefig("./results/pca_clusters.png")

print("PCA + Clustering DONE")