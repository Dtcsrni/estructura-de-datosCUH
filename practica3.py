print("Bienvenido")
salir=0
while salir!=1:
    calif1=input("Ingresar calificacion 1 ")
    calif2=input("Ingresar calificacion 2 ")
    calif3=input("Ingresar calificacion 3 ")
    calif4=input("Ingresar calificacion 4 ")
    calif5=input("Ingresar calificacion 5 ")
    prom=(calif1+calif2+calif3+calif4+calif5)/5
    print "El promedio es ",prom
    if prom>=9:
        print("El alumno tiene beca")
    else:
        print("El alumno no alcanza beca")
    salir=input("Salir? 1: Si 2: No")
    
