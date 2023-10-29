def reporte_ventas_por_cliente():
    ventas_por_cliente = {}

    with open('ventas.txt', 'r') as archivo:
        lineas = archivo.readlines()

    for linea in lineas:
        elementos = linea.strip().split(',')
        codigo_cliente, _, _, total_venta = elementos

        if codigo_cliente not in ventas_por_cliente:
            ventas_por_cliente[codigo_cliente] = 0

        total_venta = float(total_venta)
        ventas_por_cliente[codigo_cliente] += total_venta

    if not ventas_por_cliente:
        print("No hay ventas registradas para ningún cliente.")
    else:
        with open('reportecliente.txt', 'w') as archivo_reporte:
            archivo_reporte.write("Reporte de Ventas por Cliente:\n")
            for codigo_cliente, total_ventas in ventas_por_cliente.items():
                archivo_reporte.write(f"Codigo de Producto: {codigo_cliente}\n")
                archivo_reporte.write(f"Ventas Totales: Q{total_ventas}\n")
                archivo_reporte.write("------------------------------\n")
        print("Informe de Ventas por Cliente guardado en 'reportecliente.txt'.")

def reporte_ventas_por_producto():
    ventas_por_producto = {}

    with open('ventas.txt', 'r') as archivo:
        lineas = archivo.readlines()

    for linea in lineas:
        elementos = linea.strip().split(',')
        _, codigo_producto, _, total_venta = elementos

        if codigo_producto not in ventas_por_producto:
            ventas_por_producto[codigo_producto] = 0

        total_venta = float(total_venta)
        ventas_por_producto[codigo_producto] += total_venta

    if not ventas_por_producto:
        print("No hay ventas registradas para ningún producto.")
    else:
        with open('reporteproducto.txt', 'w') as archivo_reporte:
            archivo_reporte.write("Reporte de Ventas por Producto:\n")
            for codigo_producto, total_ventas in ventas_por_producto.items():
                archivo_reporte.write(f"Codigo de Clientes: {codigo_producto}\n")
                archivo_reporte.write(f"Ventas Totales: Q{total_ventas}\n")
                archivo_reporte.write("------------------------------\n")
        print("Informe de Ventas por Producto guardado en 'reporteproducto.txt'.")

# Función para mostrar el menú de opciones
def mostrar_menu():
    while True:
        print("Menú de Opciones:")
        print("1. Generar Informe de Ventas por Producto")
        print("2. Generar Informe de Ventas por Cliente")
        print("3. Salir")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            reporte_ventas_por_cliente()
        elif opcion == "2":
            reporte_ventas_por_producto()
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elija 1, 2 o 3.")

# Llamar a la función para mostrar el menú
mostrar_menu()
