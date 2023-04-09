"""
Задача 59.
1. Проверить есть ли в файле пустые значения
2. Показать median_house_value где median_income < 2
3. Показать данные в первых 2 столбцах
4. Выбрать данные где housing_median_age < 20 и
median_house_value > 70000

df[df.isnull()].count()

в колабе вводим

1. f.isnull().sum()

2. print(f['median_house_value'].mean())

3. f[['longitude', 'latitude']]

4. f[(f['housing_median_age'] < 20) & (f['median_house_value'] > 70000)]
"""

