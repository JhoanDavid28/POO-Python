from Persona import Persona


print('Creación de objetos'.center(30, '-'))
persona1 = Persona('Karla', 'Gomez', 30)
persona1.mostrar_detalle()

print('Eliminación de objetos'.center(30,'-'))
del persona1
