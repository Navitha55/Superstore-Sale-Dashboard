import pandas as pd

df = pd.read_csv("./SampleSuperstore.csv")

# Intial Exploration
print(df.info())
print(df.describe())
print(df.head(10))

# Checking uniform columns
print(df['Country'].unique())
print(df['City'].unique())
print(df['State'].unique())
print(df['Postal Code'].unique())
print(df['Region'].unique())

# Removing or dropping country as it is same for all rows and postal code
df = df.drop(['Country', 'Postal Code'], axis = 1)

# Missing Values check
print(df.isnull().sum())

# Duplicates removal
df = df.drop_duplicates()

# Datatype Check
print(df.dtypes)

# Saving the cleaned file
df.to_csv("superstore_sales_cleaned.csv", index=False)