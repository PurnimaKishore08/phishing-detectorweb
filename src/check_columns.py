import pandas as pd

df = pd.read_csv('data/phishing.csv')  # Make sure it's renamed correctly
print("📌 Available columns are:\n")
print(df.columns.tolist())