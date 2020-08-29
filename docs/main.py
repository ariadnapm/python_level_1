import dash
import dash_html_components as html
import dash_core_components as dcc
import graphs
import matplotlib
matplotlib.use('Agg')
from dash.dependencies import Input, Output
from graphs import get_data_options, make_country_graph, correlation_calc

app = dash.Dash(__name__)

graph = graphs.make_country_graph(degre=3)

graph_card = html.Div([
    html.H3("Données sur 263 pays", className ="graph-title"),
    dcc.Graph(id="country-graphs", figure=graph)], className = "graphy")


poly_card = html.Div([
    html.Div(
        html.H3("Polynominal regression degree"), className = "card-header"),
        html.Div([
            dcc.Slider(id="Degre", 
            min=1, max=10, 
            step=1,value=3, 
            marks={i : str(i) for i in range(11)})
            ], className="card-content")
], className = "card")


select_xyaxis = html.Div([
    html.Div(
        html.H3("Data source"), className = "card-header"),
    html.Div([
        html.Div([
            html.Span("X:", className="dropdown-label"),
            dcc.Dropdown(id='graph-x-dropdown',
                options=get_data_options(),
                value="GDP - per capita",
                 placeholder="Select a value")], className="clearfix"),

        html.Div([
            html.Span("Y:", className="dropdown-label"),
            dcc.Dropdown(id='graph-y-dropdown',
                options=get_data_options(),
                value="Life expectancy at birth(years)",
                placeholder="Select a value")], className="clearfix")
        ], className = "card-content")
], className="card data-card")

coco= correlation_calc(col_1_n="GDP - per capita", col_2_n="Life expectancy at birth(years)")

corcoef_present = html.Div([
    html.Div(
        html.H3("Correlation"), className = "card-header"),
        html.Div([
            html.P(id="correlation-coeff"),
            ], className="card-content")
    ], className = "card")

app.layout = html.Div(children=
    [graph_card,
    html.Div([
        poly_card,
        select_xyaxis,
        corcoef_present
        ], className = "block-double")
    ]
)

@app.callback(
    Output(component_id="country-graphs", component_property="figure"),
    [Input(component_id="Degre", component_property="value"),
    Input(component_id="graph-x-dropdown", component_property="value"),
    Input(component_id="graph-y-dropdown", component_property="value")]
)
def update_graph(degre, col_1_n, col_2_n):
    return graphs.make_country_graph(degre, col_1_n, col_2_n)

@app.callback(
    Output(component_id="correlation-coeff", component_property="children"),
    [Input(component_id="graph-x-dropdown", component_property="value"),
    Input(component_id="graph-y-dropdown", component_property="value")]
)
def update_corr(col_1_n, col_2_n):
    return f"Correlation: {correlation_calc(col_1_n, col_2_n):.3f}"

if __name__ == "__main__":
    app.run_server(debug=True)