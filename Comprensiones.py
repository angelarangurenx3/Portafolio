nums = [1, 2, 3, 4]
print([print(i) for i in nums])
cuadrados = [numero**2 for numero in nums]
print(cuadrados)

frutas = ["manzanas", "banana", "cereza"]
frutas_upper = [i.upper() for i in frutas]
print(frutas_upper)

marcas = ["Apple", "Dell", "HP", "Asus"]
marcas_len = [len(i) for i in marcas]
print(marcas_len)

nums = [1, 2, 3, 4]
pares = ["par" if n % 2 == 0 else "impar" for n in range(20)]
print(pares)

marcas2 = ["Toyota", "Mitsubishi", "Honda", "Dodge"]
len_diccionario = {marca: len(marca) for marca in marcas2}
print(len_diccionario)

nums2= [4, 3, 2, 1, 0, 20, 19]
cuadrado_dict = {numero: numero**2 for numero in nums}

print(cuadrado_dict)

diccionario = {"a": "hola", "b": "mundo", "c": "python"}
test = [("a", "hola"), ("b", "mundo")]
diccionario_trans = {clave: valor.upper() for clave, valor in diccionario.items()}
print(diccionario_trans)