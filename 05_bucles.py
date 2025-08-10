#-------------Bucle for------------
#for iterator in range(1, 11):
#    print(iterator)

#-----------Bucle while------------
cuenta_atras = 5
while cuenta_atras >= 0:
    print(cuenta_atras)
    cuenta_atras = cuenta_atras - 1

#Cuando se use bucle while tener cuidado en no caer en bucle infinito

#Crea un programa que imprima la tabla de multiplicar del 5
tabla = 5
for iterator in range(1,11):
    print (iterator)

#Escribe un while que solicite numeros e imprima cuantos numeros positivos se introdujeron.
#hasta que el  usuario introduzca 0; sl final

contador = 0
numero = None

while numero != 0:
    numero = int(input("introduzca un numero: "))

    if numero > 0:
        contador = contador + 1
print(contador)
