import math
class CalculadoraTrigonometrica:
    def __init__(self,num_1, resultado):
        self.num_1=num_1
        self.resultado=resultado
    def seno(self, ang):
        self.resultado=math.sin (ang)
        print("El seno es:", self.resultado)
    def cos(self,ang):
        self.resultado=math.cos(ang)
        print("el coseno es:",self.resultado )
    def tan(self,ang):
        self.resultado=math.tan(ang)
        print("la tangente es:",self.resultado)