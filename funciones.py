#def nombre_de_funcion(parametro1, parametro2):
    #Cuerpo de la funcion

def saludar(nombre):
    variable = True
    return f"Hola, {nombre} {variable}"

#Laidentacion es importante
#lo que venga despues del return no se ejecuta
#las variables creadas dentro de la funcion, solo existen dentro de ella misma

retorno_de_la_funcion = saludar("Angel")
print(retorno_de_la_funcion)

def es_par(numero):
    return numero % 2 == 0

print(es_par(10))

#Crea una funcion que reciba a y b como parametro y que sume esos valores

def suma(a, b):
    return a + b

print(suma(10, 4))

#Escribe una funcion que reciba una lista de numeros y devuelva la suma
#Por Ejemplo, Suma_Lista([1, 2, 3]) deberia devolver 6

def lista(numeros):
    total = 0
    for numero in numeros:
        total = total + numero
    return total

print(lista([1, 3, 5, 7, 9]))