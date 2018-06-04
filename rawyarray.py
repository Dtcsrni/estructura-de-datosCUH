alumnos =[]
nombre=raw_input("Ingresa un nombre a la lista")
alumnos.append(nombre)
decide=raw_input("Deseas dar de alta otro nombre en la lista? s/n")

while decide == "S" or decide == "s":
    nombre=raw_input("Ingresa un nombre a la lista")
    alumnos.append(nombre)
    decide=raw_input("Deseas dar de alta otro nombre en la lista? s/n")

#for elemento in alumnos:
#    print elemento


buscar = raw_input("Ingresa el nombre a buscar en la lista: ")

if buscar in alumnos:
    print "El alumno",buscar,"si esta en la lista"
else:
    print "El alumno",buscar,"no esta en la lista"
