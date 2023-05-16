num = int(input("Un numero entre 0 y 9:"))
if num >= 0 and num <= 9:
    print(f"La Tabla del {num}")
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")
else:
    print("Introduce un numero correcto")
#SA DE CV JOSE IBARRA