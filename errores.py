def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError as error:
        print("El error es: ", error)
    finally:
        print("El finally siempre se va a ejecutar")

print(dividir(5,5))

#implementa input_entero(msg): sigue preguntando hasta recibir un entero valido. Devuelve el valor. ValueError

def input_entero(msg):
    while True: int
    try:
            return int(input(msg))
    except ValueError as error:
            print(f"el error es{error}")           

input_entero("Introduce un numero entero: ")