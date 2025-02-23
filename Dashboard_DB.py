import dash
from dash import dcc, html
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Datos históricos y proyectados
meses_historicos = pd.date_range(start="2022-02", periods=36, freq='M').strftime('%Y-%m')
meses_futuros = pd.date_range(start="2025-02", periods=6, freq='M').strftime('%Y-%m')

# Simulación de datos
np.random.seed(42)
precision_modelo_hist = np.random.uniform(75, 90, len(meses_historicos))
precision_modelo_fut = np.random.uniform(75, 90, len(meses_futuros))

tendencias_detectadas_hist = np.random.randint(5, 15, len(meses_historicos))
tendencias_detectadas_fut = np.random.randint(5, 15, len(meses_futuros))

db_menciones_hist = np.random.randint(500, 1200, len(meses_historicos))
db_menciones_fut = np.random.randint(500, 1200, len(meses_futuros))

# Crear gráficos interactivos
fig_precision = go.Figure()
fig_precision.add_trace(go.Scatter(x=meses_historicos, y=precision_modelo_hist, mode='lines+markers', name='Histórico'))
fig_precision.add_trace(go.Scatter(x=meses_futuros, y=precision_modelo_fut, mode='lines+markers', name='Proyección', line=dict(dash='dash')))
fig_precision.update_layout(title='Evolución de la Precisión del Modelo Predictivo', xaxis_title='Mes', yaxis_title='Precisión (%)')

fig_tendencias = go.Figure()
fig_tendencias.add_trace(go.Scatter(x=meses_historicos, y=tendencias_detectadas_hist, mode='lines+markers', name='Histórico'))
fig_tendencias.add_trace(go.Scatter(x=meses_futuros, y=tendencias_detectadas_fut, mode='lines+markers', name='Proyección', line=dict(dash='dash')))
fig_tendencias.update_layout(title='Tendencias Detectadas: Histórico vs Proyección', xaxis_title='Mes', yaxis_title='Número de Tendencias')

fig_menciones = go.Figure()
fig_menciones.add_trace(go.Scatter(x=meses_historicos, y=db_menciones_hist, mode='lines+markers', name='Histórico'))
fig_menciones.add_trace(go.Scatter(x=meses_futuros, y=db_menciones_fut, mode='lines+markers', name='Proyección', line=dict(dash='dash')))
fig_menciones.update_layout(title='Menciones en Redes Sociales: Histórico vs Proyección', xaxis_title='Mes', yaxis_title='Número de Menciones')

# Iniciar la aplicación Dash
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Dashboard de Detección de Tendencias"),
    
    html.H3("1. Objetivo del OKR"),
    html.P("Mejorar la detección temprana de tendencias de movilidad digital."),
    
    html.H3("2. KR"),
    html.Ul([
        html.Li("KR1: Desarrollar un modelo predictivo con 85% de precisión."),
        html.Li("KR2: Aumentar en 30% la cantidad de insights accionables."),
        html.Li("KR3: Integrar datos en tiempo real de 5 fuentes externas."),
    ]),
    
    html.H3("3. KPI"),
    html.Ul([
        html.Li("Precisión del modelo predictivo (%)."),
        html.Li("Número de tendencias detectadas antes de ser adoptadas por la competencia."),
        html.Li("Número de fuentes de datos integradas en tiempo real."),
    ]),
    
    html.H3("4. Gráficos"),
    dcc.Graph(figure=fig_precision),
    dcc.Graph(figure=fig_tendencias),
    dcc.Graph(figure=fig_menciones),
    
    html.H3("5. Descripción de los datos"),
    html.Table([
        html.Tr([html.Th("Variable"), html.Th("Fuente de Datos"), html.Th("Método de Obtención"), html.Th("Transformaciones Necesarias")]),
        html.Tr([html.Td("Precisión del modelo"), html.Td("Sistema de análisis predictivo"), html.Td("Extracción de logs"), html.Td("Normalización de datos")]),
        html.Tr([html.Td("Tendencias detectadas"), html.Td("Big Data de movilidad"), html.Td("Machine Learning"), html.Td("Limpieza de datos, NLP")]),
        html.Tr([html.Td("Menciones en redes sociales"), html.Td("APIs de Twitter/Google Trends"), html.Td("Web Scraping"), html.Td("Análisis de sentimiento, categorización")]),
    ], style={'border': '1px solid black', 'width': '100%', 'textAlign': 'left'}),
    
    html.H3("6. Acciones Necesarias"),
    html.Ul([
        html.Li("Implementar herramientas de Big Data y Machine Learning."),
        html.Li("Crear un laboratorio de innovación en movilidad."),
        html.Li("Establecer alianzas con startups de movilidad."),
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)
