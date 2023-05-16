def decimal_a_binario(num):
    binario = ""
    while num > 0:
        binario = str(num % 2) + binario
        num = num // 2
    return binario

num = int(input("Ingresa un número en base 10: "))
print(f"El número {num} en base 2 es: {decimal_a_binario(num)}")