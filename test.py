# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd


# %%
df = pd.read_csv('../fortune500.csv')


# %%
df


# %%
df.head()


# %%
df.columns = ['year', 'rank', 'company', 'revenue', 'profit']


# %%
df.head()


# %%
non_num = df.profit.str.contains('[^0-9.-]')
df.loc[non_num]


# %%
set(df.loc[non_num].profit)


# %%



