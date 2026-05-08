import json
import pandas as pd

with open("data/sample_ref_data/metadata.repository.2026-04-29.json") as f:
    data = json.load(f)

records = []

for entry in data:

    # Extract UUID from filename
    file_name = entry.get("file_name", None)

    if file_name:
        file_uuid = file_name.split(".")[0]
    else:
        file_uuid = None

    # Extract TCGA barcode
    entities = entry.get("associated_entities", [])

    if len(entities) > 0:
        full_barcode = entities[0].get("entity_submitter_id", None)

        if full_barcode:
            tcga_id = full_barcode[:12]
        else:
            tcga_id = None
    else:
        tcga_id = None

    # Save valid records
    if file_uuid and tcga_id:
        records.append([file_uuid, tcga_id])

df = pd.DataFrame(records, columns=["UUID", "TCGA_ID"])

df.to_csv(
    "data/sample_ref_data/id_mapping.csv",
    index=False
)

print("Mapping created:", df.shape)
print(df.head())