import sys

# Definir una lista para almacenar el inventario de productos
inventario = []

# Función para cargar el inventario desde un archivo
def cargar_inventario():
    try:
        with open('inventario.txt', 'r') as archivo:
            for linea in archivo:
                codigo, nombre, existencia, proveedor, precio = linea.strip().split(',')
                existencia = int(existencia)
                precio = float(precio) 
                producto = {'codigo': codigo, 'nombre': nombre, 'existencia': existencia, 'proveedor': proveedor, 'precio': precio}
                inventario.append(producto)
    except FileNotFoundError:
        print("El archivo de inventario no existe. Se creará uno nuevo.")

# Función para guardar el inventario en un archivo
def guardar_inventario():
    with open('inventario.txt', 'w') as archivo:
        for producto in inventario:
            archivo.write(f"{producto['codigo']},{producto['nombre']},{producto['existencia']},{producto['proveedor']},{producto['precio']}\n")

# Función para listar productos
def listar_productos():
    if not inventario:
        print("No hay productos en el inventario")
    else:
        print("Productos en el inventario:")
        for producto in inventario:
            print(f"Código: {producto['codigo']}, Nombre: {producto['nombre']}, Existencia: {producto['existencia']}, Proveedor: {producto['proveedor']}, Precio: {producto['precio']}")

# Función para agregar un nuevo producto al inventario
def agregar_producto(codigo, nombre, existencia, proveedor, precio):
    producto = {'codigo': codigo, 'nombre': nombre, 'existencia': existencia, 'proveedor': proveedor, 'precio': precio}
    inventario.append(producto)
    guardar_inventario()  # Guardar los cambios en el archivo
    print(f"El producto con código '{codigo}' ha sido añadido al inventario")

# Función para eliminar un producto del inventario
def eliminar_producto(codigo):
    for producto in inventario:
        if producto['codigo'] == codigo:
            inventario.remove(producto)
            guardar_inventario()  #aqui esta guardando 
            print(f"Producto con código '{codigo}' eliminado del inventario")
            return
    print(f"No se encontró ningún producto con el código '{codigo}' en el inventario")

# Función para actualizar el precio de un producto en el inventario
def actualizar_producto(codigo, nuevo_precio):
    for producto in inventario:
        if producto['codigo'] == codigo:
            producto['precio'] = nuevo_precio
            guardar_inventario()  #aqui guarda
            print(f"Precio del producto con código '{codigo}' actualizado a {nuevo_precio}")
            return
    print(f"No se encontró ningún producto con el código '{codigo}' en el inventario")

# Función para actualizar la existencia de un producto en el inventario
def actualizar_existencia(codigo, nueva_existencia):
    for producto in inventario:
        if producto['codigo'] == codigo:
            producto['existencia'] = nueva_existencia
            guardar_inventario()  
            print(f"Existencia del producto con código '{codigo}' actualizada a {nueva_existencia}")
            return
    print(f"No se encontró ningún producto con el código '{codigo}' en el inventario")

# Función para mostrar ayuda
def mostrar_ayuda():
    print("Comandos disponibles:")
    print("  listar: Muestra la lista de productos en el inventario.")
    print("  crear <codigo> <nombre> <existencia> <proveedor> <precio>: Agrega un nuevo producto al inventario.")
    print("  eliminar <codigo>: Elimina un producto del inventario.")
    print("  actualizar <codigo> <nuevo_precio>: Actualiza el precio de un producto en el inventario.")
    print("  existencia <codigo> <nueva_existencia>: Actualiza la existencia de un producto en el inventario.")
    print("  ayuda: Muestra esta lista de comandos disponibles.")

# Cargar el inventario al inicio del programa
cargar_inventario()

# Función principal para ejecutar comandos
def main():
    if len(sys.argv) < 2:
        print("Uso: python mi_script.py <comando> [argumentos]")
        return

    comando = sys.argv[1]

    if comando == 'listar':
        listar_productos()
    elif comando == 'crear':
        if len(sys.argv) != 7:
            print("Uso: python mi_script.py crear <codigo> <nombre> <existencia> <proveedor> <precio>")
        else:
            codigo = sys.argv[2]
            nombre = sys.argv[3]
            existencia = int(sys.argv[4])
            proveedor = sys.argv[5]
            precio = float(sys.argv[6])
            agregar_producto(codigo, nombre, existencia, proveedor, precio)
    elif comando == 'eliminar':
        if len(sys.argv) != 3:
            print("Uso: python mi_script.py eliminar <codigo>")
        else:
            codigo = sys.argv[2]
            eliminar_producto(codigo)
    elif comando == 'actualizar':
        if len(sys.argv) != 4:
            print("Uso: python mi_script.py actualizar <codigo> <nuevo_precio>")
        else:
            codigo = sys.argv[2]
            nuevo_precio = float(sys.argv[3])
            actualizar_producto(codigo, nuevo_precio)
    elif comando == 'existencia':
        if len(sys.argv) != 4:
            print("Uso: python mi_script.py existencia <codigo> <nueva_existencia>")
        else:
            codigo = sys.argv[2]
            nueva_existencia = int(sys.argv[3])
            actualizar_existencia(codigo, nueva_existencia)
    elif comando == 'ayuda':
        mostrar_ayuda()
    else:
        print("Comando no válido. Usa 'listar', 'crear', 'eliminar', 'actualizar', 'existencia' o 'ayuda'")

if __name__ == "__main__":
    main()