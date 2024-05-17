class Persona:
    # atributos o características de una clase
    def __init__(self, nombre, apellido, edad): # *args: tupla de argumentos variables, **kwargs: para pasar un diccionario de valores
        # atributos de instancia
        # el guion bajo se conoce como ENCAPSULAMIENTO
        self._nombre = nombre 
        self._apellido = apellido
        self._edad = edad

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

    # GET para la propiedad apellido
    @property
    def apellido(self):
        return self._apellido
    
    # SET para la propiedad apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        self._edad = edad

    # Metódo o funciones de una clase
    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')


if __name__ =='__main__':
    persona1 = Persona ('Juan', 'Perez', 28 )
    persona1.nombre = 'Juan Carlos'
    persona1.apellido = 'Lara'
    persona1.edad = 30
    persona1.mostrar_detalle()

    print(__name__)

