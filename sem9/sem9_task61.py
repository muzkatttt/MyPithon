"""
Задача No61.
1. Определить какое максимальное и минимальное значение median_house_value
2. Показать максимальное median_house_value, где median_income = 3.1250
3. Узнать какая максимальная population в зоне минимального значения median_house_value

1.  f['median_house_value'].max()
    f['median_house_value'].min()

2. f[f['median_income'] == 3.1250]['median_house_value'].max()

3. f[f['median_house_value'] == f['median_house_value'].min()]['population'].max()
"""

