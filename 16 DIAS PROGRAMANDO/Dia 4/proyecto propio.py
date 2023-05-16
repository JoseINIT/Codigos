from random import *
nombre=input("Hola usuario, Cual es tu nombre? ")
secreto=randint(1,100)
print(f"Bueno {nombre} he pensado un numero entre el 1 y el 100 y tienes que adivinarlo con solo 8 intentos, suerte!!")
print(secreto)
for x in range(8):
    numero=int(input("cual es el numero que piensas?"))
    if numero <0 or numero >100:
        print("Numero no permitido")
    elif numero<secreto:
        print(f"Tu {numero} es menor que el numero secreto")
    elif numero > secreto:
        print(f"Tu {numero} es mayor que el numero secreto")
    elif numero==secreto:
        print(f"Haz ganado, y te ha tomado {x+1} intentos")
        break
if numero != secreto:
    print(f"Lo siento, se han agotado los intentos. El numero secreto era {secreto}")