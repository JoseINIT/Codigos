def suma_numeros(nombre, *args):
    suma = sum(args)
    return f"{nombre}, la suma de tus números es {suma}"
print(suma_numeros("Josesiño",67,545,3))