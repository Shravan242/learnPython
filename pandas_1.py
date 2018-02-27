# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 20:05:03 2018

@author: shravan
"""

import pandas as pd
import numpy as np

""" Converting the python list, dict into pandas series """

ds = pd.Series([2,3,4,5,6])

dss = pd.Series({0: 2, 1: 3, 2: 4, 3: 5, 4: 6})

""" add, sub, mul and div the pandas series  """

ds1 = pd.Series([1,4,6,8,5])
ds2 = pd.Series([7,2,4,3,5])

ds_sum = ds1+ds2

ds_dif = ds1-ds2

ds_mul = ds1*ds2

ds_div = ds1/ds2

""" comparing two elements in pandas Series """

ds1 == ds2
ds1 > ds2
ds1 < ds2
ds1 <= ds2
ds1 >= ds2

""" simple DataFrame in pandas """
pd.DataFrame({'A':[1,4,16],'B':[3,6,9]})


""" index in pandas """
exam_data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
        
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)

""" contactinating the two different datatype elements into another pandas Series """


df['country_score'] = df['name'] + ', ' + df['score'].astype(str)


