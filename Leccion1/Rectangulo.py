class Rectangulo:
    """
    Clase para calcular el area de un Rectangulo
    """
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    # Metodo 
    def calcular_area(self):
        return self.base * self.altura
    
base = int(input('Proporcione la base: '))
altura = int(input('Proporcione la altura: '))

rectangulo1 = Rectangulo(base, altura)
print(f'Área rectángulo: {rectangulo1.calcular_area()}')

base = int(input('Proporcione la base: '))
altura = int(input('Proporcione la altura: '))

rectangulo1 = Rectangulo(base, altura)
rectangulo2 = Rectangulo(base, altura)
print(f'Área rectángulo: {rectangulo2.calcular_area()}')