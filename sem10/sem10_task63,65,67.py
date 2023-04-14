# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TQvzkDW0_X9IR29yAIk7lTR7H-K4SWt4
"""

import pandas as pd
f = pd.read_csv('sample_data/california_housing_test.csv')

f.shape

f.dtypes

f.isnull()

f.isnull().sum()

print(f['median_house_value'].mean())

f['median_income']

import pandas as pd
f = pd.read_csv('sample_data/california_housing_test.csv')

f[f['median_income'] < 2]

f[['longitude', 'latitude']]

"""задача 59 (4)"""

f[(f['housing_median_age'] < 20) & (f['median_house_value'] > 70000)]

"""задача 61 (1) Определить какое максимальное и минимальное значение median_house_value

"""

f['median_house_value'].max()

f['median_house_value'].min()

"""задача 61 (2) Показать максимальное median_house_value, где median_income = 3.1250"""

import pandas as pd
f = pd.read_csv('sample_data/california_housing_test.csv')

f[f['median_income'] == 3.1250]['median_house_value'].max()

"""задача 61 (3) Узнать какая максимальная population в зоне минимального значения median_house_value"""

f[f['median_house_value'] == f['median_house_value'].min()]['population'].max()

"""Домашнее задание к семинару 9. Задача 40. Работать с файлом california_housing_train.csv, который находится в папке sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)"""

import pandas as pd
f = pd.read_csv('sample_data/california_housing_train.csv')

f[f['population'] <= 500]['median_house_value'].median()

"""Задача 42. Узнать какая максимальная households в зоне минимального значения population"""

import pandas as pd
f = pd.read_csv('sample_data/california_housing_train.csv')

f['population'].min()

f[f['population'] == f['population'].min()]['households'].max()

import pandas as pd
df = pd.read_csv('sample_data/california_housing_train.csv')

"""показать скрытые выходные данные"""

df.head()

import pandas as pd
df = pd.read_csv('sample_data/california_housing_train.csv')

df.tail()

df.shape

df.isnull()

df.isnull().sum()

"""построение графиков семинар 10 """

import pandas as pd
f = pd.read_csv('sample_data/california_housing_test.csv')

import seaborn as sns
import pandas as pd

f = pd.read_csv('sample_data/california_housing_train.csv')

"""1. Изобразите отношение households к population с помощью точечного графика"""

sns.scatterplot(data=f, x='households', y='population')

"""2 Визуализировать longitude по отношению к median_house_value, используя линейный график"""

import seaborn as sns
import pandas as pd
f = pd.read_csv('sample_data/california_housing_train.csv')

sns.relplot(x="longitude", y="median_house_value", kind="line", data=f)

"""3 Представить гистограмму по housing_median_age"""

sns.histplot(data=f, x="housing_median_age")

sns.displot(f, x="median_house_value", hue="housing_median_age")

"""задача 65. Написать EDA для датасета про пингвинов
Необходимо:
● Использовать 2-3 точечных графика
● Применить доп измерение в точечных графиках, используя
аргументы hue, size, stile
● Использовать PairGrid с типом графика на ваш выбор
● Изобразить Heatmap
● Использовать 2-3 гистограммы
"""

penguins = sns.load_dataset("penguins")
penguins.head()

sns.scatterplot(data=penguins, x="body_mass_g", y="flipper_length_mm")

sns.scatterplot(data=penguins, x="sex", y="flipper_length_mm")

sns.scatterplot(data=penguins, x="body_mass_g", y="bill_depth_mm")

sns.scatterplot(data=penguins, x="body_mass_g", y="bill_depth_mm", hue="species")

sns.scatterplot(data=penguins, x="body_mass_g", y="bill_depth_mm", hue="species", size="flipper_length_mm", style="sex")

"""Задача 67. Задача No67. Создать новый столбец в таблице с пингвинами,
который будет отвечать за показатель длины клюва пингвина.
high - длинный(от 42)
middle - средний(от 35 до 42)
low - маленький(до 35)
"""

df = penguins

df[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']]

p = sns.PairGrid(df)
p.map(sns.scatterplot)

p = sns.PairGrid(df)
p.map(sns.relplot)

h = sns.heatmap(df[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']])

glue = sns.load_dataset('glue').pivot('Model', 'Task', 'Score')
sns.heatmap(glue)

glue = sns.load_dataset('glue').pivot('Model', 'Task', 'Score')
sns.heatmap(glue, annot=True)

glue.head()

sns.histplot(df)

sns.histplot(df, x='body_mass_g')

sns.histplot(df, x='flipper_length_mm', hue='species')

sns.histplot(df, x='body_mass_g', hue='sex')

sns.histplot(df, x='flipper_length_mm', hue='length_bill')

glue = sns.load_dataset('glue').pivot('Model', 'Task', 'Score')
sns.heatmap(glue, annot=True, linewidth=1, cmap='crest')

"""Дополнительная задача на семинаре"""

sns.histplot(data=df, x='species', hue='length_bill')

df.groupby(['length_bill']).count()

df.loc[df['bill_length_mm'] > 42, 'length_bill']='high'
df.loc[(df['bill_length_mm'] > 35) & (df['bill_length_mm'] < 42), 'length_bill']='middle'
df.loc[df['bill_length_mm'] < 35, 'length_bill']='low'
df