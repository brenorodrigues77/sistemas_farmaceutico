from dash import html, dcc
from dash.dependencies import Input, Output, State
from datetime import date, datetime, timedelta
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import calendar
from globals import *
from app import app

layout = dbc.Col([
    #card de dashboards
    dbc.Row([
        dbc.Col([
            dbc.CardGroup([
                dbc.Card([
                    html.Legend('Saldos'),
                    html.H5('Dados', id='card-dashboards',style={}),
                    ],style={'padding-left': '20px', 'padding-top':'10px'}),

                dbc.Card(
                    html.Div(className="bi bi-cash-coin", style={'color': 'white', 'textalign': 'center', 'fontsize': '30', 'margin': 'auto'}),
                    color='blue',
                    style={'maxWidth': 75, 'height': 100, 'margin-left': '-10px'}
                ),
            ])
        ], width=4, ),

        #card de medicamentos
        dbc.Col([
            dbc.CardGroup([
                dbc.Card([
                    html.Legend('Medicamentos'),
                    html.H5('Dados', id='card-medicamentos',style={}),
                    ],style={'padding-left': '20px', 'padding-top':'10px'}),

                dbc.Card(
                    html.Div(className="bi bi-capsule", style={'color': 'white', 'textalign': 'center', 'fontsize': '30', 'margin': 'auto'}),
                    color='warning',
                    style={'maxWidth': 75, 'height': 100, 'margin-left': '-10px'}
                ),
            ])
        ], width=4),

        #card de receitas
        dbc.Col([
            dbc.CardGroup([
                dbc.Card([
                    html.Legend('Receitas'),
                    html.H5('Dados', id='card-receitas', style={}),
                ], style={'padding-left': '20px', 'padding-top': '10px' }),

                dbc.Card(
                    html.Div(className='bi bi-file-earmark-medical-fill', style={'color': 'white', 'textalign': 'center', 'fontsize': '30', 'margin': 'auto'}),
                    color='green',
                    style={'maxWidth': 75, 'height': 100, 'margin-left': '-10px'},
                ),
            ])
        ], width=4)
    ],style={'margin': '20px'} ),

    #linha dos filtros 
    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.Legend('Filtros', className='card-title'),
                html.Label('Filtrar Medicamentos'),
                html.Div(
                    dcc.Dropdown(
                    id='dropdown-medicamentos',
                    clearable=False,
                    style={'width': '100%'},
                    persistence=True,
                    persistence_type='session',
                    multi=True),
                ),
                #filtros de receitas
                html.Label('Filtrar Receitas'),
                html.Div(
                    dcc.Dropdown(
                    id='dropdown-receitas',
                    clearable=False,
                    style={'width': '100%'},
                    persistence=True,
                    persistence_type='session',
                    multi=True),
                ),
                #calendario dos filtros
                html.Legend('Periodo de Analise por Data', style={'margin-top': '10px'}),
                dcc.DatePickerRange(
                    month_format='Do MMM, YY',
                    end_date_placeholder_text='Data...',
                    start_date=datetime(2024, 1, 1).date(),
                    end_date=datetime.today() + timedelta(days=31),
                    updatemode='singledate',
                    id='date-picker-config',
                    style={'z-index': '100'},
                )
            ], style={'height': '100%', 'padding': '20px'})
        ], width=4),

        #grafico ao lado dos filtros
        dbc.Col(
            dbc.Card(dcc.Graph(id='grafico1'), style={'height': '100%', 'padding': '10px'}), width=8
        )
    ], style={'margin': '10px'}),

        #graficos abaixo dos filtros
    dbc.Row([
        dbc.Col(dbc.Card(dcc.Graph(id='grafico2'), style={'padding': '10px'}), width=6),
        dbc.Col(dbc.Card(dcc.Graph(id='grafico3'), style={'padding': '10px'}), width=3),
        dbc.Col(dbc.Card(dcc.Graph(id='grafico4'), style={'padding': '10px'}), width=3),
    ],)
]) 