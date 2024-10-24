import random

numero_secreto = random.randint(1, 100)

while True:
    intento = int(input("Adivina el número secreto (entre 1 y 100): "))
    if intento == numero_secreto:
        print("¡Felicidades! Adivinaste el número secreto.")
        break
    elif intento < numero_secreto:
        print("El número secreto es mayor que", intento)
    else:
        print("El número secreto es menor que", intento)
