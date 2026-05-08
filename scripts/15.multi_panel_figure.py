from PIL import Image
import matplotlib.pyplot as plt


# IMAGE PATHS
images = [
    "./results/pca_subtypes.png",
    "./results/marker_heatmap.png",
    "./results/volcano_plot.png",
    "./results/km_survival_plot.png"
]

titles = [
    "A. PCA Clustering",
    "B. Marker Heatmap",
    "C. Differential Expression",
    "D. Survival Analysis"
]


# CREATE PANEL
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

for ax, img_path, title in zip(axes.flatten(), images, titles):

    img = Image.open(img_path)

    ax.imshow(img)
    ax.set_title(title, fontsize=14, fontweight="bold")
    ax.axis("off")

plt.tight_layout()

plt.savefig(
    "./results/Figure1_MultiPanel.png",
    dpi=300,
    bbox_inches="tight"
)

print("Publication figure saved")