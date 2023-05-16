days = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
newlist = []

for i in days:
  if "a" in i:
    newlist.append(i)

print(newlist) #["martes", "sabado"]

newlist = [i for i in days if "a" in i]

print(newlist) # ["martes", "sabado"]
pares=[i for i in range(10) if i%2==0]
print(pares)
lista=[i**2 for i in range(101) if i%5==0]
print(lista)