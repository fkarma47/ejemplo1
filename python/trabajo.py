import datetime
# Registro de aprendices del SENA

# Funciones

def get_apprentice_name():
    """Get the apprentice's name from the user"""
    while True:
        nombre = input("Ingrese el nombre del aprendiz: ")
        if nombre:
            return nombre
        print("El nombre no puede estar vacío.")

def display_apprentice_info(id):
    """Display the apprentice's information"""
    if id in aprendices:
        print(f"Aprendiz {aprendices[id]['nombre']} encontrado:")
        print(f"  ID: {id}")
        print(f"  Entrada: {aprendices[id]['entrada']}")
        print(f"  Salida: {aprendices[id]['salida']}")
        print(f"  Asistencia: {aprendices[id]['asistencia']}")
        print(f"  Fecha de registro: {aprendices[id]['fecha_registro']}")
        print(f"  Titulo: {aprendices[id]['titulo']}")
    else:
        print(f"No se encuentra el aprendiz con ID {id} registrado.")

def registrar_aprendiz():
    """Register a new apprentice"""
    global id_counter
    nombre = get_apprentice_name()
    hora_entrada = input("Ingrese la hora de entrada: ")
    hora_salida = input("Ingrese la hora de salida: ")
    fecha_registro = datetime.date.today()
    print("Seleccione un titulo:")
    for i, titulo in enumerate(titulos.keys()):
        print(f"{i+1}. {titulo}")
    opcion = int(input("Ingrese el número del titulo: "))
    titulo = list(titulos.keys())[opcion-1]
    aprendices[id_counter] = {
        "nombre": nombre,
        "entrada": hora_entrada,
        "salida": hora_salida,
        "asistencia": 1,
        "fecha_registro": fecha_registro,
        "titulo": titulo
    }
    print(f"Aprendiz {nombre} registrado con éxito. ID: {id_counter}")
    id_counter += 1

def buscar_aprendiz():
    """Search for an apprentice by ID"""
    id = int(input("Ingrese el ID del aprendiz a buscar: "))
    display_apprentice_info(id)

def editar_aprendiz():
    """Edit an apprentice's information"""
    id = int(input("Ingrese el ID del aprendiz a editar: "))
    if id in aprendices:
        display_apprentice_info(id)
        opcion = input("¿Qué desea editar? (1) Entrada, (2) Salida, (3) Asistencia, (4) Titulo: ")
        if opcion == "1":
            nueva_entrada = input("Ingrese la nueva hora de entrada: ")
            aprendices[id]["entrada"] = nueva_entrada
            print(f"Hora de entrada actualizada con éxito.")
        elif opcion == "2":
            nueva_salida = input("Ingrese la nueva hora de salida: ")
            aprendices[id]["salida"] = nueva_salida
            print(f"Hora de salida actualizada con éxito.")
        elif opcion == "3":
            nueva_asistencia = int(input("Ingrese la nueva asistencia: "))
            aprendices[id]["asistencia"] = nueva_asistencia
            print(f"Asistencia actualizada con éxito.")
        elif opcion == "4":
            print("Seleccione un titulo:")
            for i, titulo in enumerate(titulos.keys()):
                print(f"{i+1}. {titulo}")
            opcion = int(input("Ingrese el número del titulo: "))
            titulo = list(titulos.keys())[opcion-1]
            aprendices[id]["titulo"] = titulo
            print(f"Titulo actualizado con éxito.")
        else:
            print("Opción inválida. Int ente nuevamente.")
    else:
        print(f"No se encuentra el aprendiz con ID {id} registrado.")

def eliminar_aprendiz():
    """Delete an apprentice"""
    id = int(input("Ingrese el ID del aprendiz a eliminar: "))
    if id in aprendices:
        del aprendices[id]
        print(f"Aprendiz con ID {id} eliminado con éxito.")
    else:
        print(f"No se encuentra el aprendiz con ID {id} registrado.")

def mostrar_registro():
    """Display the registry of all apprentices"""
    for id, datos in aprendices.items():
        print(f"Aprendiz: {datos['nombre']}")
        print(f"  ID: {id}")
        print(f"  Entrada: {datos['entrada']}")
        print(f"  Salida: {datos['salida']}")
        print(f"  Asistencia: {datos['asistencia']}")
        print(f"  Fecha de registro: {datos['fecha_registro']}")
        print(f"  Titulo: {datos['titulo']}")
        print()

def mostrar_estadisticas():
    """Display statistics on apprentice attendance"""
    total_aprendices = len(aprendices)
    total_asistencia = sum(datos["asistencia"] for datos in aprendices.values())
    promedio_asistencia = total_asistencia / total_aprendices if total_aprendices > 0 else 0
    print(f"Estadísticas de asistencia:")
    print(f"  Total aprendices: {total_aprendices}")
    print(f"  Total asistencia: {total_asistencia}")
    print(f"  Promedio asistencia: {promedio_asistencia:.2f}%")

def agregar_titulo():
    """Add a new title"""
    print("Seleccione un titulo:")
    opciones = [
        "Programación de software",
        "Monitoreo ambiental",
        "Producción animal",
        "Construcción de vías",
        "Cultivos agrícolas"
    ]
    for i, opcion in enumerate(opciones):
        print(f"{i+1}. {opcion}")
    seleccion = int(input("Ingrese el número de la opción: "))
    if 1 <= seleccion <= len(opciones):
        titulo = opciones[seleccion - 1]
        if titulo not in titulos:
            titulos[titulo] = True
            print(f"Titulada '{titulo}' agregado con éxito.")
        else:
            print(f"La titulada '{titulo}' ya existe.")
    else:
        print("Opción inválida. Intente nuevamente.")

# Menú principal

while True:
    print("Registro de aprendices del SENA")
    print("-------------------------------")
    print("1. Registrar nuevo aprendiz")
    print("2. Mostrar registro")
    print("3. Mostrar estadísticas")
    print("4. Buscar aprendiz")
    print("5. Editar aprendiz")
    print("6. Eliminar aprendiz")
    print("7. Agregar título")
    print("8. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_aprendiz()
    elif opcion == "2":
        mostrar_registro()
    elif opcion == "3":
        mostrar_estadisticas()
    elif opcion == "4":
        buscar_aprendiz()
    elif opcion == "5":
        editar_aprendiz()
    elif opcion == "6":
        eliminar_aprendiz()
    elif opcion == "7":
        agregar_titulo()
    elif opcion == "8":
        break
    else:
        print("Opción inválida. Intente nuevamente.")