import random
def lanzar_dados():
    dado1=random.randint(1,6)
    dado2=random.randint(1,6)
    return dado1,dado2
def evaluar_jugada(dado1,dado2):
    resultado = dado2 + dado1
    if resultado>=6:
        return f"La suma de tus dados es {resultado}. Lamentable"
    elif resultado>6:
        return f"La suma de tus dados es {resultado}. Tienes buenas chances"
    elif resultado>=10:
        return f"La suma de tus dados es {resultado}. Parece una jugada ganadora"
