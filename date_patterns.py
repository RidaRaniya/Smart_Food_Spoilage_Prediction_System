import pandas as pd

# Load the original dataset
df = pd.read_csv("food_spoilage_dataset.csv")

dates = df["Date_of_purchase"].astype("string").str.strip()

print("TOTAL ROWS:", len(dates))

print("\nDATE PATTERN COUNTS:")

print(
    "Slash-separated dates:",
    dates.str.match(r"^\d{1,2}/\d{1,2}/\d{4}$", na=False).sum()
)

print(
    "Hyphen-separated dates:",
    dates.str.match(r"^\d{1,2}-\d{1,2}-\d{4}$", na=False).sum()
)

print(
    "Other date patterns:",
    (
        ~dates.str.match(r"^\d{1,2}/\d{1,2}/\d{4}$", na=False)
        & ~dates.str.match(r"^\d{1,2}-\d{1,2}-\d{4}$", na=False)
    ).sum()
)

print("\nSAMPLE DATES AROUND THE FORMAT CHANGE:")
print(dates.iloc[100000:100020].to_list())

print("\nDATE PATTERN CHECK COMPLETED!")
