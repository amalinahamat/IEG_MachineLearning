# i design

# 1
import pandas as pd

data = [[5.1,3.5,1.4,0.2,"IrisSentosa"],
	[4.9,3.0,1.4,0.2,"IrisSentosa"],
	[4.9,3.0,1.4,0.2,"IrisVersicolor"],
	[6.4,3.2,4.5,1.5,"IrisVersicolor"],
	[6.3,3.3,6.0,2.5,"IrisVirginica"],
	[5.8,2.7,5.1,1.9,"IrisVirginica"]]

#Fill in the code here
columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species_type"]
index  = ["0", "1", "2", "3", "4", "5"]

df = pd.DataFrame(data, columns = columns, index = index)
print(df)

# 2

import pandas as pd

columns = ['sepal_length' , 'sepal_width' , 'petal_length', 'petal_width', 'species_type' ]

data = pd.read_csv('iris.csv',  names =  columns, skiprows=1)

df = pd.DataFrame(data, columns = columns)
print(df)

# by default when print pandas dataframe, it will include index by default which start from 0


# 3

import pandas as pd

data = pd.read_csv('iris_with_header.csv')

df = pd.DataFrame(data)

print(df[['sepal_length', 'sepal_width']])

# 4

import pandas as pd

data = pd.read_csv('iris_with_header.csv')

print("DataFrame")
df = pd.DataFrame(data)
print(df)

print("Shape")
shape = df.shape
print(shape)

print("Data Types")
data_type = df.dtypes
print(data_type)

print("Column Count under each type")
column_number = df.dtypes.value_counts()
print(column_number)

drop_species = df.drop("species_type", axis = 1)

print("Summary Statistics")
summary = drop_species.describe(include='all')
print(summary)

# 5
import pandas as pd

data = pd.read_csv('iris_with_header.csv')
df = pd.DataFrame(data)

print('Column Names')
column_names = df.columns
print(column_names)

print('Column Names after renaming')
data.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'SpeciesType']
print(data.columns)

# column_names2 = df.columns
# print(column_names2)

print('DataFrame')
print(df)





