import math
class CalculadoraBasica:
    def __init__(self,num_1, num_2, resultado):
        self.num_1=num_1
        self.num_2=num_2
        self.resultado=resultado
    def suma(self):
        self.resultado=self.num_1+self.num_2
    def resta(self, a, b):
        self.resultado= a-b
        return self.resultado
    def multiplicacion(self):
        self.resultado= self.num_1*self.num_2
    def divicion(self):
        self.resultado= self.num_1/self.num_2