#El juego es una versión simplificada del juego "Mastermind". El objetivo es adivinar un código secreto generado aleatoriamente por la computadora. 
#El jugador hace propuestas de códigos y recibe pistas de la computadora sobre cuántos dígitos son correctos y cuántos están en la posición correcta.
#El jugador tiene un número limitado de intentos para adivinar el código.
#El juego tiene tres niveles de dificultad: fácil, medio y difícil, que corresponden a códigos de tres, cuatro y cinco dígitos, respectivamente.

import random 
import time

digitos = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

while True:
    codigo = ''
    eleccion = input("¿Qué dificultad quieres? Escribe 'Facil', 'Medio' o 'Dificil': ")
    while True:
        eleccion = eleccion.lower()
        if eleccion == "facil":
            cant_digitos = 3
            break
        elif eleccion == "medio":
            cant_digitos = 4
            break
        elif eleccion == "dificil":
            cant_digitos = 5
            break
        else:
            eleccion = input("¿Qué dificultad quieres? Escribe 'Facil', 'Medio' o 'Dificil': ")

    for i in range(cant_digitos):
        candidato = random.choice(list(digitos))
        while candidato in codigo:
            candidato = random.choice(list(digitos))
        codigo += candidato 

    print("¡Bienvenido/a al juego de Nico!")
    print("Tienes que adivinar el número de %s cifras diferentes" % cant_digitos)
    
    while True:
        propuesta = input("¿Qué código propones? ")
        if propuesta.isdigit() and len(propuesta) == cant_digitos:
            break

    intentos = 1
    while propuesta != codigo and propuesta != "Abandono":
        intentos += 1
        aciertos = 0
        coincidencias = 0

        for i in range(cant_digitos):
            if propuesta[i] == codigo[i]:
                aciertos += 1
            elif propuesta[i] in codigo:
                coincidencias += 1

        print("Tu propuesta (%s) tiene %s aciertos y %s coincidencias" % (propuesta, aciertos, coincidencias))
        propuesta = input("Propón otro código o di 'Abandono' para rendirte: ")
        
        if propuesta == "Abandono":
            print("El código era %s" % codigo)
            print("¡Suerte la próxima vez!")
            break
    
    if propuesta == codigo:
        print("¡Felicidades! Adivinaste el código en %s intentos. El código era %s" % (intentos, codigo))
    elif propuesta != "Abandono":
        print("Has rendido después de %s intentos. El código era %s" % (intentos - 1, codigo))

    seguir = input("¿Quieres seguir jugando? Escribe 'S' para seguir o 'N' para salir: ")
    seguir = seguir.lower()
    
    while seguir != "s" and seguir != "n":
        seguir = input("¿Quieres seguir jugando? Escribe 'S' para seguir o 'N' para salir: ")
        seguir = seguir.lower()
    
    if seguir == "n":
        print("¡Vuelve pronto!")
        time.sleep(3)
        break
