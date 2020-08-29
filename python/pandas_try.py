import numpy as np
import pandas as pd
s = pd.Series([1, 3, 5, np.nan, 6, 8]) # np.nan:Not a Number Series est une classe
print(s)
# Création d'une liste de dates
dates = pd.date_range('20200824', periods=6)
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates)
print(s)

# Création d'une liste de dates
dates = pd.date_range('20200824', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=["A", "B", "C", "D"])
print(df)
print(df['A']) #print(df.A)
print(df[0:3])

# courbe de Gauss = distribution normale
# csv = coma separated values et ouvrir le dossier, dans ce cas-ci "projet data"
data = pd.read_csv('population-figures-by-country.csv', ',')
print(data)

