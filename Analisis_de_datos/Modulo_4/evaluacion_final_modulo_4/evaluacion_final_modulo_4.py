import pandas as pd

#Para cargar los archivos

df_ventas = pd.read_csv('ventas_tienda.csv')
df_estudiantes = pd.read_json('estudiantes.json')

#Para ver las primeras 5 filas de cada archivo
print(df_ventas.head())
print(df_estudiantes.head())

'''Ahora para ver un resumen, estadisticas descriptivas y valores nulos de
los datasets'''

print(df_ventas.info())
print(df_estudiantes.info())
print(df_ventas.describe())
print(df_estudiantes.describe())
print(df_estudiantes.describe())
print(df_ventas['Categoria'].value_counts(dropna=False))
print(df_estudiantes['edad'].value_counts(dropna=False))

#Uso de loc[] y iloc[]

edad = df_estudiantes.loc[df_estudiantes['edad'] < 23, :]
electronicos = df_ventas.loc[df_ventas['Categoria']=='Electrónicos', ['Nombre_Prod']]

datos = df_estudiantes.iloc[:5, :3]

'''Ahora vamos a eliminar los valores nulos existentes
por lo que revisaremos los datos y los eliminaremos'''
print('Valores nulos por columna: ')
print(df_ventas.isnull().sum())
print('Valores nulos por columna: ')
print(df_estudiantes.isnull().sum())

#Haremos arreglos en los dataset
'''DATASET DE ESTUDIANTES'''
#Dejar los nombres formato Aa
df_estudiantes['nombre'] = df_estudiantes['nombre'].str.capitalize() 
# Unificar categorías 
df_estudiantes['curso'] = df_estudiantes['curso'].replace({'Mate': 'Matemáticas', 
                                                           'Ciencas': 'Ciencias'})
df_estudiantes.columns = df_estudiantes.columns.str.capitalize()
#Reemplazar edad por la mediana
moda_edad = df_estudiantes['Edad'].mean()
mediana_edad = df_estudiantes['Edad'].median()
df_estudiantes['Edad'] = df_estudiantes['Edad'].apply(lambda x: mediana_edad 
                                                      if pd.isnull(x) or x > 100 else x)
#Remplazar las notas vacías o nulas por la moda
moda_notas = df_estudiantes['Nota_final'].mode()[0]
df_estudiantes['Nota_final'] = df_estudiantes['Nota_final'].fillna(moda_notas)

#Vamos a cambiar los nan por desconocido en la columna curso
df_estudiantes['Curso'] = df_estudiantes['Curso'].fillna('Desconocido')

#Corregir los valores mayores a 100 en la asistencia y los None
df_estudiantes['Asistencia_%'] = df_estudiantes['Asistencia_%'].str.replace('%', '').astype(float)
df_estudiantes['Asistencia_%'] = df_estudiantes['Asistencia_%'].clip(lower=0, upper=100)
mediana_asistencia = df_estudiantes['Asistencia_%'].median()
df_estudiantes['Asistencia_%'] = df_estudiantes['Asistencia_%'].fillna(mediana_asistencia)
print(df_estudiantes['Asistencia_%'])

#Finalmente comprobamos que no hay valores nulos y se corrigieron las tablas
print(df_estudiantes)

'''DATASET VENTAS'''

#Cambiar el "$" de la columna precio y dejar los nombres de categoría bien definidos

df_ventas['Precio'] = df_ventas['Precio'].str.replace('$', '').astype(int)

df_ventas['Categoria'] = df_ventas['Categoria'].replace('Electro','Electrónicos')

df_ventas['Categoria'] = df_ventas['Categoria'].fillna('Desconocido')
#Corregimos los valores en cantidad
df_ventas['Cantidad'] = df_ventas['Cantidad'].abs()
df_ventas['Cantidad'] = df_ventas['Cantidad'].fillna(0).astype(int)
df_ventas = df_ventas.rename(columns={'Nombre_Prod': 'Producto','Categoria': 'Categoría'})
print(df_ventas)
#Eliminaremos los valores 0 en la tabla cantidad ya que es redundante para el analisis
df_ventas = df_ventas[df_ventas['Cantidad'] != 0]

#Haremos algunas tablas nuevas

df_ventas['Ventas_Totales']=df_ventas['Precio']*df_ventas['Cantidad']

print(df_ventas)

#algunos datos estadísticos para los estudiantes

print(f"Mediana estudiantil: {mediana_edad:.2f}")
print(f"Moda estudiantil: {moda_edad:.2f}")

#Ahora haremos una tabla dinamica

tabla_dinamica_ventas = pd.pivot_table(df_ventas, values='Ventas_Totales', index='Fecha_Venta',
                                        columns='Categoría', aggfunc='sum', fill_value=0)

print(tabla_dinamica_ventas)

#crearemos una función para analizar un criterio de asistencia

def criterio_asistencia(porcentaje):   
    if porcentaje >= 90:
        return 'Aprobado'
    elif 75 <= porcentaje < 90:
        return 'Pendiente'
    else:
        return 'Reprobado'
df_estudiantes['Estado'] = df_estudiantes['Asistencia_%'].apply(criterio_asistencia)

tabla_final = df_estudiantes[['Nombre','Asistencia_%', 'Estado']]
print(tabla_final)