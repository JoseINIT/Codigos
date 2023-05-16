class Lavadora:
    def __init__(self):
        pass
    def lavar(self,temperatura="Caliente"):
        #encapsulamos el primer atributo
        self._llenar_tanque_de_agua(temperatura)
        self._añadir_jabon()
        self._lavar()
        self._centrifugar()
    #Encapsulamos el metodo llenar tanque de agua
    def _llenar_tanque_de_agua(self,temperatura):
        print(f"llenar el tanque con agua a la temperatura {temperatura}")
    def _añadir_jabon(self):
        print(f"añadiendo jabon al agua")
    def _lavar(self):
        print("lavar la ropa")
    def _centrifugar(self):
        print("Centrifugando la ropa")

if __name__ == "__main__":
    lavadora=Lavadora()
    lavadora.lavar()