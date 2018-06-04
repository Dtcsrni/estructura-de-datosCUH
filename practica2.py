print("Bienvenido al sistema de servicio militar")
sex=input("Ingrese sexo: 1:Hombre 2: Mujer")
edad=input("Ingrese edad")
salud=input("¿Su estado de salud es 1.-Bueno 2.- Malo")
if (sex==1 and edad>18 and salud==1):
    print("Es obligatorio el servicio militar")
if (sex==2 and edad>18 and salud==1):
    print("Es opcional el servicio militar")
if (sex==2 and edad<18):
    print("Muy joven para el servicio militar")
if (sex==1 and edad<18):
    print("Es muy joven para el servicio militar")
if (salud==2):
    print("Por su salud no puede hacer el servicio militar")
