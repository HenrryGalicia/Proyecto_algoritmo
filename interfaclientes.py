import subprocess
import tkinter as tk

def crear_clientes():
    codigo_valor = codigo1.get()
    nombre_valor = nombre1.get()
    direcion_valor = direccion1.get()
    
    informacio = f"{codigo_valor},{nombre_valor},{direcion_valor}"
    
    with open("clientes.txt", "a") as archivo:
        archivo.write(informacio + "\n")

def listar():
    datos.delete(1.0, "end")
    with open("clientes.txt", "r") as archivo:
        contenido = archivo.read()
        datos.insert("1.0", contenido)
        
    codigo1.delete(0, "end")
    nombre1.delete(0, "end")  
    direccion1.delete(0, "end") 
    
def eliminar_clientes():
    codigo_eliminar = codigo1.get()
    
    # Leer el contenido del archivo
    with open("clientes.txt", "r") as archivo:
        lineas = archivo.readlines()
    
    # Crear una nueva lista de líneas excluyendo las que comienzan con el código a eliminar
    nueva_lista = [linea for linea in lineas if not linea.startswith(codigo_eliminar + ",")]
    
    # Escribir la nueva lista de líneas de vuelta al archivo
    with open("clientes.txt", "w") as archivo:
        archivo.writelines(nueva_lista)
    
    # Borrar el código del cliente del widget de entrada
    codigo1.delete(0, "end")
    
def actualizar():
    codigo_modificar2 = codigo1.get()
    nuevo_nombre = nombre1.get()
    nueva_direccion = direccion1.get()
    
    with open("clientes.txt", "r") as archivo:
        lineas = archivo.readlines()

    encontar = False    
    
    nueva_lista = []
    for linea in lineas:
        if linea.startswith(codigo_modificar2 + ','):
            encontar = True
            elementos = linea.strip().split(',')
            elementos[1] = nuevo_nombre
            elementos[2] = nueva_direccion
            nueva_linea = ','.join(elementos)
            nueva_lista.append(nueva_linea+'\n')
        else:
            nueva_lista.append(linea)
            
            if not encontar:
                result.config(text="Cliente no encontrado")
                
            with open("clientes.txt", "w") as archivo:
                archivo.writelines(nueva_lista)

def cerrar_aplicacion():
    ventana.destroy()
    # Limpiar los campos de entrada después de modificar
    codigo1.delete(0, "end")
    nombre1.delete(0, "end")
    direccion1.delete(0, "end")        

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Clientes")
ventana.geometry('900x500')
ventana.config(bg='#262727')
ventana.iconbitmap(r'C:\Users\al881\OneDrive\Escritorio\Proyecto algoritmos\interfaz\inicios.ico')

Cliente = tk.Label(ventana, text="Clientes",width=40,font=("Helvetica", 20, "bold"),bg="#2f3136", fg="white", borderwidth=2)
Cliente.pack()

izquierda = tk.Frame(ventana,bg='#262727')
izquierda.pack(side="left")

codigo = tk.Label(izquierda, text="Escriba el Codigo del cliente",width=25,font=("Helvetica", 10, "bold"),bg="#101111", fg="white", borderwidth=2)
codigo.pack(padx=10, pady=10, anchor="w")
codigo1 = tk.Entry(izquierda, width=40,font=("Helvetica", 10, "bold"),bg="#37393f", fg="white", borderwidth=2)
codigo1.pack(padx=10, pady=10, anchor="w")
result = tk.Label(izquierda, text="",font=("Helvetica", 10, "bold"),bg="#37393f", fg="white", borderwidth=2)
result.pack(padx=10, pady=10, anchor="w")

nombre = tk.Label(izquierda, text="Escriba su nombre",width=15,font=("Helvetica", 10, "bold"),bg="#101111", fg="white", borderwidth=2)
nombre.pack(padx=10, pady=10, anchor="w")
nombre1 = tk.Entry(izquierda, width=40,font=("Helvetica", 10, "bold"),bg="#37393f", fg="white", borderwidth=2)
nombre1.pack(padx=10, pady=10, anchor="w")

direccion = tk.Label(izquierda, text="Escriba su dirección",width=15,font=("Helvetica", 10, "bold"),bg="#101111", fg="white", borderwidth=2)
direccion.pack(padx=10, pady=10, anchor="w")
direccion1 = tk.Entry(izquierda, width=40,font=("Helvetica", 10, "bold"),bg="#37393f", fg="white", borderwidth=2)
direccion1.pack(padx=10, pady=10, anchor="w")

boton_crear = tk.Button(izquierda, text="Crear Cliente", command=crear_clientes,bg="#8c14dc", fg="white")
boton_crear.pack(side="left",padx=10, pady=10,anchor="w")
boton_eliminar = tk.Button(izquierda, text="Eliminar cliente", command=eliminar_clientes,bg="#8c14dc", fg="white")
boton_eliminar.pack(side="left",padx=10, pady=10,anchor="w")
boton_actualizar = tk.Button(izquierda, text="Actualizar cliente", command=actualizar,bg="#8c14dc", fg="white")
boton_actualizar.pack(side="left",padx=10, pady=10,anchor="w")


derecha = tk.Frame(ventana,bg='#262727')
derecha.pack(side="right")

presentacion = tk.Label(derecha, text="Codido/Nombre/Direccion",font=("Helvetica", 10, "bold"),bg="#a014f0", fg="white" )
presentacion.pack(padx=10, pady=10)

datos = tk.Text(derecha, width=60, height=20, wrap=tk.WORD,font=("Helvetica", 10, "bold"),bg="#37393f", fg="white")
datos.pack(padx=10, pady=10, anchor="e")

boton_listar = tk.Button(derecha, text="Listar clientes", command=listar,bg="#8c14dc", fg="white")
boton_listar.pack(side="left",padx=10, pady=10,anchor="w")

boton_salir = tk.Button(derecha, text="Salir", command=cerrar_aplicacion,bg="#8c14dc", fg="white")
boton_salir.pack(side="left",padx=10, pady=10,anchor="w")

ventana.mainloop()