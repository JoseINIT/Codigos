nombre=input("dame el nombre del archivo que vas a crear")
archivo=open(f"{nombre}.txt","w")
archivo.write("""hola
josesiño
y
maximiliano
como 
andan 
webones""")
print(archivo.close())