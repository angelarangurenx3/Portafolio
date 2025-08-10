#los conjuntos son colecciones no ordenadas de elementos unicos
#no permiten duplicados y no tienen un orden especifico
#union, interseccion y diferencia

animales = {"perro", "pez", "gato", "caballo"} #se imprime en orden distinto

for animal in animales:
    print(animal)

animales.add("jabali")
animales.remove("perro")

print(animales)

conjunto1 = {1,2,3}
conjunto2 = {3,4,5}

union = conjunto1 | conjunto2 #union entre conjuntos
print(union) #los conjuntos numericos siempre van a tener el mismo orden y van de menor a mayor

inter = conjunto1 & conjunto2 #interseccion entre conjuntos
print(inter)

diff = conjunto1 - conjunto2 #elementos que estan en el conjunto 1 pero no en el 2
print(diff)