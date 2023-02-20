import random

# Definir una lista de palabras para que el usuario adivine
palabras = ["programacion", "python", "computadora", "algoritmo", "variable", "cadena", "lista"]

# Seleccionar una palabra al azar de la lista
palabra_secreta = random.choice(palabras)

# Inicializar las variables que vamos a utilizar
letras_adivinadas = []
intentos_restantes = 6
dibujo = ["""
 +---+
 |   |
     |
     |
     |
     |
=======""", """
 +---+
 |   |
 O   |
     |
     |
     |
=======""", """
 +---+
 |   |
 O   |
 |   |
     |
     |
=======""", """
 +---+
 |   |
 O   |
/|   |
     |
     |
=======""", """
 +---+
 |   |
 O   |
/|\  |
     |
     |
=======""", """
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=======""", """
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
======="""]

# Imprimir el mensaje de bienvenida
print("¡Bienvenido al juego del ahorcado!")
print("La palabra tiene", len(palabra_secreta), "letras.")

# Bucle principal del juego
while intentos_restantes > 0:
    # Mostrar el dibujo actual
    print(dibujo[6 - intentos_restantes])
    
    # Mostrar las letras que ya han sido adivinadas
    print("Letras adivinadas:", end=" ")
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print()
    
    # Pedir al usuario que ingrese una letra
    letra_usuario = input("Ingresa una letra: ")
    
    # Verificar si la letra está en la palabra secreta
    if letra_usuario in palabra_secreta:
        print("¡Correcto! La letra", letra_usuario, "está en la palabra.")
        letras_adivinadas.append(letra_usuario)
    else:
        print("Lo siento, la letra", letra_usuario, "no está en la palabra.")
        intentos_restantes -= 1
        
    # Verificar si el usuario ha adivinado la palabra completa
    if set(letras_adivinadas) == set(palabra_secreta):
        print("¡Felicitaciones! Has adivinado la palabra", palabra_secreta)
        break
    
    # Mostrar el número de intentos restantes
    print("Te quedan", intentos_restantes, "intentos.")
    
# Si el usuario ha agotado todos los intentos sin adivinar la palabra, mostrar un mensaje de derrota
if intentos_restantes == 0:
    print(dibujo[6 - intentos_restantes])
    print("Lo siento, has perdido. La palabra era", palabra_secreta)
