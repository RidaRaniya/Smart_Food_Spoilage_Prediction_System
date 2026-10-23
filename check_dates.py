import pandas as pd

# Load the original dataset
df = pd.read_csv("food_spoilage_dataset.csv")

print("FIRST 20 ORIGINAL DATES:")
print(df["Date_of_purchase"].head(20).to_list())

print("\nLAST 20 ORIGINAL DATES:")
print(df["Date_of_purchase"].tail(20).to_list())

# Check dates using month/day/year format
dates_mdy = pd.to_datetime(
    df["Date_of_purchase"],
    format="%m/%d/%Y",
    errors="coerce"
)

# Check dates using day/month/year format
dates_dmy = pd.to_datetime(
    df["Date_of_purchase"],
    format="%d/%m/%Y",
    errors="coerce"
)

print("\nDATE FORMAT CHECK:")
print("Valid dates using month/day/year:", dates_mdy.notna().sum())
print("Valid dates using day/month/year:", dates_dmy.notna().sum())

print("\nDATE INSPECTION COMPLETED!")
