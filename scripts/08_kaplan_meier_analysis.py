import pandas as pd
from lifelines import KaplanMeierFitter
import matplotlib.pyplot as plt

df = pd.read_csv("./results/survival_data.csv")

print("Original shape:", df.shape)

# replace GDC missing values
df = df.replace("'--", pd.NA)
df = df.replace("--", pd.NA)

# convert columns
df["time"] = pd.to_numeric(df["time"], errors="coerce")
df["event"] = pd.to_numeric(df["event"], errors="coerce")

# remove missing
df = df.dropna(subset=["time", "event", "Subtype"])

# remove invalid times
df = df[df["time"] > 0]

# event must be integer
df["event"] = df["event"].astype(int)

print("Cleaned shape:", df.shape)

print("\nSubtype counts:")
print(df["Subtype"].value_counts())

print("\nEvent counts:")
print(df["event"].value_counts())

# KAPLAN MEIER
kmf = KaplanMeierFitter()

plt.figure(figsize=(8,6))

for subtype in df["Subtype"].unique():

    subset = df[df["Subtype"] == subtype]

    print(f"\n{subtype}: {subset.shape[0]} samples")

    if subset.shape[0] < 5:
        print("Skipped (too few samples)")
        continue

    kmf.fit(
        durations=subset["time"],
        event_observed=subset["event"],
        label=subtype
    )

    kmf.plot_survival_function()

# PLOT
plt.title("TCGA-BRCA Survival by Molecular Subtype")
plt.xlabel("Days")
plt.ylabel("Survival Probability")
plt.grid(True)

plt.savefig(
    "./results/km_survival_plot.png",
    dpi=300,
    bbox_inches="tight"
)

#plt.show()

print("\n Survival plot saved")