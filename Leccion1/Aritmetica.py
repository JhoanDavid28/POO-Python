class Aritmetica:
    """
    Clase Aritmetica para realizea las operaciones de sumar, restar, etc
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    # MetodoSumar
    def sumar(self):
        return self.operandoA + self.operandoB
    
    def restar(self):
        return self.operandoA - self.operandoB

    def multiplicacion(self):
        return self.operandoA * self.operandoB
    
    def division(self): 
        return self.operandoA / self.operandoB
    

aritmetica1 = Aritmetica(5, 3)
print(f'Suma: {aritmetica1.sumar()}')
print(f'Resta: {aritmetica1.restar()}')
print(f'Multiplicación: {aritmetica1.multiplicacion()}')
print(f'División: {aritmetica1.division():.2f}')