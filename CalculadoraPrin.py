## interacción con el user
from Basic import Calculadora
print("-----Welcome to the supreme calculator UwU-----" )

miCalc= Calculadora(0,0,0)
numActual=0
ciclos=0


continuar ="s"

while (continuar=="s"):
    print(" 1.Suma \n 2. resta \n 3. multiplicacion \n 4. divicion ")
    opcion=int(input("Escoja una de las opciones :"))
   
    miCalc.num_1=miCalc.resultado

    if opcion==1 and ciclos==0:
        miCalc.num_1=int(input("ingrese el numero 1 :"))
        miCalc.num_2=int(input("ingrese el numero 2 :"))
        miCalc.suma()
        print("la suma es: ", miCalc.resultado)
    elif opcion==1 and ciclos!=0:
        miCalc.num_1=numActual
        print ("su numero uno ahora es", miCalc.num_1)
        miCalc.num_2=int(input("ingrese el numero 2 :"))
        miCalc.suma()
        print("la suma es: ", miCalc.resultado)
       
       
       
    elif opcion==2 and ciclos==0:
        n1=int(input("ingrese el numero 1 :"))
        n2=int(input("ingrese el numero 2 :"))
        print("la resta es: ", miCalc.resta(n1,n2))
       
    elif opcion==2 and ciclos!=0:
        n1=numActual
        print ("su numero uno ahora es", n1)
        n2=int(input("ingrese el numero 2 :"))
        print("la resta es: ", miCalc.resta(n1,n2))


        
    elif opcion==3 and ciclos==0:
        miCalc.num_1=int(input("ingrese el numero 1 :"))
        miCalc.num_2=int(input("ingrese el numero 2 :"))
        miCalc.multiplicacion()
        print("la multiplicacion es: ", miCalc.resultado)
       
    elif opcion==3 and ciclos!=0:
        miCalc.num_1=numActual
        print ("su numero uno ahora es", miCalc.num_1)
        miCalc.num_2=int(input("ingrese el numero 2 :"))
        miCalc.multiplicacion()
        print("la multiplicacion es: ", miCalc.resultado)
       
       

    elif opcion==4 and ciclos==0:
        miCalc.num_1=int(input("ingrese el numero 1 :"))
        miCalc.num_2=int(input("ingrese el numero 2 :"))
        if miCalc.num_2==0:
            print("no se puede dividir entre 0")
        else:
            miCalc.divicion()
            print("la divicion es: ", miCalc.resultado)
    elif opcion==4 and ciclos!=0:
        miCalc.num_1=numActual
        print ("su numero uno ahora es", miCalc.num_1)
        miCalc.num_2=int(input("ingrese el numero 2 :"))
        if miCalc.num_2==0:
            print("no se puede dividir entre 0")
        else:
            miCalc.divicion()
            print("la divicion es: ", miCalc.resultado)
       
    else:
     print("error")
    continuar=input("desea continuar? s/n :" )
    if continuar=="s" :
        ciclos=ciclos+1
        numActual=miCalc.resultado
        print("ciclos actuales",ciclos)
        print ("numero acutal", numActual)
        print ("___")