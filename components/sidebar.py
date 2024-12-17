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
from globals import *

#=====Layout

#logo e nome
layout = dbc.Card([
            dbc.Col([
                dbc.Card(
                    children=[html.Img(src='')],
                    style={'background-color': 'transparent', 'border-color': 'transparent', 'width': '70px', 'heigth': '70px'}),
                    html.H3('Sistema de Farmácia', className='text-primary'),
                    html.P('Farmácia', className='text-info'),
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
                                options=[{'label':' Receita Nova', 'value': '1'},
                                         {'label': 'Receita Recorrente', 'value':'0'}],
                                value=[1],
                                id='outra-receita',
                                switch=True
                            ),
                        ],width=4 , style={'margin-top': '10px'}),

                        dbc.Col([
                            html.Label('Categoria'),
                            dbc.Select(id='selecao-receita',
                                options=[{'label': i, 'value': i} for i in categoria_receitas],
                                value=[],
                                ),
                        ],width=4 , style={'margin-top': '10px'})
                    ]),

                    dbc.Row([
                        dbc.Accordion([
                            dbc.AccordionItem(children=[
                                dbc.Row([
                                    dbc.Col([
                                       html.Legend('Adicionar Categoria', style={'color': 'green'}),
                                       dbc.Input(type='text',placeholder='Nova Categoria',id='nova-categoria', value=""),
                                       html.Br(),
                                       dbc.Button('Adicionar',className='btn btn-success',id='botao-adicionar-receita',style={'margin-top': '20px'}),
                                       html.Br(),
                                       html.Div(id='divisao-categoria-receita'),
                                    ], width=6),
                                    dbc.Col([
                                        html.Legend('Excluir Categorias',style={'color': 'red', 'margin-left': '20px'}),
                                        dbc.Checklist(id='selecao-checklist', 
                                                      options=[],
                                                      value=[],
                                                      label_checked_style={'color': 'red'},
                                                      input_checked_style={'backgroundcolor':'blue','bordercolor': 'red'}                                                     
                                                    ),
                                    dbc.Button('Remover',color='danger', id='remover-categoria-receita', style={'margin-top': '23%', 'margin-left': '20px'})
                                    ],width=6)
                                ])
                            ], title='Adicionar e Remover Categorias')
                        ], flush=True, start_collapsed=True, id='adicionar-remover' ,style={'margin-top': '20px'}),

                        html.Div(id='teste-receita', style={'padding-top': '20px'}),
                        dbc.ModalFooter([
                            dbc.Button('Adicionar Receita', id='salvar-receita', color='success'),
                            dbc.Popover(dbc.PopoverBody('Receita Salva'), target='salvar_receita', placement='left', trigger='click')
                        ])
                    ], style={'margin-top': '25px'}),
                ]),
            ], id='modal-botao1', style={'backgroundcolor': 'rgba(17, 140,79, 0.05)' }, size='lg', is_open=False, centered=True, backdrop=True ),

            #modal dos medicamentos
            dbc.Modal([
                dbc.ModalHeader(dbc.ModalTitle('Medicamentos')),
                dbc.ModalBody([
                    dbc.Row([
                        dbc.Col([
                            dbc.Label('Descrição'),
                            dbc.Input(placeholder='Descrição', id='descricao-modal2'),
                            
                        ], width=6),
                        dbc.Col([
                            dbc.Label('Valor'),
                            dbc.Input(placeholder='Valor', id='valor-modal2', value="")
                        ], width=3),
                    ]),

                    dbc.Row([
                        dbc.Col([
                            dbc.Label('Data:'),
                            dcc.DatePickerSingle(id="data-modal2",
                            min_date_allowed=date(2024,4,1),
                            max_date_allowed=date(2029,12,31),
                            date=datetime.today(),
                            style={'width': '100%'}
                            ),
                        ],width=4 , style={'margin-top': '10px'}),

                        dbc.Col([
                            dbc.Label('Outros'),
                            dbc.Checklist(
                                options=[{'label':'Medicamento Novo', 'value': '1'},
                                         {'label': 'Medicamento Recorrente', 'value':'0'}],
                                value=[1],
                                id='outros-medicamento',
                                switch=True
                            ),
                        ],width=4 , style={'margin-top': '10px'}),

                        dbc.Col([
                            html.Label('Categoria'),
                            dbc.Select(
                                id='selecao-medicamentos',
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
                                       dbc.Input(type='text',placeholder='Nova Categoria',id='nova-categoria', value=""),
                                       html.Br(),
                                       dbc.Button('Adicionar',className='btn btn-success',id='botao-adicionar-medicamentos',style={'margin-top': '20px'}),
                                       html.Br(),
                                       html.Div(id='divisao-categoria-medicamentos'),
                                    ], width=6),
                                    dbc.Col([
                                        html.Legend('Excluir Categorias',style={'color': 'red', 'margin-left': '20px'}),
                                        dbc.Checklist(id='selecao-checklist', 
                                                      options=[],
                                                      value=[],
                                                      label_checked_style={'color': 'red'},
                                                      input_checked_style={'backgroundcolor':'blue','bordercolor': 'red'}                                                     
                                                    ),
                                    dbc.Button('Remover',color='danger', id='remover-categoria-medicamentos', style={'margin-top': '23%', 'margin-left': '20px'})
                                    ],width=6)
                                ])
                            ], title='Adicionar e Remover Categorias')
                        ], flush=True, start_collapsed=True, id='adicionar-remover' ,style={'margin-top': '20px'}),

                        html.Div(id='teste-medicamentos', style={'padding-top': '20px'}),
                        dbc.ModalFooter([
                            dbc.Button('Adicionar medicamentos', id='salvar-receita', color='success'),
                            dbc.Popover(dbc.PopoverBody('Medicamentos Salvo'), target='salvar_medicamento', placement='left', trigger='click')
                        ])
                    ], style={'margin-top': '25px'}),
                ]),
            ], id='modal-botao2', style={'backgroundcolor': 'rgba(17, 140,79, 0.05)' }, size='lg', is_open=False, centered=True, backdrop=True ),

            
            html.Hr(),

            #seção de navegação
            dbc.Nav([
                dbc.NavLink('Dashboard', href='/dashboards', active='exact'),
                dbc.NavLink('Receitas', href='/receitas', active='exact'),
                dbc.NavLink('Medicamentos', href='/medicamentos', active='exact'),
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
