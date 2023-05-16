class Animal(object):
    def __init__(self, identificacion, nombre):
        self.identificacion = identificacion
        self.nombre = nombre
    def __str__(self):
        return f" mi IDENTIFICACION ES [{self.identificacion}]  mi nombre es [{self.nombre}]"
    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__)

class scGato(Animal):
    def __init__(self, id, nombre, tamaño):# constructor completo de la subclase gato
        # Alternativa 1
        super().__init__(self, id, nombre )# pasa los atributos de la clase base a Subclase agrega un atributo subclase gato
        self.tamaño=tamaño

class scPerro(Animal):
    def __init__(self, id, nombre,dueño):
        # Alternativa 2
        super().__init__(id, nombre)
        self.dueño = dueño

class scLoro(Animal):
    def __init__(self, id, nombre, tipo):
        # Alternativa 3
        super().__init__(id,nombre)
        self.tipo=tipo