from colorama import Fore,Back
class Texto:
    def __init__(self,titulo,color_de_texto,color_de_fondo):
        self.titulo=titulo
        if color_de_texto==1:
            self.colortexto=Fore.GREEN
        elif color_de_texto==2:
            self.colortexto=Fore.BLUE
        elif color_de_texto==3:
            self.colortexto=Fore.BLACK

        if color_de_fondo==1:
            self.colorfondo= Back.YELLOW
        elif color_de_fondo == 2:
            self.colorfondo = Back.CYAN
        elif color_de_fondo == 3:
            self.colorfondo = Back.RED
    def imprimirtexto(self):
        print(self.colortexto,self.colorfondo,self.titulo)