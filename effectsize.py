#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/6/21 11:31
#@Author: Yuanqing Mei
#@File  : effectsize.py.py

'''

this script calculate the effect size between RDC-meta and GM0.6 in term of cliff's delta

'''

from __future__ import division
import pandas as pd
from scipy.stats import wilcoxon

def cliffsDelta(lst1, lst2, **dull):

    """Returns delta and true if there are more than 'dull' differences"""
    if not dull:
        dull = {'small': 0.147, 'medium': 0.33, 'large': 0.474} # effect sizes from (Hess and Kromrey, 2004)
    m, n = len(lst1), len(lst2)
    lst2 = sorted(lst2)
    j = more = less = 0
    for repeats, x in runs(sorted(lst1)):
        while j <= (n - 1) and lst2[j] < x:
            j += 1
        more += j*repeats
        while j <= (n - 1) and lst2[j] == x:
            j += 1
        less += (n - j)*repeats
    d = (more - less) / (m*n)
    size = lookup_size(d, dull)
    return d, size

def lookup_size(delta: float, dull: dict) -> str:
    """
    :type delta: float
    :type dull: dict, a dictionary of small, medium, large thresholds.
    """
    delta = abs(delta)
    if delta < dull['small']:
        return 'negligible'
    if dull['small'] <= delta < dull['medium']:
        return 'small'
    if dull['medium'] <= delta < dull['large']:
        return 'medium'
    if delta >= dull['large']:
        return 'large'

def runs(lst):
    """Iterator, chunks repeated values"""
    for j, two in enumerate(lst):
        if j == 0:
            one, i = two, 0
        if one != two:
            yield j - i, one
            i = j
        one = two
    yield j - i + 1, two

workingDirectory = "E:\\RD\\metaData\\cliffsDelta\\"

dfRDC = pd.read_csv(workingDirectory + "rdcmeta_3bug.csv")
# dfRDC = pd.read_csv(workingDirectory + "rdcmeta.csv")
dfGM06 = pd.read_csv(workingDirectory + "gm06_3bug.csv")
# dfGM06 = pd.read_csv(workingDirectory + "gm06.csv")
# print(dfRDC)
# print(dfRDC.columns.values.tolist())
metric = dfRDC.columns.values.tolist()
# print(dfRDC["amc"])
# print(metric)
# print(len(metric))

for k in range(0, len(metric)):
    print(metric[k])

# print(dfRDC[metric[0]])
# for j in range(0, 1):
d1 = list()
d2 = list()
d1total = []
d2total = []
dtotal = []

for j in range(0, len(metric)):
    metricName = metric[j]
    print("the metric name is ", metricName)
    d1 = dfRDC[metricName]
    d2 = dfGM06[metricName]
    # print("the d1 is ", d1)
    # print("the d2 is ", d2)
    d = []
    for i in range(0, len(d1)):
        if d2[i] < 0.6:
            continue
        # if d1[i] == d2[i]:
        #     continue
        d.append(d2[i]-d1[i])
        d1total.append(d1[i])
        d2total.append(d2[i])
        dtotal.append(d2[i]-d1[i])

    # d = [d2[i]-d1[i] for i in range(0, len(d1))]
    print("the d is ", d)
    try:
        w, p = wilcoxon(d)
        print("the w value is ", w)
        print("the p value is ", p)
    except:
        print("error")

print("the dtotal is ", dtotal)
try:
    wtotal, ptotal = wilcoxon(dtotal)
    print("the wtotal value is ", wtotal)
    print("the ptotal value is ", ptotal)
except:
    print("error")

d, res = cliffsDelta(d1total, d2total)

print("the total cliffs delta value is ", d)
print("the total effect size is ", res)