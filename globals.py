import pandas as pd
import os

if ('df_receitas.csv' in os.listdir()) and ('df_medicamentos.csv' in os.listdir()):
    df_receitas = pd.read_csv('df_receitas.csv', index_col=0, parse_dates=True)
    df_medicamentos = pd.read_csv('df_medicamentos.csv', index_col=0, parses_dates=True)

else:
    data_stracture = {'valor':[],
    'efetuado':[],
    'tipo': [],
    'data':[],
    'categoria':[],
    'descrição':[],
    }

    df_receitas = pd.DataFrame(data_stracture)
    df_medicamentos = pd.DataFrame(data_stracture)
    df_receitas.to_csv('df_receitas.csv')
    df_medicamentos.to_csv('df.medicamentos.csv')


if ('df_categoria_receitas.csv' in os.listdir()) and ('df_categoria_medicamentos.csv' in os.listdir()):
    df_categoria_receitas = pd.read_csv('df_categoria_receitas.csv', index_col=0,)
    df_categoria_medicamentos = pd.read_csv('df_categoria_medicamentos.csv', index_col=0,)
    categoria_receitas = df_categoria_receitas.values.tolist()
    categoria_medicamentos = df_categoria_medicamentos.values.tolist()

else: 
    categoria_receitas = {'categoria_receita': ['Valor', 'Nome',]}
    categoria_medicamentos = {'categoria_medicamentos': ['Valor', 'Nome',]}

    df_categoria_receitas = pd.DataFrame(categoria_receitas)
    df_categoria_medicamentos = pd.DataFrame(categoria_medicamentos)
    df_categoria_receitas.to_csv('df_categoria_receitas.csv')
    df_categoria_medicamentos.to_csv('df_categoria_medicamentos.csv')
