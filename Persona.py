class Persona:
    # atributos o características de una clase
    def __init__(self, nombre, apellido, edad, *valores, **terminos ): # *args: tupla de argumentos variables, **kwargs: para pasar un diccionario de valores
        # atributos de instancia
        self._nombre = nombre # el guion bajo se conoce como encapsulamiento
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos

    # Metódo o funciones de una clase
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')


persona1 = Persona('Juan', 'Perez', 28, '44553322', 2,3,5, m='manzana', p='pera')
#print(f'Objeto Persona 2: {persona1.nombre}, {persona1.apellido}, {persona1.edad}')
persona1.mostrar_detalle()  
#persona1.telefono = '555442211'
#print(persona1.telefono)


persona2 = Persona('Karla', 'Gomez', 30)
#print(f'Objeto Persona 2: {persona2.nombre}, {persona2.apellido}, {persona2.edad}')
persona2.mostrar_detalle()