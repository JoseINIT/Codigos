from ClaseDatos import Datos
from ClasePersonas import Personas
op=0
Posicion = 0
ArregloNombre = []
ArregloControl = []
R = 0
lista=Datos()
print('PyCharm')
while op != 5:
    print("*****Menu Principal*****")
    print("[1] Altas ")
    print("[2] Bajas ")
    print("[3] Cambios ")
    print("[4] Consultas")
    print("[5] Salir")
    op = int(input("Da entrada a un numero:"))
    if op != 5:
        if op == 1:
            print("Estoy en Altas")
            Nombre=input("Introduce tu nombre:")
            Control=input("Introduce tu N. de control:")
            objetos=Personas(Nombre,Control)
            lista.Datos(objetos)
            Posicion=Posicion+1
        elif op == 2:
            print("Estoy en Baja")
            Control = input("Control")
            for c in range(0, Posicion):
                if Control== ArregloControl[c]:
                    print("El Nombre", ArregloNombre[c], "esta en la Posicion", c)
                    ArregloControl.pop(c)
                    ArregloNombre.pop(c)
                    Posicion=Posicion-1
                    break
        elif op == 3:
            print("Estoy en Cambios")
            Control = input("Control")
            for c in range(0, Posicion):
                if Control == ArregloControl[c]:
                    print("El Nombre", ArregloNombre[c], "esta en la Posicion", c)
                    NombreCambio=input("Nuevo Nombre ")
                    ArregloNombre[c] = NombreCambio
        elif op == 4:
            print("Estoy Consulta General")
            print("El Control Nombre" )
            for c in range(0, Posicion):
                print(ArregloControl[c]," ",ArregloNombre[c])
        else:
            print("Opcion no Valida o")
    else:
        print("Salir de la aplicacion")