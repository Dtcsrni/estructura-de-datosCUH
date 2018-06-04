accion=input("Elija accion a realizar 1.- Suma 2.- Resta 3.-Multiplicacion 4.- Division 5.- Promedio")
if (accion==1):
    num1=input("Ingrese primer numero a sumar")
    num2=input("Ingrese segundo numero a sumar")
    suma=num1+num2
    print("El resultado de la suma es ",suma)
if (accion==2):
    num1=input("Ingrese primer numero a restar")
   num2=input("Ingrese segundo numero a restar")
    resta=num1-num2
    print("El resultado de la suma es ",resta)
if (accion==3):
     num1=input("Ingrese primer numero a multiplicar")
     num2=input("Ingrese segundo numero a multiplicar")
     multi=num1*num2
    print("El resultado de la suma es ",multi)
if (accion==4):
     num1=input("Ingrese primer numero a division")
     num2=input("Ingrese segundo numero a division")
     div=num1/num2
    print("El resultado de la suma es ",div)
if (accion==5):
     num1=input("Ingrese primer numero a promediar")
     num2=input("Ingrese segundo numero a promediar")
    num3=input("Ingrese tercero numero a promediar")
   num4=input("Ingrese cuarto numero a promediar")
    result=(num1+num2+num3+num4)/4
    print("El resultado de la suma es ",result)
    
