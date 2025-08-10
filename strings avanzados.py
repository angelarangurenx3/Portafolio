texto = "      hola Python      ".strip().lower()
print(texto)
texto1 = "      hola Python      ".strip().title()
print(texto1)

precio = 12.574962
print(f'${precio:.2f} USD') #2f es texto con el segundo decimal redondeado

texto2 = "python es increible"
texto2_limpio = texto2.strip().title()
print(texto2_limpio)
texto_a_lista = texto2_limpio.split()
print(texto_a_lista)
lista_a_texto = " ".join(texto_a_lista)
print(lista_a_texto)

#slicing
muestra = "ABCDEFGHIJK"
#corta el string desde la posicion 2 hasta la 7 incluyendo la 7
#haz un slicing para obtener las 3 ultimas posiciones

print(muestra[2:8])
print(muestra[-3:])

#Pide una frase. Imprime
#   a)n° de palabras
#   b)frase en MAYUSCULAS sin vocales (usa replace)
#   por ejemplo: "Hola Python" -> "Hl Pythn"

print("cadena".replace("a", "3"))

frase = input("inserte una frase: ")
frase_limpia = frase.strip() #limpiar frase
numero_de_caracteres = len(frase_limpia)
frase_a_lista = frase.split()
sin_vocales = frase.upper().replace("A","")().replace("E","")().replace("I","")().replace("O","")().replace("U","")
print(sin_vocales.lower())
#TAREA: Meter todas las vocales dentro de una sola estructura. Hint: puede ser una lista o un string
