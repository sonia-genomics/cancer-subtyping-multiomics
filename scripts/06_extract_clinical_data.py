import json
import pandas as pd


with open("data/sample_ref_data//clinical.project-tcga-brca.2026-04-29.json") as f:
    data = json.load(f)

records = []

for case in data:
    tcga_id = case.get("submitter_id", None)

    diag = case.get("diagnoses", [{}])[0]

    stage = diag.get("ajcc_pathologic_stage", None)
    laterality = diag.get("laterality", None)

    # Extract treatments (optional)
    treatments = diag.get("treatments", [])
    
    treatment_types = []
    drugs = []

    for t in treatments:
        t_type = t.get("treatment_type", None)
        drug = t.get("therapeutic_agents", None)

        if t_type:
            treatment_types.append(t_type)
        if drug:
            drugs.append(drug)

    records.append([
        tcga_id,
        stage,
        laterality,
        ",".join(treatment_types),
        ",".join(drugs)
    ])

df = pd.DataFrame(records, columns=[
    "TCGA_ID",
    "Stage",
    "Laterality",
    "Treatment_Type",
    "Drugs"
])

df.to_csv("./data/processed/clinical_cleaned.csv", index=False)

print("Clinical data extracted:", df.shape)