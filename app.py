import os
import pandas as pd
import plotly.express as px
import streamlit as st

# Imprime el directorio de trabajo actual
print("Current working directory:", os.getcwd())

# Lee el archivo CSV
df = pd.read_csv('vehicles_us.csv')

st.header('Análisis de Datos de Vehículos')
# Botón para construir el histograma
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir el gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig_scatter = px.scatter(df, x="odometer", y="price", title="Precio vs Odometer")
    st.plotly_chart(fig_scatter, use_container_width=True)
