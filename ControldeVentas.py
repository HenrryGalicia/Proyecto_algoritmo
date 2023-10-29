ventas = []

# Función para cargar el inventario desde el archivo "inventario.txt"
def cargar_inventario():
    inventario = {}
    try:
        with open('inventario.txt', 'r') as archivo:
            for linea in archivo:
                codigo, nombre, existencia, proveedor, precio = linea.strip().split(',')
                inventario[codigo] = (nombre, int(existencia), float(precio))
        return inventario
    except FileNotFoundError:
        print("El archivo de inventario no existe.")
        return {}

# Función para cargar los datos de clientes desde el archivo "clientes.txt"
def cargar_clientes():
    clientes = {}
    try:
        with open('clientes.txt', 'r') as archivo:
            for linea in archivo:
                codigo, nombre, otros_datos = linea.strip().split(',')
                clientes[codigo] = (nombre, otros_datos)  # Puedes almacenar otros datos relevantes aquí
        return clientes
    except FileNotFoundError:
        print("El archivo de clientes no existe.")
        return {}

inventario = cargar_inventario()
clientes = cargar_clientes()

def crear_venta():
    codigo_producto = input("Ingrese el código del producto: ")
    codigo_cliente = input("Ingrese el código del cliente: ")

    # Verificar si el código del producto existe en el inventario
    if codigo_producto not in inventario:
        print(f"El código de producto '{codigo_producto}' no existe en el inventario.")
        return

    # Verificar si el código del cliente existe en la lista de clientes
    if codigo_cliente not in clientes:
        print(f"El código de cliente '{codigo_cliente}' no existe en la lista de clientes.")
        return

    cantidad_productos = int(input("Ingrese la cantidad de productos: "))
    total_venta = float(input("Ingrese el total de la venta: "))
    
    venta = {'codigo_producto': codigo_producto, 'codigo_cliente': codigo_cliente, 'cantidad_productos': cantidad_productos, 'total_venta': total_venta}
    ventas.append(venta)
    print("Venta creada exitosamente.")

    # Guardar los datos de la venta en el archivo "ventas.txt"
    with open('ventas.txt', 'a') as archivo_ventas:
        archivo_ventas.write(f"{codigo_producto},{codigo_cliente},{cantidad_productos},{total_venta}\n")


def listar_ventas():
    with open('ventas.txt', 'r') as archivo:
        lineas = archivo.readlines()
        
    if not lineas:
        print("No hay ventas registradas.")
    else:
        print("Listado de Ventas:")
        for linea in lineas:
            elementos = linea.strip().split(',')
            codigo_producto, codigo_cliente, cantidad_productos, total_venta = elementos
            print(f"Código de Producto: {codigo_producto}")
            print(f"Código del Cliente: {codigo_cliente}")
            print(f"Cantidad de Productos: {cantidad_productos}")
            print(f"Total de Venta: {total_venta}")
            print("------------------------------")


def anular_venta():
    codigo_producto = input("Ingrese el código del producto de la venta a anular: ")
    
    # Variable para rastrear si se encontró la venta
    venta_encontrada = False

    # Crear una lista para almacenar las ventas actualizadas
    ventas_actualizadas = []

    with open('ventas.txt', 'r') as archivo:
        for linea in archivo:
            elementos = linea.strip().split(',')
            if elementos[0] == codigo_producto:
                venta_encontrada = True
                print("Venta anulada.")
                
                # Devolver la cantidad de productos al inventario
                cantidad_productos = int(elementos[2])
                if codigo_producto in inventario:
                    inventario[codigo_producto] = (inventario[codigo_producto][0], inventario[codigo_producto][1] + cantidad_productos, inventario[codigo_producto][2])
                else:
                    print(f"ADVERTENCIA: El producto con código '{codigo_producto}' no está en el inventario, pero se ha anulado una venta.")
            else:
                ventas_actualizadas.append(linea)

    if venta_encontrada:
        with open('ventas.txt', 'w') as archivo:
            archivo.writelines(ventas_actualizadas)
    else:
        print(f"No se encontró ninguna venta con el código de producto '{codigo_producto}'.")

while True:
    print("\nMenú:")
    print("1. Crear Venta")
    print("2. Listar Ventas")
    print("3. Anular Venta")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        crear_venta()
    elif opcion == '2':
        listar_ventas()
    elif opcion == '3':
        anular_venta()
    elif opcion == '4':
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
