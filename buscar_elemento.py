alumnos=["Marco","Antonio","Alonso","Luis"]

def altas():
    nuevo=raw_input("Ingresar nombre de alumno: ")
    alumnos.append(nuevo)
    
decide='s'
print alumnos
while decide=="s" or decide=="s":
    altas()
    decide=raw_input("Deseas dar de alta otro alumno? S/N")
anexar=raw_input("Ingresa el nuevo nombre a anexar en la lista: ")
posicion=input("Ingresa la posicion del nuevo alumno en la lista: ")
#el metodo insert nos sirve para agregar elementos dentro de una lista en el orden que eljamos
alumnos.insert(posicion,anexar)

print alumnos

buscar=raw_input("Ingresa el nombre a buscar en la lista ")

if buscar in alumnos:
    posicion=alumnos.index(buscar)
    print "El alumno ",buscar,"se encuentra en la lista en la posicion", posicion
else:
       print("El alumno ", buscar,"NO se encuentra en lista")
