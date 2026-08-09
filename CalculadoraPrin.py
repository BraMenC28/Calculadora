from Basic import CalculadoraBasica
from Trigo import CalculadoraTrigonometrica
from Especi import CalculadoraEspecial
print("-----Calculadora Completa-----" )
miCalcBasic= CalculadoraBasica(0,0,0)
miCalcTrigo= CalculadoraTrigonometrica(0,0)
miclasEspe=CalculadoraEspecial(0,0,0,0)
numActual=0
ciclos=0
continuar ="s"
while (continuar=="s"):
    print(" 1.Suma \n 2. resta \n 3. multiplicacion \n 4. divicion \n 5. seno \n 6. coseno \n 7. tangente \n 8. factorial \n 9. maximo comun divisor \n 10. minimo comun multiplo \n 11. IVA \n 12. potencia \n 13. raiz \n 14. fibonacci")
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

    elif opcion==8:
       miclasEspe.num_1=int(input("ingrese el numero al que desea calcular el factorial: "))
       miclasEspe.factorial()
       print("El factorial es: ", miclasEspe.resultado)

    elif opcion==9:
      miclasEspe.num_1=int(input("ingrese el primer numero: "))
      miclasEspe.num_2=int(input("ingrese el segundo numero: "))
      print("El maximo comun divisor es: ", miclasEspe.MaxComDiv())
    elif opcion==10:
      miclasEspe.num_1=int(input("ingrese el primer numero: "))
      miclasEspe.num_2=int(input("ingrese el segundo numero: "))
      print("El minimo comun multiplo es: ", miclasEspe.MinComMul())
    elif opcion==11:
      miclasEspe.Precio=float(input("ingrese el precio del producto: "))
      miclasEspe.IVA()
      print("El precio total con IVA es: ", miclasEspe.resultado) 
    elif opcion==12:
        miclasEspe.num_1=float(input("ingrese la base de la potencia: "))
        miclasEspe.num_2=int(input("ingrese el exponente de la potencia: "))
        miclasEspe.potencia()
    elif opcion==13:
        miclasEspe.num_1=float(input("ingrese el indice: "))
        miclasEspe.num_2=float(input("ingrese el argumento: "))
        miclasEspe.raiz()
    elif opcion==14:
        miclasEspe.num_1=int(input("ingrese la posicion del numero de fibonacci que desea conocer (La cuenta inicia desde el 0): "))
        print("El numero de la posicion es", miclasEspe.fibonacci())

    else:
     print("error")
    continuar=input("desea continuar? s/n :" )
    if continuar=="s" and 1<=opcion<=4:
        ciclos=ciclos+1
        numActual=miCalcBasic.resultado
        print("ciclos actuales",ciclos)
        print ("numero acutal", numActual)
        print ("___")