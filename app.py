import streamlit as st
import pandas as pd
import plotly.express as px

# Título de la aplicación
st.title("Análisis de Vehículos en Venta")

# Cargar el archivo CSV con manejo de errores
# Asegúrate de que el archivo esté en el mismo directorio
file_path = "vehicles_us.csv"
try:
    car_data = pd.read_csv(file_path)
    st.write("Archivo CSV cargado correctamente.")
    st.write(car_data.head())  # Muestra las primeras filas para verificar
except FileNotFoundError:
    st.error(f"Error: No se encontró el archivo en {file_path}")
    st.stop()  # Detiene la ejecución de la app
except Exception as e:
    st.error(f"Error al cargar el archivo: {e}")
    st.stop()

# Crear histograma del odómetro
st.subheader("Distribución del Odómetro")
fig1 = px.histogram(car_data, x="odometer", title="Distribución del Odómetro")
st.plotly_chart(fig1)

# Crear scatter plot de odómetro vs precio
st.subheader("Relación entre Precio y Odómetro")
fig2 = px.scatter(car_data, x="odometer", y="price",
                  title="Precio vs Odómetro")
st.plotly_chart(fig2)
