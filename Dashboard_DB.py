import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Simulación de datos históricos y proyectados
meses_historicos = pd.date_range(start="2022-02", periods=36, freq='M').strftime('%Y-%m')
meses_futuros = pd.date_range(start="2025-02", periods=6, freq='M').strftime('%Y-%m')

np.random.seed(42)
precision_modelo_hist = np.random.uniform(75, 90, len(meses_historicos))
precision_modelo_fut = np.random.uniform(75, 90, len(meses_futuros))

tendencias_detectadas_hist = np.random.randint(5, 15, len(meses_historicos))
tendencias_detectadas_fut = np.random.randint(5, 15, len(meses_futuros))

db_menciones_hist = np.random.randint(500, 1200, len(meses_historicos))
db_menciones_fut = np.random.randint(500, 1200, len(meses_futuros))

# Título del Dashboard
st.title("📊 Dashboard de Detección de Tendencias")

# Objetivo del OKR
st.header("1️⃣ Objetivo del OKR")
st.write("Mejorar la detección temprana de tendencias de movilidad digital.")

# KR
st.header("2️⃣ Key Results (KR)")
st.markdown("""
- **KR1:** Desarrollar un modelo predictivo con 85% de precisión.
- **KR2:** Aumentar en 30% la cantidad de insights accionables.
- **KR3:** Integrar datos en tiempo real de 5 fuentes externas.
""")

# KPI
st.header("3️⃣ KPI")
st.markdown("""
- **Precisión del modelo predictivo (%)**
- **Número de tendencias detectadas antes de ser adoptadas por la competencia**
- **Número de fuentes de datos integradas en tiempo real**
""")

# Gráficos con Plotly
st.header("4️⃣ Gráficos")

# Precisión del modelo
fig_precision = go.Figure()
fig_precision.add_trace(go.Scatter(x=meses_historicos, y=precision_modelo_hist, mode='lines+markers', name='Histórico'))
fig_precision.add_trace(go.Scatter(x=meses_futuros, y=precision_modelo_fut, mode='lines+markers', name='Proyección', line=dict(dash='dash')))
fig_precision.update_layout(title='Evolución de la Precisión del Modelo Predictivo', xaxis_title='Mes', yaxis_title='Precisión (%)')
st.plotly_chart(fig_precision)

# Tendencias detectadas
fig_tendencias = go.Figure()
fig_tendencias.add_trace(go.Scatter(x=meses_historicos, y=tendencias_detectadas_hist, mode='lines+markers', name='Histórico'))
fig_tendencias.add_trace(go.Scatter(x=meses_futuros, y=tendencias_detectadas_fut, mode='lines+markers', name='Proyección', line=dict(dash='dash')))
fig_tendencias.update_layout(title='Tendencias Detectadas: Histórico vs Proyección', xaxis_title='Mes', yaxis_title='Número de Tendencias')
st.plotly_chart(fig_tendencias)

# Menciones en redes sociales
fig_menciones = go.Figure()
fig_menciones.add_trace(go.Scatter(x=meses_historicos, y=db_menciones_hist, mode='lines+markers', name='Histórico'))
fig_menciones.add_trace(go.Scatter(x=meses_futuros, y=db_menciones_fut, mode='lines+markers', name='Proyección', line=dict(dash='dash')))
fig_menciones.update_layout(title='Menciones en Redes Sociales: Histórico vs Proyección', xaxis_title='Mes', yaxis_title='Número de Menciones')
st.plotly_chart(fig_menciones)

# Descripción de los datos
st.header("5️⃣ Descripción de los Datos")
data_desc = pd.DataFrame({
    "Variable": ["Precisión del modelo", "Tendencias detectadas", "Menciones en redes sociales"],
    "Fuente de Datos": ["Sistema de análisis predictivo", "Big Data de movilidad", "APIs de Twitter/Google Trends"],
    "Método de Obtención": ["Extracción de logs", "Machine Learning", "Web Scraping"],
    "Transformaciones Necesarias": ["Normalización de datos", "Limpieza de datos, NLP", "Análisis de sentimiento, categorización"]
})
st.table(data_desc)

# Acciones necesarias
st.header("6️⃣ Acciones Necesarias")
st.markdown("""
- 📌 **Implementar herramientas de Big Data y Machine Learning.**
- 🚀 **Crear un laboratorio de innovación en movilidad.**
- 🤝 **Establecer alianzas con startups de movilidad.**
""")
