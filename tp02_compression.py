import pandas as pd

file = r"D:\BigData_TP02\HI-Large_Trans.csv"
output = r"D:\BigData_TP02\HI-Large_Trans.csv.gz"

chunksize = 100000

print("Starting compression...")

first = True

for chunk in pd.read_csv(file, chunksize=chunksize):
    chunk.to_csv(
        output,
        mode="a",
        index=False,
        compression="gzip",
        header=first
    )
    first = False
    print("Chunk compressed")

print("Compression finished")