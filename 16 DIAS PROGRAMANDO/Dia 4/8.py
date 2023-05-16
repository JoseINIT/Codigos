lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]
suma_pares = 0
suma_impares =0
for x in lista_numeros:
    if x%2==0:
        suma_pares+=x
    else:
        suma_impares+=x
print(suma_pares)
print(suma_impares)