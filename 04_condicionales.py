"""Estructuras if, else, elif"""

nota = 100
if nota >= 100:
    print("Excelente")
elif nota == 70: # = es asignacion, == es comparacion
    print("Aprobado")
elif nota >= 50:
    print("estudia mas")
else:
    print("Reprobado")

#---------Condicionales anidados-----------
nota1 = 200
if nota1 >= 100:
    print("excelente")
    if nota1 >= 200:
        print("eres un crack")

#-------Operadores Logicos-------

nota2 = 200
if nota >= 60 and nota < 70:
    print ("Aprobado justo")
if nota < 60 or nota == 0:
    print ("Reprobado o no presentado")
if not nota: #nota == 0
    print ("No has ingresado una nota")

# valor_izquierda and valor_derecha
# valor_izquierda or valor_derecha
# not es cierto si el valor no se cumple

# pregunta al usuario un año y verifica si es bisiesto:
#   es divisible entre 4
#   divisible entre 4 pero no entre 100, excepto si es divisible entre 400
# Muestra True/False o un mensaje descriptivo.

año = 2020

if año %4 == 0 or año %400 == 0:
    print(f"{año} es bisiesto")
    if año % 100 > 0:
        print(f"{año} es bisiesto")

else:
    print(f"(año)no es bisiesto")

