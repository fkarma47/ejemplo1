# Calculadora completa en Python

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Error: no se puede dividir entre cero"
    return  num1 / num2

def potencia(num1, num2):
    return num1 ** num2

def raiz_cuadrada(num):
    return round (num ** 0.5, 2)

def main():
    print("Calculadora completa")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Salir")

    while True:
        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            print("El resultado de la suma es:", suma(num1, num2))
        elif opcion == "2":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            print("El resultado de la resta es:", resta(num1, num2))
        elif opcion == "3":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            print("El resultado de la multiplicación es:", multiplicacion(num1, num2))
        elif opcion == "4":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            print("El resultado de la división es:", division(num1, num2))
        elif opcion == "5":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            print("El resultado de la potencia es:", potencia(num1, num2))
        elif opcion == "6":
            num = float(input("Ingrese el número: "))
            print("El resultado de la raíz cuadrada es:", raiz_cuadrada(num))
        elif opcion == "7":
            print("Adiós!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
