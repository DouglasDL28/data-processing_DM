# Universidad del Valle de Guatemala
# Data Mining
# Douglas de León Molina
# Carné 18037
# 16/02/2021

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('../fortune500.csv')

df

df.head()

df.columns = ['year', 'rank', 'company', 'revenue', 'profit']

df.head()

non_num = df.profit.str.contains('[^0-9.-]')
print(df.loc[non_num])

set(df.loc[non_num].profit)
print(set(df.loc[non_num].profit))
# Por lo tanto 'N.A.' es el único valor que no es un número.

print(len(df.loc[non_num].profit))

plt.hist(df.loc[non_num].year, 50)
plt.show()

df.drop(df.loc[non_num].index)

len(df.drop(df.loc[non_num].index))
df = df.drop(df.loc[non_num].index)
df.profit = df.profit.astype('float64')
len(df)

# df.dtypes
avg_profit = df.groupby('year').agg([np.mean, np.std])
avg_profit.profit['mean'] - avg_profit.profit['std']̦

plt.plot(avg_profit.index, avg_profit.profit['mean'])

plt.plot(avg_profit.index, avg_profit.revenue)

lower_bound = avg_profit.profit['mean'] - avg_profit.profit['std']
upper_bound = avg_profit.profit['mean'] + avg_profit.profit['std']
fig, ax = plt.subplots()
ax.plot(avg_profit.index, avg_profit.profit['mean'])
ax.fill_between(avg_profit.index, lower_bound, upper_bound, facecolor='skyblue', alpha=0.5)

lower_bound = avg_profit.revenue['mean'] - avg_profit.revenue['std']
upper_bound = avg_profit.revenue['mean'] + avg_profit.revenue['std']
fig, ax = plt.subplots()
ax.plot(avg_profit.index, avg_profit.revenue['mean'])
ax.fill_between(avg_profit.index, lower_bound, upper_bound, facecolor='grey', alpha=0.5)




