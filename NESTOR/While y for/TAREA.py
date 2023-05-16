a=0
n=0
arreglonombre = []
arreglocontrol = []
while n<=5:
    print("1.-Altas")
    print("2.-Bajas")
    print("3.-Cambios")
    print("4.-Consultas")
    print("5.-Salida")
    n=int(input("elige un numero:"))
    if n == 1:
        nombre=input("tu nombre:")
        arreglonombre.append(nombre)
        control = input("numero de control:")
        arreglocontrol.append(control)
        a=a+1
    elif n==2:
        print("estas en bajas")
        control = input("numero de control:")
        for x in range(0,a):
            if control==arreglocontrol[x]:
                print("nombre",arreglonombre[x])
    elif n==3:
        print("Cambios")
    elif n==4:
        print("Consultas")
        for i in range (0,4):
            nombre=input("nombre:")
    elif n==5:
        break
    else:
        print("el numero no es correcto biejin")
        n=0