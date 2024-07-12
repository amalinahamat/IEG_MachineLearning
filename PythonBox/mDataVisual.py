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

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the csv file
data = pd.read_csv('Medals.csv')

df = pd.DataFrame(data)

# Create a scatter 
plt.scatter(df["Rank"], df["Rank_by_Total"], label = "Rank Comparison", color = "b", marker = "o")

# Set the x-axis label
plt.xlabel('Rank')

# Set the y-axis label
plt.ylabel('Rank_by_Total')

# Set the title
plt.title('Rank Comparison')

# Set the legend location
plt.legend(loc='upper left')

# Save the plot to a file
plt.savefig('plot4.png')

# 5

import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = sns.load_dataset('tips', cache=True, data_home=r'\temp')

# Create a bar plot
sns.barplot(x="day", y="total_bill", data=data, palette='PuRd', ci=None)

# Set the x-axis label
plt.xlabel('day')

# Set the y-axis label
plt.ylabel('total_bill')

# Save the plot to a file
plt.savefig('splot3.png')

# Show the plot (optional)
#plt.show()

# 6

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset('car_crashes', cache=True, data_home=r'\temp')

# Create a scatter plot
plt.scatter(data["speeding"], data["alcohol"])
sns.set(style="whitegrid", rc={'grid.color': '.5', 'grid.linestyle': '-'})

# Save the plot to a file
plt.savefig('splot1.png')

# 7
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset('tips', cache=True, data_home=r'\temp')

# histogram
sns.histplot(data = data, x = "total_bill", kde = True)

# Save the plot to a file
plt.savefig('splot2.png')


# 8

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset('tips', cache=True, data_home=r'\temp')

sns.countplot(data = data, x = "day", hue = "sex", palette = 'magma')

# Save the plot to a file
plt.savefig('splot6.png')

# i assess

# 1

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the csv file
data = pd.read_csv('Medals.csv')

df = pd.DataFrame(data)

# Create a line
#plt.plot(df["Team"], df["Total"], color = "b", marker = "o", linestyle = "-")
plt.plot(df["Team"], df["Total"], linestyle="-", color="b", marker="o")
# Set the x-axis label
plt.xlabel('Team Name')

# Set the y-axis label
plt.ylabel('Total Number of Medals')

# Set the title
plt.title('Team-wise Total Medal Data')

# Save the plot to a file
plt.savefig('plot1.png')


# 2

import matplotlib.pyplot as plt
import seaborn as sns

# Read the csv file
data = sns.load_dataset('tips', cache=True, data_home=r'\temp')

palette = {"Thur": "#1f77b4", "Fri": "#ff7f0e", "Sat": "#2ca02c", "Sun": "#d62728"}

#plt.figure(figsize=(8,10))
plt.figure()
sns.boxplot(x = 'day', y = 'total_bill', data = data, palette = palette, flierprops={"marker": "D", "markerfacecolor": "grey", "markeredgecolor": "black"} )

# Remove horizontal grid lines
plt.axhline(linewidth=0)

# Remove vertical grid lines
plt.axvline(linewidth=0)

# Remove grid
plt.grid(False)

plt.xlabel('day')
plt.ylabel('total_bill')

# Save the plot to a file
plt.savefig('splot8.png') # use the output name