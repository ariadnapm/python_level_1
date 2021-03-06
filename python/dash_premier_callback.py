import dash
import dash_html_components as html 
import dash_core_components as dcc

app.layout = html.Div([
    dcc.Input(id="my-id", value="initial value", type="text"),
    html.Div(id="my-div")
])

@app.callback(
    Output(component_id="my-div", component_property="children"),
    [Input(component_id="my-id", component_property="value")]
)

def update_output_div(input_value):
    return "Votre texte: " + input_value