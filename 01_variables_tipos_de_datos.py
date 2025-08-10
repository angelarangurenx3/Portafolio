#---------Variables y tipos primitivos------------
pi = 3.14 #float
edad = 28 #int
profesor = "Edinson" #str (string)
es_alumno = True #bool

# Python es un lenguaje de tipado dinamico
edad = "veinte" #Reasignando

print(type(pi)) #imprime el tipo de variable, no el valor
print(type(es_alumno))
print(type(edad)) #imprime el ultimo valor reasignado

#Ejercicio: Crea tres variables:
#Ciudad (str)
#Temperatura (float)
#Llueve (bool)
#Muestra cada una en pantalla junto con su tipo
ciudad = "Caracas"
temperatura = 20.3
llueve = False
print(type(ciudad),type(temperatura),type(llueve))