# Todas las clases heredan atributos de la clase "object", es el padre de todas las clases
# Clase Padre
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Clase Hija
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        # metodo super sirve para acceder a los metodos de la clase padre
        super().__init__(nombre, edad)
        self.sueldo = sueldo

empleado1 = Empleado("Pablo", 28, 5000)
print(empleado1.nombre)