def media_aritmetica(numeros):
    return sum(numeros) / len(numeros)

numeros = list(map(int,input("Ingresa una lista de números separados por espacio: ").strip().split()))
print("La media aritmética es: ", media_aritmetica(numeros))
