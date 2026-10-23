import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv("food_spoilage_dataset.csv")

print("=" * 60)
print("SMART FOOD SPOILAGE PREDICTION SYSTEM")
print("DATASET EXPLORATION")
print("=" * 60)

# Step 2: Dataset size
print("\n1. DATASET SIZE")
print("Total rows:", df.shape[0])
print("Total columns:", df.shape[1])

# Step 3: Column names
print("\n2. COLUMN NAMES")
print(df.columns.tolist())

# Step 4: Data types
print("\n3. DATA TYPES")
print(df.dtypes)

# Step 5: Statistical summary
print("\n4. STATISTICAL SUMMARY")
print(df.describe())

# Step 6: Unique values in categorical columns
print("\n5. UNIQUE VALUES")

categorical_columns = [
    "Food_type",
    "Storage_condition",
    "Packaging"
]

for column in categorical_columns:
    print(f"\n{column}:")
    print(df[column].value_counts(dropna=False))

# Step 7: Missing values
print("\n6. MISSING VALUES")
print(df.isnull().sum())

# Step 8: Duplicate rows
print("\n7. DUPLICATE ROWS")
print("Number of duplicate rows:", df.duplicated().sum())

print("\nEXPLORATION COMPLETED!")
