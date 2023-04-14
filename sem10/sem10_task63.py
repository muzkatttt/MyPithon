"""
Задача No63. Решение в группах
1. Изобразите отношение households к population с помощью точечного графика
2. Визуализировать longitude по отношения к median_house_value, используя линейный график
3. Представить гистограмму по housing_median_age
4. Изобразить гистограмму по median_house_value с
оттенком housing_median_age

решение  колаб

1. sns.scatterplot(data=f, x='households', y='population')
2. sns.relplot(x="longitude", y="median_house_value", kind="line", data=f)
3. sns.histplot(data=f, x="housing_median_age")
4. sns.displot(f, x="median_house_value", hue="housing_median_age")
"""