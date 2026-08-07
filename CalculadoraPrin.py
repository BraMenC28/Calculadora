## interacción con el user
from Basic import CalculadoraBasica
from Trigo import CalculadoraTrigonometrica
print("-----CWelcome to the supreme calculator UwU-----" )

miCalcBasic= CalculadoraBasica(0,0,0)
miCalcTrigo= CalculadoraTrigonometrica(0,0)
numActual=0
ciclos=0


continuar ="s"

while (continuar=="s"):
    print(" 1.Suma \n 2. resta \n 3. multiplicacion \n 4. divicion \n 5. seno \n 6. coseno \n 7. tangente \n 8. factorial \n 9. maximo comun divisor \n 10. minimo comun multiplo \n 11. IVA")
    opcion=int(input("Escoja una de las opciones :"))
   
    miCalcBasic.num_1=miCalcBasic.resultado

    if opcion==1 and ciclos==0:
        miCalcBasic.num_1=int(input("ingrese el numero 1 :"))
        miCalcBasic.num_2=int(input("ingrese el numero 2 :"))
        miCalcBasic.suma()
        print("la suma es: ", miCalcBasic.resultado)
    elif opcion==1 and ciclos!=0:
        miCalcBasic.num_1=numActual
        print ("su numero uno ahora es", miCalcBasic.num_1)
        miCalcBasic.num_2=int(input("ingrese el numero 2 :"))
        miCalcBasic.suma()
        print("la suma es: ", miCalcBasic.resultado)
       
       
       
    elif opcion==2 and ciclos==0:
        n1=int(input("ingrese el numero 1 :"))
        n2=int(input("ingrese el numero 2 :"))
        print("la resta es: ", miCalcBasic.resta(n1,n2))
       
    elif opcion==2 and ciclos!=0:
        n1=numActual
        print ("su numero uno ahora es", n1)
        n2=int(input("ingrese el numero 2 :"))
        print("la resta es: ", miCalcBasic.resta(n1,n2))



    elif opcion==3 and ciclos==0:
        miCalcBasic.num_1=int(input("ingrese el numero 1 :"))
        miCalcBasic.num_2=int(input("ingrese el numero 2 :"))
        miCalcBasic.multiplicacion()
        print("la multiplicacion es: ", miCalcBasic.resultado)
       
    elif opcion==3 and ciclos!=0:
        miCalcBasic.num_1=numActual
        print ("su numero uno ahora es", miCalcBasic.num_1)
        miCalcBasic.num_2=int(input("ingrese el numero 2 :"))
        miCalcBasic.multiplicacion()
        print("la multiplicacion es: ", miCalcBasic.resultado)
       
       

    elif opcion==4 and ciclos==0:
        miCalcBasic.num_1=int(input("ingrese el numero 1 :"))
        miCalcBasic.num_2=int(input("ingrese el numero 2 :"))
        if miCalcBasic.num_2==0:
            print("no se puede dividir entre 0")
        else:
            miCalcBasic.divicion()
            print("la divicion es: ", miCalcBasic.resultado)
    elif opcion==4 and ciclos!=0:
        miCalcBasic.num_1=numActual
        print ("su numero uno ahora es", miCalcBasic.num_1)
        miCalcBasic.num_2=int(input("ingrese el numero 2 :"))
        if miCalcBasic.num_2==0:
            print("no se puede dividir entre 0")
        else:
            miCalcBasic.divicion()
            print("la divicion es: ", miCalcBasic.resultado)



    elif opcion==5:
        angulo=float(input("ingrese el ángulo en radianes: "))
        miCalcTrigo.seno(angulo)

    
    elif opcion==6:
        angulo=float(input("ingrese el angulo en radianes: "))
        miCalcTrigo.cos(angulo)


    elif opcion==7:
        angulo=float(input("ingrese el ángulo en radianes: "))
        miCalcTrigo.tan(angulo)
    
    else:
     print("error")
    continuar=input("desea continuar? s/n :" )
    if continuar=="s" :
        ciclos=ciclos+1
        numActual=miCalcBasic.resultado
        if opcion>=5 and opcion<=7:
            numActual=miCalcTrigo.resultado
        print("ciclos actuales",ciclos)
        print ("numero acutal", numActual)
        print ("___")