import subprocess
import tkinter as tk

#aqui van las def
def cerrar_aplicacion():
    ventana.destroy()

def guardar_informacion():
    # Obtener los valores ingresados en los campos de entrada
    codigo_valor = codigo.get()
    nombre_valor = nombre1.get()
    existencia_valor = existencia1.get()
    proveedor_valor = proveedor1.get()
    precio_valor = precio1.get()

    # Combinar los valores en una cadena separada por comas
    informacion = f"{codigo_valor},{nombre_valor},{existencia_valor},{proveedor_valor},{precio_valor}"

    # Guardar la información en el archivo "inventario.txt"
    with open("inventario.txt", "a") as archivo:
        archivo.write(informacion + "\n")

    # Limpiar los campos de entrada después de guardar
    codigo.delete(0, "end")
    nombre1.delete(0, "end")
    existencia1.delete(0, "end")
    proveedor1.delete(0, "end")
    precio1.delete(0, "end")
    
def eliminar_informacion():
    # Obtener el valor del código a eliminar
    codigo_a_eliminar = codigo.get()

    # Leer el contenido del archivo "inventario.txt" y almacenarlo en una lista
    with open("inventario.txt", "r") as archivo:
        lineas = archivo.readlines()

    # Crear una nueva lista que excluya todas las líneas con el código a eliminar
    nueva_lista = [linea for linea in lineas if not linea.startswith(codigo_a_eliminar + ',')]

    # Sobrescribir el archivo "inventario.txt" con la lista actualizada
    with open("inventario.txt", "w") as archivo:
        archivo.writelines(nueva_lista)

    # Limpiar el campo de entrada después de eliminar
    codigo_a_eliminar.delete(0, "end") 
 
def modificar_existencia():
    # Obtener el valor del código del producto a modificar
    codigo_a_modificar = codigo.get()
    nueva_existencia = existencia1.get()

    # Leer el contenido del archivo "inventario.txt" y almacenarlo en una lista
    with open("inventario.txt", "r") as archivo:
        lineas = archivo.readlines()

    encontrado = False

    # Crear una nueva lista que actualiza la existencia del producto
    nueva_lista = []
    for linea in lineas:
        if linea.startswith(codigo_a_modificar + ','):
            encontrado = True
            elementos = linea.strip().split(',')
            elementos[2] = nueva_existencia
            nueva_linea = ','.join(elementos)
            nueva_lista.append(nueva_linea + '\n')
        else:
            nueva_lista.append(linea)

    # Si el producto no se encuentra, mostrar un mensaje
    if not encontrado:
        resultado.config(text="Producto no encontrado")

    # Sobrescribir el archivo "inventario.txt" con la lista actualizada
    with open("inventario.txt", "w") as archivo:
        archivo.writelines(nueva_lista)

    # Limpiar los campos de entrada después de modificar
    codigo.delete(0, "end")
    existencia1.delete(0, "end")   
    
    
#aqui modifico el precio
def precio_nuevo():
    codigo_modificar2 = codigo.get()
    nuevo_precio = precio1.get()
    
    with open("inventario.txt", "r") as archivo:
        lineas = archivo.readlines()

    encontar = False    
    
    nueva_lista = []
    for linea in lineas:
        if linea.startswith(codigo_modificar2 + ','):
            encontar = True
            elementos = linea.strip().split(',')
            elementos[4] = nuevo_precio
            nueva_linea = ','.join(elementos)
            nueva_lista.append(nueva_linea+'\n')
        else:
            nueva_lista.append(linea)
            
            if not encontar:
                result.config(text="Producto no encontrado")
                
            with open("inventario.txt", "w") as archivo:
                archivo.writelines(nueva_lista)

    # Limpiar los campos de entrada después de modificar
    codigo.delete(0, "end")
    precio1.delete(0, "end")    
             
def mostrar_inventario():
    # Limpiar el widget de texto antes de mostrar el contenido
    text_widget.delete("1.0", "end")

    # Leer el contenido del archivo "inventario.txt" y mostrarlo en el widget de texto
    with open("inventario.txt", "r") as archivo:
        contenido = archivo.read()
        text_widget.insert("1.0", contenido)      
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Vista de inventario")
ventana.geometry('900x900')
ventana.config(bg='#262727')
ventana.iconbitmap(r'C:\Users\al881\OneDrive\Escritorio\Proyecto algoritmos\interfaz\inicios.ico')


#texto en la pagina
titulo = tk.Label(ventana, text="Inventario",width=40,font=("Helvetica", 20, "bold"),bg="#2f3136", fg="white", borderwidth=2)
titulo.pack(padx=10, pady=10)
#productos
izquierda = tk.Frame(ventana,bg='#262727')
izquierda.pack(side="left")

producto = tk.Label(izquierda, text="Producto",width=15,font=("Helvetica", 10, "bold"),bg="#101111", fg="white", borderwidth=2)
producto.pack(padx=10, pady=10,anchor="w" )

codigo1 = tk.Label(izquierda, text="Codigo",width=15,font=("Helvetica", 10, "bold"),bg="#101111", fg="white", borderwidth=2)
codigo1.pack(padx=10, pady=10,anchor="w")
codigo = tk.Entry(izquierda, width=15)
codigo.pack(padx=10, pady=10,anchor="w")

nombre = tk.Label(izquierda, text="nombre",width=15,font=("Helvetica", 10, "bold"),bg="#101111", fg="white", borderwidth=2)
nombre.pack(padx=10, pady=10,anchor="w")
nombre1 = tk.Entry(izquierda, width=15)
nombre1.pack(padx=10, pady=10,anchor="w")

existencia = tk.Label(izquierda,text="existencia",width=15,font=("Helvetica", 10, "bold"),bg="#101111", fg="white", borderwidth=2)
existencia.pack(padx=10, pady=10,anchor="w")
existencia1 = tk.Entry(izquierda,width=15)
existencia1.pack(padx=10, pady=10,anchor="w")
resultado = tk.Label(izquierda, text="",font=("Helvetica", 10, "bold"),bg="#37393f", fg="white", borderwidth=2)
resultado.pack(padx=10, pady=10,anchor="w")

proveedor = tk.Label(izquierda,text="Proveedor",width=15,font=("Helvetica", 10, "bold"),bg="#101111", fg="white", borderwidth=2)
proveedor.pack(padx=10, pady=10,anchor="w")
proveedor1 = tk.Entry(izquierda,width=15)
proveedor1.pack(padx=10, pady=10,anchor="w")

precio = tk.Label(izquierda,text="precio",width=15,font=("Helvetica", 10, "bold"),bg="#101111", fg="white", borderwidth=2)
precio.pack(padx=10, pady=10,anchor="w")
precio1 = tk.Entry(izquierda,width=15)
precio1.pack(padx=10, pady=10,anchor="w")
result = tk.Label(izquierda, text="",font=("Helvetica", 10, "bold"),bg="#37393f", fg="white", borderwidth=2)
result.pack(padx=10, pady=10,anchor="w")


boton_crear = tk.Button(izquierda, text="Crear", command=guardar_informacion,bg="#8c14dc", fg="white")
boton_crear.pack(side="left",padx=10, pady=10,anchor="w")

boton_eliminar = tk.Button(izquierda, text="Eliminar", command=eliminar_informacion,bg="#8c14dc", fg="white")
boton_eliminar.pack(side="left",padx=10, pady=10,anchor="w")

boton_actualizarex = tk.Button(izquierda, text="actualizar existencia",bg="#8c14dc", fg="white", command=modificar_existencia)
boton_actualizarex.pack(side="left",padx=10, pady=10,anchor="w")

boton_actualizarpre = tk.Button(izquierda, text="actualizar precio", command=precio_nuevo,bg="#8c14dc", fg="white")
boton_actualizarpre.pack(side="left",padx=10, pady=10,anchor="w")

boton_cerrar = tk.Button(izquierda, text="Cerrar", command=cerrar_aplicacion,bg="#8c14dc", fg="white")
boton_cerrar.pack(side="left",padx=10, pady=10,anchor="w")


listado = tk.Label(ventana, text="Listado",width=15,font=("Helvetica", 10, "bold"),bg="#101111", fg="white")
listado.pack(padx=10, pady=10)

presentacion = tk.Label(ventana, text="Codido/Nombre/Existencia/Proveedor/Precio",font=("Helvetica", 10, "bold"),bg="#a014f0", fg="white" )
presentacion.pack(padx=10, pady=10)

# texto del listado
text_widget = tk.Text(ventana,  width=60, height=25, wrap=tk.WORD,font=("Helvetica", 10, "bold"),bg="#37393f", fg="white")
text_widget.pack()

# Botón para listar
boton_cargar = tk.Button(ventana, text="Listar", command=mostrar_inventario,bg="#8c14dc", fg="white")
boton_cargar.pack(padx=10, pady=10, side="right")



ventana.mainloop()


































# Define el comando que deseas ejecutar en CMD
comando = "inventario.py"

# Abre una nueva instancia de CMD y ejecuta el comando
subprocess.Popen(["cmd.exe", "/k", comando])