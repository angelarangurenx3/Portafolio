#Una lista de elementos clave-valor

libro = {
    "Titulo": "Cien años de soledad",           #"Clave":valor
    "Autor": "G.G Marquez",
    "Publicacion": 1967,
}

libro["paginas"] = 500      #diccionario[nueva_clave] = valor
print(libro)

#for element in libro:
#    print(element)          #imprime la clave

print(libro.items())    #convertimos el diccionario a una lista de tuplas

for clave, valor in libro.items():
    print(f'{clave}:{valor}')

#Crea un diccionario llamado computadora con
#marca, ram_gb, sistema
#Recorre las claves y valores e imprimelos

computadora = {
    "marca": "Acer",
    "RAM_GB": 16,
    "SO": "Windows",
}

for clave, valor in computadora.items():
    print(f'{clave}:{valor}')

#Crea un diccionario llamado cine que tenga como clave el genero y valor una lista de peliculas de ese genero

cine = {
    "Terror": ["Saw", "It", "El Conjuro", "Megan", "Abigail"],
    "Sci-Fi": ["Interestelar", "Blade Runner", "Matrix", "Terminator"],
}

for clave, valor in cine.items():
    print(f'{clave}:{valor}')
