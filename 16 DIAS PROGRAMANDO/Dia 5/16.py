def suma_absolutos(*args):
    suma = 0
    for arg in args:
        suma += abs(arg)

    return suma
print(suma_absolutos(3,5,7,6))