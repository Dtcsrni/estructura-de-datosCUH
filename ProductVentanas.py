from Tkinter import *

temp=0
opcion=""
campos=[]
def altas():
    temp=1
    global ventana
    ventana.destroy()
    ventana=Tk()
    ventana.geometry("800x600+100+100")
    ventana.title("Altas")
    archivo=open('productos.txt','a')
    lblAlta=Label(text="Nombre de producto:").place(x=10,y=10)
    lblAlta1=Label(text="Presentacion:").place(x=10,y=30)
    lblAlta2=Label(text="Costo:").place(x=10,y=50)
    lblAlta3=Label(text="Proveedor:").place(x=10,y=70)
    lblAlta4=Label(text="Existencia:").place(x=10,y=90)
    nombre=StringVar()
    presentacion=StringVar()
    costo=StringVar()
    proveedor=StringVar()
    existencia=StringVar()
   
    txtNombre=Entry(ventana,textvariable=nombre).place(x=130,y=10)
    txtPresent=Entry(ventana,textvariable=presentacion).place(x=130,y=30)
    txtCosto=Entry(ventana,textvariable=costo).place(x=130,y=50)
    txtProvee=Entry(ventana,textvariable=proveedor).place(x=130,y=70)
    txtExist=Entry(ventana,textvariable=existencia).place(x=130,y=90)
    
    def registrar():
        
        registro=nombre.get()+","+presentacion.get()+","+costo.get()+","+proveedor.get()+","+existencia.get()+"\n"
        print registro
        archivo.write(registro)
        lblProducto=Label(text="El producto "+registro+" ha sido agregado a la base de datos").place(x=300,y=80);
        archivo.close()
    def cerrar():
        ventana.destroy()
        menu()
    boton5= Button(ventana, text="Registrar", width=10, command=registrar).place(x=220,y=350)

    boton4= Button(ventana, text="Regresar", width=10, command=cerrar).place(x=400,y=380)

    
    ventana.mainloop()
def consultas():
    global ventana
    ventana.destroy()
    ventana=Tk()
    ventana.geometry("800x600+100+100")
    ventana.title("Altas")
    archivo=open('productos.txt','r')
    lineas=archivo.readlines()
    archivo.close()
    
    lblProd=Label(text="Producto a buscar:").place(x=10,y=10)
    entrada1=StringVar()
    txtProd=Entry(ventana,textvariable=entrada1).place(x=150,y=10)
    def consul():
        encontrado=0
        for elemento in lineas:
            if entrada1.get() in elemento:
                campos=elemento.split(",")
                lblConsulta=Label(text="Producto: "+campos[0]+"\n Presentacion: "+campos[1]+"\n Existencias: "+campos[2]+"\n Proveedor: "+campos[3]+"\n Existencias: "+campos[4],width=50).place(x=50,y=100)
                encontrado=1
        if encontrado==0:
           lblConsulta=Label(text="No existe tal producto",width=50).place(x=20,y=150)
        else:
            encontrado=0
    def cerrar():
        ventana.destroy()
        menu()   
    boton1= Button(ventana, text="Consultar", width=10, command=consul).place(x=90,y=280)
    boton4= Button(ventana, text="Regresar", width=10, command=cerrar).place(x=400,y=380)

 
def ventas():
    global ventana
    ventana.destroy()
    ventana=Tk()
    ventana.geometry("800x600+100+100")
    ventana.title("Ventas")
    archivo=open('productos.txt','r')
    lineas=archivo.readlines()
    archivo.close()
    campos=[]
    index=0
    global precio
    global nproducto
    lblProd=Label(text="Producto a vender:").place(x=10,y=10)
    prodvent=StringVar()
    txtProd=Entry(ventana,textvariable=prodvent).place(x=150,y=10)
    def cerrar():
        ventana.destroy()
        menu()
    productoventa=StringVar()     
    def vender():
        global index
        archivo=open('productos.txt','r')
        lineas=archivo.readlines()
        archivo.close()
        total=float(productoventa.get())*float(precio)
        vtotal=int(existencias)-int(productoventa.get())
        formato=str(nproducto)+","+str(presentacion)+","+str(precio)+","+str(proveedor)+","+str(vtotal)+"\n"
        lineas[index]=formato
        archivo1=open('productos.txt','w')
        for linea in lineas:
            archivo1.write(linea)
        archivo1.close()
        lblventa=Label(text="Se han vendido "+str(productoventa.get())+" piezas de "+str(nproducto)+". \n Total: "+str(total)+" pesos").place(x=600,y=200)         
   
    def consula():
        encontrado=0
        for elemento in lineas:
            if prodvent.get() in elemento:
                campos=elemento.split(",")
                encontrado=1
                global precio
                global nproducto
                global presentacion
                global existencias
                global proveedor
                global index
                precio=campos[2]
                nproducto=campos[0]
                presentacion=campos[1]
                proveedor=campos[3]
                existencias=campos[4]
                for linea in lineas:
                    if prodvent.get() in linea:
                        index=elemento.index(linea) 
        if encontrado==0:
           lblChecar=Label(text="No existe tal producto",width=50).place(x=20,y=150)
        else:
            lblproducto=Label(text="Producto: "+campos[0]+"\n Presentacion: "+campos[1]+"\n Costo: "+campos[2]+"\n Proveedor: "+campos[3]+"\n Existencias: "+campos[4],width=50).place(x=50,y=100)
            lblProd=Label(text="Cantidad a vender:").place(x=300,y=200)
            txtProd=Entry(ventana,textvariable=productoventa).place(x=450,y=200)
            boton19= Button(ventana, text="Vender", width=10, command=vender).place(x=500,y=300)
            
            encontrado=0
      
    boton11= Button(ventana, text="Revisar", width=10, command=consula).place(x=90,y=280)
    boton12= Button(ventana, text="Regresar", width=10, command=cerrar).place(x=400,y=380)

 
def menu():
    global ventana
    if(temp==1):
        ventana.destroy()
    ventana=Tk()
    ventana.geometry("800x600+100+100")
    ventana.title("Menu")
    lblProd=Label(text="Elija la opcion a realizar: ").place(x=10,y=10)
    boton1= Button(ventana, text="Altas", width=10, command=altas).place(x=50,y=100)
    boton1= Button(ventana, text="Consultas", width=10, command=consultas).place(x=50,y=140)
    boton1= Button(ventana, text="Ventas", width=10, command=ventas).place(x=50,y=180)
         

    
menu()    
ventana.mainloop()
