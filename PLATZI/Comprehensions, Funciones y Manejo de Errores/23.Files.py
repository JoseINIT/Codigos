file=open("./txt.txt")
#print(file.read())
#print(file.readline())
#print(file.readline())
#print(file.readline())
#print(file.readline())
#en esta se cierra el archivo de forma manual
for line in file:
    print(line)
file.close()
#aqui se cierra el archivo de manera automatica
with open("./txt.txt") as file:
    for line in file:
        print(line)