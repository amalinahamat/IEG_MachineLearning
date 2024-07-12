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