# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TQvzkDW0_X9IR29yAIk7lTR7H-K4SWt4
"""

"""Домашнее задание к семинару 10 (задача 44). 
В ячейке ниже представлен код генерирующий DataFrame,
которая состоит всего из 1 столбца. Ваша задача перевести
его в one hot вид. Сможете ли вы это сделать без get_dummies?
"""

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame(list('whoAmI'))
pd.get_dummies(data)

import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame(list('whoAmI'))
pd.get_dummies(data)

"""без метода pd.get_dummies перевести в one hot вид не получилось"""

import random
import pandas as get_dummies
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
pd.get_dummies(data)