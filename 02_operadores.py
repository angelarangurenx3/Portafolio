"""
Operadores aritmeticos 
suma, resta. division

docstring
"""

#------Aritmetica basica----------
a = 10
b = 5

suma = a + b #15
print(suma)
resta = a - b #5
print(resta)
producto = a * b #50
print(producto)
division = a / b #2.00000000
print(division)
division_sin_decimal =  a // b #2
print(division_sin_decimal)

modulo = a % b #2            #residuo de la division
print(modulo)
potencia = a**b #100000
print(potencia)
operacion = a + b * 2 #20           #se respeta la jerarquia de operaciones
print(operacion)

print(a == b)         #= es asignacion , == es comparacion
print("a es igual a b?: ", a == b)

# <, >, =<, =>
print("a mayor a b?", a >= b)

#Calcula el indice de masa corporal con:
#peso_kg = 70
#altura_m = 1.75
#usa  la formula: imc = peso_kg / (altura_m ** 2)
#muestra el resultado en una variable imc.

peso_kg = 70
altura_m = 1.75

imc = peso_kg / (altura_m ** 2)
print("el imc es:",imc, "kg por m")

# usa operadores para responder:
# b es divisor de a?
division = a/b
print(division)
modulo = a%b
print("print es divisor de a", modulo == 0)

# comparar si a^2 es mayor que 100

print(a**2 >= 100)