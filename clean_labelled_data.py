import pandas as pd

print("=" * 55)
print("SMART FOOD SPOILAGE PREDICTION SYSTEM")
print("CLEANING THE DOWNLOADED DATASET")
print("=" * 55)

# 1. Load the downloaded dataset
df = pd.read_csv("Dataset.csv")

print("\nOriginal dataset shape:", df.shape)

# 2. Standardize column names
df.columns = df.columns.str.strip()

# 3. Remove leading and trailing spaces from text columns
for column in df.select_dtypes(include=["str", "object"]).columns:
    df[column] = df[column].str.strip()

# 4. Standardize the class labels
df["Class"] = df["Class"].str.capitalize()

print("\nClass counts before removing duplicates:")
print(df["Class"].value_counts(dropna=False))

# 5. Remove exact duplicate rows
duplicates_before = df.duplicated().sum()
df = df.drop_duplicates().copy()

print("\nDuplicate rows removed:", duplicates_before)

# 6. Check missing values
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# 7. Check class labels
print("\nClass counts after cleaning:")
print(df["Class"].value_counts(dropna=False))

# 8. Save the cleaned dataset
df.to_csv("Dataset_cleaned.csv", index=False)

print("\nCleaned dataset shape:", df.shape)
print("Saved as Dataset_cleaned.csv")

print("\nCLEANING COMPLETED SUCCESSFULLY!")