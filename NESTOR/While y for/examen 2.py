import random
a=1
i=0
aux=0
vector=[]
for i in range(0,4):
    x=random.randint(0,100)
    vector.append(x)
    print("Tu numero generado es:",x)
for v in range(0,3):
    for i in range(0,3):
        if vector[i+1]>vector[i]:
            aux=vector[i]
            vector[i]=vector[i+1]
            vector[i+1]=aux
for i in range(0,4):
    print("los numeros de la lista son:",vector[i])
