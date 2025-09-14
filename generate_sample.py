import pandas as pd

# Create messy sample data
data = {
    "Name": [" Alice ", "bob", "BOB", None, "Charlie", "alice", "Eve  "],
    "Date": ["2021-01-05", "05/02/2021", "2021.03.01", "2021/04/02", None, "15-05-2021", "June 6 21"],
    "Amount": ["1,200", "300.50", "1,200", "N/A", "500", None, "$1,000.00"],
    "Phone": ["+91 98765 43210", "9876543210", None, "09876543210", "98765-43210", "98765 43210", ""]
}

df = pd.DataFrame(data)

# Save inside /data/ folder
df.to_excel("data/sample_dirty.xlsx", index=False)

print("✅ sample_dirty.xlsx generated in data/ folder")