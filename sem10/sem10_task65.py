''''
Задача No65. Написать EDA для датасета про пингвинов
Необходимо:
● Использовать 2-3 точечных графика
● Применить доп измерение в точечных графиках, используя
аргументы hue, size, stile
● Использовать PairGrid с типом графика на ваш выбор
● Изобразить Heatmap
● Использовать 2-3 гистограммы

решение на колаб

penguins = sns.load_dataset("penguins")
penguins.head()

sns.scatterplot(data=penguins, x="body_mass_g", y="flipper_length_mm")

sns.scatterplot(data=penguins, x="sex", y="flipper_length_mm")

sns.scatterplot(data=penguins, x="body_mass_g", y="bill_depth_mm")

sns.scatterplot(data=penguins, x="body_mass_g", y="bill_depth_mm", hue="species")

sns.scatterplot(data=penguins, x="body_mass_g", y="bill_depth_mm", hue="species", size="flipper_length_mm", style="sex")



'''