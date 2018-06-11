registro=[]
def altas():
    archivo=open('productos.txt','a')
    producto=raw_input("Nombre: ")
    presentacion=raw_input("Presentacion: ")
    costo=raw_input("Costo: ")
    proveedor=raw_input("Proveedor: ")
    existencia=raw_input("Existencia: ")
    registro=producto+" "+presentacion+" "+costo+" "+proveedor+" "+existencia
    print registro
    archivo.write(registro)
    print "El producto ",producto," se ha agregado a la lista"
    archivo.close()
    menu()

def bajas():
    borrado=0
    archivo=open('productos.txt','r')
    lineas=archivo.readlines()
    archivo.close()
    consul=raw_input("Ingrese el producto a eliminar ")
    for linea in lineas:
        if consul in linea:
            lineas_index=lineas.index(linea)
            borrado=1    
    if borrado==0:
        print "No se ha encontrado ningún registro con ese nombre"
    if borrado==1:         
        archivo=open('productos.txt','w')
        for linea in lineas:
          if lineas.index(linea)!= lineas_index:
            archivo.write(linea)
        archivo.close()    
        print "El producto ", consul, " ha sido removido"
        borrado=0
    menu()

def modifica():
    print "Sin implementar con archivos"

def consultas():
    archivo=open('productos.txt','r')
    lineas=archivo.readlines()
    archivo.close()
    print lineas
    menu()
def buscarproducto():
    criterio=raw_input("Ingresa el criterio de busqueda ")
    for registro in registros:
        if criterio in registro:
            registro
            menu()
def error():
    print "La opcion elegida no es valida, ingresa un numero valido"
    menu()

def menu():

    print""
    opcion=input("Elije la accion a realizar: \n 1. Alta de productos \n 2. Baja de productos \n 3.Consultas \n 4.Salir del programa\n") 
    if opcion==1:
        altas()
    elif opcion==2:
        bajas()
    elif opcion ==3:
        consultas()
    elif opcion==4:
        print "Hasta luego"
    else:
        error()
menu()
