
#-----------------------------------------------------------
#Estructuras de datos
#--Programa realizado por Erick Renato Vega Cerón de la Carrera Ingeniería en Sistemas Computacionales, en el Centro Universitario Hidalguense
#--13 de junio de 2018 

def altas():#Método para agregar contactos
    archivo=open('agenda.txt','a') #Abrir fichero, luego pedir campos
    contacto=raw_input("Nombre de contacto: ")
    celular=raw_input("No. de Celular: ")
    email=raw_input("Email: ")
    casa=raw_input("No Casa: ")
    registro=contacto+","+celular+","+email+","+casa #unir campos
    print registro #mostrar los campos en pantalla ya unificados
    archivo.write(registro) #escribir los campos unificados en el fichero
    print "El contacto ",contacto," se ha agregado a la lista" #avisar
    archivo.close()
    menu()

def bajas():#Método para borrar contactos
    borrado=0 #esta variable se usa para revisar si se encuentran concordancias para borrar, en caso de que sea 0, mostrara un mensaje
    archivo=open('agenda.txt','r')
    lineas=archivo.readlines() #leer las lineas del archivo y guardarlas en una lista (array)
    archivo.close() 
    consul=raw_input("Ingrese el contacto a eliminar ")
    for linea in lineas: #este for repasa linea por linea en la lista (array) que guardamos previamente  
        if consul in linea:#si el nombre que el usuario ingresó se encuentra en el array, entonces
            lineas_index=lineas.index(linea)#guarda la posicion de ese array en la variable lineas_index para saber qué linea borrar
            borrado=1    #se alza la bandera de que hay algo que borrar
    if borrado==0: #si no hay nada que borrar, es que no se ha encontrado el nombre en el registro y se avisa alo usuario
        print "No se ha encontrado ningún registro con ese nombre"
    if borrado==1:         #si se encontró algo que borrar entonces se procede al algoritmo de borrado
        archivo=open('agenda.txt','w')#se abre el archivo
        for linea in lineas: #de nuevo, se recorre cada linea del archivo
          if lineas.index(linea)!= lineas_index:#si la linea no es igual a la que se va a borrar, entonces se escribe. Solo se escriben en el archivo las lineas que no se han marcado para borrar
            archivo.write(linea)
        archivo.close()    
        print "El contacto ", consul, " ha sido removido"
        borrado=0#se vuelve a bajar la bandera de borrado, una vez borrada la linea
    menu()

def consultas():
    archivo=open('agenda.txt','r')
    lineas=archivo.readlines()
    archivo.close()
    for linea in lineas:#imprime cada linea encontrada en el fichero
        print linea
    menu()

def modificar():
    archivo=open('agenda.txt','r')#Se abre el archivo en modo lectura, se leen las lineas del mismo y se guardan en la variable contactos
    contactos=archivo.readlines()
    archivo.close()
    contact=raw_input("Ingresa el telefono del contacto a modificar: ")

    for elemento in contactos: #por cada elemento en la lista contactos
        if contact in elemento: #buscar el numero de telefono guardado en la variable contact, si se encuentra guardarlo en una lista llamada campos 
            campos=elemento.split(",") #y meter en cada indice un campo
            for linea in contactos: #por cada elemento en la lista contactos
                if contact in linea: #si el numero de telefono coincide en alguna linea
                    index=contactos.index(linea)  #se guarda el indice de esa linea
            print "-----------------------\n -Nombre de contacto: ",campos[0],"\n -No. Celular: ",campos[1],"\n -Email: ",campos[2],"\n No. de Casa: ",campos[3]
    elec=raw_input("Ingrese elemento a modificar \n 1.-Nombre\n 2.-No.Celular \n3.-Email\n 4.-No de casa \n 5.-Dejar de modificar\n")
    if elec=='1':#luego se da a elegir el campo a modificar 
      campos[0]=raw_input("Nombre: ")
    if elec=='2':
      campos[1]=raw_input("No. Celular: ")
    if elec=='3':
      campos[2]=raw_input("Email: ")
    if elec=='4':
      campos[3]=raw_input("No de Casa: ")

                
#y se procede a unir los campos en una sola variable tipo string                
    formato=str(campos[0])+","+str(campos[1])+","+str(campos[2])+","+str(campos[3])+"\n"
    contactos[index]=formato #se sustituye la linea antigua con la modificada en la variable temporal
    archivo1=open('agenda.txt','w')
    for linea in contactos:#y seescribe en el fichero
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
