import tkinter as tk   
import yagmail
#definiciones aca
def reporte_ventas_por_producto():
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
            archivo_reporte.write("Reporte de Ventas por producto:\n")
            for codigo_cliente, total_ventas in ventas_por_cliente.items():
                archivo_reporte.write(f"Codigo de Producto: {codigo_cliente}\n")
                archivo_reporte.write(f"Ventas Totales: Q{total_ventas}\n")
                archivo_reporte.write("------------------------------\n")
        print("Informe de Ventas por Cliente guardado en 'reportecliente.txt'.")
        
    # Limpiar el widget de texto antes de mostrar el contenido
    ventanilla.delete("1.0", "end")

    # Leer el contenido del archivo "inventario.txt" y mostrarlo en el widget de texto
    with open("reportecliente.txt", "r") as archivo:
        contenido = archivo.read()
        ventanilla.insert("1.0", contenido)   


# Ruta al archivo que deseas adjuntar
archivo = "reporteproducto.txt"

# Configura tu información de correo electrónico
correo = yagmail.SMTP('galiciahenrry2023@gmail.com', 'scem hlcm ugbr mlsw')

# Destinatarios, asunto y mensaje
destinatarios = ['Henrrygalicia2002@gmail.com']
asunto = 'Reportes'
mensaje = 'Reportes de Productos'

# Adjunta el archivo al correo
correo.send(destinatarios, asunto, [mensaje, archivo])

# Cierra la conexión SMTP
correo.close()    
        
def reporte_ventas_por_cliente():
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
            archivo_reporte.write("Reporte de Ventas por Clientes:\n")
            for codigo_producto, total_ventas in ventas_por_producto.items():
                archivo_reporte.write(f"Codigo de Clientes: {codigo_producto}\n")
                archivo_reporte.write(f"Ventas Totales: Q{total_ventas}\n")
                archivo_reporte.write("------------------------------\n")
        print("Informe de Ventas por Producto guardado en 'reporteproducto.txt'.")
        
        ventanilla.delete("1.0", "end")

    # Leer el contenido del archivo "inventario.txt" y mostrarlo en el widget de texto
    with open("reporteproducto.txt", "r") as archivo:
        contenido = archivo.read()
        ventanilla.insert("1.0", contenido)   
    import yagmail

# Ruta al archivo que deseas adjuntar
archivo = "reporteproducto.txt"

# Configura tu información de correo electrónico
correo = yagmail.SMTP('galiciahenrry2023@gmail.com', 'scem hlcm ugbr mlsw')

# Destinatarios, asunto y mensaje
destinatarios = ['Henrrygalicia2002@gmail.com']
asunto = 'Reportes'
mensaje = 'Reportes de Clientes'

# Adjunta el archivo al correo
correo.send(destinatarios, asunto, [mensaje, archivo])

# Cierra la conexión SMTP
correo.close()    
                   
ventana = tk.Tk()
ventana.title("Reportes")
ventana.geometry('900x300')
ventana.config(bg='#262727')
ventana.iconbitmap(r'C:\Users\al881\OneDrive\Escritorio\Proyecto algoritmos\interfaz\inicios.ico')
#label y entrys aquii

titulo = tk.Label(ventana, text="Sistema de Reportes",width=40,font=("Helvetica", 20, "bold"),bg="#2f3136", fg="white", borderwidth=2)
titulo.pack()

izquierda = tk.Frame(ventana,bg='#262727')
izquierda.pack(side="left")

cliente = tk.Label(izquierda, text="Aqui se encuentra los reportes de Clientes ",font=("Helvetica", 10, "bold"),bg="#101111", fg="white", borderwidth=2)
cliente.pack(padx=10, pady=10, anchor="w")
clientes1 = tk.Button(izquierda, text="Reportes de Clientes", command=reporte_ventas_por_cliente,bg="#8c14dc", fg="white")
clientes1.pack()

producto = tk.Label(izquierda, text="Aqui aparecera los reportes de Productos",font=("Helvetica", 10, "bold"),bg="#101111", fg="white", borderwidth=2)
producto.pack(padx=10, pady=10, anchor="w")
producto1 = tk.Button(izquierda, text="Reportes de Productos", command=reporte_ventas_por_producto,bg="#8c14dc", fg="white")
producto1.pack()
#botones aca

derecha = tk.Frame(ventana,bg='#262727')
derecha.pack(side="right")

#wiht de lo que se pida
ventanilla = tk.Text(derecha,  width=60, height=10, wrap=tk.WORD,font=("Helvetica", 10, "bold"),bg="#37393f", fg="white")
ventanilla.pack(padx=10, pady=10, anchor="e")

ventana.mainloop()