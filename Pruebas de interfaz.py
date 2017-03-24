from tkinter import *
from  easygui import *


def Diccionario():
    personas = dict()
    personas = {
        205450650: "Freddy Gerardo Rocha Boza",
        305520852: "Roberto Perez Bolanos",
        308520963: "Roberto Alpizar Pique",
        508520963: "Jolanda Ramirez Perez",
        111150933: "Lorena Alvarez Perez",
        104745096: "Karla Robles Perez",
        701520485: "Xinia Maria Roblero Alpizar",
        952585: "Bryan Alpizar Jimenez",
        108520963: "Pedro Gomez Roblero",
    }

    BorrarLista()

    for k, v in personas.items():
        lstPersona.insert(END,str(k)+' '+v)



def Imagenes():
    vImagen = Tk()
    vImagen.geometry("500x500+10+10")
    # Titulo de la ventana
    vImagen.wm_title("Ejemplo de Carga de Imagenes")
    #imagenLoad = PhotoImage(file="C:\Python35\Proyects\Mustang.gif")
    #lblImagen = Label(vImagen, image=imagenLoad).place(x=10, y=10)
    vImagen.mainloop()

def Personas():
    vPersonas=Tk()
    vPersonas.geometry("500x500+100+100")
    vPersonas.wm_title("Mantenimiento de Personas")
    vPersonas.mainloop()

def Agregar():
    #lstPersona.insert(END,entrada.get())
    lstPersona.insert(END,cedula.get()+" "+nombre.get())

    msgbox(msg='Persona Agregada Correctamente a la lista',
           title='Mensajes de la Aplicacion',
           ok_button='Continua',
           image=None)

def BorrarLista():
    lstPersona.delete(0,10)

def Salir():
    vPrincipal.destroy()

#Creacion de la ventana Principal
vPrincipal =Tk()
vPrincipal.geometry("800x600+0+0")
#Titulo de la ventana
vPrincipal.wm_title("Ejemplo de Interfaz Grafica PYTHON")

#Diseño del Menu
barraMenu=Menu(vPrincipal)

#Creacion del detalle del menu
mnuArchivo=Menu(barraMenu)
mnuEdicion=Menu(barraMenu)

#Desglose de cada Menu con acciones en ellos
mnuArchivo.add_command(label="Registrar Personas",command=Personas)
mnuArchivo.add_separator()

mnuArchivo.add_command(label="Ejemplo Imagenes",command=Imagenes)
mnuArchivo.add_separator()

mnuArchivo.add_cascade(label="Salir del Sistema",command=Salir)
mnuArchivo.add_separator()

mnuEdicion.add_command(label="Modificar Personas",command=Personas)
mnuEdicion.add_separator()

#Agregar los detalles al Menu
barraMenu.add_cascade(label="Archivo",menu=mnuArchivo)
barraMenu.add_cascade(label="Edicion",menu=mnuEdicion)

#Carga de la menu a la ventana
vPrincipal.config(menu=barraMenu)

#Elementos
cedula = StringVar()
lblCedula = Label(vPrincipal, text='Cedula').place(x=70, y=30)
lblNombre = Label(vPrincipal, text='Nombre').place(x=70, y=50)
txtCedula = Entry(vPrincipal, textvariable=cedula, width=40).place(x=140, y=30)
nombre = StringVar()
txtNombre = Entry(vPrincipal, textvariable=nombre, width=40).place(x=140, y=50)


lblPersona = Label(vPrincipal, text="Listado de Personas").place(x=100, y=100)


lstPersona =Listbox(vPrincipal, width=100)

lstPersona.place(x=100, y=120)

lstPersona.insert(0, "Registros Insertado por Codigo")


btnAgregar = Button(vPrincipal, text="Agregar Persona", height=2,
                    width=15, command=Agregar).place(x=390, y=30)

btnBorrar = Button(vPrincipal, text="Borrar Lista", height=2,
                    width=15, command=BorrarLista).place(x=390, y=70)

btnCarga = Button(vPrincipal, text="Cargar Dic.", height=2,
                    width=15, command=Diccionario).place(x=550, y=30)


imagenLoad = PhotoImage(file="Mustang.gif")
lblImagen = Label(vPrincipal, image=imagenLoad).place(x=250, y=300)

vPrincipal.mainloop()

