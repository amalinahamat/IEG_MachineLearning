import numpy as np
import pandas as pd

population = pd.read_csv('population.csv')
print(population)
population.drop([0,1], axis = 0, inplace=True)
population.reset_index(inplace=True)
population.drop('index', axis=1, inplace=True)
print(population)

population.drop('idxs', axis=1, inplace=True)
population = population[['state', 'pop_5', 'pop_12', 'pop_18','pop_60','pop']]
population.columns = ['state','children','teenager','adult','senior','total']
print(population)

population.to_excel("population.xlsx")