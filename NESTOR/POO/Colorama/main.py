from Datos import Texto
if __name__ == "__main__":
    titulo2=input("Imprime un titulo:")
    colodetitulo2=int(input("ELige cualquiera de los siguientes colores para tu texto:Verde[1] Azul[2] Negro[3]"))
    colodefondo2=int(input("ELige cualquiera de los siguientes colores para tu fondo:Amarillo[1] Azul Oscuro[2] Rojo[3]"))
    mensaje=Texto(titulo2,colodetitulo2,colodefondo2)
    print("EL TITULO ES")
    mensaje.imprimirtexto()
