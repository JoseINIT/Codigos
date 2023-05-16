num_user = int(input(" Introduce un numero: "))

if num_user < 1:
    num_user = 1

print(f"Tabla del {num_user}")

contador = 1
while contador <= 10:
    print(f"{num_user} x {contador} = {num_user*contador}")
    contador += 1
else:
    print("Tabla terminada")
#SA DE CV JOSE IBARRA