"""
Задача No67. Создать новый столбец в таблице с пингвинами,
который будет отвечать за показатель длины клюва пингвина.
high - длинный(от 42)
middle - средний(от 35 до 42)
low - маленький(до 35)

glue = sns.load_dataset('glue').pivot('Model', 'Task', 'Score')
sns.heatmap(glue, annot=True, linewidth=1, cmap='crest')

sns.histplot(data=df, x='species', hue='length_bill')

df.groupby(['length_bill']).count()

df.loc[df['bill_length_mm'] > 42, 'length_bill']='high'
df.loc[(df['bill_length_mm'] > 35) & (df['bill_length_mm'] < 42), 'length_bill']='middle'
df.loc[df['bill_length_mm'] < 35, 'length_bill']='low'
df
"""