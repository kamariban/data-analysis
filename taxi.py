import pandas as pd
import pyarrow


#NYC Taxi Trips

file = "/Users/kamari/Documents/project_info/yellow_tripdata_2026-APRIL.parquet"

data = pd.read_parquet(file)


df = pd.DataFrame(data)

#print(df.head())

print(df.columns)