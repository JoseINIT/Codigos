class CasillaDeVotacion:
    def __init__(self,id,pais):
        self.__id=id
        self.__pais=pais
        self.__Region=None
    @property
    def Region(self):
        return self.__Region
    @Region.setter
    def Region(self,Region):
        if Region in self.__pais:
            self.__Region=Region
        else:
            raise ValueError (f"La region {Region} no es valida en {self.__pais}")
if __name__ == "__main__":
    casilla=CasillaDeVotacion(123,["Ciudad de Mexico","Morelos"])
    print(casilla.Region)
    casilla.Region=input()
    print(casilla.Region)