#%%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import colors
data = pd.read_csv('factbook.csv', ';')

col_1 = "GDP - per capita"
col_2 = "Life expectancy at birth(years)"
plot_data = data.loc [:, [col_1, col_2]]
plot_data = plot_data.dropna()

data1 = plot_data.loc[:, col_1]
data2 = plot_data.loc[:, col_2]

plt.ylabel(col_2)
plt.xlabel(col_1)

coeff = np.polyfit(data1, data2, 3)

p = np.poly1d(coeff)
x = np.linspace(data1.max(),data1.min())

plt.plot(data1, data2, 'ro')
plt.plot(x, p(x), "k-")

plt.show()
# %%
