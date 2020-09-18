import pandas as pd
import seaborn as sns

sns.set()

# Import data from csv file
# Use dayfirst=True to import datetimes with UK format date

df = pd.read_csv("SP1.csv", dayfirst=True)

# First will carry out a small amount of data exploration and cleaning

print(df.isnull().sum())

# This shows a limited number of null values in two of the columns,
# so I will remove the rows containing these.

df.dropna(subset=["Site", "Count"], inplace=True)

# I want to find out which client Sites had the most call outs in 2019,
# so the .groupby() function is useful for this.

sites = df.groupby("Site").sum()
print(sites)

