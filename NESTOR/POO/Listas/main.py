from personas import cpersona
from listado import clista
if __name__ == '__main__':
    lista = clista()
    while True:
        print("Resgistro [1]")
        print("Impresion [2]")
        print("Salir [3]")
        dp = int(input("Decide:"))
        if dp == 1:
            while True:
                print("#####REGISTRO#######")
                n = input("Ingresa un nombre:")
                i = int(input("Ingresa una id:"))
                persona = cpersona(n,i)
                lista.registrar(persona)
                d = input("Quieres registrar otra vez?? si [cualquier tecla] no [1]")
                if d == "1":
                    break
        elif dp == 2:
            lista.imprimir()
        elif dp == 3:
            exit()
        else:
            print("####ESA OPCION NO ESTA####")

