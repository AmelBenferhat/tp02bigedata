import pandas as pd
import time

file = r"D:\BigData_TP02\HI-Large_Trans.csv"

start = time.time()

chunksize = 10000
total_rows = 0
i = 0

for chunk in pd.read_csv(file, chunksize=chunksize):
    total_rows += len(chunk)
    i += 1
    print("Chunk:", i)

end = time.time()

print("Total rows:", total_rows)
print("Execution time:", end - start)
