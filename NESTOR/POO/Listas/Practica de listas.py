class Persona:
    def __init__(self,nom,id):
        self.nom=nom
        self.id=id
def Mostrar():
    k=0
    while k < len(lista):
        print(lista[k].nom," ",lista[k].id)
        k+=1
i=0
lista=[]
while i==0:
    print("""Menu
    1.-Registrar Personas
    2.-Mostras Personas
    3.-Salir""")
    opcion=int(input("Eleccion:"))
    if opcion==1:
        print("REGISTAR")
        nombre=input("tu nombre:")
        numero=int(input("tu id:"))
        per= Persona(nombre,numero)
        lista.append(per)
        print("Persona guardada con exito!")
    elif opcion==2:
        print("MOSTRAR")
        Mostrar()
    elif opcion==3:
        exit()
    else:
        print("Opcion invalida")