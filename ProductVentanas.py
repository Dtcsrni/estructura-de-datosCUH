#Punto de Venta en Ventanas
#Por Erick Renato Vega Cer�n
#29/Junio/2018



from Tkinter import *

temp=0
opcion=""
campos=[]
global index
negocio= "Erick Vega"


def menu():
    global ventana
    if(temp==1):
        ventana.destroy()
    ventana=Tk()
    ventana.geometry("400x300+100+100")
    ventana.title("Punto de Venta")
    ventana.configure(background='gray18')
    lblInicio=Label(text="||||||Bienvenido||||||", fg="darkgreen").place(x=140,y=20)
    lblInicio4=Label(text="Punto de Venta de "+negocio+"",fg="darkgreen").place(x=115,y=40)
    blInicio2=Label(text="V 2.0", fg="darkgreen", bg="gray18").place(x=170,y=270)
    lblInicio3=Label(text="Elija la opcion a realizar: ").place(x=130,y=100)
    boton1= Button(ventana, text="+ |Altas| +", width=10, command=altas).place(x=150,y=130)
    boton1= Button(ventana, text="° |Consultas| °", width=10, command=consultas).place(x=150,y=160)
    boton1= Button(ventana, text="$ |Ventas| $", width=10, command=ventas).place(x=150,y=190)
         
def altas():
    temp=1
    global ventana
    ventana.destroy()
    ventana=Tk()
    ventana.geometry("340x200+100+100")
    ventana.title("Altas")
    ventana.configure(background='gray18')
    
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
   
    txtNombre=Entry(ventana,textvariable=nombre).place(x=135,y=10)
    txtPresent=Entry(ventana,textvariable=presentacion).place(x=135,y=30)
    txtCosto=Entry(ventana,textvariable=costo).place(x=135,y=50)
    txtProvee=Entry(ventana,textvariable=proveedor).place(x=135,y=70)
    txtExist=Entry(ventana,textvariable=existencia).place(x=135,y=90)
    
    def registrar():
        archivo=open('productos.txt','a')
        registro=nombre.get()+","+presentacion.get()+","+costo.get()+","+proveedor.get()+","+existencia.get()+"\n"
        archivo.write(registro)
        lblProducto=Label(text="El producto "+nombre.get()+" ha sido agregado a la base de datos", width=50, heigh=9,fg="darkgreen", bg='gray18').place(x=0,y=0);
        archivo.close()
    def cerrar():
        ventana.destroy()
        menu()
    boton5= Button(ventana, text="Registrar", width=10, command=registrar).place(x=120,y=115)

    boton4= Button(ventana, text="< Regresar", width=10, command=cerrar).place(x=0,y=150)

    
    ventana.mainloop()
def consultas():
    global ventana
    global entrada1
    global resurt
    ventana.destroy()
    ventana=Tk()
    ventana.geometry("400x300+100+100")
    ventana.title("Consultas")
    ventana.configure(background='gray18')
    def archivoz(modo,productos):
        if modo==1:#modo escritura
            archivo1=open('productos.txt','w')
            for linea in productos:
                archivo1.write(linea)
            archivo1.close()
        if modo==2:#modo lectura
            archivo=open('productos.txt','r')
            productos=archivo.readlines()
            archivo.close()
            return productos
    def indexar(prod):
        conta=0
        productos=archivoz(2,0)
        for elemento in productos:
            element=elemento.split(",")
            if prod.get() not in element[0]:
                 conta=conta+1
            if prod.get() in element[0]:
                break;
            
        indexa=conta
        return indexa
    def resurtir():
        global resurt
        indexa=indexar(entrada1)
        productos=archivoz(2,0)
        for elemento in productos:
            element=elemento.split(",")
            if entrada1.get() == element[0]:
                campos=elemento.split(",")       
        vtotal=int(resurt.get())+int(campos[4])
        formato=str(campos[0])+","+str(campos[1])+","+str(campos[2])+","+str(campos[3])+","+str(vtotal)+"\n"
        productos[indexa]=formato#se iguala el formato a la posicion que corresponde al producto a vender
        archivoz(1,productos)
        lblConsulta=Label(text="Se ha resurtido con "+resurt.get()+" "+str(campos[1])+"", width=50, heigh=2,fg="darkgreen",bg='gray18').place(x=10,y=250)
        productos=archivoz(2,0)
        for elemento in productos:
            element=elemento.split(",")
            if entrada1.get() == element[0]:
                campos=elemento.split(",")
                lblConsulta=Label(text="Producto: "+campos[0]+"\n Presentacion: "+campos[1]+"\n Costo: "+campos[2]+"\n Proveedor: "+campos[3]+"\n Existencias: "+campos[4],width=50).place(x=0,y=150)
        
        boton1= Button(ventana, text="Consultar", width=10, state=DISABLED,command=consul).place(x=150,y=40)
    def consul():
        global resurt
        encontrado=0
        element=""
        for elemento in productos:
            element=elemento.split(",")
            if entrada1.get() == element[0]:
                campos=elemento.split(",")
                lblConsulta=Label(text="Producto: "+campos[0]+"\n Presentacion: "+campos[1]+"\n Costo: "+campos[2]+"\n Proveedor: "+campos[3]+"\n Existencias: "+campos[4],width=50).place(x=0,y=150)
                boton1150= Button(ventana, text="Borrar?", width=10, command=borrar, fg="darkred").place(x=20,y=215)
                lblProd=Label(text="Cantidad:").place(x=50,y=250)
                resurt=StringVar()
                txtresurt=Entry(ventana,textvariable=resurt).place(x=110,y=250)
                boton100= Button(ventana, text="Resurtir", width=10, command=resurtir, fg="darkgreen").place(x=240,y=250)
                
                encontrado=1
        if encontrado==0:
           lblConsulta=Label(text="No existe tal producto",width=65, heigh=10, fg="brown").place(x=0,y=120)
        else:
            encontrado=0
    def borrar():
        productos=archivoz(2,0)
        indexa=indexar(entrada1)
        archivo=open('productos.txt','w')
        for linea in productos:
             if entrada1.get() not in linea:
                archivo.write(linea)
        archivo.close()
        lblConsulta=Label(text="Producto borrado de la base de datos",width=60, heigh=8, fg="white", bg='gray18').place(x=10,y=150)
        
    def cerrar():
        ventana.destroy()
        menu()   
    boton1= Button(ventana, text="Consultar", width=10, command=consul).place(x=150,y=40)
    boton4= Button(ventana, text="< Regresar", width=10, command=cerrar).place(x=0,y=80)
    lblProd=Label(text="Producto a buscar:").place(x=10,y=10)
    entrada1=StringVar()
    txtProd=Entry(ventana,textvariable=entrada1).place(x=150,y=10)
    productos=archivoz(2,0)
 
def ventas():
    global ventana
    ventana.destroy()
    ventana=Tk()
    ventana.geometry("600x250+100+100")
    ventana.title("Ventas")
    ventana.configure(background='gray18')
    index=0
    global precio
    precio=0
    global nproducto
    nproducto=""
    global presentacion
    presentacion=""
    global existencias
    existencias=0
    global proveedor
    proveedor=""
    def consula():
        global precio
        global nproducto
        global presentacion
        global proveedor
        global existencias
        global index
        global boton19
        conta=0
        encontrado=0
        lblflecha=Label(text="   ", fg="darkgreen", bg='gray18').place(x=125,y=27)
        blventa=Label(text="                                                                                    ", fg="darkgreen",bg='gray18', width=40, heigh=5).place(x=280,y=160)
        lineasa = archivo(2,0)#abrir archivo en modo lectura para leer productos
        for elemento in lineasa:
            element=elemento.split(",")
            if prodvent.get() == element[0]:
                campos=elemento.split(",")
                encontrado=1
                precio=campos[2]
                nproducto=campos[0]
                presentacion=campos[1]
                proveedor=campos[3]
                existencias=campos[4]
            else:
                 conta=conta+1
        index=conta
        
        if (encontrado==0):#no se encontró el elemento indicado
           lblChecar=Label(text="No existe tal producto",width=40, heigh=10, fg="brown").place(x=280,y=0)
        else:#significa que si encontró el elemento indicado, por lo que lo muestra en la ventana
            lblproducto=Label(text="Producto: "+campos[0]+"\n Presentacion: "+campos[1]+"\n Costo: "+campos[2]+"\n Proveedor: "+campos[3]+"\n Existencias: "+campos[4],width=40).place(x=280,y=0)
            lblProd=Label(text="Cantidad a vender:").place(x=300,y=100)
            txtProd=Entry(ventana,textvariable=productoventa).place(x=410,y=100)#se pide la cantidad a vender
            boton19= Button(ventana, text="Vender", width=10, command=vender).place(x=370,y=125)
            encontrado=0
    def vender():
        global precio
        global nproducto
        global presentacion
        global proveedor
        global existencias
        global index
        campos=[]
        venta=0
        total=float(productoventa.get())*float(precio)
        if int(existencias)>=int(productoventa.get()) and int(productoventa.get())>0:
            vtotal=int(existencias)-int(productoventa.get())
            venta=1
        else:
            lblventa=Label(text=" No quedan suficientes piezas de "+str(nproducto)+"!", fg="darkred", width=40, heigh=5).place(x=280,y=160)
            boton19= Button(ventana, text="Vender", width=10, command=vender, state=DISABLED, background='gray').place(x=370,y=125)
            lblflecha=Label(text="<", fg="darkgreen").place(x=125,y=27)
        if (venta==1):
             formato=str(nproducto)+","+str(presentacion)+","+str(precio)+","+str(proveedor)+","+str(vtotal)+"\n"
             productos=archivo(2,0)#Se leen los productos existentes
             productos[index]=formato#se iguala el formato a la posicion que corresponde al producto a vender
             archivo(1,productos)
             lblventa=Label(text="Se han vendido "+str(productoventa.get())+" "+str(presentacion)+" de "+str(nproducto)+". \n Total: "+str(total)+" pesos", fg="darkgreen", width=40, heigh=5).place(x=280,y=160)
             lineasa = archivo(2,0)#abrir archivo en modo lectura para leer productos
             for elemento in lineasa:
                element=elemento.split(",")
                if str(nproducto)== element[0]:
                    campos=elemento.split(",")
             lblproducto=Label(text="Producto: "+campos[0]+"\n Presentacion: "+campos[1]+"\n Costo: "+campos[2]+"\n Proveedor: "+campos[3]+"\n Existencias: "+campos[4],width=40).place(x=280,y=0)
             boton19= Button(ventana, text="Vender", width=10, command=vender, state=DISABLED, background='gray').place(x=370,y=125)
             lblflecha=Label(text="<", fg="darkgreen").place(x=125,y=27)
    def cerrar():
        ventana.destroy()
        menu()  
    def archivo(modo,productos):
        if modo==1:#modo escritura
            archivo1=open('productos.txt','w')
            for linea in productos:
                archivo1.write(linea)
            archivo1.close()
        if modo==2:#modo lectura
            archivo=open('productos.txt','r')
            productos=archivo.readlines()
            archivo.close()
            return productos
   
    
    lblProd=Label(text="Producto a vender:").place(x=0,y=0)
    prodvent=StringVar()
    txtProd=Entry(ventana,textvariable=prodvent).place(x=150,y=0)
    boton11= Button(ventana, text="Revisar", width=10, command=consula).place(x=40,y=25)
    boton12= Button(ventana, text="< Regresar", width=10, command=cerrar).place(x=0,y=80)
    productoventa=StringVar()     

menu()    
ventana.mainloop()


