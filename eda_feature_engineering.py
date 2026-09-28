import pandas as pd

df = pd.read_csv("lieferungen_cleaned.csv")

print(df.info())

## Wie viele Lieferungen sind pünktlich und wie viele verspätet?
print(df["verspaetet"].value_counts())
print(df["verspaetet"].value_counts(normalize=True) * 100)