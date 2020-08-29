import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from graphs import make_country_graph, get_data_options

app = dash.Dash(__name__)

graph_card = html.Div([
    dcc.Graph(id="graph-countries", figure=make_country_graph())
], className="card graph-card")

data_card = html.Div([
    html.Div(
        html.H3("Data source"),
        className="card-header"
    ),
    html.Div([
        html.Div([
            html.Span("X:", className="dropdown-label"),
            dcc.Dropdown(
                id="graph-x-value",
                options=get_data_options(),
                value="GDP - per capita"
            )
        ], className="clearfix"),
        html.Div([
            html.Span("Y:", className="dropdown-label"),
            dcc.Dropdown(
                id="graph-y-value",
                options=get_data_options(),
                value="Life expectancy at birth(years)"
            )
        ], className="clearfix"),
    ], className="card-content")
], className="card data-card")

polynomial_card = html.Div([
    html.Div(
        html.H3("Polynomial regression degree"),
        className="card-header"
    ),
    html.Div(
        dcc.Slider(
            id="slider-degree",
            min=0,
            max=15,
            marks={i: str(i) for i in range(16)},
            value=3
        ),
        className="card-content"
    )
], className="card polynomial-card")

app.layout = html.Div([
    graph_card,
    data_card,
    polynomial_card,
])

@app.callback(
    Output(component_id="graph-countries", component_property="figure"),
    [Input(component_id="slider-degree", component_property="value"),
     Input(component_id="graph-x-value", component_property="value"),
     Input(component_id="graph-y-value", component_property="value")]
)
def update_graph(degree, data_x_name, data_y_name):
    return make_country_graph(degree, data_x_name, data_y_name)

if __name__ == "__main__":
    app.run_server(debug=True)
