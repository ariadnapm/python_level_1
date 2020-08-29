import dash
import dash_html_components as html 
import matplotlib.pyplot as plt
import numpy as np
from plotly.tools import mpl_to_plotly
import dash_core_components as dcc

def create_sine_graph():
    fig, ax = plt.subplots()
    x = np.arange(0, 3 * np.pi, 0.1)
    ax.set_title("Sine Wave Form")
    ax.plot(x, np.sin(x), "r--")
    return mpl_to_plotly(fig)

app = dash.Dash()
app.layout = html.Div(children=
    [html.H1(children="My Title"),
    dcc.Graph(id="example-graph", figure=create_sine_graph())
    ])

if __name__ == '__main__' :
    app.run_server(debug=True)