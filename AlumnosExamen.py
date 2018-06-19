agenda=[]
promedio=[]
def altas():
    archivo=open('calificaciones.txt','a')
    alumno=raw_input("Nombre de alumno: ")
    matricula=raw_input("Matricula de alumno: ")
    calif1=raw_input("Calificacion 1: ")
    calif2=raw_input("Calificacion 2: ")
    calif3=raw_input("Calificacion 3: ")
    calif4=raw_input("Calificacion 4: ")
    calif5=raw_input("Calificacion 5: ")
    registro=alumno+","+matricula+","+calif1+","+calif2+","+calif3+","+calif4+","+calif5+"\n"
    print registro
    archivo.write(registro)
    print "El alumno ",alumno," se ha agregado a la lista"
    archivo.close()
    menu()

def bajas():
    borrado=0
    archivo=open('calificaciones.txt','r')
    lineas=archivo.readlines()
    archivo.close()
    consul=raw_input("Ingrese el alumno a eliminar de la base de datos")
    for linea in lineas:
        if consul in linea:
            lineas_index=lineas.index(linea)
            borrado=1    
    if borrado==0:
        print "No se ha encontrado ningún registro con ese nombre"
    if borrado==1:         
        archivo=open('calificaciones.txt','w')
        for linea in lineas:
          if lineas.index(linea)!= lineas_index:
            archivo.write(linea)
        archivo.close()    
        print "El alumno ", consul, " ha sido removido"
        borrado=0
    menu()

def clasificar():
    archivo=open('calificaciones.txt','r')
    lineas=archivo.readlines()
    archivo.close()
    
    
    cont=0
    for elemento in lineas:
        campos=elemento.split(",")
        promedio=((float(campos[2])+float(campos[3])+float(campos[4])+float(campos[5])+float(campos[6]))/5)
        if promedio>9:
            print promedio
            temp1=campos[0]+','+campos[1]+"\n"
            archivo=open('becados.txt','a')
            archivo.write(str(temp1))
            archivo.close()
        else:
            print promedio
            temp2=campos[0]+','+campos[1]+"\n"
            archivo1=open('no_becados.txt','a')
            archivo1.write(str(temp2))
            archivo1.close()
   
    
    
    print "Alumnos Clasificados"   
    menu()            
        

def consultas():
    print "Calificaciones"
    elec=raw_input("¿Cuales quieres ver? 1.-Becados 2.- No becados")
    if elec=='1':
        archivo=open('becados.txt','r')
        lineas=archivo.readlines()
        archivo.close()
        for linea in lineas:
            print linea
    if elec=='2':
        archivo=open('no_becados.txt','r')
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
    opcion=input("Elije la accion a realizar: \n1. Agregar alumno \n2. Clasificar Becados \n3.Consultar alumnos \n4.Modificar alumno \n5.-Borrar alumnos \n") 
    if opcion==1:
        altas()
    elif opcion==2:
        clasificar()
    elif opcion ==3:
        consultas()
    elif opcion==4:
        modificar()
    elif opcion==5:
        borrar()
    else:
        error()
menu()    
