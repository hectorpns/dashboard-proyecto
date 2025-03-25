import pandas as pd
import plotly.express as px

# Carga el archivo CSV con manejo de errores
file_path = "vehicles_us.csv"  # Asegúrate de que la ruta es correcta
try:
    car_data = pd.read_csv(file_path)
    print("Archivo CSV cargado correctamente.")
    print(car_data.head())  # Muestra las primeras filas para verificar
except FileNotFoundError:
    print(f"Error: No se encontró el archivo en {file_path}")
    exit()  # Termina el script si el archivo no existe
except Exception as e:
    print(f"Error al cargar el archivo: {e}")
    exit()

# Crear histograma del odómetro
fig1 = px.histogram(car_data, x="odometer", title="Distribución del Odómetro")
fig1.show()

# Crear scatter plot de odómetro vs precio
fig2 = px.scatter(car_data, x="odometer", y="price",
                  title="Precio vs Odómetro")
fig2.show()
