import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app
from datetime import datetime, date
import plotly.express as px
import numpy as np
import pandas as pd

#=====Layout

#logo e nome
layout = dbc.Card([
            dbc.Col([
                dbc.Card(
                    children=[html.Img(src='./assets/brasao-do-acre.png')],
                    style={'background-color': 'transparent', 'border-color': 'transparent', 'width': '70px', 'heigth': '70px'}),
                    html.H3('Sistema de Receitas', className='text-primary'),
                    html.P('SESACRE', className='text-info'),
                    html.Hr(),

            #perfil
            dbc.Button(id='perfil',
                    children=[html.Img(src='./assets/icon.png', id='icone_perfil', alt='avatar', className='perfil_avatar')],
                    style={'background-color': 'transparent', 'border-color': 'transparent',}),
                    
            #botoes para modais
            dbc.Col([
                dbc.Col([
                    dbc.Button(color='success', id='botao-receita', children=['Receitas'])
                    ], width=4, style={'margin': '5px'}),
                dbc.Col(
                    [dbc.Button(color='danger', id='botao-medicamentos', children=['Medicamentos'])
                    ], width=4, style={'margin': '5px' }),
                ]),
        
            #modal da receita
            dbc.Modal([
                dbc.ModalHeader(dbc.ModalTitle('Receitas')),
                dbc.ModalBody([
                    dbc.Row([
                        dbc.Col([
                            dbc.Label('Descrição'),
                            dbc.Input(placeholder='Descrição', id='descricao-modal1'),
                            
                        ], width=6),
                        dbc.Col([
                            dbc.Label('Valor'),
                            dbc.Input(placeholder='Valor', id='valor-modal1', value="")
                        ], width=3),
                    ]),

                    dbc.Row([
                        dbc.Col([
                            dbc.Label('Data:'),
                            dcc.DatePickerSingle(id="data-modal1",
                            min_date_allowed=date(2024,4,1),
                            max_date_allowed=date(2029,12,31),
                            date=datetime.today(),
                            style={'width': '100%'}
                            ),
                        ],width=4 , style={'margin-top': '10px'}),

                        dbc.Col([
                            dbc.Label('Outros'),
                            dbc.Checklist(
                                options=[],
                                value=[],
                                id='outros-receita',
                                switch=True
                            ),
                        ],width=4 , style={'margin-top': '10px'}),

                        dbc.Col([
                            html.Label('Categoria da Receita'),
                            dbc.Select(
                                id='selecao-receita',
                                options=[],
                                value=[]
                                ),
                        ],width=4 , style={'margin-top': '10px'})
                    ]),

                    dbc.Row([
                        dbc.Accordion([
                            dbc.AccordionItem(children=[
                                dbc.Row([
                                    dbc.Col([
                                       html.Legend('Adicionar Categoria', style={'color': 'green'}),
                                       dbc.Input()
                                    ])
                                ])
                            ])
                        ])
                    ])
                ]),
            ], id='modal-botao1'),

            #modal dos medicamentos
            dbc.Modal([
                dbc.ModalHeader(dbc.ModalTitle('Medicamentos')),
                dbc.ModalBody([
                
                ]),
            ], id='modal-botao2'),
            
            html.Hr(),

            #seção de navegação
            dbc.Nav([
                dbc.NavLink('Dashboard', href='/dashboards', active='exact'),
                dbc.NavLink('Medicamentos', href='/medicamentos', active='exact'),
                dbc.NavLink('Receitas', href='/receitas', active='exact'),
            ], vertical=True, pills=True, id='nav_bottons', style={'margin-bottom': '50px'}),
            ], id='sidebar_completa')
            ], style={'margin-top': '20px'}
        )



#========CALLBACKS
#callback modal receita
@app.callback(
        Output('modal-botao1', 'is_open'),
        Input('botao-receita', 'n_clicks'),
        State('modal-botao1', 'is_open'),
    )
def toggle_modal(n1, is_open):
    if n1: 
        return not is_open

#callback modal medicamentos
@app.callback(
    Output('modal-botao2', 'is_open'),
    Input('botao-medicamentos', 'n_clicks'),
    State('modal-botao2', 'is_open'),
)

def toggle_modal(n1, is_open):
    if n1:
        return not is_open
