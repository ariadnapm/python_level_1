#%%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('population-figures-by-country.csv', ',')

#%%
pop = data.loc[4, "Year_1960":] #ligne 4 et toutes les colonnes àpd 1960
country1 = data.loc[4, "Country"] #country = data.iloc[country_id, 0]
plt.plot(range(1960, 2017),pop, "b-", label = country1)

country2 = data.loc[15, "Country"]
pop2 = data.loc[15, "Year_1960":] #ligne 4 et toutes les colonnes àpd 1960
plt.plot(range(1960, 2017),pop2, "r-",label = country2)

plt.ylabel("Population of "+country1+ " and "+country2)
plt.xlabel("Years")
plt.legend(loc="best")
plt.show()
# %%