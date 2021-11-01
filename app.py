
import datetime
from datetime import datetime, timedelta

import requests

import dash
from dash import dash_table
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

import pandas as pd

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]
external_scripts = [
    'https://www.google-analytics.com/analytics.js',
    {'src': 'https://cdn.polyfill.io/v2/polyfill.min.js'},
    {
        'src': 'https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.10/lodash.core.js',
        'integrity': 'sha256-Qqd/EfdABZUcAxjOkMi8eGEivtdTkh3b65xCZL4qAQA=',
        'crossorigin': 'anonymous'
    }
]

app = dash.Dash(__name__,
                external_scripts=external_scripts,
                external_stylesheets=external_stylesheets)


# FUNÇÕES

def buscar_candles(data_inicio, data_fim):
  mes_dict = { "01" : "JAN","02" : "FEV","03" : "MAR","04" : "ABR","05" : "MAI","06" : "JUN","07" : "JUL","08" : "AGO","09" : "SET","10" : "OUT","11" : "NOV","12" : "DEZ" }
  mes_nome_num_dict = {   "JAN" : "01","FEV" : "02","MAR" : "03","ABR" : "04","MAI" : "05","JUN" : "06","JUL" : "07","AGO" : "08","SET" : "09","OUT" : "10","NOV" : "11","DEZ" : "12"}
  submercado_bbce_dict = {0 : "SE",1 : "SU",2 : "NE",3 : "NO"}
  fonte_bbce_dict = {0 : "I0", 1 : "I5", 2 : "I1", 3 : "CON", 4 : "I8", 5 : "CQ5"}

  # recebe maturidade e retorna NUMERO de MÊS INICIAL  
  conversao_maturidade_produto_mes_num_inicial = pd.DataFrame({"M+0": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"], "M+1": ["02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "01"], "M+2": ["03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "01", "02"],  "M+3": ["04", "05", "06", "07", "08", "09", "10", "11", "12", "01", "02", "03"], "M+4": ["05", "06", "07", "08", "09", "10", "11", "12", "01", "02", "03", "04"],  "TRI+0": ["01", "04", "04", "04", "07", "07", "07", "10", "10", "10", "01", "01"], "TRI+1":["04", "07", "07", "07", "10", "10", "10", "01", "01", "01", "04", "04"], "SEM+0": ["01", "07", "07", "07", "07", "07", "07", "01", "01", "01", "01", "01"], "ANU+0":["01","01","01","01","01","01","01","01","01","01","01","01"], "ANU+1":["01","01","01","01","01","01","01","01","01","01","01","01"], "ANU+2":["01","01","01","01","01","01","01","01","01","01","01","01"]})  
  # recebe maturidade e retorna NUMERO de MÊS FINAL  
  conversao_maturidade_produto_mes_num_final = pd.DataFrame({"M+0": ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"], "M+1": ["02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "01"], "M+2": ["03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "01", "02"], "M+3": ["04", "05", "06", "07", "08", "09", "10", "11", "12", "01", "02", "03"], "M+4": ["05", "06", "07", "08", "09", "10", "11", "12", "01", "02", "03", "04"], "TRI+0": ["03", "06", "06", "06", "09", "09", "09", "12", "12", "12", "03", "03"], "TRI+1":["06", "09", "09", "09", "12", "12", "12", "03", "03", "03", "06", "06"], "SEM+0": ["06", "12", "12", "12", "12", "12", "12", "06", "06", "06", "06", "06"], "ANU+0": ["12","12","12","12","12","12","12","12","12","12","12","12"], "ANU+1": ["12","12","12","12","12","12","12","12","12","12","12","12"], "ANU+2": ["12","12","12","12","12","12","12","12","12","12","12","12"]}) 
  # recebe maturidade e retorna NOME de MÊS INICIAL
  conversao_maturidade_produto_mes_inicial = pd.DataFrame({"M+0": ["JAN", "FEV", "MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ"],"M+1": ["FEV", "MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ", "JAN"],"M+2": ["MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ", "JAN", "FEV"],"M+3": ["ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ", "JAN", "FEV", "MAR"],"M+4": ["MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ", "JAN", "FEV", "MAR", "ABR"],"TRI+0": ["JAN", "ABR", "ABR", "ABR", "JUL", "JUL", "JUL", "OUT", "OUT", "OUT", "JAN", "JAN"],"TRI+1":["ABR", "JUL", "JUL", "JUL", "OUT", "OUT", "OUT", "JAN", "JAN", "JAN", "ABR", "ABR"],"SEM+0": ["JAN", "JUL", "JUL", "JUL", "JUL", "JUL", "JUL", "JAN", "JAN", "JAN", "JAN", "JAN"],"ANU+0":["JAN","JAN","JAN","JAN","JAN","JAN","JAN","JAN","JAN","JAN","JAN","JAN"],"ANU+1":["JAN","JAN","JAN","JAN","JAN","JAN","JAN","JAN","JAN","JAN","JAN","JAN"],"ANU+2":["JAN","JAN","JAN","JAN","JAN","JAN","JAN","JAN","JAN","JAN","JAN","JAN"]})
  # recebe maturidade e retorna NOME de MÊS FINAL 
  conversao_maturidade_produto_mes_final = pd.DataFrame({"M+0": ["JAN", "FEV", "MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ"],"M+1": ["FEV", "MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ", "JAN"],"M+2": ["MAR", "ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ", "JAN", "FEV"],"M+3": ["ABR", "MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ", "JAN", "FEV", "MAR"],"M+4": ["MAI", "JUN", "JUL", "AGO", "SET", "OUT", "NOV", "DEZ", "JAN", "FEV", "MAR", "ABR"],"TRI+0": ["MAR", "JUN", "JUN", "JUN", "SET", "SET", "SET", "DEZ", "DEZ", "DEZ", "MAR", "MAR"],"TRI+1":["JUN", "SET", "SET", "SET", "DEZ", "DEZ", "DEZ", "MAR", "MAR", "MAR", "JUN", "JUN"],"SEM+0": ["JUN", "DEZ", "DEZ", "DEZ", "DEZ", "DEZ", "DEZ", "JUN", "JUN", "JUN", "JUN", "JUN"],"ANU+0": ["DEZ","DEZ","DEZ","DEZ","DEZ","DEZ","DEZ","DEZ","DEZ","DEZ","DEZ","DEZ"],"ANU+1": ["DEZ","DEZ","DEZ","DEZ","DEZ","DEZ","DEZ","DEZ","DEZ","DEZ","DEZ","DEZ"],"ANU+2": ["DEZ","DEZ","DEZ","DEZ","DEZ","DEZ","DEZ","DEZ","DEZ","DEZ","DEZ","DEZ"]})
  # recebe maturidade e retorna FATOR ADITIVO de ANO INICIAL
  conversao_maturidade_produto_ano_inicial = pd.DataFrame({"M+0": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],"M+1": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],"M+2": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],"M+3": [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1], "M+4": [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],"TRI+0": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],"TRI+1": [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],"SEM+0": [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],"ANU+0": [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],"ANU+1": [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],"ANU+2": [2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]})

  # SYSTEM
  # API dos candles
  r = requests.get("https://ogqwg4icu8.execute-api.us-west-2.amazonaws.com/PROD/balcao", headers={"date":data_inicio, "end":data_fim})

  prox_sexta = (datetime.today() + timedelta(days = (4 - datetime.today().weekday()))).strftime("%d/%m/%y")

  candles = r.json()

  candles_out = pd.DataFrame()

  # cada index_dia é um dia
  for index_dia in range(len(candles)):
    dia = candles[index_dia]["date"]
    prox_sexta = (datetime.strptime(dia, '%Y-%m-%dT%H:%M:%S'+'-03:00') + timedelta(days =(4 - datetime.strptime(dia,'%Y-%m-%dT%H:%M:%S'+'-03:00').weekday()))).strftime("%d/%m/%y")
    candles_dict = candles[index_dia]["data"]

    ano_vetor = conversao_maturidade_produto_ano_inicial.applymap(lambda x: x + int(datetime.strptime(prox_sexta, "%d/%m/%y").strftime("%y"))).loc[(conversao_maturidade_produto_mes_inicial["M+0"] == mes_dict[datetime.strptime(prox_sexta, "%d/%m/%y").strftime("%m")]),:] 
    mes_inicial_vetor = conversao_maturidade_produto_mes_inicial.loc[(conversao_maturidade_produto_mes_inicial["M+0"] == mes_dict[datetime.strptime(prox_sexta, "%d/%m/%y").strftime("%m")]),:] 
    mes_final_vetor = conversao_maturidade_produto_mes_final.loc[(conversao_maturidade_produto_mes_final["M+0"] == mes_dict[datetime.strptime(prox_sexta, "%d/%m/%y").strftime("%m")]),:] 

    # cada index_produto é um produto de uma periodicidade diferente
    for index_produto in range(len(candles_dict['M'])):

      maturidade = 'M' + "+" + str(index_produto)
      mes_ano_inicial = mes_inicial_vetor.iloc[0][maturidade] + "/" + str(ano_vetor.iloc[0][maturidade])
      mes_ano_final = mes_final_vetor.iloc[0][maturidade] + "/" + str(ano_vetor.iloc[0][maturidade])
      produto = "SE CON MEN " + mes_ano_inicial +  " - Preço Fixo"
      candles_dict['M'][index_produto].update({'MATURIDADE':maturidade, 'PRODUTO':produto, 'DATA':dia})
      candles_out = candles_out.append(candles_dict['M'][index_produto], ignore_index=True)

    for index_produto in range(len(candles_dict['TRI'])):

      maturidade = 'TRI' + "+" + str(index_produto)
      mes_ano_inicial = mes_inicial_vetor.iloc[0][maturidade] + "/" + str(ano_vetor.iloc[0][maturidade])
      mes_ano_final = mes_final_vetor.iloc[0][maturidade] + "/" + str(ano_vetor.iloc[0][maturidade])
      produto = "SE CON TRI " + mes_ano_inicial + " " + mes_ano_final + " - Preço Fixo"
      candles_dict['TRI'][index_produto].update({'MATURIDADE':maturidade, 'PRODUTO':produto, 'DATA':dia})
      candles_out = candles_out.append(candles_dict['TRI'][index_produto], ignore_index=True)

    for index_produto in range(len(candles_dict['SEM'])):

      maturidade = 'SEM' + "+" + str(index_produto)
      mes_ano_inicial = mes_inicial_vetor.iloc[0][maturidade] + "/" + str(ano_vetor.iloc[0][maturidade])
      mes_ano_final = mes_final_vetor.iloc[0][maturidade] + "/" + str(ano_vetor.iloc[0][maturidade])
      produto = "SE CON SEM " + mes_ano_inicial + " " + mes_ano_final + " - Preço Fixo"
      candles_dict['SEM'][index_produto].update({'MATURIDADE':maturidade, 'PRODUTO':produto, 'DATA':dia})
      candles_out = candles_out.append(candles_dict['SEM'][index_produto], ignore_index=True)
    
    for index_produto in range(len(candles_dict['ANU'])):

      maturidade = 'ANU' + "+" + str(index_produto)
      mes_ano_inicial = mes_inicial_vetor.iloc[0][maturidade] + "/" + str(ano_vetor.iloc[0][maturidade])
      mes_ano_final = mes_final_vetor.iloc[0][maturidade] + "/" + str(ano_vetor.iloc[0][maturidade])
      produto = "SE CON ANU " + mes_ano_inicial + " " + mes_ano_final + " - Preço Fixo"
      candles_dict['ANU'][index_produto].update({'MATURIDADE':maturidade, 'PRODUTO':produto, 'DATA':dia})
      candles_out = candles_out.append(candles_dict['ANU'][index_produto], ignore_index=True)
      
  candles_out = candles_out.loc[:,["DATA","MATURIDADE","PRODUTO", "ABE", "FEC", "MIN", "MAX", "VOL", "C", "V", "percentV"]].sort_values(by='DATA')

  return candles_out


# GLOBAIS
data_inicio = "2020-01-01"
data_fim = datetime.today().strftime("%Y-%m-%d")

df = buscar_candles(data_inicio, data_fim)

app.layout = html.Div([
    # div da tabela
    html.Div([
        dash_table.DataTable(
                            id='table',
                            columns=[{"name": i, "id": i} for i in df.columns],
                            data=df.to_dict('records'),
                            )
    ], style={"background-color":"red"}),

    # criação do evento com frequência por minuto
    dcc.Interval(id='interval1min', interval=60 * 1000, n_intervals=0, max_intervals=-1),
    # criação da tag de texto H1 do relógio de 1 minuto
    html.H1(id='label1', children=''), 

    # criação do evento com frequência a cada 10 minutos
    dcc.Interval(id='interval10min', interval=10 * 60 * 1000, n_intervals=0, max_intervals=-1),
    # criação da tag de texto H1 do relógio de 10 minutos
    html.H1(id='label2', children=''), 

    # criação do evento com frequência a cada hora
    dcc.Interval(id='interval1hr', interval= 1* 60 * 60 * 1000, n_intervals=0, max_intervals=-1),
    # criação da tag de texto H1 do relógio de 60 minutos
    html.H1(id='label3', children='')
])

##### EVENTOS DE 1 MINUTO #########################################
# evento = callback
#
@app.callback(Output('label1', 'children'),
    [Input('interval1min', 'n_intervals')])
def update_interval1min(n):
    hora = datetime.now()
    return str(hora)[0:16]

##### EVENTOS DE 10 MINUTOS #######################################
# evento = callback
# EXEMPLOS DE EVENTOS:
# - 1) Busca de dados relativos ao portfólio
@app.callback(Output('label2', 'children'),
    [Input('interval10min', 'n_intervals')])
def update_interval10min(n):
    hora = datetime.now()
    return str(hora)[0:16]

##### EVENTOS DE 1 HORA ###########################################
# evento = callback
@app.callback(Output('label3', 'children'),
    [Input('interval1hr', 'n_intervals')])
def update_interval1hr(n):
    hora = datetime.now()
    return str(hora)[0:16]

app.run_server(debug=False, port=5000)