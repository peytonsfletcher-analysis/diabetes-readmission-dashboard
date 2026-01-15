import pandas as pd

# STEP 1: Load raw dataset (put the CSV in the same folder as this script)
df = pd.read_csv("diabetic_data.csv")

# STEP 2: Clean column names
df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace("-", "_")
    .str.replace(" ", "_")
)

# STEP 3: Create readmission flags
# readmitted values are typically: "NO", "<30", ">30"
df["readmitted_30_flag"] = df["readmitted"].apply(lambda x: 1 if x == "<30" else 0)

# STEP 4: Keep a few high-value clinical + operational columns
cols_to_keep = [
    "race",
    "gender",
    "age",
    "time_in_hospital",
    "num_lab_procedures",
    "num_procedures",
    "num_medications",
    "number_outpatient",
    "number_emergency",
    "number_inpatient",
    "a1cresult",
    "diabetesmed",
    "readmitted",
    "readmitted_30_flag"
]

# Some Kaggle versions may have slightly different columns, so filter safely
cols_to_keep = [c for c in cols_to_keep if c in df.columns]
df = df[cols_to_keep].copy()

# STEP 5: Basic cleanup (common missing marker is '?')
df = df.replace("?", pd.NA)

# Optional: drop rows missing the target or key columns
df = df.dropna(subset=["readmitted"])

# STEP 6: Export cleaned dataset for Power BI
df.to_csv("cleaned_diabetes_data.csv", index=False)

print("Done! Saved cleaned file: cleaned_diabetes_data.csv")
