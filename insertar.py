alumnos=["Marco","Antonio","Alonso","Luis"]

def altas():
    nuevo=raw_input("Ingresar nombre de alumno: ")
    alumnos.append(nuevo)
    
decide='s'

while decide=="s" or decide=="s":
    altas()
    decide=raw_input("Deseas dar de alta otro alumno? S/N")
anexar=raw_input("Ingresa el nuevo nombre a anexar en la lista: ")
posicion=input("Ingresa la posicion del nuevo alumno en la lista: ")

alumnos.insert(posicion,anexar)

print alumnos
