"""
Lab 03: NumPy, Matplotlib, Pandas
File: lab03_numpy_matplotlib_pandas.py

Codes in this file (in order):
  1. numpy_arrays      - ones, full, arange, linspace, slicing, aggregates
  2. matplotlib_plots  - plot, bar, barh, hist, pie, subplot
  3. pandas_dataframe  - loc, filter with &, isnull, dropna, fillna, rename, to_csv
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# ---------- NUMPY ----------
a = np.array([1, 2, 3, 4, 5])
print(np.ones(5), np.zeros(3), np.full(5, 10))
print(np.arange(1, 10))                  # 1..9
print(np.linspace(0, 1, 5))              # 0, .25, .5, .75, 1

print(a[1:4], a[::2], a[-1])             # slicing, end excluded
m = np.array([[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10]])
print(m[0, 1])                           # row 0, col 1 -> 2
print(m[1, 1:4])                         # [7 8 9]
print(m[:, 2])                           # column 2 -> [3 8]
print(m.shape, m.size)                   # (2, 5) 10

print(a + 5, a * 2)                      # vectorised
b = np.array([10, 20, 30, 40, 50])
print(a + b)                             # element-wise
print(a.sum(), a.mean(), np.median(a), a.min(), a.max(), a.std(), a.var())

# ---------- MATPLOTLIB ----------
x = [1, 2, 3, 4]
y = [2, 4, 6, 8]
plt.plot(x, y, 'o:r')                    # marker o, dotted, red
plt.title("Line")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

plt.bar(["A", "B", "C"], [3, 5, 2])
plt.show()
plt.barh(["A", "B", "C"], [3, 5, 2])
plt.show()
plt.hist([1, 2, 2, 3, 3, 3])
plt.show()
plt.pie([30, 70], labels=["X", "Y"], autopct="%1.1f%%")
plt.show()

plt.subplot(1, 2, 1)                     # 1 row, 2 cols, plot 1
plt.plot(x, y)
plt.subplot(1, 2, 2)
plt.bar(x, y)
plt.tight_layout()
plt.show()

# ---------- PANDAS ----------
df = pd.DataFrame({"Name": ["Ali", "Sara", "Omar"],
                   "Age": [20, None, 25],
                   "Marks": [80, 90, 60]})
print(df.head(), df.shape, df.columns)
print(df.loc[0])                         # row 0
print(df["Marks"])                       # one column
print(df[df.Marks > 70])                 # filter
print(df[(df.Marks > 60) & (df.Age > 18)])   # use & not "and"

print(df.isnull().sum())                 # missing per column
print(df.dropna())
print(df.fillna(0))
df["Age"] = df["Age"].fillna(df["Age"].mean())

df.rename(columns={"Marks": "Score"}, inplace=True)
df["Double"] = df["Score"] * 2           # new column
print(df["Score"].mean(), df["Score"].max())
df.to_csv("out.csv", index=False)
df2 = pd.read_csv("out.csv")
