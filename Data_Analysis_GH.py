import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import re
import numpy as np

sns.set()

# Import data from csv file
# Use dayfirst=True to import datetimes with UK format date

df = pd.read_csv("DummyFile.csv", dayfirst=True)

# First will carry out a small amount of data exploration and cleaning

print(df.isnull().sum())

# This shows a limited number of null values in two of the columns,
# so I will remove the rows containing these.

df.dropna(subset=["Site", "Count"], inplace=True)

# I want to find out which client Sites had the most call outs in 2019,
# so the .groupby() function is useful for this.

sites = df.groupby("Site").sum()
sites.sort_values(by="Count", ascending=False, inplace=True)

# I just want to plot the top 5 sites
sites_top5 = sites[:5]

sites_top5.plot.bar()
plt.title("Top 5 Sites - 2019")
plt.xlabel("Site")
plt.ylabel("Quantity of Jobs")
plt.xticks(rotation=45)
plt.savefig("Top 5 Sites")


# Next I will move on to visualising the number of Types of Job

types = df.groupby("Type of Job").sum()
types.sort_values(by="Count", ascending=True, inplace=True)

# This time I want to use a horizontal bar chart to show data in a different way

# Use plt.figure() to create new plot so data isn't shown on same plot above
plt.figure()

types.plot.barh(color="r", title="Types of Job")
plt.savefig("Job Types")


# A big part of working out our price is determining the number of jobs that take place out of
# normal working hours. In my data I have a datetime column, however it is intially set as a string.

# I want to show how jobs are distributed throughout the 24 hour period
#  and how many jobs are carried out outside of working hours.

# First I convert this column to datetime

df["Date / Time Requested"] = pd.to_datetime(df["Date / Time Requested"])

# Here I use a list comprehension to build a new column

df["Time"] = [datetime.datetime.time(i) for i in df["Date / Time Requested"]]

df["Time"] = df["Time"].astype("str")

# To extract the information I want in order to create a histogram, I will import re to extract
# just the hour.

pattern = re.compile(r'(\d{2}):')

df["Time_2"] = [re.findall(pattern, string)[0] for string in df["Time"]]

df["Time_2"] = df["Time_2"].astype("float")

# Now I will use groupby again to sum the quantity of jobs for each hour slot

times = df.groupby("Time_2").sum()

bins = np.arange(0, 25)

# I want to use different colours to show in and out of hours works, so
# I will use the following notation to take 'patches' from the plt.hist() method.

plt.figure()

n, b, patches = plt.hist(df["Time_2"], bins=bins, histtype="bar")
plt.xticks(bins)

am = patches[0:8]
pm = patches[17:25]

for a in am:
    plt.setp(a, "facecolor", "r")

for b in pm:
    plt.setp(b, "facecolor", "r")

plt.xlabel("Time of Day")
plt.ylabel("Job Quantity")
plt.title("Annual Jobs by Time of Day")

plt.savefig("Time of Day")


# For the rest of the analysis, I will need to create an index with the datetime data.

df.set_index("Date / Time Requested", inplace=True)

ooh = df.between_time("17:00:00", "08:00:00")

ooh_sum = ooh["Count"].sum()
total = df["Count"].sum()
in_hours_sum = total - ooh_sum

print(ooh_sum, in_hours_sum, total)

plt.figure()

bar_chart = plt.bar(x=["In Hours", "Out of Hours"], height=[in_hours_sum, ooh_sum])
bar_chart[1].set_color("r")

plt.title("In Hours vs Out of Hours")

plt.savefig("IH vs OOH")


# Finally I want to show how jobs varied by week and then by month, so I will use
# the resample() method for this.

plt.figure()

weeks = df["Count"].resample("W").sum()

weeks.plot(title="Weekly Jobs", legend=False)

plt.savefig("Weekly Jobs")


plt.figure()

months = df.resample("M").sum()
months.plot(title="Monthly Jobs", legend=False)
plt.ylim(0, 100)

plt.savefig("Monthly Jobs")








