import random
categorias = {
    "programacion": ["python", "programa", "variable", "funcion", "bucle"],
    "Equipos": ["estudiantes", "boca", "river", "san lorenzo", "independiente","racing"],
    "Paises": ["argentina", "brasil", "uruguay", "chile","bolivia"]
}


print("Categorías disponibles:")
print("1. programacion")
print("2. Equipos")
print("3. Paises")

opcion = input("Elegí una categoría (1-3): ")

while opcion not in ["1", "2", "3"]:
    print("Entrada no válida")
    opcion = input("Elegí una categoría (1-3): ")
    
if opcion == "1":
    categoria_elegida = "programacion"
elif opcion == "2":
    categoria_elegida = "Equipos"
else:
    categoria_elegida = "Paises"


palabras_disponibles = random.sample(
    categorias[categoria_elegida],
    len(categorias[categoria_elegida])
)
seguir_jugando = "si"
indice = 0

letras_adivinadas = []
intentos = 6
errores = 0

print("¡Bienvenido al juego del ahorcado!")
while seguir_jugando == "si" and indice < len(palabras_disponibles):
    palabra= palabras_disponibles[indice]
    indice= indice + 1

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
        puntaje = 6 - errores
        print ("Puntaje", puntaje)
        break

    intento = input("Ingresá una letra: ").lower()

    if len(intento) != 1 or not ('a' <= intento <= 'z'):
        print("Entrada no válida")
        continue

    if intento in letras_adivinadas:
        print("Ya intentaste esa letra")
    elif intento in palabra:
        letras_adivinadas.append(intento)
        print("¡Bien!")
    else:
        letras_adivinadas.append(intento)
        intentos -= 1
        errores = errores + 1
        print("Incorrecto. Intentos restantes:", intentos)

if intentos == 0:
    print("Perdiste. La palabra era:", palabra)
    print("Puntaje = 0")

if indice < len(palabras_disponibles):
    seguir_jugando = input("¿Querés jugar otra ronda? (si/no): ").lower()

    while seguir_jugando not in ["si", "no"]:
        print("Entrada no válida")
        seguir_jugando = input("¿Querés jugar otra ronda? (si/no): ").lower()
