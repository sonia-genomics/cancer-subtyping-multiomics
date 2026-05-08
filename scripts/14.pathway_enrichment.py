import pandas as pd
import gseapy as gp
import os


deg = pd.read_csv(
    "./results/differential_expression.csv"
)

# FILTER SIGNIFICANT GENES
sig = deg[
    (deg["pvalue"] < 0.05) &
    (abs(deg["logFC"]) > 1)
]

print("Significant genes:", sig.shape)

# TOP UPREGULATED GENES
up = sig[sig["logFC"] > 1]

genes = up["Gene"].dropna().unique().tolist()

print("Genes used:", len(genes))


# RUN ENRICHR
enr = gp.enrichr(
    gene_list=genes,
    gene_sets=[
        "KEGG_2021_Human",
        "GO_Biological_Process_2021"
    ],
    organism="homo sapiens",
    outdir="./results/enrichment",
    cutoff=0.05
)

print("\nENRICHMENT COMPLETE")