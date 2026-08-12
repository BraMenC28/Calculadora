import math
class CalculadoraEspecial:
    def __init__(self,num_1, num_2, resultado, precio):
        self.num_1=num_1
        self.num_2=num_2
        self.resultado=resultado
        self.Precio=precio
    def potencia(self):
       if self.num_2<0 and self.num_1==0:
          print("El signo del exponente y la base no permiten una divicion por cero")
       else:
        self.resultado=self.num_1**self.num_2
        print ("El resultado de la potencia es:", self.resultado)
    def raiz(self):#num_1=indice, num_2=argumento
        if self.num_1==0:
            print("No se puede sacar raiz a un numeor evaluado con un indice igua a cero")
        elif self.num_1%2==0 and self.num_2<0:
            print("Los datos escritos no tienen solucion real")
        elif self.num_1>0 and self.num_2<0:
            resultado=-1*((self.num_2*-1)**(1/self.num_1))
            print("El resultado es", resultado)
        else:
            resultado=self.num_2**(1/self.num_1)
            print("El resultado es", resultado)
    def fibonacci(self):
        i=0
        fibo=[0,1]
        for i in range (self.num_1):
            aumento=fibo[-1]+fibo[-2]
            fibo.append(aumento)
        return fibo[self.num_1-1]
    def factorial(self):
        if self.num_1<0:
            print("No se puede calcular el factorial de un numero negativo")
        elif self.num_1==0:
           self.resultado=1
           print("El factorial es: ", self.resultado)
        else:
           menor=None
           while menor!=1:
             if menor==None:
              menor=self.num_1
              menor=menor-1
             else :
              menor=menor-1
             self.resultado=self.num_1*menor
             self.num_1=self.resultado
           print("El factorial es: ", self.resultado)
    def MaxComDiv(self):
        if  self.num_1<0:
            self.num_1=-1*self.num_1
        if self.num_2<0:
            self.num_2=-1*self.num_2
        if abs(self.num_1)==abs(self.num_2) and self.num_2!=0 and self.num_1!=0:
             self.resultado=abs(self.num_2)
             return self.resultado
        if self.num_2==0 and self.num_1==0:
           return None
        if  self.num_2==0 or self.num_1==0:
           if self.num_2==0:
              return self.num_1
           else:
              return self.num_2
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
        iva=float(input("ingrese el valor del IVA: "))
        self.resultado = (self.Precio * iva)+self.Precio