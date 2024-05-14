from dash import Dash, html
import dash_cytoscape as cyto

app = Dash(__name__)

app.layout = html.Div([
    html.P("Dash Cytoscape:"),
    cyto.Cytoscape(
        id='cytoscape',
        elements=[
            {'data': {'id': 'SS', 'label': 'San Sebastian'}}, 
            {'data': {'id': 'LE', 'label': 'León'}}, 
            {'data': {'id': 'MA', 'label': 'Madrid'}},
            {'data': {'source': 'SS', 'target': 'LE'}}, 
            {'data': {'source': 'SS', 'target': 'MA'}}
        ],
        layout={'name': 'breadthfirst'},
        style={'width': '400px', 'height': '500px'}
    )
])


app.run_server(debug=True)