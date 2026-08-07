import math
class CalculadoraEspecial:
    def __init__(self,num_1, num_2, resultado, precio):
        self.num_1=num_1
        self.num_2=num_2
        self.resultado=resultado
        self.Precio=precio

    def factorial(self):
        if self.num_1<0:
            print("No se puede calcular el factorial de un numero negativo")
            self.resultado = None
        else:
            self.resultado = math.factorial(self.num_1)


        
    def MaxComDiv(self):
        if  self.num_1<0:
            self.num_1=-1*self.num_1
        if self.num_2<0:
            self.num_2=-1*self.num_2
        if self.num_1>self.num_2 and self.num_2!=0:
            mayor=self.num_1
            menor=self.num_2
            while menor!=0:
             mayor, menor= menor, mayor % menor
            self.resultado=mayor
            return self.resultado
        elif self.num_2>self.num_1 and self.num_1!=0:
            mayor=self.num_2
            menor=self.num_1
            while menor!=0:
             mayor, menor = menor, mayor % menor
            self.resultado=mayor
            return self.resultado
        else:
            print("No existe un maximo comun divisor")
            return
    def MinComMul(self):
        if self.num_1*self.num_2 <0:
            self.resultado= ((self.num_1*self.num_2 * -1)/self.MaxComDiv())
            return self.resultado
        else:
            self.resultado= ((self.num_1*self.num_2)/self.MaxComDiv())
        return self.resultado

    def IVA(self):
        self.resultado = (self.Precio * 0.19)+self.Precio

miclasEspe=CalculadoraEspecial(0,0,0,0)

opcion=int(input("Ingrese la opcion que desea realizar: \n 1. Factorial \n 2. Maximo comun divisor \n 3. Minimo comun multiplo \n 4. IVA \n"))

match opcion :
   case 1:
      miclasEspe.num_1=int(input("ingrese el numero al que desea calcular el factorial: "))
      miclasEspe.factorial()
      print("El factorial es: ", miclasEspe.resultado)
   case 2:
      miclasEspe.num_1=int(input("ingrese el primer numero: "))
      miclasEspe.num_2=int(input("ingrese el segundo numero: "))
      print("El maximo comun divisor es: ", miclasEspe.MaxComDiv())
   case 3:
      miclasEspe.num_1=int(input("ingrese el primer numero: "))
      miclasEspe.num_2=int(input("ingrese el segundo numero: "))
      print("El minimo comun multiplo es: ", miclasEspe.MinComMul())
   case 4:
      miclasEspe.Precio=float(input("ingrese el precio del producto: "))
      miclasEspe.IVA()
      print("El precio total con IVA es: ", miclasEspe.resultado)