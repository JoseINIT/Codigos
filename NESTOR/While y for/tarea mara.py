#JOSE DANIEL IBARRA NIEBLAS
def listas(c):
    if Opcion == 1:
        while True:
            print("Estas en Alta")
            Control = int(input("ingresa el N.Control: "))
            Nombre = input("Ingresa un nombre: ")
            g = input(f"Desea guardar {Nombre} con el numero de control {Control}?\n Si[1], No[Cualquier tecla]\n")
            if g == "1":
                ArregloControl.append(Control)
                ArregloNombre.append(Nombre)
                print("!!Guardado!!")
                C = C + 1
            else:
                print("No se guardo")
            g2 = input("Desea dar de alta otra vez?\nSi[1], No[Cualquier tecla]\n: ")
            if g2 != "1":
                break
def bajas():
    print("Bajas")
    Control1 = int(input("ingresa el N.Control: "))
    for x in range(0, C):
        if ArregloControl[x] == Control1:
            g = input(f"Desea eliminar {Nombre} con el numero de control {Control}\n Si[1], No[Cualquier tecla]\n")
        if g == "1":
            print(f" !!se elimino {Nombre[x]}!!")
            ArregloControl.pop(x)
            ArregloNombre.pop(x)
            C = C - 1
        break
    g2 = input("Desea dar de alta otra vez?\n Si[1], No[Cualquier tecla]\n: ")
def cambios():
    while True:
        print("Estas en Cambios")
        Control2 = int(input("Ingresa el N.Control:"))
        for x in range(0, C):
            if ArregloControl[x] == Control2:
                g = input(f"Nombre elegido {Nombre} con el numero de control {Control}\nIngrese el nuevo nombre:")
                print(f"Se cambio el nombre a {Nombre}")
                Nombre = g
                break
        g2 = input("Desea hacer cambios otra vez?\n Si[1], No[Cualquier tecla]\n:")
        if g2 != "1":
            break
def consultas():
    print(" Estas en Consultas")
    if C != 0:
        for x in range(0, C):
            print("Nombre:[", ArregloNombre[x], "]\nNumero de control:[", ArregloControl[x], "]")
    else:
        print("No hay datos guardados")
ArregloNombre = []
ArregloControl = []
x = 0
Opcion = 0
C = 0
Nombre = 0
Control = 0
while Opcion!= 5:
    print("Menu principal: ")
    print("[1]Altas")
    print("[2]Bajas")
    print("[3]Cambios")
    print("[4]Consultas")
    print("[5]Salir")
    Opcion = int(input("Ingresa la opcion: "))
    if Opcion == 1:
        listas()
    elif Opcion == 2:
        bajas()
    elif Opcion == 3:
        cambios()
    elif Opcion == 4:
        consultas()
    elif Opcion == 5:
        print("Saliste")
        break
    else:
    	print("Opcion no valida, ingrese otra")