agenda=[]

def altas():
    archivo=open('agenda.txt','a')
    contacto=raw_input("Nombre de contacto: ")
    celular=raw_input("No. de Celular: ")
    email=raw_input("Email: ")
    casa=raw_input("No Casa: ")
    registro=contacto+","+celular+","+email+","+casa
    print registro
    archivo.write(registro)
    print "El contacto ",contacto," se ha agregado a la lista"
    archivo.close()
    menu()

def bajas():
    borrado=0
    archivo=open('agenda.txt','r')
    lineas=archivo.readlines()
    archivo.close()
    consul=raw_input("Ingrese el contacto a eliminar ")
    for linea in lineas:
        if consul in linea:
            lineas_index=lineas.index(linea)
            borrado=1    
    if borrado==0:
        print "No se ha encontrado ningún registro con ese nombre"
    if borrado==1:         
        archivo=open('agenda.txt','w')
        for linea in lineas:
          if lineas.index(linea)!= lineas_index:
            archivo.write(linea)
        archivo.close()    
        print "El contacto ", consul, " ha sido removido"
        borrado=0
    menu()

def consultas():
    archivo=open('agenda.txt','r')
    lineas=archivo.readlines()
    archivo.close()
    for linea in lineas:
        print linea
    menu()

def modificar():
    archivo=open('agenda.txt','r')
    contactos=archivo.readlines()
    archivo.close()
    contact=raw_input("Ingresa el telefono del contacto a modificar: ")

    for elemento in contactos:
        if contact in elemento:
            campos=elemento.split(",")
            for linea in contactos:
                if contact in linea:
                    index=contactos.index(linea) 
            print "-----------------------\n -Nombre de contacto: ",campos[0],"\n -No. Celular: ",campos[1],"\n -Email: ",campos[2],"\n No. de Casa: ",campos[3]
    elec=raw_input("Ingrese elemento a modificar \n 1.-Nombre\n 2.-No.Celular \n3.-Email\n 4.-No de casa \n 5.-Dejar de modificar\n")
    if elec=='1':
      campos[0]=raw_input("Nombre: ")
    if elec=='2':
      campos[1]=raw_input("No. Celular: ")
    if elec=='3':
      campos[2]=raw_input("Email: ")
    if elec=='4':
      campos[3]=raw_input("No de Casa: ")

                
                
    formato=str(campos[0])+","+str(campos[1])+","+str(campos[2])+","+str(campos[3])+"\n"
    contactos[index]=formato
    archivo1=open('agenda.txt','w')
    for linea in contactos:
        archivo1.write(linea)
    archivo1.close()
    print ("Contacto modificado satisfactoriamente!")
    menu()    

def menu():

    print""
    opcion=input("Elije la accion a realizar: \n1. Agregar contacto \n2. Borrar contacto \n3.Consultar contactos \n4.Modificar contacto \n5.-Salir \n") 
    if opcion==1:
        altas()
    elif opcion==2:
        bajas()
    elif opcion ==3:
        consultas()
    elif opcion==4:
        modificar()
    else:
        error()
menu()    
