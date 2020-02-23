import pandas as pd
import thinkstats2
import thinkplot

df = pd.read_excel("FinalProject/GSS.xls",sheet_name="Data")
print(df.count())
print(df.head())
print(df['occupation'])
hist = thinkstats2.Hist(df['occupation'])
print(hist)
thinkplot.Hist(hist)
thinkplot.Config(xlabel='Occupation', ylabel='Count')