import dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc

# Import layout and callbacks from Overview
from Overview import layout as overview_layout, register_callbacks

# Initialize Dash app
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Sidebar layout
sidebar = html.Div([
    html.H2("Valenta", className="text-white text-center mt-4"),
    html.Hr(),
    dbc.Nav([
        dbc.NavLink("Overview", href="/", active="exact"),
    ], vertical=True, pills=True),
], style={"backgroundColor": "#1e1e1e", "height": "100vh", "padding": "20px"})

# App layout
app.layout = dbc.Container([
    dcc.Location(id="url"),
    dbc.Row([
        dbc.Col(sidebar, width=2),
        dbc.Col(html.Div(id="page-content"), width=10)
    ])
], fluid=True, style={"padding": "0"})

# Route handling
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/" or pathname == "/overview":
        return overview_layout
    return html.H3("404 - Page Not Found", className="text-danger text-center mt-5")

# Register app-specific callbacks
register_callbacks(app)

# Local development entry point
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
