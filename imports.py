#import nombre_de_libreria
import math
import random
import datetime as dt #as se usa para renombrar la libreria

print(math.pi)

objetivo = random.randint(1, 10)
intento = int(input("Adivina un numero de 1 a 10: "))
print("el objetivo era: ", objetivo)
print(objetivo == intento)

dado1 = random.randint (1, 6)
dado2 = random.randint (1, 6)
print(f"Los dados son: {dado1} y {dado2}")