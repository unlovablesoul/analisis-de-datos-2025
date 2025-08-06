import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Para cargar los datos
boletas = pd.read_csv('boletas.csv')
clientes = pd.read_csv('clientes.csv', encoding='cp1252')
detalle = pd.read_csv('detalle.csv')
productos = pd.read_csv('productos.csv', encoding='cp1252') #Tuve que usar ese encoding

print('=== Boletas ===')
print(boletas.info())
print('\n=== Clientes ===')
print(clientes.info())
print('\n=== Detalle ===')
print(detalle.info())
print('\n=== Productos ===')
print(productos.info())

#Haciendo el analisis

# Estadísticas descriptivas
print('=====================')
print('=== Boletas ===',boletas.describe())

# Verificar duplicados de la columna boleta
print(f"\nBoletas duplicadas: {boletas.duplicated().sum()}")

# Convertir fecha a datetime
boletas['fecha'] = pd.to_datetime(boletas['fecha'])

# Distribución temporal
boletas['fecha'].hist(bins=20)
plt.title('Distribución de boletas por fecha')
plt.show()

print('====== Tabla Clientes ======')

# Valores faltantes
print("Valores faltantes por columna:")
print(clientes.isnull().sum())

# Ver si hay algún RUT duplicado
print(f"\nClientes con RUT duplicado: {clientes.duplicated(subset=['rut']).sum()}")

print('====== Tabla Cantidad ======')
print(detalle['cantidad'].describe())
sns.boxplot(x=detalle['cantidad'])
plt.title('Distribución de cantidades vendidas')
plt.show()

print('====== Tabla Productos ======')
print(productos['precio'].describe())
productos['precio'].hist(bins=20)
plt.title('Distribución de precios de productos')
plt.show()