import random

def ordenar_burbuja(numeros):
    for i in range(len(numeros)-1):
        for j in range(len(numeros)-1):
            if numeros[j] < numeros[j+1]:
                numeros[j], numeros[j+1] = numeros[j+1], numeros[j]
    return numeros

numeros = [random.randint(0, 100) for _ in range(10)]
print("Lista de números aleatorios: ", numeros)
print("Lista ordenada de mayor a menor: ", ordenar_burbuja(numeros))
