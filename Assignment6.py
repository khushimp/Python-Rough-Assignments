#Assignment 6

# Import Pandas library
import pandas as pd

filename = input("Enter file name (.csv/.xls/.xlsx): ").strip()

# Step 1: Read the CSV file
data = pd.read_csv(filename)

# Step 2: Display original DataFrame
print("ORIGINAL HEALTHCARE DATASET:")
print(data.head())

# Step 3: Display information about the dataset
print("\nDATASET INFORMATION:")
data.info()

# Step 4: Display statistical description
print("\nSTATISTICAL DESCRIPTION:")
print(data.describe())

# Step 5: Check missing values
print("\nMISSING VALUES:")
print(data.isnull().sum())

# Step 6: Remove rows having missing Name
data = data.dropna(subset=["Name"])

# Step 7: Fill missing Age with mean
data["Age"] = data["Age"].fillna(data["Age"].mean())

# Step 8: Fill missing Gender with mode
data["Gender"] = data["Gender"].fillna(data["Gender"].mode()[0])

# Step 9: Count duplicate records
print("\nNUMBER OF DUPLICATE RECORDS:")
duplicate_rows = data[data.duplicated()].index
print(len(duplicate_rows))

# Step 10: Remove duplicate records using drop()
data = data.drop(index=duplicate_rows)

# Step 11: Display cleaned DataFrame
print("\nCLEANED HEALTHCARE DATASET:")
print(data.head())

# Step 12: Filter patients whose age is greater than 50
filtered_data = data.loc[data["Age"] > 50]

# Step 13: Display filtered DataFrame
print("\nPATIENTS HAVING AGE GREATER THAN 50:")
print(filtered_data.head())

# Step 14: Display final number of records
print("\nTOTAL RECORDS AFTER PREPROCESSING:")
print(len(data))
