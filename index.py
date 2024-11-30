from dash import html, dcc
from dash.dependencies import Input, Output
import dash
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

from app import *
from components import sidebar, dashboards, medicamentos, receitas

#=== layout do site
content = html.Div(id='page-content')

app.layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col([
            dcc.Location(id='url'),
            sidebar.layout
        ], md=2,),
        dbc.Col([
            content
        ], md=10,),
    ])

], fluid=True,)

@app.callback(Output('page-content', 'children'), [Input('url','pathname')])
def page_render(pathname):
    if pathname == '/' or pathname == '/dashboards':
        return dashboards.layout
    
    if pathname == '/medicamentos':
        return medicamentos.layout
    
    if pathname == '/receitas':
        return receitas.layout


if __name__ == '__main__':
    app.run_server(port=8080, debug=True)


