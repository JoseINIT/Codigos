cantidad=int(input("Cuantos valores vas a introducir:"))
lista=[]
varianza=0
for i in range(cantidad):
    x=float(input("Valor a introducir:"))
    lista.append(x)
media=sum(lista)/len(lista)
for x in lista:
    suma1=((x-media)**2)/len(lista)
    varianza+=suma1
print("la varianza es es:",varianza)
print("la desviacion estandar es:",varianza**.5)