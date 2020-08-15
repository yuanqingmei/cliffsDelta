#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/6/21 9:10
#@Author: Yuanqing Mei
#@File  : wilcoxon.py.py

from scipy.stats import wilcoxon

# d1 = [0.588,0.549,0.507,0.607,0.573,0.563,0.53,0.555,0.543,0.633,0.557,0.519,0.563,0.637,0.583]
# d2 = [0.593,0.54,0.542,0.608,0.573,0.563,0.53,0.557,0.554,0.634,0.558,0.514,0.559,0.642,0.584]

# d1 = [0.627162924,0.557556782,0.644104564,0.680553153,0.670639679,0.520126332,0.735980072,0.259778103,\
# 0.313146535,0.307150472,0.309359995,0.774596669,0.982904723,0.774596669,0.547722558,0.577350269,\
# 0.744545382,0.552770798,0.678232998,0.685530395,0.632455532,0.587409997,0.632592955,0.601721668,\
# 0.459059049,0.718243006,0.571095668,0.502247202,0.314970394,0.584564775,0.489231394,0.511455904,\
# 0.763120529,0.456435465,0.558744237,0.602464076,0.402232247,0.628307426,0.36574704,0.425528717,\
# 0.624986683,0.640961071,0.695365833,0.581540823,0.559142794,0.57704296,0.630511818,0.641307786,\
# 0.635988078,0.558733824,0.577447462,0.67629518,0.631567519,0.608032286,0.56512826,0.686644165,\
# 0.626770119,0.625070524,0.604633429,0.626033613,0.553315742,0.551575093,0.679191838,0.59579905,\
# 0.557594663,0.554054821,0.544501985,0.558307873,0.496903995,0.640697922,0.707106781,0.66244229,\
# 0.511392837,0.629854607,0.570435645,0.441367415,0.673484151,0.680154668,0.621695764,0.65153004,\
# 0.576172603,1,0.78173596,0.614955246,0.575264711,0.674192941,0.634756308,0.411113226,0.625362214,\
# 0.543053011,0.557605927,0.759554525]
# d2 = [0.653197265,0.54089968,0.653790891,0.688187826,0.650446712,0.492927253,0.756147644,0.234978135,\
# 0.280457595,0.277814087,0.270772966,0.774596669,0.982904723,0.774596669,0.547722558,0.577350269,\
# 0.744545382,0.472455591,0.646357314,0.631568053,0.618695307,0.581087203,0.621153344,0.608950139,\
# 0.486832864,0.642416074,0.549262226,0.469809239,0.336787657,0.548185357,0.495938194,0.487151075,\
# 0.860916065,0.5,0.49138927,0.644061189,0.332223329,0.618446715,0.341053369,0.39025054,0.613865532,\
# 0.637196098,0.692495376,0.573676379,0.563185397,0.573865856,0.639430207,0.635580954,0.598032641,\
# 0.623947421,0.637369345,0.674273421,0.639996083,0.623647639,0.582458116,0.676656543,0.634941331,\
# 0.627938756,0.619395617,0.642623488,0.557272527,0.594523586,0.678878114,0.595402088,0.518708296,\
# 0.56238694,0.520919172,0.549783588,0.521157307,0.657342198,0.612372436,0.694775335,0.532387278,\
# 0.599418323,0.570435645,0.441367415,0.673484151,0.682960448,0.6172134,0.596678338,0.539019191,\
# 1,0.78173596,0.594951323,0.558516755,0.66872699,0.61367292,0.407241973,0.608042913,0.480388101,\
# 0.554996748,0.759554525]

d1 = [0.608, 0.634, 0.642]
d2 = [0.607, 0.633, 0.637]

d = [d2[i]-d1[i] for i in range(0,len(d1))]

print("the d is ", d)
# d = [0.001, 0.001, 0.005]

w, p = wilcoxon(d)

print("the w value is ", w)
print("the p value is ", p)