import thinkstats2
import thinkplot

d={7:8,12:8,17:14,22:4,27:6,32:12,38:8,42:3,47:2}

pmf = thinkstats2.Pmf(d,label='actual')
pmf
print('mean',pmf.Mean())