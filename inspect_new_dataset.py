import pandas as pd
import os

file_path = "Dataset.csv"

print("=" * 55)
print("SMART FOOD SPOILAGE PREDICTION SYSTEM")
print("DOWNLOADED DATASET INSPECTION")
print("=" * 55)

if not os.path.exists(file_path):
    print("\nERROR: Dataset.csv was not found!")
    print("Make sure Dataset.csv is inside your project folder.")
else:
    df = pd.read_csv(file_path)

    print("\n1. DATASET SIZE")
    print("Number of records:", df.shape[0])
    print("Number of columns:", df.shape[1])

    print("\n2. COLUMN NAMES")
    print(df.columns.tolist())

    print("\n3. FIRST 5 RECORDS")
    print(df.head().to_string())

    print("\n4. MISSING VALUES")
    print(df.isnull().sum())

    print("\n5. DUPLICATE RECORDS")
    print(df.duplicated().sum())

    print("\n6. DATA TYPES")
    print(df.dtypes)

    print("\n7. POSSIBLE LABEL COLUMNS")

    for column in df.columns:
        if any(word in column.lower()
               for word in ["class", "label", "status", "spoil", "fresh"]):
            print(f"\nColumn: {column}")
            print(df[column].value_counts(dropna=False))

    print("\n" + "=" * 55)
    print("DATASET INSPECTION COMPLETED")
    print("=" * 55)