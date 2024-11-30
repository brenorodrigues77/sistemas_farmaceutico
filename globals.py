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

    df_receitas = pd.DataFrame (data_stracture)
    df_medicamentos = pd.DataFrame (data_stracture)