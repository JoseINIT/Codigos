import io
#r+ sirve para leer y escribir y w+ es lo mismo pero sobreescribe el texto
with open("./txt.txt","r+") as file:
    for line in file:
        print(line)
        file.write("Nuevas cosas\n")
        file.write("Hecyor\n")
        file.write("platzi\n")

