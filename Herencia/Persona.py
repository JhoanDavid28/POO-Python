# Todas las clases heredan atributos de la clase "object", es el padre de todas las clases
# Clase Padre
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # metodo str sirve para sobreescribir
    def __str__(self):
        # muestramos el estado de la clase
        return f'Persona: [Nombre: {self.nombre}, Edad: {self.edad}]'        

# Clase Hija
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        # metodo super sirve para acceder a los metodos de la clase padre
        super().__init__(nombre, edad)
        self.sueldo = sueldo
        
    def __str__(self):
        return f"Empleado: [Sueldo: {self.sueldo}] {super().__str__()} "


#empleado1 = Empleado("Pablo", 28, 5000)
#print(empleado1.nombre)