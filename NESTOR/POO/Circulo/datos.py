class Circulo:
    __pi = 3.141592
    def __init__(self, radio):
        self.__radio = radio
    def __cuadrado(self, n):
        return n ** 2
    def area(self):
        return Circulo2.__pi * self.__cuadrado(self.__radio)
    def valorRadio(self):
        return self.__radio
    def fijaRadio(self, nuevoRadio):
        self.__radio = nuevoRadio