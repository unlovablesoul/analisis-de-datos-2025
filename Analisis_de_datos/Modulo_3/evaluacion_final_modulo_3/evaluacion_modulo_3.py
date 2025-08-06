import pandas as pd
from datetime import datetime, date
from typing import List, Dict, Union

#Vamos a limpiar la tabla considerando los 3 puntos importantes: Fecha, Moneda y Cantidad. 

def convertir_fecha(fecha_str, formatos=("%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y")):

    if not isinstance(fecha_str, str):
        return None
        
    for formato in formatos:
        try:
            return datetime.strptime(fecha_str, formato).date()
        except ValueError:
            continue
    return None
def convertir_precio(precio_str: str) -> float:
    
    if pd.isna(precio_str):
        return 0.0
        
    try:
        if isinstance(precio_str, (int, float)):
            return float(precio_str)
            
        if isinstance(precio_str, str):
            limpio = ''.join(c for c in precio_str if c.isdigit() or c == '.')
            return float(limpio)
            
    except (ValueError, TypeError, AttributeError):
        pass
        
    return 0.0

def convertir_cantidad(cantidad_str: Union[str, int]) -> int:
    if pd.isna(cantidad_str):
        return 0
        
    try:
        return int(cantidad_str)
    except (ValueError, TypeError):
        return 0
    
#Ahora se van a definir las funciones de cálculo requeridas

def calcular_total_venta(precio: float, cantidad: int) -> float:

    return precio * cantidad

def analizar_ventas(df: pd.DataFrame) -> Dict:
    
    total_mes = df['Total_Venta'].sum()
    
    promedio = df['Total_Venta'].mean()
    
    metodos_pago = df['Método de Pago'].value_counts().to_dict()
    
    return {
        'Total_Ventas_Mes': round(total_mes, 2),
        'Promedio_Venta': round(promedio, 2),
        'Ventas_por_Metodo_Pago': metodos_pago
    }

#Ahora se van a definir las funciones para analizar los datos

def limpiar_datos(df: pd.DataFrame) -> pd.DataFrame:

    df_limpio = df.copy()
    
    df_limpio['Fecha'] = df_limpio['Fecha'].apply(convertir_fecha)
    df_limpio['Precio'] = df_limpio['Precio'].apply(convertir_precio)
    df_limpio['Cantidad'] = df_limpio['Cantidad'].apply(convertir_cantidad)
    df_limpio['Total_Venta'] = df_limpio.apply(
        lambda x: calcular_total_venta(x['Precio'], x['Cantidad']), axis=1
    )
    
    return df_limpio

def main():
    try:
        df = pd.read_excel('dataset_modulo_3.xlsx', engine='openpyxl')
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return
    
    df_limpio = limpiar_datos(df)
    print("\nDatos limpios (primeras 5 filas):")
    print(df_limpio.head())
    reporte = analizar_ventas(df_limpio)  
    print("\nReporte de Ventas:")
    print(f"Total de ventas del mes: ${reporte['Total_Ventas_Mes']:,.2f}")
    print(f"Promedio por transacción: ${reporte['Promedio_Venta']:,.2f}") 
    print("\nVentas por método de pago:")
    for metodo, cantidad in reporte['Ventas_por_Metodo_Pago'].items():
        print(f"- {metodo}: {cantidad} ventas")
    #Para exportar los nuevos datos a un nuevo archivo para visualizar en Excel
    df_limpio.to_excel('ventas_limpias.xlsx', index=False)
    print("\nDatos limpios exportados a 'ventas_limpias.xlsx'")
if __name__ == "__main__":
    main()


