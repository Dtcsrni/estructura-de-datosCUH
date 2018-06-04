TNOCTURNO=[0,1,2,3]
TDIURNO=[0,1,2,3]
contador=0
print("Turno Nocturno")
for empleados in TNOCTURNO:
    salario=raw_input("Ingrese el salario del trabajador "+str(contador+1)+" ")
    TNOCTURNO[contador]=salario
    contador=contador+1
contador=0    
print("Turno Diurno")
for empleado in TDIURNO:
    salario=raw_input("Ingrese el salario del trabajador "+str(contador+1)+" ")
    TDIURNO[contador]=salario
    contador=contador+1
promedio=(float(TNOCTURNO[0])+float(TNOCTURNO[1])+float(TNOCTURNO[2])+float(TNOCTURNO[3]))/4
print("El sueldo promedio del Turno Nocturno es "+str(promedio)+" pesos")
promedio1=(float(TDIURNO[0])+float(TDIURNO[1])+float(TDIURNO[2])+float(TDIURNO[3]))/4
print("El sueldo promedio del Turno Diurno es "+str(promedio1)+" pesos")

if(promedio<promedio1):
    print("El Turno Diurno es el mejor pagado")
if(promedio1<promedio):
    print("El turno Nocturno es el mejor pagado")
if(promedio1==promedio):
    print("Ambos turnos ganan lo mismo")

    
