from fastapi import FastAPI #Framework para crear APIs y servidores
from pydantic import BaseModel #Valida formato del body
from datetime import date #Para hacer ejemplos con fechas

#Creacion del servidor o API

app = FastAPI( #instanciando una clase para acceder a sus metodos
    title="Mi primer API con FastAPI",
    description=("lorem ipsum"),
    version="0.0.1"
)

@app.get("/ping") #aplica una funcion a lo que este debajo
def ping():
    """funcion de prueba"""
    return {"msg": "ping"}

@app.get("/square")
def square(n: int):
    """devuelve el cuadrado de n"""
    return{"n": n, "square": n*n}

@app.get("/greet")
def greet(name = "mundo"):
    """saludo simple"""
    return {"saludo": f"hola {name}"}

class Echo(BaseModel):
    text: str

@app.post("/echo")
def echo(body: Echo):
    return body

@app.get("/today")
def today():
    return{"today": date.today().isoformat()} #formato aaa/mm/dd

# =============================================================================
# === TODO  =====================================================
# Crea un nuevo endpoint *GET /palindrome/{word}* que reciba una palabra y
# responda JSON con esta estructura:
#
#     {
#       "word": "oso",
#       "is_palindrome": true
#     }
#
# Reglas:
#   • Ignora mayúsculas/minúsculas (convierte a minúsculas antes de comparar).
#   • No uses clases ni librerías externas, solo slicing o reversed().
#   • Recuerda que la ruta debe devolver un dict (FastAPI lo convierte a JSON).
    #   palabra[::-1] == palabra
# Sugerencia de prueba:
#   http://127.0.0.1:8000/palindrome/Neuquen  → true

@app.get("/palindromo")
def palindromo(texto):

    texto = texto.lower().replace(" ", "").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
    return{"texto": texto, "es_palindromo": texto == texto[::-1]}
