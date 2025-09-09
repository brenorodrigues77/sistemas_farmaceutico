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

# =====Layout

# logo e nome
layout = dbc.Card([
    dbc.Col([
        dbc.Card(
            children=[html.Img(src='')],
            style={'background-color': 'transparent', 'border-color': 'transparent', 'width': '70px', 'heigth': '70px'}),
        html.H3('Sistema de Farmácia', className='text-primary'),
        html.P('Farmácia', className='text-info'),
        html.Hr(),

        # perfil
        dbc.Button(id='perfil',
                   children=[html.Img(
                       src='./assets/icon.png', id='icone_perfil', alt='avatar', className='perfil_avatar')],
                   style={'background-color': 'transparent', 'border-color': 'transparent', }),

        # botoes para modais
        dbc.Col([
            dbc.Col([
                dbc.Button(color='success', id='botao-receita',
                           children=['Receitas'])
            ], width=4, style={'margin': '5px'}),
            dbc.Col(
                [dbc.Button(color='danger', id='botao-medicamentos', children=['Medicamentos'])
                 ], width=4, style={'margin': '5px'}),
        ]),

        # modal da receita
        dbc.Modal([
            dbc.ModalHeader(dbc.ModalTitle('Receitas')),
            dbc.ModalBody([
                dbc.Row([
                    dbc.Col([
                        dbc.Label('Descrição'),
                        dbc.Input(placeholder='Descrição',
                                  id='descricao-modal1'),
                    ], width=6),
                    dbc.Col([
                        dbc.Label('Valor'),
                        dbc.Input(placeholder='Valor',
                                  id='valor-modal1', value="")
                    ], width=3),
                ]),

                dbc.Row([
                    dbc.Col([
                        dbc.Label('Data:'),
                        dcc.DatePickerSingle(id="data-modal1",
                                             min_date_allowed=date(
                                                 2024, 4, 1),
                                             max_date_allowed=date(
                                                 2029, 12, 31),
                                             date=datetime.today(),
                                             style={'width': '100%'}
                                             ),
                    ], width=4, style={'margin-top': '10px'}),

                    dbc.Col([
                        dbc.Label('Outros'),
                        dbc.Checklist(
                            options=[{'label': ' Receita Nova', 'value': '1'},
                                     {'label': 'Receita Recorrente', 'value': '0'}],
                            value=[1],
                            id='outra-receita',
                            switch=True
                        ),
                    ], width=4, style={'margin-top': '10px'}),

                    dbc.Col([
                        html.Label('Categoria'),
                        dbc.Select(id='selecao-receita',
                                   options=[{'label': i, 'value': i}
                                            for i in categoria_receitas],
                                   value=categoria_receitas[0],
                                   ),
                    ], width=4, style={'margin-top': '10px'})
                ]),

                dbc.Row([
                    dbc.Accordion([
                        dbc.AccordionItem(children=[
                            dbc.Row([
                                dbc.Col([
                                    html.Legend('Adicionar Categoria', style={
                                                'color': 'green'}),
                                    dbc.Input(
                                        type='text', placeholder='Nova Categoria', id='nova-categoria-receitas', value=""),
                                    html.Br(),
                                    dbc.Button('Adicionar', className='btn btn-success',
                                               id='botao-adicionar-receita', style={'margin-top': '20px'}),
                                    html.Br(),
                                    html.Div(
                                        id='divisao-categoria-receita'),
                                ], width=6),
                                dbc.Col([
                                    html.Legend('Excluir Categorias', style={
                                                'color': 'red', 'margin-left': '20px'}),
                                    dbc.Checklist(id='selecao-checklist-receitas',
                                                  options=[{'label': i, 'value': i}
                                                           for i in categoria_receitas],
                                                  value=[],
                                                  label_checked_style={
                                                      'color': 'red'},
                                                  input_checked_style={
                                                      'backgroundcolor': 'blue', 'bordercolor': 'red'}
                                                  ),
                                    dbc.Button('Remover', color='danger', id='remover-categoria-receita', style={
                                        'margin-top': '23%', 'margin-left': '20px'})
                                ], width=6)
                            ])
                        ], title='Adicionar e Remover Categorias')
                    ], flush=True, start_collapsed=True, id='adicionar-remover', style={'margin-top': '20px'}),

                    html.Div(id='teste-receita',
                             style={'padding-top': '20px'}),
                    dbc.ModalFooter([
                        dbc.Button('Adicionar Receita',
                                   id='salvar-receita', color='success'),
                        dbc.Popover(dbc.PopoverBody(
                                    'Receita Salva'), target='salvar_receita', placement='left', trigger='click'),
                    ])
                ], style={'margin-top': '25px'}),
            ]),
        ], id='modal-botao1', style={'backgroundcolor': 'rgba(17, 140,79, 0.05)'}, size='lg', is_open=False, centered=True, backdrop=True),

        # modal dos medicamentos
        dbc.Modal([
            dbc.ModalHeader(dbc.ModalTitle('Medicamentos')),
            dbc.ModalBody([
                dbc.Row([
                    dbc.Col([
                        dbc.Label('Descrição'),
                        dbc.Input(placeholder='Descrição',
                                  id='descricao-modal2'),

                    ], width=6),
                    dbc.Col([
                        dbc.Label('Valor'),
                        dbc.Input(placeholder='Valor',
                                  id='valor-modal2', value="")
                    ], width=3),
                ]),

                dbc.Row([
                    dbc.Col([
                        dbc.Label('Data:'),
                        dcc.DatePickerSingle(id="data-modal2",
                                             min_date_allowed=date(
                                                 2024, 4, 1),
                                             max_date_allowed=date(
                                                 2029, 12, 31),
                                             date=datetime.today(),
                                             style={'width': '100%'}
                                             ),
                    ], width=4, style={'margin-top': '10px'}),

                    dbc.Col([
                        dbc.Label('Outros'),
                        dbc.Checklist(
                            options=[{'label': 'Medicamento Novo', 'value': '1'},
                                     {'label': 'Medicamento Recorrente', 'value': '0'}],
                            value=[1],
                            id='outros-medicamento',
                            switch=True
                        ),
                    ], width=4, style={'margin-top': '10px'}),

                    dbc.Col([
                        html.Label('Categoria'),
                        dbc.Select(
                            id='selecao-medicamentos',
                            options=[{'label': i, 'value': i}
                                     for i in categoria_medicamentos],
                            value=categoria_medicamentos[0],
                        ),
                    ], width=4, style={'margin-top': '10px'})
                ]),

                dbc.Row([
                    dbc.Accordion([
                        dbc.AccordionItem(children=[
                            dbc.Row([
                                dbc.Col([
                                    html.Legend('Adicionar Categoria', style={
                                                'color': 'green'}),
                                    dbc.Input(
                                        type='text', placeholder='Nova Categoria', id='nova-categoria-medicamentos', value=""),
                                    html.Br(),
                                    dbc.Button('Adicionar', className='btn btn-success',
                                               id='botao-adicionar-medicamentos', style={'margin-top': '20px'}),
                                    html.Br(),
                                    html.Div(
                                        id='divisao-categoria-medicamentos'),
                                ], width=6),
                                dbc.Col([
                                    html.Legend('Excluir Categorias', style={
                                                'color': 'red', 'margin-left': '20px'}),
                                    dbc.Checklist(id='selecao-checklist-medicamentos',
                                                  options=[{'label': i, 'value': i}
                                                           for i in categoria_medicamentos],
                                                  value=[],
                                                  label_checked_style={
                                                      'color': 'red'},
                                                  input_checked_style={
                                                      'backgroundcolor': 'blue', 'bordercolor': 'red'}
                                                  ),
                                    dbc.Button('Remover', color='danger', id='remover-categoria-medicamentos', style={
                                        'margin-top': '23%', 'margin-left': '20px'})
                                ], width=6)
                            ])
                        ], title='Adicionar e Remover Categorias')
                    ], flush=True, start_collapsed=True, id='adicionar-remover', style={'margin-top': '20px'}),

                    html.Div(id='teste-medicamentos',
                             style={'padding-top': '20px'}),
                    dbc.ModalFooter([
                        dbc.Button('Adicionar medicamentos',
                                   id='salvar-medicamento', color='success'),
                        dbc.Popover(dbc.PopoverBody(
                                    'Medicamentos Salvo'), target='salvar_medicamento', placement='left', trigger='click')
                    ])
                ], style={'margin-top': '25px'}),
            ]),
        ], id='modal-botao2', style={'backgroundcolor': 'rgba(17, 140,79, 0.05)'}, size='lg', is_open=False, centered=True, backdrop=True),


        html.Hr(),

        # seção de navegação
        dbc.Nav([
            dbc.NavLink('Dashboard', href='/dashboards',
                        active='exact'),
            dbc.NavLink('Receitas', href='/receitas', active='exact'),
            dbc.NavLink('Medicamentos', href='/medicamentos',
                        active='exact'),
        ], vertical=True, pills=True, id='nav_bottons', style={'margin-bottom': '50px'}),
    ], id='sidebar_completa')
], style={'margin-top': '20px'}
)

# ========CALLBACKS

# callback modal receita


@app.callback(
    Output('modal-botao1', 'is_open'),
    Input('botao-receita', 'n_clicks'),
    State('modal-botao1', 'is_open'),
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open


# callback modal medicamentos
@app.callback(
    Output('modal-botao2', 'is_open'),
    Input('botao-medicamentos', 'n_clicks'),
    State('modal-botao2', 'is_open'),
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open


# callback salvar receita
@app.callback(
    Output('memoria-receitas', 'data'),
    Input('salvar-receita', 'n_clicks'),

    [State('descricao-modal1', 'value'),
     State('valor-modal1', 'value'),
     State('data-modal1', 'date'),
     State('outra-receita', 'value'),
     State('selecao-receita', 'value'),
     State('memoria-receitas', 'data'),
     ],
)
def salvar_receita(n_clicks, descricao, valor, data, outra_receita, categoria_receita, memoria_receitas):
    # Define the columns for the DataFrame
    columns = ['valor', 'recebido', 'fixo',
               'data', 'categoria_receita', 'descricao']

    # Create the DataFrame with the given columns, ensuring that the column names are set
    df_receitas = pd.DataFrame(memoria_receitas, columns=columns)

    if n_clicks and not (valor == "" or valor == None):
        valor = round(float(valor), 2)
        data = pd.to_datetime(data).date()
        categoria_receita = categoria_receita[0] if type(
            categoria_receita) == list else categoria_receita
        recebido = 1 if 1 in outra_receita else 0
        fixo = 1 if 2 in outra_receita else 0

        # Add a new row to the DataFrame
        df_receitas.loc[df_receitas.shape[0]] = [
            valor, recebido, fixo, data, categoria_receita, descricao]

        # Save the DataFrame to a CSV file
        df_receitas.to_csv('df_receitas.csv', index=False)

    # Convert the DataFrame to a dictionary and return it
    # Changed to orient='records' for a better structure
    data_return = df_receitas.to_dict(orient='records')
    return data_return


# == callback modal medicamentos
@app.callback(
    Output('memoria-medicamentos', 'data'),
    Input('salvar-medicamento', 'n_clicks'),

    [State('descricao-modal2', 'value'),
     State('valor-modal2', 'value'),
     State('data-modal2', 'date'),
     State('outros-medicamento', 'value'),
     State('selecao-medicamentos', 'value'),
     State('memoria-medicamentos', 'data'),
     ],
)
def salvar_receita(n_clicks, descricao, valor, data, outra_receita, categoria_receita, memoria_medicamentos):

    columns = ['valor', 'recebido', 'fixo',
               'data', 'categoria_receita', 'descricao']

    df_medicamentos = pd.DataFrame(memoria_medicamentos, columns=columns)

    if n_clicks and not (valor == "" or valor == None):
        valor = round(float(valor), 2)
        data = pd.to_datetime(data).date()
        categoria_receita = categoria_receita[0] if type(
            categoria_receita) == list else categoria_receita
        recebido = 1 if 1 in outra_receita else 0
        fixo = 1 if 2 in outra_receita else 0

        # Add a new row to the DataFrame
        df_medicamentos.loc[df_medicamentos.shape[0]] = [
            valor, recebido, fixo, data, categoria_receita, descricao]

        # Save the DataFrame to a CSV file
        df_medicamentos.to_csv('df_medicamentos.csv', index=False)

    data_return = df_medicamentos.to_dict(orient='records')
    return data_return


@app.callback(
    [Output('selecao-medicamentos', 'options'),
     Output('selecao-checklist-medicamentos', 'value'),
     Output('selecao-checklist-medicamentos', 'options'),
     Output('memoria-categoria-medicamentos', 'data'),
     ],

    [Input('remover-categoria-medicamentos', 'n_clicks'),
     Input('botao-adicionar-medicamentos', 'n_clicks'),
     ],

    [State('nova-categoria-medicamentos', 'value'),
     State('selecao-checklist-medicamentos', 'value'),
     State('memoria-categoria-medicamentos', 'data'),
     ],
)
def adicionar_categoria_medicamentos(n, n2, nova_categoria, selecao_checklist, memoria_categoria):

    categoria_medicamentos = list(memoria_categoria['categoria'].values())

    if n and not (nova_categoria == "" or nova_categoria == None):
        categoria_medicamentos = categoria_medicamentos + \
            [nova_categoria] if nova_categoria not in categoria_medicamentos else categoria_medicamentos

    if n2:
        if len(selecao_checklist) > 0:
            categoria_medicamentos = [
                i for i in categoria_medicamentos if i not in selecao_checklist]

    opt_medicamentos = [{'label': i, 'value': i}
                        for i in categoria_medicamentos]
    df_categoria_medicamentos = pd.DataFrame(
        categoria_medicamentos, columns=['categoria'])
    df_categoria_medicamentos.to_csv('df_categoria_medicamentos.csv')
    df_return = df_categoria_medicamentos.to_dict()

    return [opt_medicamentos, [], opt_medicamentos, df_return]
