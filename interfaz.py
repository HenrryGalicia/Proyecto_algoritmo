import tkinter as tk
from tkinter import messagebox

# Agrega esta parte al principio de tu código
def cargar_productos():
    try:
        with open('inventario.txt', 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 5:
                    codigo, nombre, existencia, proveedor, precio = parts
                    producto = Producto(codigo, nombre, int(existencia), proveedor, float(precio))
                    productos.append(producto)
    except FileNotFoundError:
        # Manejo de excepciones si el archivo no existe
        pass

cargar_productos()

class Producto:
    def __init__(self, codigo, nombre, existencia, proveedor, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.existencia = existencia
        self.proveedor = proveedor
        self.precio = precio

productos = []

def listar_productos():
    if not productos:
        messagebox.showinfo("Inventario", "No hay productos en el inventario.")
        return
    
    lista_productos = "Lista de productos:\n"
    for producto in productos:
        lista_productos += f"Código: {producto.codigo}, Nombre: {producto.nombre}, Existencia: {producto.existencia}, Proveedor: {producto.proveedor}, Precio: {producto.precio}\n"
    
    messagebox.showinfo("Inventario", lista_productos)

def crear_producto():
    codigo = entry_codigo.get()
    nombre = entry_nombre.get()
    existencia = int(entry_existencia.get())
    proveedor = entry_proveedor.get()
    precio = float(entry_precio.get())

    producto = Producto(codigo, nombre, existencia, proveedor, precio)
    productos.append(producto)

    messagebox.showinfo("Inventario", "Producto creado exitosamente.")

# Crear una ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Gestión de Inventario")

# Crear etiquetas y entradas para los datos del producto
tk.Label(ventana, text="Código:").grid(row=0, column=0)
entry_codigo = tk.Entry(ventana)
entry_codigo.grid(row=0, column=1)

tk.Label(ventana, text="Nombre:").grid(row=1, column=0)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=1, column=1)

tk.Label(ventana, text="Existencia:").grid(row=2, column=0)
entry_existencia = tk.Entry(ventana)
entry_existencia.grid(row=2, column=1)

tk.Label(ventana, text="Proveedor:").grid(row=3, column=0)
entry_proveedor = tk.Entry(ventana)
entry_proveedor.grid(row=3, column=1)

tk.Label(ventana, text="Precio:").grid(row=4, column=0)
entry_precio = tk.Entry(ventana)
entry_precio.grid(row=4, column=1)

# Crear botones para operaciones
tk.Button(ventana, text="Listar Productos", command=listar_productos).grid(row=5, column=0)
tk.Button(ventana, text="Crear Producto", command=crear_producto).grid(row=5, column=1)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
