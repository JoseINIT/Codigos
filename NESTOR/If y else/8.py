#SA DE CV JOSE IBARRA
nombre = "Lucho"
ciudad = "Barcelona"
continente = "Europa"
edad = 99
mayor_edad = 18

if edad >= mayor_edad:
    print(nombre, " es mayor de edad")
    if continente != "Europa":
        print("No estas en Europa")
    else:
        print("Estas en Europa y la ciudad de", ciudad)
else:
    print(nombre," no es mayor de edad")