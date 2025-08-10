# =============================================================================
# Mini-proyecto: Gestor de Cursos con POO
# Herencia + Polimorfismo + Composición (explicado paso a paso)
# -----------------------------------------------------------------------------
# Objetivo:
#   - Reforzar POO con un ejemplo útil y entendible.
#   - Ver CÓMO y POR QUÉ se usan clases base y subclases.
#   - Practicar: _init, self, métodos de instancia, override, __str, __len_.
#
# Cómo ejecutar:
#   Mac: python3 poo_avanzado.py
#   Win: py poo_avanzado.py
#
# Estructura:
#   Alumno        → clase sencilla (entidad)
#   Curso (base)  → comportamiento común (matricular, desmatricular, resumen…)
#   ├─ CursoPython     (subclase)
#   ├─ CursoFinanzas   (subclase)
#   └─ CursoJS         (subclase)
#
# Demostración:
#   La función demo() crea cursos de distintos tipos, matricula alumnos y
#   muestra polimorfismo llamando .resumen() sin “preguntar” el tipo.
# =============================================================================

class Alumno:


	"""
	Representa a una persona con nombre y email
	"""
	def __init__(self, nombre: str, email: str):
		self.nombre = nombre.strip() #strip elimina espacios al principio y al final de un string
		self.email = email.strip().lower()

		if not self.nombre:
			raise ValueError("el nombre no puede estar vacio")		#raise es un return de error
		if "@" not in self.email or "." not in self.email:
			raise ValueError("Email invalido")
	
	def __str__(self):

		return f"{self.nombre} {self.email}"
	
class Curso:

	"""
	Clase base para distintos tipos de cursos.

    Conceptos clave:
    - HERENCIA: las subclases (CursoPython, CursoFinanzas, CursoJS) heredan lo común.
    - COMPOSICIÓN: un Curso “contiene” alumnos (lista interna de Alumno).
    - POLIMORFISMO: todas las subclases tendrán un método resumen() con la misma “forma”,
      pero cada una responderá a su manera (emoji, extras, etc.).
	"""
	def __init__(self, nombre: str, duracion_horas: int, cupo_max: int = 30):
		self.nombre = nombre.strip()
		self.duracion_horas = int(duracion_horas)
		self.cupo_max = int(cupo_max)
		
		#Atributo Privado
		self._alumnos: list[Alumno] = []

		if not self.nombre:
			raise ValueError("El nombre del curso no puede estar vacio")
		if self.duracion_horas <= 0:
			raise ValueError ("La duracion debe ser mayor a 0")
		if self.cupo_max <= 0:
			raise ValueError ("EL cupo debe ser mayor a 0")
		
	#----------------Metodos Comunes (todas las subclases heredan)------------

	def hay_cupo(self) -> bool:
		return len(self._alumnos) < self.cupo_max				#len() es longitud
	
	def matricular(self, alumno: Alumno) -> bool:
		"""
		intenta añadir un alumno
		Devuelve True si lo agrega: False si no hay cupo o ya existe ese email
		-"Primero ver si hay cupo"
		-"Luego evitar duplicados por email"
		-"Si todo ok, agregamos"
		"""
		if not self.hay_cupo():					#self hace referencia a la clase
			return False
		
		for a in self._alumnos:
			if a.email == alumno.email:
				return False
		self._alumnos.append(alumno)
		return True
	
	def desmatricular(self, email:str) -> bool:

		"""
		Quita el alumno por email
		"""
		email_formateado = email.strip().lower()

		for i, a in enumerate(self._alumnos):		#itera indice y elemento
			if a.email == email_formateado:
				self._alumnos.pop(i)		#pop recibe solo indices como parametros
				return True
		return False
	
	def inscritos(self) -> list[Alumno]:
		"""Devuelve una copia de la lista Alumno"""
		return list(self._alumnos)
	
	def resumen(self) -> str:
		"""
		Metodo pensado para ser sobreescrito por las subclases
		Polimorfismo: misma estructura distintos resultados
		"""
		return f"{self.nombre} . {self.duracion_horas}h . cupo {len(self._alumnos)}/{self.cupo_max}"
	
	#-------Clases Amables (dunder helpers)----

	def __len__(self) -> int:
		"""retorna la cantidad de alumnos inscritos"""
		return len(self._alumnos)
	
class CursoPython(Curso):		#CursoPython hereda de Curso
	"""
	Subclase que personaliza
	-Nombre fijo
	-Atributo extra: nivel
	-resumen() con estilo propio (🐍)
	"""

	def __init__(self, duracion_horas: int = 20, cupo_max: int = 25, nivel: str = "Basico"):
		super().__init__("Curso de Python", duracion_horas, cupo_max)			#entras al init de tu clase madre
		self.nivel = nivel

	def resumen(self):
		return f"🐍 {self.nombre} ({self.nivel}) · {self.duracion_horas}h · {len(self)}/{self.cupo_max} inscritos"
	
class CursoFinanzas(Curso):

	def __init__(self, duracion_horas: int = 24, cupo_max: int = 29, nivel: str = "Avanzado"):
		super().__init__("Curso de Finanzas", duracion_horas, cupo_max)
		self.nivel = nivel

	def resumen(self):
		return f"{self.nombre} Nivel {self.nivel} . {self.duracion_horas}h . {len(self._alumnos)/{self.cupo_max}}"

class CursoJS(Curso):

	def __init__(self, duracion_horas: int = 16, cupo_max: int = 21, nivel: str = "Intermedio"):
		super().__init__("Curso de JavaScript", duracion_horas, cupo_max)
		self.nivel = nivel

def demo():
	"""
	Crea varios cursos, matricula alumnos y muestra polimorfismo:
	-Recorremos una lista de cursos (de distintos tipos)
	-Llamamos SIEMPRE .resumen() -> cada clase responde diferente
	"""

	py = CursoPython()

	a1 = Alumno("Edinson", "ed@ed.com")
	a2 = Alumno("Angel", "an@an.com")
	a3 = Alumno( "Diego", "die@die.com")

	py.matricular(a1)
	py.matricular(a2)
	py.matricular(a3)

	print(py.resumen())

	py.desmatricular(a1.email)
	py.desmatricular(a2.email)
	py.desmatricular(a3.email)

	print(py.resumen())

demo()

class Matematicas(Curso):
	def __init__(self, nombre: str, duracion_horas: int, cupo_max: int = 30):
		self.nombre = nombre.strip()
		self.duracion_horas = int(duracion_horas)
		self.cupo_max = int(cupo_max)
		
		self._alumnos: list[Alumno] = []

		if not self.nombre:
			raise ValueError("El nombre del curso no puede estar vacio")
		if self.duracion_horas <= 0:
			raise ValueError ("La duracion debe ser mayor a 0")
		if self.cupo_max <= 0:
			raise ValueError ("EL cupo debe ser mayor a 0")
	def hay_cupo(self) -> bool:
			return len(self._alumnos) < self.cupo_max
	def matricular(self, alumno: Alumno) -> bool:
		
		if not self.hay_cupo():					#self hace referencia a la clase
			return False
		
		for a in self._alumnos:
			if a.email == alumno.email:
				return False
		self._alumnos.append(alumno)
		return True
	
	def desmatricular(self, email:str) -> bool:

		email_formateado = email.strip().lower()

		for i, a in enumerate(self._alumnos):		#itera indice y elemento
			if a.email == email_formateado:
				self._alumnos.pop(i)		#pop recibe solo indices como parametros
				return True
		return False
	
	def inscritos(self) -> list[Alumno]:

		return list(self._alumnos)

	def resumen(self):
		
		return f"{self.nombre} Nivel {self.nivel} . {self.duracion_horas}h . {len(self._alumnos)/{self.cupo_max}}"
	
	def __len__(self) -> int:
	
		return len(self._alumnos)
	

	
class Fisica(Curso):
	def __init__(self, nombre: str, duracion_horas: int, cupo_max: int = 20):
		self.nombre = nombre.strip()
		self.duracion_horas = int(duracion_horas)
		self.cupo_max = int(cupo_max)
		
		self._alumnos: list[Alumno] = []

		if not self.nombre:
			raise ValueError("El nombre del curso no puede estar vacio")
		if self.duracion_horas <= 0:
			raise ValueError ("La duracion debe ser mayor a 0")
		if self.cupo_max <= 0:
			raise ValueError ("EL cupo debe ser mayor a 0")
	def hay_cupo(self) -> bool:
			return len(self._alumnos) < self.cupo_max
	def matricular(self, alumno: Alumno) -> bool:
		
		if not self.hay_cupo():					#self hace referencia a la clase
			return False
		
		for a in self._alumnos:
			if a.email == alumno.email:
				return False
		self._alumnos.append(alumno)
		return True
	
	def desmatricular(self, email:str) -> bool:

		email_formateado = email.strip().lower()

		for i, a in enumerate(self._alumnos):		#itera indice y elemento
			if a.email == email_formateado:
				self._alumnos.pop(i)		#pop recibe solo indices como parametros
				return True
		return False
	
	def inscritos(self) -> list[Alumno]:

		return list(self._alumnos)
	
	def resumen(self) -> str:

		return f"{self.nombre} . {self.duracion_horas}h . cupo {len(self._alumnos)}/{self.cupo_max}"
	
	def __len__(self) -> int:
	
		return len(self._alumnos)