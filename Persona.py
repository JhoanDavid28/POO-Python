class Persona:
    # atributos o características de una clase
    def __init__(self, nombre, apellido, edad): # *args: tupla de argumentos variables, **kwargs: para pasar un diccionario de valores
        # atributos de instancia
        self._nombre = nombre # el guion bajo se conoce como encapsulamiento
        self.apellido = apellido
        self.edad = edad

    # Decorador para modificar el comportamiento de nuestro método
    @property # el método "nombre" va a recuperar la informacion del atributo "_nombre"
    # método get
    def nombre(self):
        print('Llamando método get nombre')
        return self._nombre
    
    # método set, para modificar el atributo _nombre, accedemos sin el guin bajo
    @nombre.setter
    def nombre(self, nombre):
        print('Llamando método set nombre')
        self._nombre = nombre # ahora el se puede modificar los valores del atributo 

  
    # Metódo o funciones de una clase
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')


persona1 = Persona ('Juan', 'Perez', 28 )

#print(f'Objeto Persona 2: {persona1.nombre}, {persona1.apellido}, {persona1.edad}')
#persona1.mostrar_detalle()  
#print(persona1.nombre)
# agregando el nuevo valor mediante el método set, se encapsula el atributo _nombre
persona1.nombre = 'Juan Carlos'
print(persona1.nombre)

#persona1.telefono = '555442211'
#print(persona1.telefono)

