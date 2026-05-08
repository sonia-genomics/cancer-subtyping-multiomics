import pandas as pd
#import glob
import os

#files = glob.glob("/home/sonia/bioinformatics/cancer-subtyping-multiomics/data/gene_counts/*.tsv")

#print("Total files found:", len(files))
data_dir = "./data/raw"

files = []

# Collect all STAR count files
for root, dirs, filenames in os.walk(data_dir):
    for f in filenames:
        if f.endswith("gene_counts.tsv"):
            files.append(os.path.join(root, f))

print(f"Total files found: {len(files)}")

if len(files) == 0:
    raise ValueError("No files found")

dfs = []

for f in files:
    sample_id = os.path.basename(f).split(".")[0]

    try:
        # Read only required columns
        df = pd.read_csv(
            f,
            sep="\t",
            comment="#",
            usecols=["gene_id", "gene_name", "gene_type", "unstranded"]
        )
        

        df = df[~df["gene_id"].str.startswith("N_")]

        df = df[df["gene_type"] == "protein_coding"]

        df = df[df["gene_name"].notna()]

        df = df[["gene_name", "unstranded"]]

        df.set_index("gene_name", inplace=True)

        df.columns = [sample_id]

        dfs.append(df)

    except Exception as e:
        print(f"Error in file {f}: {e}")

print("Processed files:", len(dfs))

merged = pd.concat(dfs, axis=1)

merged = merged.groupby(merged.index).mean()

print("After removing duplicates:", merged.shape)

merged = merged.loc[merged.sum(axis=1) > 0]

merged.to_csv("./data/processed/expression_cleaned.tsv", sep="\t")

print("MERGE DONE")
print("Final shape:", merged.shape)