class clista:
    def __init__(self):
        self.lista = []

    def registrar(self,ob):
        self.lista.append(ob)

    def imprimir(self):
        for x in range(len(self.lista)):
            print(f"Nombre [{self.lista[x].nombre}]--id [{self.lista[x].id}]")