# videos 1 intro
'''
use cases
1. voice assistants
2. stock price prediction
3. email filtering
4. product recommendations
5. predictive maintenace
6. self driving cars -> superb .use reinforce learning

ham = not a spam mail/ legitimate email
netflix send a lot of recommended movies that in aligned with our choice/interest
recommended movies basen od history

predictive - cloud computing, sensor send a lot of data. make a pattern of data to figured out the machine is okay or not

'''
# videos 2 terminology
'''
deep learning - neural network. mimic the human brain. brain comprise of neuron. neuron gets acivated. 
machine learning - linear regression. logistic regression, random forest
deep learning - cnn, rnn
artificial intelligence - super set
neural network - cnn, rnn
data science - exploratory data analysis
big data - data warehouse, data lakes

'''

# 3 history

'''

'''

# 4 cases and tyoes
'''

'''
# 5 role of data in ml
'''

'''
# 6 challenges
'''

'''

# 7 lifecycle and pipelines

'''

'''

# 8 regression pb
'''

'''

# 9 reg model and performance metrics
'''

'''

# 10 classification problem and performance metrics
'''

'''

# 11 optimizinf classification metrics
'''

'''

# 12 bias and variance


# i design 
# 1

import numpy as np

start_number = int(input("Enter Starting Number:\n"))
end_number = int(input("Enter Ending Number:\n"))

arr = np.arange(start_number,end_number + 1)
print("Array")
print(arr)

# 2

import pandas as pd

data = pd.read_csv("training_data.csv")

no_duplicate_data = data.drop_duplicates()

print("Dataset after removing duplicate rows:")
print(no_duplicate_data)

no_single_value_columns = no_duplicate_data.loc[:, no_duplicate_data.nunique() > 1]

print("\nDataset after removing columns with a single value:")
print(no_single_value_columns)

# 3

import pandas as pd

data = pd.read_csv("dataset.csv")

total_records = len(data)

count_golf = len(data[data["recreation"] == "golf"])
unconditional_prob_golf = count_golf / total_records

count_medRisk = len(data[data["credit_worthiness"] == "medRisk"])
count_single_and_medrisk = len(data[(data["credit_worthiness"] == "medRisk") & (data["status"] == "single")])
conditional_prob_single_given_medRisk = count_single_and_medrisk / count_medRisk

print(f"Unconditional probability of golf: = {unconditional_prob_golf:.2f}")
print(f"Conditional probability of single given medRisk: = {conditional_prob_single_given_medRisk:.2f}")

# 4

import pandas as pd
import seaborn as sns
import matplotplib.pyplot as plt

data = pd.read_csv("vehicle_data_1.csv")

df = pd.DataFrame(data)

print("DF Shape")
shape = df.shape
print(shape)

print("Data Types")
data_type = df.dtypes
print(data_type)

print("Top 5 rows")
five_rows = df.head(5)
print(five_rows)

numeric_feature = ['year', 'selling_price', 'km_driven', 'mileage_kmpl','engine_cc','max_power_bhp','seats']


# histogram
plt.figure(figsize = (15,15))
plt.subtitle('Histogram')
for i, feature in enumerate(numeric_feature):
    plt.subplot(3,3, i+1)
    sns.histplot(data[feature])
    plt.title(feature)

plt.tight_layout(h_pad = 0.5, w_pad = 0.5)
# Save the plot to a file
plt.savefig('uahistogram.png')
plt.clf()

# kde
plt.figure(figsize = (15,15))
plt.suptitle('KDE Plot')
for i, feature in enumerate(numeric_feature):
    plt.subplot(3,3, i+1)
    sns.kdeplot(data[feature])
    plt.title(feature)
plt.tight_layout(h_pad = 0.5, w_pad = 0.5)
# Save the plot to a file
plt.savefig('uakdeplot.png')
plt.clf()

# Rug
plt.figure(figsize = (15,15))
plt.suptitle('Rug Plot')
for i, feature in enumerate(numeric_feature):
    plt.subplot(3,3, i+1)
    sns.rugplot(data[feature])
    plt.title(feature)

plt.tight_layout(h_pad = 0.5, w_pad = 0.5)
# Save the plot to a file
plt.savefig('uarugplot.png')
plt.clf()

# box plot
plt.figure(figsize = (15,15))
plt.suptitle('Box Plot')
for i, feature in enumerate(numeric_feature):
    plt.subplot(3,3, i+1)
    sns.boxplot(data[feature])
    plt.title(feature)

plt.tight_layout(h_pad = 0.5, w_pad = 0.5)
# Save the plot to a file
plt.savefig('uaboxplot.png')
plt.clf()


# violin plot
plt.figure(figsize = (15,15))
plt.suptitle('Violin Plot')
for i, feature in enumerate(numeric_feature):
    plt.subplot(3,3, i+1)
    sns.violinplot(data[feature])
    plt.title(feature)

plt.tight_layout(h_pad = 0.5, w_pad = 0.5)
# Save the plot to a file
plt.savefig('uaviolinplot.png')
plt.clf()


# strip
plt.figure(figsize = (15,15))
plt.suptitle('Strip Plot')
for i, feature in enumerate(numeric_feature):
    plt.subplot(3,3, i+1)
    sns.stripplot(data[feature])
    plt.title(feature)

plt.tight_layout(h_pad = 0.5, w_pad = 0.5)
# Save the plot to a file
plt.savefig('stripplot.png')
plt.clf()


categorical_features = ['fuel', 'seller_type', 'transmission', 'owner']
# countplot
plt.figure(figsize = (15,15))
plt.suptitle('Count Plot')
for i, feature in enumerate(categorical_features):
    plt.subplot(2,2, i+1)
    sns.countplot(data[feature])
    plt.title(feature)

plt.tight_layout(h_pad = 0.5, w_pad = 0.5)
# Save the plot to a file
plt.savefig('uacountplot.png')
plt.clf()


# piechart
plt.figure(figsize = (10,10))
plt.suptitle('Pie Chart')
for i, feature in enumerate(categorical_features):
    plt.subplot(2,2, i+1)
    data[feature].value_counts().plot.pie(autopct="%.0f%%")
    plt.title(feature)

plt.tight_layout(h_pad = 0.5, w_pad = 0.5)
# Save the plot to a file
plt.savefig('uapiechart.png')
plt.clf()





import pandas as pd
pd.set_option('display.max_columns', 100)
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.simplefilter('ignore')

# Load the dataset
data = pd.read_csv("vehicle_data_1.csv")
df = pd.DataFrame(data)

# Step 1: Shape or Dimensions of the DataFrame
print("DF Shape")
shape = df.shape
print(shape)

# Step 2: Explore Data Types of the various columns
print("DF Column Types")
data_type = df.dtypes
print(data_type)

# Step 3: Explore data by displaying 5 rows
print("Top 5 rows")
five_rows = df.head(5)
print(five_rows)

# Numerical Features Plots
num_cols = data.select_dtypes(include=['float64', 'int64']).columns

# Set size of figure
cols = 3
rows = 3

# Step 4: Plot Histogram for all numeric features
fig = plt.figure(figsize=(15, 15))
plt.suptitle("Histogram")
for i, col in enumerate(num_cols):
    ax = fig.add_subplot(rows, cols, i + 1)
    sns.histplot(x=data[col], ax=ax)
plt.tight_layout(h_pad=0.5, w_pad=0.5)
plt.savefig("uahistogram.png")
plt.clf()

# Step 5: Plot KDE plot for all numeric features
fig = plt.figure(figsize=(15, 15))
plt.suptitle('KDE Plot')
for i, col in enumerate(num_cols):
    ax = fig.add_subplot(rows, cols, i + 1)
    sns.kdeplot(x=data[col], ax=ax)
plt.tight_layout(h_pad=0.5, w_pad=0.5)
plt.savefig('uakdeplot.png')
plt.clf()

# Step 6: Plot Rug Plot for all numeric features
fig = plt.figure(figsize=(15, 15))
plt.suptitle('Rug Plot')
for i, col in enumerate(num_cols):
    ax = fig.add_subplot(rows, cols, i + 1)
    sns.rugplot(x=data[col], ax=ax)
plt.tight_layout(h_pad=0.5, w_pad=0.5)
plt.savefig('uarugplot.png')
plt.clf()

# Step 7: Plot Box Plot for all numeric features
fig = plt.figure(figsize=(15, 15))
plt.suptitle('Box Plot')
for i, col in enumerate(num_cols):
    ax = fig.add_subplot(rows, cols, i + 1)
    sns.boxplot(x=data[col], ax=ax)
plt.tight_layout(h_pad=0.5, w_pad=0.5)
plt.savefig('uaboxplot.png')
plt.clf()

# Step 8: Plot Violin Plot for all numeric features
fig = plt.figure(figsize=(15, 15))
plt.suptitle('Violin Plot')
for i, col in enumerate(num_cols):
    ax = fig.add_subplot(rows, cols, i + 1)
    sns.violinplot(x=data[col], ax=ax)
plt.tight_layout(h_pad=0.5, w_pad=0.5)
plt.savefig('uaviolinplot.png')
plt.clf()

# Step 9: Plot Strip Plot for all numeric features
fig = plt.figure(figsize=(15, 15))
plt.suptitle('Strip Plot')
for i, col in enumerate(num_cols):
    ax = fig.add_subplot(rows, cols, i + 1)
    sns.stripplot(x=data[col], ax=ax)
plt.tight_layout(h_pad=0.5, w_pad=0.5)
plt.savefig('uastripplot.png')
plt.clf()

# Categorical Features Plots
cat_cols = data.select_dtypes(include=['object']).columns
cat_cols = [col for col in cat_cols if data[col].nunique() < 10]

# Step 10: Plot Count Plot for all categoric features
fig = plt.figure(figsize=(10, 10))
plt.suptitle("Count Plot")
for i, col in enumerate(cat_cols):
    ax = fig.add_subplot(2, 2, i + 1)
    sns.countplot(x=data[col], ax=ax)
plt.tight_layout(h_pad=0.5, w_pad=0.5)
plt.savefig("uacountplot.png")
plt.clf()

# Step 11: Plot Pie Charts for all categoric features
fig = plt.figure(figsize=(10, 10))
plt.suptitle("Pie Chart")
for i, col in enumerate(cat_cols):
    ax = fig.add_subplot(2, 2, i + 1)
    data[col].value_counts().plot.pie(autopct="%.0f%%", ax=ax)
plt.tight_layout(h_pad=0.5, w_pad=0.5)
plt.savefig("uapiechart.png")
plt.clf()

# 4 correct
import pandas as pd
pd.set_option('display.max_columns', 100)
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.simplefilter('ignore')

# Load the dataset
data = pd.read_csv("vehicle_data_1.csv")
df = pd.DataFrame(data)

# Step 1: Shape or Dimensions of the DataFrame
print("DF Shape")
shape = df.shape
print(shape)

# Step 2: Explore Data Types of the various columns
print("DF Column Types")
data_type = df.dtypes
print(data_type)

# Step 3: Explore data by displaying 5 rows
print("Top 5 rows")
five_rows = df.head(5)
print(five_rows)

# Numerical Features Plots
num_cols = data.select_dtypes(include=['float64', 'int64']).columns

# Set size of figure
cols = 3
rows = 3

# Step 4: Plot Histogram for all numeric features
fig = plt.figure(figsize=(15, 15))
plt.suptitle("Histogram")
for i, col in enumerate(num_cols):
    ax = fig.add_subplot(rows, cols, i + 1)
    sns.histplot(x=data[col], ax=ax)
plt.tight_layout(h_pad=0.5, w_pad=0.5)
plt.savefig("uahistogram.png")
plt.clf()

# Step 5: Plot KDE plot for all numeric features
fig = plt.figure(figsize=(15, 15))
plt.suptitle('KDE Plot')
for i, col in enumerate(num_cols):
    ax = fig.add_subplot(rows, cols, i + 1)
    sns.kdeplot(x=data[col], ax=ax)
plt.tight_layout(h_pad=0.5, w_pad=0.5)
plt.savefig('uakdeplot.png')
plt.clf()

# Step 6: Plot Rug Plot for all numeric features
fig = plt.figure(figsize=(15, 15))
plt.suptitle('Rug Plot')
for i, col in enumerate(num_cols):
    ax = fig.add_subplot(rows, cols, i + 1)
    sns.rugplot(x=data[col], ax=ax)
plt.tight_layout(h_pad=0.5, w_pad=0.5)
plt.savefig('uarugplot.png')
plt.clf()

# Step 7: Plot Box Plot for all numeric features
fig = plt.figure(figsize=(15, 15))
plt.suptitle('Box Plot')
for i, col in enumerate(num_cols):
    ax = fig.add_subplot(rows, cols, i + 1)
    sns.boxplot(x=data[col], ax=ax)
plt.tight_layout(h_pad=0.5, w_pad=0.5)
plt.savefig('uaboxplot.png')
plt.clf()

# Step 8: Plot Violin Plot for all numeric features
fig = plt.figure(figsize=(15, 15))
plt.suptitle('Violin Plot')
for i, col in enumerate(num_cols):
    ax = fig.add_subplot(rows, cols, i + 1)
    sns.violinplot(x=data[col], ax=ax)
plt.tight_layout(h_pad=0.5, w_pad=0.5)
plt.savefig('uaviolinplot.png')
plt.clf()

# Step 9: Plot Strip Plot for all numeric features
fig = plt.figure(figsize=(15, 15))
plt.suptitle('Strip Plot')
for i, col in enumerate(num_cols):
    ax = fig.add_subplot(rows, cols, i + 1)
    sns.stripplot(x=data[col], ax=ax)
plt.tight_layout(h_pad=0.5, w_pad=0.5)
plt.savefig('uastripplot.png')
plt.clf()

# Categorical Features Plots
cat_cols = data.select_dtypes(include=['object']).columns
cat_cols = [col for col in cat_cols if data[col].nunique() < 10]

# Step 10: Plot Count Plot for all categoric features
fig = plt.figure(figsize=(10, 10))
plt.suptitle("Count Plot")
for i, col in enumerate(cat_cols):
    ax = fig.add_subplot(2, 2, i + 1)
    sns.countplot(x=data[col], ax=ax)
#plt.tight_layout(h_pad=0.5, w_pad=0.5)
plt.savefig("uacountplot.png")
plt.clf()

# Step 11: Plot Pie Charts for all categoric features
fig = plt.figure(figsize=(10, 10))
plt.suptitle("Pie Chart")
for i, col in enumerate(cat_cols):
    ax = fig.add_subplot(2, 2, i + 1)
    data[col].value_counts().plot.pie(autopct="%.0f%%", ax=ax)
plt.tight_layout(h_pad=0.5, w_pad=0.5)
plt.savefig("uapiechart.png")
plt.clf()


# i assess

# 1

import numpy as np
from scipy import stats

number = int(input("Enter the number"))
