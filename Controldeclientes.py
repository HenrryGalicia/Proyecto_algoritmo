class Cliente:
    def __init__(self, codigo, nombre, direccion):
        self.codigo = codigo
        self.nombre = nombre
        self.direccion = direccion

clientes = []

def listar_clientes():
    if not clientes:
        print("No hay clientes en el registro.")
        return
    
    print("Lista de clientes:")
    for cliente in clientes:
        print(f"Código: {cliente.codigo}, Nombre: {cliente.nombre}, Dirección: {cliente.direccion}")

def crear_cliente():
    print("Creación de un nuevo cliente:")
    codigo = input("Ingrese el código del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")

    cliente = Cliente(codigo, nombre, direccion)
    clientes.append(cliente)
    print("Cliente creado exitosamente.")
    guardar_clientes()

def editar_cliente():
    codigo = input("Ingrese el código del cliente que desea editar: ")

    for cliente in clientes:
        if cliente.codigo == codigo:
            print("Editar cliente:")
            nuevo_nombre = input(f"Nombre actual: {cliente.nombre}. Ingrese el nuevo nombre del cliente (deje en blanco para mantener el actual): ")
            nuevo_direccion = input(f"Dirección actual: {cliente.direccion}. Ingrese la nueva dirección del cliente (deje en blanco para mantener la actual): ")

            if nuevo_nombre:
                cliente.nombre = nuevo_nombre
            if nuevo_direccion:
                cliente.direccion = nuevo_direccion

            print("Cliente actualizado exitosamente.")
            guardar_clientes()
            return
    
    print(f"No se encontró ningún cliente con el código '{codigo}'.")

def eliminar_cliente():
    codigo = input("Ingrese el código del cliente que desea eliminar: ")

    for cliente in clientes:
        if cliente.codigo == codigo:
            clientes.remove(cliente)
            print(f"Cliente '{cliente.nombre}' eliminado exitosamente.")
            guardar_clientes()
            return
    
    print(f"No se encontró ningún cliente con el código '{codigo}'.")

def guardar_clientes():
    with open('clientes.txt', 'w') as archivo:
        for cliente in clientes:
            archivo.write(f"{cliente.codigo},{cliente.nombre},{cliente.direccion}\n")

def cargar_clientes():
    try:
        with open('clientes.txt', 'r') as archivo:
            for linea in archivo:
                partes = linea.strip().split(',')
                if len(partes) == 3:
                    codigo, nombre, direccion = partes
                    cliente = Cliente(codigo, nombre, direccion)
                    clientes.append(cliente)
    except FileNotFoundError:
        pass
    
cargar_clientes()

while True:
    print("---- Menú de Operaciones ----")
    print("1. Listar clientes")
    print("2. Crear cliente")
    print("3. Editar cliente")
    print("4. Eliminar cliente")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion.lower() == '1':
        listar_clientes()
    elif opcion.lower() == '2':
        crear_cliente()
    elif opcion.lower() == '3':
        editar_cliente()
    elif opcion.lower() == '4':
        eliminar_cliente()
    elif opcion.lower() == '5':
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
