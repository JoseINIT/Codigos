def suma_cuadrados(*args):
    total=0
    for f in args:
        total=f**2 + total
    return total

print(suma_cuadrados(1,2,3))