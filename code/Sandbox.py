import thinkstats2
import thinkplot
import nsfg
import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import warnings

hist = thinkstats2.Hist([1,2,2,3,5])
plt.hist(hist)
str(hist)
n = hist.Total()
print('n =' + str(n))
d = {}
for x,freq in hist.Items():
    d[x] = freq/n

print(d)

pmf = thinkstats2.Pmf(hist)
print(pmf)

pmf.Prob(2)
pmf[2]
pmf.Incr(2,0.2)
pmf.Prob(2)
pmf.Mult(2,.05)
pmf.Prob(2)
pmf.Total()
pmf.Normalize()
pmf.Total()

thinkplot.Hist(hist)
preg = nsfg.ReadFemPreg()

live = preg[preg.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

first_pmf = thinkstats2.Pmf(firsts.prglngth, label='first')
other_pmf = thinkstats2.Pmf(others.prglngth, label='other')
width = 0.45

thinkplot.PrePlot(2, cols=2)
thinkplot.Hist(first_pmf, align='right', width=width)
thinkplot.Hist(other_pmf, align='left', width=width)
thinkplot.Config(xlabel='weeks',
                     ylabel='probability',
                     axis=[27, 46, 0, 0.6])

thinkplot.PrePlot(2)
thinkplot.SubPlot(2)
thinkplot.Pmfs([first_pmf, other_pmf])
thinkplot.Save(root='probability_nsfg_pmf',
                   xlabel='weeks',
                   axis=[27, 46, 0, 0.6])

# plot the differences in the PMFs
weeks = range(35, 46)
diffs = []
for week in weeks:
    p1 = first_pmf.Prob(week)
    p2 = other_pmf.Prob(week)
    diff = 100 * (p1 - p2)
    diffs.append(diff)

thinkplot.Bar(weeks, diffs)
thinkplot.Save(root='probability_nsfg_diffs',
                title='Difference in PMFs',
                xlabel='weeks',
                ylabel='percentage points',
                legend=False)

