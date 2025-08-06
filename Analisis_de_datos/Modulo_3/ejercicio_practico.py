import math




# 1. 
numero = float(input('Ingrese un número: '))
def cuadrado():
    return numero**2
print(f'El cuadrado de {numero} es: ', cuadrado())

#2. 
numero1 = int(input('Ingrese un número entero: '))
def factorial(numero1):
    resultado = 1
    for i in range(1, numero1+1):
        resultado *= i
    return resultado
print(f'El factorial de {numero1} es: ', factorial(numero1))


#3

radio = float(input('Ingrese el valor del rádio: '))
def area_circulo():
    return math.pi*radio**2
print(f'El área del círculo de radio {radio} es: ', area_circulo())

#4

def es_bisiesto(año):
    return año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)

def bisiestos():
    año1 = int(input("Ingrese el primer año: "))
    año2 = int(input("Ingrese el segundo año: "))
    
    if año1 > año2:
        año1, año2 = año2, año1
    
    contador = 0
    for año in range(año1, año2 + 1):
        if es_bisiesto(año):
            contador += 1
    
    print(f"Entre {año1} y {año2} hay {contador} años bisiestos.")

bisiestos()

#5

def sumatoria():
    numero3 = int(input('Ingrese el número hasta donde se quiere hacer la sumatoria: '))
    resultado_sum = numero3*(numero3 + 1)/2
    print(f'El resultado de sumar todos los números hasta el {numero3} es: ', resultado_sum)
sumatoria()

#6 
numero4 = int(input('Ingrese el número a calcular sus divisores: '))

def total_divisores(num):
    if num <= 0:
        return 'El número debe ser positivo'
    
    divisores = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisores.append(i)
    return divisores

print(f' Los divisores del {numero4} son:', total_divisores(numero4))

#7 
def promedio(lista):
    return sum(lista)/len(lista)
lista = [2, 4, 5, 6, 10, 12, 13]
print('El promedio de la lista es: ', promedio(lista))

#8

from operaciones import multiplicacion
num_x = float(input('Ingrese primer número: '))
num_y = float(input('Ingrese segundo número: '))

resultado_final = multiplicacion(num_x, num_y)

print('El resultado de la multiplicación de ambos números es: ', resultado_final)

#9
potencia = lambda base, exponente: base ** exponente
resultado_potencia = potencia(12, 14)
print('El resultado de la potencia es: ', resultado_potencia)

#10

lista_10 = [1, 3, 2, 7, 1, 4, 8, 2, 10, 12, 9]
lista_10.sort()
print(lista_10)

#11

def promedio(lista_numeros):
    return sum(lista_numeros)/len(lista_numeros)
def suma(lista_numeros):
    return sum(lista_numeros)
def mediana(lista_numeros):
    lista_ordenada = sorted(lista_numeros)
    n = len(lista_ordenada)
    mitad = n // 2
    
    if n % 2 == 1:
        return lista_ordenada[mitad]
    else:
        return (lista_ordenada[mitad - 1] + lista_ordenada[mitad]) / 2
def calcular(numeros, operacion):
    return operacion(numeros)

def mostrar_menu():
    print("\nMenú de operaciones:")
    print("1. Calcular promedio")
    print("2. Calcular suma")
    print("3. Calcular mediana")
    print("4. Salir")
    return input("Seleccione una opción (1-4): ")

def main():
    print("Calculadora Estadística")
    
    entrada = input("Ingrese números separados por espacios: ")
    numeros = [float(num) for num in entrada.split()]
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == '1':
            resultado = calcular(numeros, promedio)
            print(f"\nEl promedio es: {resultado:.2f}")
        elif opcion == '2':
            resultado = calcular(numeros, suma)
            print(f"\nLa suma es: {resultado}")
        elif opcion == '3':
            resultado = calcular(numeros, mediana)
            print(f"\nLa mediana es: {resultado}")
        elif opcion == '4':
            print("\n¡Hasta luego!")
            break
        else:
            print("\nOpción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()

#12 

def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9

def celsius_a_kelvin(c):
    return c + 273.15

def kelvin_a_celsius(k):
    return k - 273.15

def fahrenheit_a_kelvin(f):
    return celsius_a_kelvin(fahrenheit_a_celsius(f))

def kelvin_a_fahrenheit(k):
    return celsius_a_fahrenheit(kelvin_a_celsius(k))

def convertir_temperatura(valor, unidad_entrada, unidad_salida):
    if unidad_entrada == unidad_salida:
        return valor
    
    if unidad_entrada == 'C':
        temp_c = valor
    elif unidad_entrada == 'F':
        temp_c = fahrenheit_a_celsius(valor)
    elif unidad_entrada == 'K':
        temp_c = kelvin_a_celsius(valor)
    else:
        raise ValueError("Unidad de entrada no válida")
    
    if unidad_salida == 'C':
        return temp_c
    elif unidad_salida == 'F':
        return celsius_a_fahrenheit(temp_c)
    elif unidad_salida == 'K':
        return celsius_a_kelvin(temp_c)
    else:
        raise ValueError("Unidad de salida no válida")

def main():
    print("Conversor de Temperaturas")
    print("Unidades disponibles: Celsius (C), Fahrenheit (F), Kelvin (K)")
    
    while True:
        try:
            valor = float(input("\nIngrese el valor de temperatura a convertir: "))
            unidad_entrada = input("Ingrese la unidad de entrada (C/F/K): ").upper()
            unidad_salida = input("Ingrese la unidad de salida (C/F/K): ").upper()
            
            if unidad_entrada not in ['C', 'F', 'K'] or unidad_salida not in ['C', 'F', 'K']:
                print("Error: Unidades deben ser C, F o K")
                continue
            
            resultado = convertir_temperatura(valor, unidad_entrada, unidad_salida)
            print(f"\n{valor} °{unidad_entrada} = {resultado:.2f} °{unidad_salida}")
            
            continuar = input("\n¿Desea hacer otra conversión? (s/n): ").lower()
            if continuar != 's':
                print("¡Hasta luego!")
                break
                
        except ValueError as e:
            print(f"Error: {e}. Por favor ingrese valores válidos.")

if __name__ == "__main__":
    main()