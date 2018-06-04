PRODUCTOS=[0,1,2,3,4]
PRECIOS=[0,1,2,3,4]
contador=0
print("Bienvenido")
for product in PRODUCTOS:
    producto=raw_input("Ingrese el nombre de el producto "+str(contador+1)+" ")
    precio=raw_input("Ingrese el precio del producto "+str((contador+1))+" ")
    PRODUCTOS[contador] = producto
    PRECIOS[contador]= precio
    contador=contador+1
contador=0    
for product in PRODUCTOS:
    print("Producto ",str((contador+1)),": ",PRODUCTOS[contador]," su precio es $",str(PRECIOS[contador])," ")
    contador=contador+1
