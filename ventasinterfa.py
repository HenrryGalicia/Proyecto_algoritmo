import tkinter as tk

def cargar_inventario():
    # Cargar datos de inventario desde el archivo "inventario.txt"
    inventario = {}
    try:
        with open('inventario.txt', 'r') as archivo:
            for linea in archivo:
                codigo, nombre, existencia, proveedor, precio = linea.strip().split(',')
                inventario[codigo] = {'nombre': nombre, 'existencia': int(existencia), 'proveedor': proveedor, 'precio': float(precio)}
        return inventario
    except FileNotFoundError:
        print("El archivo de inventario no existe.")
        return {}

def cargar_clientes():
    # Cargar datos de clientes desde el archivo "clientes.txt"
    clientes = {}
    try:
        with open('clientes.txt', 'r') as archivo:
            for linea in archivo:
                codigo, nombre, otros_datos = linea.strip().split(',')
                clientes[codigo] = {'nombre': nombre, 'otros_datos': otros_datos}
        return clientes
    except FileNotFoundError:
        print("El archivo de clientes no existe.")
        return {}

def crear_venta():
    codigo_producto = codigop1.get()
    codigo_cliente = codigoc1.get()

    if codigo_producto in inventario and codigo_cliente in clientes:
        try:
            cantidad_productos = int(existencia1.get())
            total_venta = float(total1.get())
        except ValueError:
            resultado_label.config(text="La cantidad de productos y el total de la venta deben ser números válidos.")
            return

        venta = f"{codigo_producto},{codigo_cliente},{cantidad_productos},{total_venta}\n"
        with open('ventas.txt', 'a') as archivo_ventas:
            archivo_ventas.write(venta)

        resultado_label.config(text="Venta creada exitosamente y registrada en ventas.txt.")
    else:
        resultado_label.config(text="El producto o el cliente no existen.")

    codigoc1.delete(0, "end")
    codigop1.delete(0,"end")
    existencia1.delete(0,"end")
    total1.delete(0,"end")
    
def eliminar_venta():
    codigo_eliminar = codigop1.get()
    
    # Leer el contenido del archivo
    with open("ventas.txt", "r") as archivo:
        lineas = archivo.readlines()
    
    # Crear una nueva lista de líneas excluyendo las que comienzan con el código a eliminar
    nueva_lista = [linea for linea in lineas if not linea.startswith(codigo_eliminar + ",")]
    
    # Escribir la nueva lista de líneas de vuelta al archivo
    with open("ventas.txt", "w") as archivo:
        archivo.writelines(nueva_lista)
    
    # Borrar el código del cliente del widget de entrada
    codigop1.delete(0, "end")   

def listar():
    datos.delete(1.0, "end")
    with open("ventas.txt", "r") as archivo:
        contenido = archivo.read()
        datos.insert("1.0", contenido)

def cerrar_aplicacion():
    ventana.destroy()   

ventana = tk.Tk()
ventana.title("Ventas")
ventana.geometry('900x500')
ventana.config(bg='#262727')
ventana.iconbitmap(r'C:\Users\al881\OneDrive\Escritorio\Proyecto algoritmos\interfaz\inicios.ico')

Ventas = tk.Label(ventana, text="Ventas",width=40,font=("Helvetica", 20, "bold"),bg="#2f3136", fg="white", borderwidth=2)
Ventas.pack()

izquierda = tk.Frame(ventana,bg='#262727')
izquierda.pack(side="left")

codigop = tk.Label(izquierda, text="Escribir Codigo del producto",width=25,font=("Helvetica", 10, "bold"),bg="#101111", fg="white", borderwidth=2)
codigop.pack(padx=10, pady=10, anchor="w")
codigop1 = tk.Entry(izquierda, width=40,font=("Helvetica", 10, "bold"),bg="#37393f", fg="white", borderwidth=2)
codigop1.pack(padx=10, pady=10, anchor="w")

codigoc = tk.Label(izquierda, text="Escribir Codigo del Cliente",width=25,font=("Helvetica", 10, "bold"),bg="#101111", fg="white", borderwidth=2)
codigoc.pack(padx=10, pady=10, anchor="w")
codigoc1 = tk.Entry(izquierda, width=40,font=("Helvetica", 10, "bold"),bg="#37393f", fg="white", borderwidth=2)
codigoc1.pack(padx=10, pady=10, anchor="w")

existencia = tk.Label(izquierda, text="Escribir Existencia que quiere adquirir",width=35,font=("Helvetica", 10, "bold"),bg="#101111", fg="white", borderwidth=2)
existencia.pack(padx=10, pady=10, anchor="w")
existencia1 = tk.Entry(izquierda, width=40,font=("Helvetica", 10, "bold"),bg="#37393f", fg="white", borderwidth=2)
existencia1.pack(padx=10, pady=10, anchor="w")

total = tk.Label(izquierda, text="Escribir el total de ventas",width=25,font=("Helvetica", 10, "bold"),bg="#101111", fg="white", borderwidth=2)
total.pack(padx=10, pady=10, anchor="w")
total1 = tk.Entry(izquierda, width=40,font=("Helvetica", 10, "bold"),bg="#37393f", fg="white", borderwidth=2)
total1.pack(padx=10, pady=10, anchor="w")

resultado_label = tk.Label(izquierda, text="",font=("Helvetica", 10, "bold"),bg="#37393f", fg="white", borderwidth=2)
resultado_label.pack(padx=10, pady=10,anchor="w")

boton_crear = tk.Button(izquierda, text="Crear Venta", command=crear_venta ,bg="#8c14dc",fg="white")
boton_crear.pack(side="left",padx=10, pady=10,anchor="w")
boton_borrar = tk.Button(izquierda, text="Eliminar venta", command=eliminar_venta,bg="#8c14dc",fg="white")  # Puedes agregar la función para eliminar ventas aquí
boton_borrar.pack(side="left",padx=10, pady=10,anchor="w")

derecha = tk.Frame(ventana,bg='#262727')
derecha.pack(side="right")

presentacion = tk.Label(derecha, text="CodidoPro./CodidoClie./Existencia/Total",font=("Helvetica", 10, "bold"),bg="#a014f0", fg="white" )
presentacion.pack(padx=10, pady=10)

datos = tk.Text(derecha, width=60, height=10, wrap=tk.WORD,font=("Helvetica", 15, "bold"),bg="#37393f", fg="white")
datos.pack(padx=10, pady=10,anchor="e")

boton_listar = tk.Button(derecha, text="Listar clientes", command=listar,bg="#8c14dc",fg="white")
boton_listar.pack(side="left",padx=10, pady=10,anchor="w")

boton_salir = tk.Button(derecha, text="Salir", command=cerrar_aplicacion,bg="#8c14dc",fg="white")
boton_salir.pack(side="left",padx=10, pady=10,anchor="w")



ventas = []
inventario = cargar_inventario()
clientes = cargar_clientes()

ventana.mainloop()
