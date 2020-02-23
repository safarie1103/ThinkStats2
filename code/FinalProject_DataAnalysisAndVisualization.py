
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np

import pandas as pd
import thinkstats2
import thinkplot

plt.style.use('fivethirtyeight')

df_main = pd.read_csv("FinalProject/fifa19_data.csv")
data = df_main.sample(frac=.25)

def country(x):
    return data[data['Nationality'] == x][['Name','Overall','Potential','Position']]


# let's check the Indian Players
country('India')