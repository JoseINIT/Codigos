import random
#Datos y acumuladores
wins_usuario=0
empates=0
wins_computadora=0
def elecciones():
    #Elecciones
    opcion_computadora = random.choice(["piedra","papel","tijeras"])
    opcion_usuario = input("piedra(1),papel(2) o tijeras(3):").lower()
for x in range(5):

    #Condicionales
    if opcion_computadora==opcion_usuario:
        print("**EMPATE**")
        empates+=1
    elif opcion_usuario =="papel" or "1":
        if opcion_computadora== "piedra":
            print("El usuario gano!!")
            wins_usuario+=1
        else:
            print("La computadora gano!!")
            wins_computadora+=1
    elif opcion_usuario =="tijeras" or "2":
        if opcion_computadora=="papel":
            print("El usuario gano!!")
            wins_usuario+=1
        else:
            print("La computadora gano!!!")
            wins_computadora+=1
    elif opcion_usuario =="piedra" or "3":
        if opcion_computadora=="tijeras":
            print("El usuario gano!!")
            wins_usuario+=1
        else:
            print("La computadora gano!!")
            wins_computadora+=1
print(f"El usuario gano {wins_usuario} veces y la computadora {wins_computadora} y hubo {empates} empates")
