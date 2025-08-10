"""
sumar, restar, dividir y multiplicar
Vamos a poder preguntarle al usuario que numero desea y que operacion desea
"""

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def mult(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        print("Error, no se puede dividir entre 0")
        return None
    return a / b

while True:
    print("""\n Calculadora
            1. Sumar
            2. Restar
            3. Multiplicar
            4. Dividir
            0. Salir          
""")

    opcion = input("Selecciona una opcion: ")

    if opcion == "0":
        break               #break se usa para salir del bucle

    a = float(input("Primmer Numero: "))
    b = float(input("Segundo Numero: "))

    if opcion == "1":
        resultado = sumar(a, b)

    if opcion == "2":
        resultado = restar(a, b)

    if opcion == "3":
        resultado = mult(a, b)

    if opcion == "4":
        resultado = dividir(a, b)

    if resultado is not None:
        print("Resultado", resultado)

#Tarea 1 
#Refactorizar el menu para que las operaciones sean un diccionario
# {"1": ("Sumar", sumar), ...} y el codigo sea mas completo

#Tarea 2
#Mejora la calculadora añadiendo la operacion potencia (a^b)

#Tarea 3
#Lanzar un mensaje por defecto, si el usuario pone una opcion no valida

#Tarea 4
#Refactorizar la calculadora de la Clase 1 para:
#Repetir menu hasta que el usuario escriba "salir"
#Manejar entradas no numericas con try/except