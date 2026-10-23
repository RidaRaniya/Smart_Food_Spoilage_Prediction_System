import pandas as pd

df = pd.read_csv("food_spoilage_cleaned.csv")

print("=" * 50)
print("CHECKING THE FOOD SPOILAGE DATASET")
print("=" * 50)

print("\nDataset shape:")
print(df.shape)

print("\nAvailable columns:")
print(df.columns.tolist())

print("\nFirst 5 records:")
print(df.head())

print("\nDoes the dataset contain a spoilage label?")

if "Spoiled" in df.columns:
    print("Yes, the Spoiled column exists.")
elif "Spoilage_Status" in df.columns:
    print("Yes, the Spoilage_Status column exists.")
else:
    print("No actual spoilage label was found.")
    print("We must decide how to create or obtain a valid target.")

print("\nDataset check completed.")