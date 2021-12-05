import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
# manipular dataframe
import pandas as pd
# manipular tabela
from dash import dash_table
# plotar gráficos
import plotly.graph_objects as go
from plotly.subplots import make_subplots

######################################################################################
################################# INICIALIZAÇÃO APP ##################################
######################################################################################

app = dash.Dash(__name__, 
                suppress_callback_exceptions=True, # por termos callbacks de elementos 
                                                   # que não existem no app.layout,
                                                   # isso gera alertas sendo útil 
                                                   # para supressão dos mesmos 
                external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME])
                                                   # utilizamos bootstrap no navbar

server = app.server
######################################################################################
###################################### NAVBAR ########################################
######################################################################################
navbar = dbc.Navbar(
    dbc.Container([
        dbc.Row([
                dbc.Col(
                    dbc.Row([
                        html.Div(dbc.Button(html.Span([html.I(id="span_botao",className="fas fa-bars ml-2")]), outline=True, color="info", className="d-grid gap-2 d-md-block", id="btn_sidebar"),style={"width":"30%", "color":"#C1B9AE"}),
                        html.Div("MEZ",style={"width":"50%", "color":"#C1B9AE"})],
                        justify="center",align="center",
                    ),
                    width=2,xl = 2,md = 3, xs = 4,),
                dbc.Col(html.Div(""),
                   width=9,xl=9,md = 7,xs = 5),
                dbc.Col(                    
                    dbc.Row([html.Div(dbc.NavItem(dbc.NavLink("KPIs", href="/page-kpis",style={"color":"#C1B9AE"} )),style={"width":"50%"}),
                             html.Div(dbc.DropdownMenu(
                                                        children=[
                                                            dbc.DropdownMenuItem("Página 1", href="/page-1"),
                                                            dbc.DropdownMenuItem("Página 2", href="/page-2"),
                                                            dbc.DropdownMenuItem("Página 3", href="/page-3"),
                                                            dbc.DropdownMenuItem("Página de KPIs", href="/page-kpis"),
                                                        ],
                                                        group=True,
                                                        in_navbar=True,
                                                        label="Status",
                                                        color="info", className="m-1",
                                                        align_end = True,
                                                       ),style={"width":"50%", "color":"#ffffff"})],justify="center",align="center"),
                    width=1,  
                    xl = 1,
                    md = 2,
                    xs = 3,
                    )],align="center",
                ),

        ],
        fluid="center",
        style={"width":"92%"},
        ),
    color="dark",
    dark=True,
    fixed="top",
    style={"z-index":2}
)

######################################################################################
###################################### FOOTER ########################################
######################################################################################

footer = html.Footer(
  dbc.Row([html.Div(html.Img(src='http://mezenergia.com/wp-content/uploads/2020/09/avada-taxi-logo@2x-retina.png',style={"height":"3em"}),style={"text-align":"center"})],
                          justify="center",
                   ), style={"position": "fixed","left": "0","bottom": "0","justify-content": "bottom","text-align":"center", "width": "100%","background-color": "#212529","color": "#c1b9a3"} )

######################################################################################
###################################### SIDEBAR #######################################
######################################################################################

SIDEBAR_STYLE = {
    "position": "fixed",
    "top":"3.5rem",
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "height": "100%",
    "z-index": 1,
    "overflow":"auto",
    "transition": "all 0.5s",
    "padding": "0rem 1rem",
    "background-color": "#f8f9fa",}
SIDEBAR_HIDDEN = {
    "top":"3.5rem",
    "position": "fixed",
    "left": "-16rem",
    "bottom": 0,
    "width": "16rem",
    "height": "100%",
    "z-index": 2,
    "overflow":"auto",
    "transition": "all 0.5s",
    "padding": "0rem 1rem",
    "background-color": "#f8f9fa",}

sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P(
            "A simple sidebar layout with navigation links", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Página 1", href="/page-1", id="page-1-link"),
                dbc.NavLink("Página 2", href="/page-2", id="page-2-link"),
                dbc.NavLink("Página 3", href="/page-3", id="page-3-link"),
                dbc.NavLink("Página de KPIs", href="/page-kpis", id="page-kpis-link")            ],
            vertical=True,
            pills=True,
        ),
    ],
    id="sidebar",
    style=SIDEBAR_STYLE,)

######################################################################################
################################# CONTEÚDO DA PÁGINA #################################
######################################################################################

CONTENT_STYLE = {
    "position": "relative",
    "top":"4rem",
    "transition": "margin-left .5s",
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "0rem 1rem",
    "background-color": "#f8f9fa",}
CONTENT_STYLE_sidebar_hidden = {
    "position": "relative",
    "top":"4rem",
    "transition": "margin-left .5s",
    "margin-left": "2rem",
    "margin-right": "2rem",
    "padding": "0rem 1rem",
    "background-color": "#f8f9fa",}

content = html.Div(

    id="page-content",
    style=CONTENT_STYLE)

######################################################################################
###################################### LAYOUT ########################################
######################################################################################

# layout da página principal
app.layout = html.Div([
    navbar,
    sidebar,
    content,
    footer,
    dcc.Store(id='side_click'),

    dcc.Location(id='url', refresh=False)])
home_page = html.Div([
    html.H1('HOME'),
    dcc.Link('Go to Page 1', href='/page-1'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page-2'),
    html.Br(),
    dcc.Link('Go to Page 3', href='/page-3'),
    html.Br(),
    dcc.Link('Go to Page KPI', href='/page-kpis'),])

# página de path errado
index_page = html.Div([
    html.H1('URL não encontrada'),
    dcc.Link('Go to Page 1', href='/page-1'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page-2'),
    html.Br(),
    dcc.Link('Go to Page 3', href='/page-3'),
    html.Br(),
    dcc.Link('Go to Page KPI', href='/page-kpis'),])

###########################################################################################
#################################### PAGINA 1 #############################################
###########################################################################################

################
# FUNÇÕES ######

# QUEBRA DE NOME
def nome_produto_to_submercado(nome_produto):
  try:
    submercado = nome_produto.split()[0] 
  except:
    submercado = ''
  return submercado

def nome_produto_to_fonte(nome_produto):
  try:
    fonte = nome_produto.split()[1] 
  except:
    fonte =''
  return fonte

def nome_produto_to_periodicidade(nome_produto):
  try:
    periodicidade = nome_produto.split()[2] 
  except:
    periodicidade =''
  return periodicidade

def nome_produto_to_data_inicial(nome_produto):
  try:
    posicao_primeira_barra = nome_produto.find('/')
    data_inicial = nome_produto[(posicao_primeira_barra-3):(posicao_primeira_barra+3)]
  except:
    data_inicial =''
  return data_inicial

def nome_produto_to_data_final(nome_produto):
  try:
    posicao_segunda_barra = nome_produto.rfind('/')
    data_final = nome_produto[(posicao_segunda_barra-3):(posicao_segunda_barra+3)]
  except:
    data_final =''
  return data_final

def nome_produto_to_precificacao(nome_produto):
  try:
    posicao_hifen = nome_produto.find('-')
    precificacao = nome_produto[posicao_hifen+1:]
  except:
    precificacao =''
  return precificacao.upper()

def datahora_to_data(datahora):
  data_operacao = datahora[6:10]+'-'+datahora[3:5]+'-'+datahora[0:2]
  return data_operacao

# FILTRO DE OPERAÇÕES SEM SENTIDO/FORA DE PADRÃO
def filtrar_ruido(operacoes_bbce):
  # Filtro dos produtos
  periodicidade_padrao = ['MEN', 'TRI', 'SEM', 'ANU', 'OUTROS', 'OTR', 'BIM', 'QUA']
  operacoes_filtradas = operacoes_bbce[operacoes_bbce['Cancelado']=="Não"]
  operacoes_filtradas = operacoes_filtradas[operacoes_filtradas['Periodicidade'].apply(lambda x: x in periodicidade_padrao)]
  operacoes_filtradas = operacoes_filtradas[operacoes_filtradas['Tipo Contrato']=="Balcão"]

  # Classificação das operações
  operacoes_filtradas['Data/Hora'] = pd.to_datetime(operacoes_filtradas['Data/Hora'], format='%d/%m/%Y %H:%M:%S')
  operacoes_filtradas = operacoes_filtradas.sort_values(by='Data/Hora',ascending=False)

  return operacoes_filtradas

# MODIFCAÇÃO PARA CANDLES
def operacoes_to_candles(operacoes_filtradas):
  # VOLUME
  volume_total_mwm_agg = operacoes_filtradas.loc[:,['Produto','Data Operação','MWm']].groupby(['Produto','Data Operação']).agg(func='sum')
  volume_total_mwh_agg = operacoes_filtradas.loc[:,['Produto','Data Operação','MWh']].groupby(['Produto','Data Operação']).agg(func='sum')
  # MÁXIMO
  max_agg = operacoes_filtradas.loc[:,['Produto','Data Operação','Preço (R$)']].groupby(['Produto','Data Operação']).agg(func='max')
  max_agg.columns=['MAX']
  # MÍNIMO
  min_agg = operacoes_filtradas.loc[:,['Produto','Data Operação','Preço (R$)']].groupby(['Produto','Data Operação']).agg(func='min')
  min_agg.columns=['MIN']
  # FECHAMENTO
  fec_agg = operacoes_filtradas.loc[:,['Produto','Data Operação','Preço (R$)']].groupby(['Produto','Data Operação']).agg(func='first')
  fec_agg.columns=['FEC']
  # ABERTURA
  abe_agg = operacoes_filtradas.loc[:,['Produto','Data Operação','Preço (R$)']].groupby(['Produto','Data Operação']).agg(func='last')
  abe_agg.columns=['ABE']

  candles_bbce = volume_total_mwm_agg.join(volume_total_mwh_agg).join(max_agg).join(min_agg).join(fec_agg).join(abe_agg)
  
  # COLUNAS PARA APLICAÇÃO DE FILTRO
  candles_bbce['Submercado']=pd.Series(candles_bbce.index.get_level_values('Produto')).apply(lambda x: nome_produto_to_submercado(x)).values
  candles_bbce['Fonte']=pd.Series(candles_bbce.index.get_level_values('Produto')).apply(lambda x: nome_produto_to_fonte(x)).values
  candles_bbce['Periodicidade']=pd.Series(candles_bbce.index.get_level_values('Produto')).apply(lambda x: nome_produto_to_periodicidade(x)).values
  candles_bbce['Data Inicial']=pd.Series(candles_bbce.index.get_level_values('Produto')).apply(lambda x: nome_produto_to_data_inicial(x)).values
  candles_bbce['Data Final']=pd.Series(candles_bbce.index.get_level_values('Produto')).apply(lambda x: nome_produto_to_data_final(x)).values
  candles_bbce['Precificacao']=pd.Series(candles_bbce.index.get_level_values('Produto')).apply(lambda x: nome_produto_to_precificacao(x)).values
  candles_bbce['Data'] = candles_bbce.index.get_level_values('Data Operação')
  candles_bbce = candles_bbce.loc[:,['Data','ABE','MIN','MAX','FEC','Submercado','Fonte','Periodicidade','Data Inicial','Data Final','Precificacao']]

  return candles_bbce

# BUSCA POR OPERAÇÕES
operacoes_bbce = pd.read_excel("bbce_todos_negocios_03_12_2021.xlsx")

operacoes_bbce['Submercado'] = operacoes_bbce['Produto'].apply(lambda x: nome_produto_to_submercado(x))
operacoes_bbce['Fonte'] = operacoes_bbce['Produto'].apply(lambda x: nome_produto_to_fonte(x))
operacoes_bbce['Periodicidade'] = operacoes_bbce['Produto'].apply(lambda x: nome_produto_to_periodicidade(x))
operacoes_bbce['Data Inicial'] = operacoes_bbce['Produto'].apply(lambda x: nome_produto_to_data_inicial(x))
operacoes_bbce['Data Final'] = operacoes_bbce['Produto'].apply(lambda x: nome_produto_to_data_final(x))
operacoes_bbce['Precificacao'] = operacoes_bbce['Produto'].apply(lambda x: nome_produto_to_precificacao(x))
operacoes_bbce['Data Operação'] = operacoes_bbce['Data/Hora'].apply(lambda x: datahora_to_data(x))

# TRATAMENTO DAS OPERAÇÕES
operacoes_filtradas = filtrar_ruido(operacoes_bbce)

# TRANSFORMAÇÃO EM CANDLES
candles_bbce = operacoes_to_candles(operacoes_filtradas)

params = candles_bbce.columns.values
produtos = candles_bbce.index.get_level_values('Produto').values

# layout ####
page_1_layout = html.Div([
    html.H1('Candles'),
    dcc.Dropdown(
        id='candles_dropdown',
        options=[{'label': i, 'value': i} for i in produtos]
    ),
    dcc.Graph(id='grafico_candles'),
    html.Div([
        dash_table.DataTable(
            id='tabela_candles',
            columns=(
                [{'id': p, 'name': p} for p in params]
            ),
            data=candles_bbce.to_dict('records'),
            )
        ]),

    html.Div(id='page-1-content'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page-2'),
    html.Br(),
    dcc.Link('Go to Page 3', href='/page-3'),
    html.Br(),
    dcc.Link('Go to KPIs Page', href='/page-kpis'),
    html.Br(),
    dcc.Link('Go back to home', href='/'),],
    )
# callback ####
# texto que diz o o produto selecionado
@app.callback(dash.dependencies.Output('page-1-content', 'children'),
              [dash.dependencies.Input('candles_dropdown', 'value')])
def page_1_dropdown(value):
    return 'Produto selecionado "{}"'.format(value)

# grafico de candles
@app.callback(dash.dependencies.Output('grafico_candles', 'figure'),
              [dash.dependencies.Input('candles_dropdown', 'value')])
def display_graph(nome_produto):
    filtro_candles = candles_bbce.iloc[candles_bbce.index.get_level_values('Produto') == nome_produto]
    
    fig_candles = make_subplots(rows=1, cols=1, column_widths=[1], vertical_spacing= 0.02)
    fig_candles.add_trace(go.Candlestick(x = filtro_candles.loc[:,"Data"].values,  open = filtro_candles.loc[:,"ABE"].values,  high = filtro_candles.loc[:,"MAX"].values,  low = filtro_candles.loc[:,"MIN"].values,   close = filtro_candles.loc[:,"FEC"].values,      showlegend=False),   row = 1, col = 1)
    fig_candles.update_layout(showlegend = True,
                                # desenhando caracteristicas do eixo x
                                xaxis=dict(
                                    # seletor de data por botão
                                    rangeselector = dict( buttons=list([ dict(count=1, label="1m", step="month", stepmode="backward"), dict(count=6, label="6m", step="month", stepmode="backward"), dict(count=1, label="YTD", step="year", stepmode="todate"), dict(count=1, label="1y", step="year", stepmode="backward"), dict(step="all") ]) ),
                                    rangeslider = dict( visible=False ),
                                    type="date"))
    return fig_candles


# tabela de candles
@app.callback(dash.dependencies.Output('tabela_candles', 'data'),
              [dash.dependencies.Input('candles_dropdown', 'value')])
def display_table(value):
    data = candles_bbce.iloc[candles_bbce.index.get_level_values('Produto') == value].to_dict('records')
    return data


###########################################################################################
#################################### PAGINA 2 #############################################
###########################################################################################

# layout ####
page_2_layout = html.Div([
    html.H1('Page 2'),
    dcc.RadioItems(
        id='page-2-radios',
        options=[{'label': i, 'value': i} for i in ['Orange', 'Blue', 'Red']],
        value='Orange'
    ),
    html.Div(id='page-2-content'),
    html.Br(),
    dcc.Link('Go to Page 1', href='/page-1'),
    html.Br(),
    dcc.Link('Go to Page 3', href='/page-3'),
    html.Br(),
    dcc.Link('Go to KPIs page', href='/page-kpis'),
    html.Br(),
    dcc.Link('Go back to home', href='/')])

###########################################################################################
#################################### PAGINA 3 #############################################
###########################################################################################

# layout ####
page_3_layout = html.Div([
    html.H1('Page 3'),


    dcc.Input(id='input-1-state', type='text', value='Montreal'),
    dcc.Input(id='input-2-state', type='text', value='Canada'),
    html.Button(id='submit-button', n_clicks=0, children='Submit'),
    html.Div(id='output-state'),



    html.Div(id='page-3-content'),
    html.Br(),
    dcc.Link('Go to Page 1', href='/page-1'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page-2'),
    html.Br(),
    dcc.Link('Go to KPIs Page', href='/page-kpis'),
    html.Br(),
    dcc.Link('Go back to home', href='/')])

# callback ####
@app.callback(dash.dependencies.Output('page-3-content', 'children'),
              [dash.dependencies.Input('page-3-radios', 'value')])
def page_3_radios(value):
    return 'You have selected "{}"'.format(value)

@app.callback(dash.dependencies.Output('output-state', 'children'),
              dash.dependencies.Input('submit-button', 'n_clicks'),
              dash.dependencies.State('input-1-state', 'value'),
              dash.dependencies.State('input-2-state', 'value'))
def update_output(n_clicks, input1, input2):
    return ('The Button has been pressed {} times,'
            'Input 1 is "{}",'
            'and Input 2 is "{}"').format(n_clicks, input1, input2)


###########################################################################################
#################################### PAGINA KPIS #############################################
###########################################################################################

# layout ####
page_kpis_layout = html.Div([
    html.H1('KPIs'),

    html.Div(id='page-kpis-content'),
    html.Br(),
    dcc.Link('Go to Page 1', href='/page-1'),
    html.Br(),
    dcc.Link('Go to Page 2', href='/page-2'),
    html.Br(),
    dcc.Link('Go to Page 3', href='/page-3'),
    html.Br(),
    dcc.Link('Go back to home', href='/')])







###########################################################################################
############################## Mudança de página do app ###################################
###########################################################################################

@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return home_page
    elif pathname == '/page-1':
        return page_1_layout
    elif pathname == '/page-2':
        return page_2_layout
    elif pathname == '/page-3':
        return page_3_layout
    elif pathname == '/page-kpis':
        return page_kpis_layout
    else:
        return index_page
    # You could also return a 404 "URL not found" page here

@app.callback(
    [
        Output("sidebar", "style"),
        Output("page-content", "style"),
        Output("side_click", "data"),
    ],
    [Input("btn_sidebar", "n_clicks")],
    [
        State("side_click", "data"),
    ])
def toggle_sidebar(n, nclick):
    if n:
        if nclick == "SHOW":
            sidebar_style = SIDEBAR_HIDDEN
            content_style = CONTENT_STYLE_sidebar_hidden
            cur_nclick = "HIDDEN"
        else:
            sidebar_style = SIDEBAR_STYLE
            content_style = CONTENT_STYLE
            cur_nclick = "SHOW"
    else:
        sidebar_style = SIDEBAR_STYLE
        content_style = CONTENT_STYLE
        cur_nclick = 'SHOW'

    return sidebar_style, content_style, cur_nclick

###########################################################################################
############################### Inicialização do APP ######################################
###########################################################################################
import os
if __name__ == '__main__':
    app.run_server(debug=False,port=os.getenv("PORT",5000))