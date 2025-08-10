"""Tarea Calculadora"""

#Refactorizar el menu para que las operaciones sean un diccionario
# {"1": ("Sumar", sumar), ...} y el codigo sea mas completo

#Mejora la calculadora añadiendo la operacion potencia (a^b)

#Lanzar un mensaje por defecto, si el usuario pone una opcion no valida

#Refactorizar la calculadora de la Clase 1 para:
#Repetir menu hasta que el usuario escriba "salir"
#Manejar entradas no numericas con try/except

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def mult(a, b):
    return a * b

def dividir(a, b):
   try:
    return a / b
   except ZeroDivisionError:
       return "Math Error"

def potencia(a, b):
    try:
     return a ** b
    except KeyError:
       return "Math Error"

operaciones = {
   "1": ["Sumar", sumar],
   "2": ["Restar", restar],
   "3": ["Multiplicar", mult],
   "4": ["Dividir", dividir],
   "5": ["Potencia", potencia]
}

def mostrar_menu():
   print("\n Menu de Operaciones:")
   for clave, (nombre, _) in operaciones.items():
      print(f"{clave}, {nombre}")
   print("Escribe 'salir' para terminar la calculadora")

while True:
   mostrar_menu()
   opcion = input("Elige una opcion: ").strip()

   if opcion.lower() == "salir":
      print("Hasta luego")

   if opcion not in operaciones:
     print("opcion invalida")

   try:
     a = float(input("ingresa el primer numero: "))
     b = float(input("ingresa el segundo numero: "))
     _, operacion = operaciones[opcion]
     resultado = operacion (a, b)
     print(f"Resultado: {resultado}")

   except ValueError:
        print("Error Num: Entrada no Real")