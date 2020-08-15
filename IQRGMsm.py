#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/6/26 22:21
#@Author: Yuanqing Mei
#@File  : IQRGMsm.py.py


'''

this script will compare the range of a metric values and the performance by OLS method.

'''
import pandas as pd
import numpy as np
from pandas import DataFrame
import statsmodels.api as sm

# X = [27.19, 1, 2, 0.28, 2, 13, 13, 0.5, 3, 2, 8, 1.11, 146, 3, 0.9, 0, 0, 3, 21, 4]

X = [29.81, 1.29, 3.32, 0.54, 1.66, 14.11, 10.91, 0.26, 2.84, 0.97, 51.69, 1.31, 195.95, 3.46, 0.58, 0.23, 0.58, 4.43, \
     25.38, 6.33]

Y = [0.593,0.54,0.542,0.607,0.512,0.573,0.563,0.53,0.511,0.516,0.557,0.554,0.634,0.558,0.51,0.494,0.321,0.559,0.642,0.583]

# X = sm.add_constant(X) # adding a constant
#
# model = sm.OLS(Y, X).fit()
# predictions = model.predict(X)
#
# print_model = model.summary()
# print(print_model)

def box_plot_outliers(data_ser, box_scale):
    """
    利用箱线图去除异常值
    :param data_ser: 接收 pandas.Series 数据格式
    :param box_scale: 箱线图尺度，
    :return:
    """
    iqr = box_scale * (data_ser.quantile(0.75) - data_ser.quantile(0.25))
    val_low = data_ser.quantile(0.25) - iqr
    val_up = data_ser.quantile(0.75) + iqr
    rule_low = (data_ser < val_low)
    rule_up = (data_ser > val_up)
    return (rule_low, rule_up), (val_low, val_up)

print(box_plot_outliers(pd.DataFrame(X), 3))
a, b = box_plot_outliers(pd.DataFrame(X), 3)
print("###################")
print(pd.DataFrame(X).shape[0])
index = np.arange(pd.DataFrame(X).shape[0])[a[0] | a[1]]
print("###################")
print(type(index))
print("###################")
print(type([a[0] | a[1]]))
print("###################")
print([a[0] | a[1]])
print("*****************")
print(a[1])