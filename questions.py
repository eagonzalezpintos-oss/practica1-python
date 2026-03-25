import random

palabras = ["python", "programa", "variable", "funcion", "bucle"]

palabra = random.choice(palabras)

letras_adivinadas = []
intentos = 6

print("¡Bienvenido al juego del ahorcado!")

while intentos > 0:
    progreso = ""

    for letra in palabra:
        if letra in letras_adivinadas:
            progreso += letra
        else:
            progreso += "_"

    print("Palabra:", progreso)

    if "_" not in progreso:
        print("¡Ganaste!")
        break

    intento = input("Ingresá una letra: ").lower()

    if intento in letras_adivinadas:
        print("Ya intentaste esa letra")
    elif intento in palabra:
        letras_adivinadas.append(intento)
        print("¡Bien!")
    else:
        letras_adivinadas.append(intento)
        intentos -= 1
        print("Incorrecto. Intentos restantes:", intentos)

if intentos == 0:
    print("Perdiste. La palabra era:", palabra)
