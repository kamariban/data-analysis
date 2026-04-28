import pandas as pd

file_path = "/Users/kamari/Documents/project_info/Crime_Data_from_2020_to_2024.csv"


try:
    data = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"Error: The file at {file_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
    
#print(data.head())


#print(data.shape) (1004894, 28)

#crucial to check for missing values in the dataset

print(data.isnull().sum())

#print(data.nunique()) 