

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_cuadrado(lado):
    return lado ** 2

def area_circunferencia(radio):
    return math.pi * (radio ** 2)

while True:
    print("\nSeleccione una opción:")
    print("1. Triángulo")
    print("2. Cuadrado")
    print("3. Circunferencia")
    print("4. Salir")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = area_triangulo(base, altura)
        print("El área del triángulo es:", area)
    elif opcion == 2:
        lado = float(input("Ingrese el lado del cuadrado: "))
        area = area_cuadrado(lado)
        print("El área del cuadrado es:", area)
    elif opcion == 3:
        radio = float(input("Ingrese el radio de la circunferencia: "))
        area = area_circunferencia(radio)
        print("El área de la circunferencia es:", area)
    elif opcion == 4:
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida")
