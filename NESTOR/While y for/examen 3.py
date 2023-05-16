import random
suma=0
c=1
vector=[]
for i in range(0,9):
    x=random.randint(1,9)
    vector.append(x)
    print(i," . ", x)
for v in range(0,8):
    for i in range(0,8):
        if vector[i+1]>vector[i]:
            aux=vector[i]
            vector[i]=vector[i+1]
            vector[i+1]=aux
            vectorarreglado = vector[i]
for i in range(0,9):
    print("La lista ordenada es:",vector[i])
for i in range(0,8):
    if vector[i+1]==vector[i]:
           c=c+1
    else:
        print(f" el numero {vector[i]} tiene una frecuencia de {c}"," ",c*"*")
        c=1
print("La Mediana es:",vector[4])
for elemento in vector:
    suma+=elemento
print("La Media es:",suma/9)
print("La Moda es:",)