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
