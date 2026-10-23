import pandas as pd

# ==========================================
# 1. LOAD THE ORIGINAL DATASET
# ==========================================

df = pd.read_csv("food_spoilage_dataset.csv")

print("=" * 60)
print("SMART FOOD SPOILAGE PREDICTION SYSTEM")
print("DATA CLEANING")
print("=" * 60)

print("\nOriginal dataset shape:", df.shape)


# ==========================================
# 2. CHECK MISSING VALUES
# ==========================================

print("\nMissing values before cleaning:")
print(df.isnull().sum())

print("\nTotal missing cells:", df.isnull().sum().sum())


# ==========================================
# 3. HANDLE MISSING VALUES
# ==========================================

# Fill the missing food type with the most frequent food type
df["Food_type"] = df["Food_type"].fillna(
    df["Food_type"].mode()[0]
)

# Fill missing storage conditions with the most frequent value
df["Storage_condition"] = df["Storage_condition"].fillna(
    df["Storage_condition"].mode()[0]
)

# Fill missing packaging values with the most frequent value
df["Packaging"] = df["Packaging"].fillna(
    df["Packaging"].mode()[0]
)


# ==========================================
# 4. CONVERT DATE FORMATS
# ==========================================

# Dates with slashes use month/day/year.
# Dates with hyphens use day-month-year.

date_text = df["Date_of_purchase"].astype("string").str.strip()

slash_mask = date_text.str.contains("/", regex=False, na=False)
hyphen_mask = date_text.str.contains("-", regex=False, na=False)

parsed_dates = pd.Series(
    pd.NaT,
    index=df.index,
    dtype="datetime64[ns]"
)

parsed_dates.loc[slash_mask] = pd.to_datetime(
    date_text.loc[slash_mask],
    format="%m/%d/%Y",
    errors="coerce"
)

parsed_dates.loc[hyphen_mask] = pd.to_datetime(
    date_text.loc[hyphen_mask],
    format="%d-%m-%Y",
    errors="coerce"
)

df["Date_of_purchase"] = parsed_dates

print("\nInvalid dates after conversion:", df["Date_of_purchase"].isna().sum())


# ==========================================
# 5. CHECK DUPLICATES
# ==========================================

duplicates_before = df.duplicated().sum()

print("\nDuplicate rows found:", duplicates_before)

df = df.drop_duplicates()


# ==========================================
# 6. VERIFY MISSING VALUES
# ==========================================

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nTotal missing cells after cleaning:", df.isnull().sum().sum())


# ==========================================
# 7. SAVE THE CLEANED DATASET
# ==========================================

df["Date_of_purchase"] = df["Date_of_purchase"].dt.strftime("%Y-%m-%d")

df.to_csv("food_spoilage_cleaned.csv", index=False)

print("\nCleaned dataset saved as food_spoilage_cleaned.csv")
print("Final dataset shape:", df.shape)

print("\nDATA CLEANING COMPLETED!")
