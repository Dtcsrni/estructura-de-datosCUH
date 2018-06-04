productos=[]
def altas():
    producto=raw_input("Ingresa un producto a la lista: ")
    productos.append(producto)
    menu()

def bajas():
    baja=raw_input("Ingresa el producto a dar de baja de la lista: ")
    if baja in productos:
        productos.remove(baja)
        print "El producto ", baja, " ha sido removido"
    else:
        print "El producto", baja, "no se encuentra en la lista"
    menu()

def modifica():
    modif=raw_input("Ingresa el producto a modificar: ")
    if modif in productos:
        posicion=productos.index(modif)
        nuevo=raw_input("Ingresa el producto modificado: ")
        productos[posicion]=nuevo
    else:
        print "El producto", baja, "no se encuentra en la lista"
    menu()

def consultas():
    for elemento in productos:
        print elemento
    menu()
def error():
    print "La opcion elegida no es valida, ingresa un numero valido"
    menu()

def menu():
    print""
    opcion=input("Elije la accion a realizar: \n 1. Alta de productos \n 2. Baja de productos \n 3. Modificacion de productos \n 4.Consultas \n 5. Salir del programa\n") 
    if opcion==1:
        altas()
    elif opcion==2:
        bajas()
    elif opcion ==3:
        modifica()
    elif opcion==4:
        consultas()
    elif opcion==5:
        print "Hasta luego"
    else:
        error()
menu()
