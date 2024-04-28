class Cubo:
    """
    Clase para calcular el area de un Rectangulo
    """
    def __init__(self, ancho, alto, profundio):
        self.ancho = ancho 
        self.alto = alto
        self.profundo = profundio

    # Metodo 
    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundo
    
ancho = int(input('Proporcione la ancho: '))
alto = int(input('Proporcione la alto: '))
profundo = int(input('Proporcione la profundo: '))

cubo1 = Cubo(ancho, alto, profundo)
print(f'Área rectángulo: {cubo1.calcular_volumen()}')
