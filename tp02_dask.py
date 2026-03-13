import dask.dataframe as dd
import time

file = r"D:\BigData_TP02\HI-Large_Trans.csv"

print("Starting to read the file with Dask...")

start = time.time()

df = dd.read_csv(file)

print("File loaded. Now computing number of rows...")

total_rows = df.shape[0].compute()

end = time.time()

print("Total rows:", total_rows)
print("Execution time:", end - start)
print("Finished.")