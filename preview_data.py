import pandas as pd

df = pd.read_csv("HI-Large_Trans.csv", nrows=10000)

print(df.head())