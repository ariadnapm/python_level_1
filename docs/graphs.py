import numpy as np
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from plotly.tools import mpl_to_plotly
import pathlib

folder = pathlib.Path(__file__).parent.absolute()
file_name = folder.joinpath("factbook.csv") #file_name = folder / "factbook.csv"
data = pd.read_csv(file_name, ';')

def get_data_options():
    result = []
    for col in data.columns[1:]:
        result.append({"label": col, "value": col})
    return result

#def get_data_options():
#    return [{"label": col, "value": col} for col in data.colums]

def make_country_graph(degre=3, 
                        col_1_n="GDP - per capita", 
                        col_2_n="Life expectancy at birth(years)"):
    plot_data = None
    if col_1_n == col_2_n:
        plot_data = data.loc [:, ["Country", col_1_n]]
    else:
        plot_data = data.loc [:, ["Country", col_1_n, col_2_n]]

    plot_data = plot_data.dropna()

    data1 = plot_data.loc[:, col_1_n]
    data2 = plot_data.loc[:, col_2_n]
    country = plot_data["Country"]

    coeff = np.polyfit(data1, data2, degre)
    p = np.poly1d(coeff)
    x = np.linspace(data1.max(),data1.min())

    fig, ax = plt.subplots()
    ax.plot(data1, data2, 'ro')
    ax.plot(x, p(x), "k-")
    ax.set_xlabel(col_1_n)
    ax.set_ylabel(col_2_n)

    graph = mpl_to_plotly(fig)
    graph.data[0].text = country
    return graph

def correlation_calc(col_1_n, col_2_n):
    plot_data = None
    if col_1_n == col_2_n:
        plot_data = data.loc [:, ["Country", col_1_n]]
    else:
        plot_data = data.loc [:, ["Country", col_1_n, col_2_n]]

    plot_data = plot_data.dropna()

    data1 = plot_data.loc[:, col_1_n]
    data2 = plot_data.loc[:, col_2_n]

    corcoef = np.corrcoef(data1, data2)[0,1]
    
    return corcoef