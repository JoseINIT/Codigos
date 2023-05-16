n = 0
n1 = int(input("escribe un valor"))
n2 = int(input("escribe un valor"))
while (n < 4):
    n = int(input("inserte[1] para sumar,[2] para restar,[3] para multiplicar,[4] para salir: "))

    if n == 1:
        print('#sumando#')
        suma = n1 + n2
        print("resultado es", suma)
    if n == 2:
        print("restando")
        resta = n1 - n2
        print("resultado es", resta)
    if n == 3:
        print('#multiplicando#')
        multiplicacion = (n1 * n2)
        print("el resultado es", multiplicacion)
else:
    print("el numero que inserto no es una opción")
#SA DE CV JOSE IBARRA