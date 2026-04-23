import pandas as pd
import pycountry

file_path = "/Users/kamari/Documents/project_info/IHME_GBD_2010_MORTALITY_AGE_SPECIFIC_BY_COUNTRY_1970_2010.csv"


try:
    data = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"Error: The file at {file_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
    

df = pd.DataFrame(data)
##print(df)

# check for null values
##print(df.isnull().sum())

# check for data types
##print(df.dtypes)

# look at unique values
##print(df["Country Code"].unique())

# look at unique values
##print(df["Sex"].unique())

# look at unique values
##print(df["Year"].unique())

# look at unique values
##print(df["Age Group"].unique())






   
   