"""
Day 33: Building Data Cleaner using Pandas
Topcics Coverd:
1. Introduction to Pandas
2. Pandas Data structures (series, DataFrame)
3. Data Cleaning and Preparation
4. Data Transformation
5. Data Aggregation and Grouping in Pandas
6. Project: Data Cleaner
"""

# # What is Pandas?
# '''
# Pandas is powerful python library for data analysis
# and manipulation. It provides a easy-to-use data
# structures which is serires and dataframes.
# '''
# # Pandas Data structures
# # - Series: One-dimensional labeled array capable of holding any data type.
# # - DataFrame: Two-dimensional labeled data structure with columns of potentially different types.

# # Importing Pandas
# import pandas as pd
# from tomlkit import value
# # Creating a Series
# s = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
# print(s)

# # Creating a DataFrame
# data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#         'Age': [25, 30, 35, 40],
#         'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}

# df = pd.DataFrame(data)
# print(df)

# # Loading data from CSV, Excel, and other sources
# # - Common Data loading methods:
# # - pd.read_csv("Filename.csv"): Load data from a CSV file.
# # - pd.read_excel("Filename.xlsx"): Load data from an Excel file.

# # Saving data to CSV, Excel, and other formats
# # - Common Data saving methods:
# # - df.to_csv("Filename.csv"): Save DataFrame to a CSV file.
# # - df.to_excel("Filename.xlsx"): Save DataFrame to an Excel file.

# # Basic DataFrame Operations
# # - Viewing Data: df.head(), df.tail(), df.info(), df.describe()
# df.head()  # Display first 5 rows (also can specify number of rows to display, e.g., df.head(10) for first 10 rows)
# df.tail()  # Display last 5 rows (also can specify number of rows to display, e.g., df.tail(10) for last 10 rows)
# df.info()  # Display summary of DataFrame including data types and non-null values
# df.describe()  # Display statistical summary of numerical columns in DataFrame

# # Selecting and indexing data
# # Selecting a single column:
# df['column_name'] or df.column_name
# # Selecting multiple columns:
# df[['column1', 'column2']]
# # Selecting rows:
# df[df["column_name"] == "value"]  # Filter rows based on a condition
# # Selecting rows by index:
# df.iloc[0]  # Select first row
# df.iloc[:, 0]  # Select first column
# # Selecting by label:
# df.loc[0]  # Select first row by label
# df.loc[:, 'column_name']  # Select column by label

# # Data Cleaning and Preparation
# # - Handling missing data:

# # Dropping rows or columns with missing values.
# df = df.dropna() # Drop rows with missing values
# df = df.dropna(axis=1) # Drop columns with missing values

# # Filling missing values with a specified value.
# df['column_name'] = df['column_name'].fillna('value') # Fill missing values with a specified value
# df.fillna(method='ffill') # Forward fill missing values
# df.fillna(method='bfill') # Backward fill missing values

# # Replacing values in DataFrame
# df = df.replace('to_replace', 'value') # Replace values in DataFrame

# # Converting to datetime
# df['column_name'] = pd.to_datetime(df['column_name'])  # Convert column to datetime format

# # Interpolating missing values
# df['column_name'] = df['column_name'].interpolate()  # Fill missing values using interpolation

# # Data Transformation
# # - Renaming columns 
# df = df.rename(columns={'old_name': 'new_name'})  # Rename columns in DataFrame

# # Changing data types
# df['column_name'] = df['column_name'].astype('data_type')  # Change data type of a column in DataFrame

# # Creating or modifying columns
# df['new_column'] = df['column1'] + df['column2']  # Create a new column by performing operations on existing columns
# df[['new_column']] = df[['column1']] * 2 # Create a new column by performing operations on existing columns

# # Combining and Merging DataFrames
# # - Concatenating DataFrames
# df_combined = pd.concat(['df1', 'df2'], axis=0)  # Concatenate DataFrames vertically (stacking rows)
# df_combined = pd.concat(['df1', 'df2'], axis=1)  # Concatenate DataFrames horizontally (stacking columns)

# # - Merging DataFrames
# df_merged = pd.merge('df1', 'df2', on='common_column')  # Merge DataFrames based on a common column (inner join by default)
# df_merged = pd.merge('df1', 'df2', how='outer', on='common_column')  # Merge DataFrames with outer join
# df_merged = pd.merge('df1', 'df2', how='left', on='common_column')  # Merge DataFrames with left join
# df_merged = pd.merge('df1', 'df2', how='right', on='common_column')  # Merge DataFrames with right join
# df_merged = pd.merge('df1', 'df2', how='inner', on='common_column')  # Merge DataFrames with inner join

# # Joining DataFrames
# df_joined = pd.join('df1', 'df2', on='common_column', how='left') # Join DataFrames with left join
# df_joined = pd.join('df1', 'df2', on='common_column', how='right') # Join DataFrames with right join
# df_joined = pd.join('df1', 'df2', on='common_column', how='outer') # Join DataFrames with outer join
# df_joined = pd.join('df1', 'df2', on='common_column', how='inner') # Join DataFrames with inner join
# df_joined = pd.join('df1', 'df2', on='common_column', how='cross')  # Cross join (Cartesian product) of two DataFrames


# # Data Aggregation and Grouping in Pandas
# # Grouping data by categories
# # Why group data?
# '''
# Grouping data alows you to perfron oerations
# on subsets of data basd on shared categories.
# We can do: 
# '''
# grouped = df.groupby("column_name")
# # Operations:
# # Iterate over groups
# for name, group in grouped:
#     print(name)
#     print(group)

# # Apply aggregation
# grouped.sum()
# grouped.mean()

# # Combine grouping with aggregation methods
# # using groupby
# df.groupby("category_column")["numeric_column"].mean()
# df.groupby("category_column").agg({"numeric_column": ["mean","max","min"]})

# # Using pivot_table
# pivot = df.pivot_table(
#     values="numeric_column",
#     index="category_column",
#     aggfunc="mean"
# )

# # Custom aggregation
# def range_func(x):
#     return x.max() - x.min()

# df.groupby("category_column"["numeric_column"].agg(range_func))

# # Calclating Summary Statistics for grouped data
# # Common Statistics: mean, max, min
# df.groupby("category_column"["numeric_column"]).mean()
# df.groupby("category_column"["numeric_column"]).max()
# df.groupby("category_column"["numeric_column"]).min()

# # Multi-aggregation
# df.groupby("category_column").agg(
#     {"numeric_column":["mean","max","min"]}
# )

# --- Project: Data Cleaner Using Pandas --- 
''' 
The goal here is to build a CLI based data cleaner
tool that accepts a csv file as an input cleans the data by:
1. Missing and Handling mising value
2. Removing dulicates
3. Save clean data to a new file '''

import pandas as pd

# Load data
def load_data():
    """Load data from data.csv"""
    try:
        df = pd.read_csv("data.csv")
        print("Data loaded successfully!")
        return df
    except Exception as e:
        print("Error loading data:", e)
        return None


# Clean Data
def clean_data(df):
    """Clean the data."""
    print("\n--- Cleaning Data ---")
    print("Initial Shape:", df.shape)

    # Handle Missing Values
    print("\nHandling Missing Values...")
    df = df.dropna()
    print("After Dropping Missing Values:", df.shape)

    # Remove Duplicates
    print("\nRemoving Duplicates...")
    df = df.drop_duplicates()
    print("After Removing Duplicates:", df.shape)

    return df


# Save data
def save_data(df):
    """Save the cleaned data to cleaned_data.csv"""
    try:
        df.to_csv("cleaned_data.csv", index=False)
        print("Cleaned data saved to cleaned_data.csv")
    except Exception as e:
        print("Error Saving Data:", e)


# Main program
def main():
    print("Welcome to the Data Cleaner Tool!")

    # Load data
    df = load_data()
    if df is None:
        return

    # Show initial data
    print("\n--- Initial Data ---")
    print(df.head())

    # Clean data
    df = clean_data(df)

    # Save cleaned data
    save_data(df)

    print("\nData Cleaning Completed Successfully!")


if __name__ == "__main__":
    main()