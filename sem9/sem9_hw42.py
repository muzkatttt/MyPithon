"""
Задача 42:
Узнать какая максимальная households в зоне минимального значения population

import pandas as pd
f = pd.read_csv('sample_data/california_housing_train.csv')

f['population'].min()

f[f['population'] == f['population'].min()]['households'].max()

"""