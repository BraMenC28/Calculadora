## interacción con el user
from Basic import Calculadora
print("-----Welcome to the supreme calculator UwU-----" )

miCalc= Calculadora(0,0,0)
continuar ="s"
while (continuar=="s"):
    print(" 1.Suma \n 2. resta \n 3. multiplicacion \n 4. divicion ")

    opcion=int(input("EScoja una de las opciones "))

    if opcion==1:
        miCalc.num_1=int(input("ingrese el numero 1 "))
        miCalc.num_2=int(input("ingrese el numero 2 "))
        miCalc.suma()
        print("la suma es: ", miCalc.resultado)
    elif opcion==2:
        n1=int(input("ingrese el numero 1 "))
        n2=int(input("ingrese el numero 2 "))
        print("la resta es: ", miCalc.resta(n1,n2))
    elif opcion==3:
        miCalc.num_1=int(input("ingrese el numero 1 "))
        miCalc.num_2=int(input("ingrese el numero 2"))
        miCalc.multiplicacion()
        print("la multiplicacion es: ", miCalc.resultado)

    elif opcion==4:
        miCalc.num_1=int(input("ingrese el numero 1 "))
        miCalc.num_2=int(input("ingrese el numero 2 "))
        miCalc.divicion()
        print("la divicion es: ", miCalc.resultado)
    else:
     print("error")
    continuar=input("desea continuar? s/n" )