frutas = ["manzanas", "pera", "naranja"] #las listas pueden tener cualquier tipo de valor
print(frutas)
#las listas tienen muchos metodos para manipularlas
nums = [1, 4, 17, 25, 2]

frutas.append("durazno") #append agrega un elemento al final de la lista
print(frutas)
frutas.insert(1, "kiwi") #una funcion que inserta parametros nuevos en una posicion (las posiciones empiezan en 0)
print(frutas)
frutas.remove("pera") #quita el elemento que digamos
print(frutas)
frutas.sort() #ordena alfabeticamente
print(frutas)
nums.sort() #ordena las listas. Solo pueden ser listas de enteros o strings
print(nums)
frutas.reverse() #invierte la lista
print(frutas)
frutas.pop() #elimina el ultimo elemento de la lista
print(frutas)

print('posicion 0 de la lista:', frutas[0])
print('posicion 2 de la lista:', frutas[2])

print("ultima posicion de la lista:", frutas[-1])

#slicing: como acceder a partes de una lista
print(frutas[1:3]) #el 3 es no inclusivo
print(len(frutas)) #ver la longitud de diferentes estructuras de datos

#listas anidadas (matriz o arreglo bidimensional)
anidada = [
    ["manzana","pera", ["naranja","durazno"]],
    ["fresa","mango"],
    ["kiwi","mango"]
]

print(anidada[0][2][0]) #para imprimir naranja
print(anidada[1][0]) #para imprimir fresa

#Recorrer istas
for fruta in frutas: #se crea una nueva variable
    print(fruta.upper()) #pone todos los strings en mayuscula

#Enumerate es una funcion que permite recorrer una lista y obtener el indice de cada elemento
for indice, fruta in enumerate(frutas):
    print(f"fruta{indice}: {fruta}")
    