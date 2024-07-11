# video 1

import matplotlib.pyplot as plt # type: ignore
plt.style.use("classic")
fig = plt.figure()
ax = plt.axes()

plt.style.available

file_path = open("Medals.csv","rt")
content = file_path.readlines()
print(content)

#i design 

# 1
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Medals.csv')

# Correct the line style to dotted and the legend label
plt.plot(df["Team"], df["Total"], linestyle="--", color="red", marker="o", markerfacecolor="k", linewidth=3)

plt.xlabel("Team Name")
plt.ylabel("Total Number of Medals")
plt.legend(["Team-wise Total Medal Data"], loc="lower right")
plt.title("Team-wise Total Medal Data")

# Save the plot with the specified file name
plt.savefig("plot2.png")

# 2

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the csv file
df = pd.read_csv('Medals.csv')

# Create bins for the histogram
bins = [10, 20, 30, 40]

# Create a histogram of the total medals
plt.hist(df['Total'], bins=bins, edgecolor='black', label='Total Medals Distribution')

# Set the x-axis label
plt.xlabel('Total Medals Range')

# Set the y-axis label
plt.ylabel('Count')

# Set the title
plt.title('Total Medals Histogram')

# Set the legend location
plt.legend(loc='upper left')

# Save the plot to a file
plt.savefig('plot6.png')

# 3

import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np

# Read the csv file
df = pd.read_csv('Medals.csv')

# Calculate the total medals for each type
gold_total = df['Gold'].sum()
silver_total = df['Silver'].sum()
bronze_total = df['Bronze'].sum()

# Create a pie chart
plt.pie([gold_total, silver_total, bronze_total], labels=['Gold', 'Silver', 'Bronze'], autopct='%1.1f%%')

# Set the title
plt.title('Medals data')

# Set the axis to be equal
plt.axis('equal')

# Set the legend location
plt.legend(loc='lower right')

# Save the plot to a file
plt.savefig('plot7.png')

# 4


import matplotlib.pyplot as plt
import seaborn as sns

# Read the csv file
data = sns.load_dataset('tips')

# Create a scatter 
sns.barplot(x = "day", y = "total_bill", data = data , palette = "PuRd", ci = None)

# Set the x-axis label
plt.xlabel('Day')

# Set the y-axis label
plt.ylabel('Total Bill')

# Set the title
plt.title('Total Bill by Day')

# Save the plot to a file
plt.savefig('splot3.png')

# 5

import matplotlib.pyplot as plt
import seaborn as sns

# Read the csv file
data = sns.load_dataset('tips')

# Create a scatter 
sns.barplot(x = "day", y = "total_bill", data = data , palette = "PuRd", ci = None)

# Set the x-axis label
plt.xlabel('Day')

# Set the y-axis label
plt.ylabel('Total Bill')

# Set the title
plt.title('Total Bill by Day')

# Save the plot to a file
plt.savefig('splot3.png')
