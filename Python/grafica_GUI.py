from tkinter import filedialog
from tkinter import *
from tkinter import ttk
import os
import grafica_procesamiento

window0=Tk()
window0.title("GRAFICADOR")
window0.geometry("700x600")


def openfile():
    number=0
    cwd=os.getcwd()
    file_name=filedialog.askopenfilename(initialdir=cwd,title="Seleccione archivo",filetypes= (("archivo de texto","*.txt"),("CSV","*.csv"),("Todos los archivos","*.*")))
    while(True):
        try:
            tree.insert('','end',iid=number,text=str(number),value=(file_name,"0"))
            break
        except TclError:
            number=number+1
           
def process():
    i=0
    files_name=[]
    while(True):
        files_name.append(tree.item(i)['values'][0])
        if tree.next(i):
            i+=1
        else:
            break
    grafica_procesamiento.graphics(files_name,separator_entry.get(),number_separator_entry.get(),organization_entry.get(),name_entry.get(),x_entry.get(),y_entry.get(),samples_entry.get(),box.get())
    print(box.get())
def delete():
    tree.delete(deleter_entry.get()) 


var= IntVar()
#Objects
tree=ttk.Treeview(window0,columns=("File"))

separator_label=Label(window0,text="Separador de datos")
separator_entry=Entry(window0,width=10)

number_separator_label=Label(window0,text="Separador de numero")
number_separator_entry=Entry(window0,width=10)

organization_label=Label(window0,text="Organizacion")
organization_entry=Entry(window0)

name_label=Label(window0,text="Nombre de la grafica")
name_entry=Entry(window0)

x_label=Label(window0,text="Titulo eje X")
x_entry=Entry(window0)

y_label=Label(window0,text="Titulo eje Y")
y_entry=Entry(window0)

box=Spinbox(window0,values=("lineal","logaritmico"))
samples_label=Label(window0,text="Cantidad muestras")
samples_entry=Entry(window0)

deleter_entry=Entry(window0)

Button(text="Abrir archivo",command=openfile).place(x=10,y=420)
Button(text="Procesar",command=process).place(x=150,y=420)
Button(text="Borrar",command=delete).place(x=150,y=500)


tree.heading('#0',text="ID")
tree.heading('#1',text="File")
tree.column('#0', stretch=NO)
tree.column('#1', stretch=NO,width=400)


organization_label.place(x=300,y=400)
organization_entry.place(x=300,y=420)
"""La entrada de organizacion especifíca cual va a ser al disposicion de las graficas, esto se logra
    escribiendo "," para las graficas que van a estar en una misma figura y ";" para separar las graficas
    por columnas. Ejemplo: 1,2,3;4,5,6 -> para este caso las primeras tres graficas estarán en una misma figura
    y las siguientes tres en otra figura"""

name_label.place(x=450,y=400)
name_entry.place(x=450,y=420)

samples_label.place(x=450, y=500)
samples_entry.place(x=450, y=520)

separator_label.place(x=10,y=300)
separator_entry.place(x=10,y=320)

number_separator_label.place(x=150,y=300)
number_separator_entry.place(x=150,y=320)

x_label.place(x=300,y=300)
x_entry.place(x=300,y=320)

y_label.place(x=400,y=300)
y_entry.place(x=400,y=320)

deleter_entry.place(x=50,y=500)

box.place(x=200, y=500)
tree.grid(row=1, columnspan=3, sticky='nsew')

window0.mainloop()