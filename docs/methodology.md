# Methodology

# Overview

This project implements a transcriptomics-based computational workflow for identifying molecular breast cancer subtypes using TCGA-BRCA RNA-seq data.

The analysis combines unsupervised machine learning, survival analysis, differential expression analysis, and pathway enrichment to identify biologically meaningful tumor groups.

---

# Data Acquisition

## Dataset Source

- TCGA-BRCA
- GDC Data Portal

## Data Types

- RNA-seq gene expression
- Clinical metadata

Approximately 1120 breast cancer samples were analyzed.

---

# RNA-seq Workflow

The conceptual RNA-seq workflow includes:

```text
FASTQ
   ↓
Quality Control (FastQC)
   ↓
Read Trimming (fastp)
   ↓
Alignment (STAR/HISAT2)
   ↓
Quantification (featureCounts/HTSeq)
   ↓
Gene Expression Matrix
   ↓
Normalization
   ↓
Downstream Transcriptomic Analysis
```

This project primarily focuses on downstream computational analysis using processed expression matrices.

---

# Data Preprocessing

## Gene Expression Matrix Construction

RNA-seq count files were merged into a unified gene expression matrix.

Processing steps included:

- Removal of non-gene rows
- Handling missing values
- Gene filtering
- Matrix cleaning

---

# Normalization

Expression values were normalized using z-score standardization.

## Purpose

Normalization ensures:

- Cross-sample comparability
- Reduced technical variation
- Improved clustering performance

---

# Dimensionality Reduction

## Principal Component Analysis (PCA)

PCA was applied to reduce transcriptomic dimensionality while preserving major sources of variation.

### Objectives

- Visualize subtype separation
- Identify transcriptomic patterns
- Reduce high-dimensional complexity

---

# Unsupervised Clustering

## K-means Clustering

K-means clustering was performed using:

```text
k = 3
```

### Objectives

- Identify molecularly distinct tumor groups
- Explore transcriptomic heterogeneity
- Detect subtype-specific patterns

---

# Subtype Annotation

Clusters were interpreted using known breast cancer biomarkers.

## Marker Genes

| Gene | Biological Role |
|---|---|
| ESR1 | Estrogen receptor signaling |
| PGR | Progesterone receptor signaling |
| ERBB2 | HER2 signaling |
| EGFR | Basal-like signaling |
| KRT5 | Basal epithelial marker |
| FOXA1 | Luminal differentiation |
| GATA3 | Luminal transcription factor |
| MKI67 | Cell proliferation |
| TP53 | Tumor suppressor |

---

# Survival Analysis

## Kaplan-Meier Analysis

Kaplan-Meier survival curves were generated to compare subtype-associated survival trends.

### Variables Used

- Survival time
- Vital status
- Subtype classification

### Objective

Evaluate prognostic differences among identified molecular subtypes.

---

# Differential Expression Analysis

Differential expression analysis was performed to identify subtype-associated biomarkers.

## Objectives

- Detect significantly altered genes
- Identify subtype-specific transcriptional programs
- Discover candidate biomarkers

---

# Pathway Enrichment Analysis

GO and KEGG enrichment analyses were performed using significantly differentially expressed genes.

## Biological Objectives

Identify enriched pathways related to:

- Hormone signaling
- Cell cycle regulation
- Proliferation
- DNA replication
- Cancer-associated signaling

---

# Visualization

The following visualizations were generated:

- PCA plots
- Heatmaps
- Survival curves
- Volcano plots
- Multi-panel publication figures

These visualizations support interpretation of transcriptomic subtype structure and biological relevance.

---

# Computational Environment

## Programming Language

- Python

## Major Libraries

- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Lifelines
- GSEApy

## Operating System

- Linux

---

# Reproducibility

The project is fully reproducible through sequential execution of pipeline scripts.

## Pipeline Steps

```bash
python scripts/0.id_mapping.py
python scripts/1.merge_clean.py
python scripts/2.normalize.py
python scripts/3.pca_cluster.py
python scripts/4.subtype_annotation.py
python scripts/5.extract_clinical.py
python scripts/6.survival_data.py
python scripts/7.survival_plot.py
python scripts/8.heatmap.py
python scripts/9.stage_analysis.py
python scripts/10.pca_plot.py
python scripts/11.marker_heatmap.py
python scripts/12.differential_expression.py
python scripts/13.Volcano_plot.py
python scripts/14.pathway_enrichment.py
python scripts/15.multi_panel_figure.py
```

---

# Summary

This workflow demonstrates how transcriptomic profiling combined with computational analysis can be used to:

- Identify molecular cancer subtypes
- Explore tumor heterogeneity
- Interpret biologically relevant pathways
- Connect molecular data with clinical outcomes

The project highlights the integration of bioinformatics, machine learning, and cancer biology in modern genomics research.
