registros=[]
def altas():
    producto=raw_input("Nombre: ")
    presentacion=raw_input("Presentacion: ")
    costo=raw_input("Costo: ")
    proveedor=raw_input("Proveedor: ")
    existencia=raw_input("Existencia: ")
    registro=producto+" "+presentacion+" "+costo+" "+proveedor+" "+existencia
    registros.append(registro)
    print "El producto ",producto," se ha agregado a la lista"
    menu()

def bajas():
    baja=raw_input("Ingresa el producto a dar de baja de la lista: ")
    for registro in registros:
        if baja in registro:
            registros.remove(baja)
            print "El producto ", baja, " ha sido removido"
    menu()

def modifica():
    modif=raw_input("Ingresa el producto a modificar: ")
    if modif in registros:
        posicion=registros.index(modif)
        nuevo=raw_input("Ingresa el producto modificado: ")
        registros[posicion]=nuevo
    else:
        print "El producto", baja, "no se encuentra en la lista"
    menu()

def consultas():
    for elemento in registros:
        print elemento
    menu()
def buscarproducto():
    criterio=raw_input("Ingresa el criterio de busqueda ")
    for registro in registros:
        if criterio in registro:
            print registro
            menu()
def error():
    print "La opcion elegida no es valida, ingresa un numero valido"
    menu()

def menu():
    print""
    opcion=input("Elije la accion a realizar: \n 1. Alta de productos \n 2. Baja de productos \n 3. Modificacion de productos \n 4.Consultas \n 5. Buscar producto \n 6.Salir del programa\n") 
    if opcion==1:
        altas()
    elif opcion==2:
        bajas()
    elif opcion ==3:
        modifica()
    elif opcion==4:
        consultas()
    elif opcion==5:
        buscarproducto()    
    elif opcion==6:
        print "Hasta luego"
    else:
        error()
menu()
