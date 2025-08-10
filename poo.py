class Animal:   #plantilla de objetos de un mismo tipo
    pass        #pass es para  que no se ejecute la clase y no de error

class Perro(Animal):    #Subclase que hereda los atributos de la clase en parentesis
    
    """
    atributos:
        nombre: str
        edad: it
        raza: str
    """
    
    def __init__(self,nombre,edad,raza):
        #pass es para que no haga nada y no de error
        #se pone primero self
        """
        se ejecuta automaticamente al crear una instancia:
        - Guarda datos en el propio objeto (self).
        """
    
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} guau!")

    def cumple_años(self):
        self.edad += 1      #el += es para que le sume 1 a la variable self.edad
        print(f"{self.nombre} ahora tiene {self.edad} años")

primer_perro = Perro("Lola", 4, "Doberman") #nombre, edad, raza (self se omite)
segundo_perro = Perro("Firulais", 2, "Mestizo")

primer_perro.ladrar() #Metodo
segundo_perro.cumple_años()

"""
TODO 1.
------
Implementa la clase *Libro* siguiendo estas reglas:

Atributos de instancia
    * titulo      (str)
    * autor       (str)
    * paginas     (int)

Métodos
    * _init_()      → guarda atributos
    * resumen()       → devuelve str "«<titulo>» de <autor>, <paginas> pág."

Ejemplo de uso (cuando lo tengas listo):

    l1 = Libro("1984", "George Orwell", 328)
    l2 = Libro("Clean Code", "R. Martin", 464)

    print(l1.resumen())                 # «1984» de George Orwell, 328 pág.
"""
class Libro:
    pass
    def __init__(self,titulo,autor,paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def titulo(self):
        print(f"{self.titulo} Harry Potter")

    def autor(self):
        print(f"{self.autor} J.K. Rowling")

    def paginas(self):
        print(f"{self.paginas} 500")
    
    def resumen(self) -> str:
        return f"{self.titulo} de {self.autor}, {self.paginas} pag."