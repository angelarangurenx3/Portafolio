"""lectura de datos del usuario y casting a tipos numericos"""

nombre = input("Cual es tu nombre?: ")
print(nombre)

#casting de datos
edad = int(input("Cual es tu edad: "))
edad1 = int(input("cual es la mitad de tu edad"))
print(edad + edad1)

#Pide al usuario 2 numeros (pueden ser flotantes) y muestra:
#suma
#resta
#multiplicacion
#division
#division sin decimal
#ejemplo de entrada: 10.5 y 2.3

numero1 = 10.5
numero2 = 2.3

suma = numero1 + numero2
print(suma)
resta = numero1 - numero2
print(resta)
multiplicacion = numero1 * numero2
print(multiplicacion)
division = numero1 / numero2
print(division)
division_sin_decimal = numero1 // numero2
print(division_sin_decimal)