"""
Задача 57.
1.  Прочесть с помощью pandas файл california_housing_test.csv,
    который находится в папке sample_data
2.  Посмотреть сколько в нем строк и столбцов
3.  Определить какой тип данных имеют столбцы
sample_data/california_housing_train.csv
на сайте colab (авторизация через аккаунт google)

import pandas as pd
f = pd.read_csv('sample_data/california_housing_test.csv')

f.shape

f.dtypes

f.isnull()

"""