#metemos datos al arreglo
cantidad=int(input("Cuantos valores vas a introducir:"))
lista=[]
for i in range(cantidad):
    x=float(input("Valor a introducir:"))
    lista.append(x)
#Sacamos la media
media=sum(lista)/len(lista)
#Ordenamos la lista y Sacamos la mediana
lista.sort()
if len(lista)%2==0:
    mediana = (lista[len(lista) // 2 - 1] + lista[len(lista) // 2]) / 2
else:
    mediana=lista[len(lista)//2]
#Sacamos la moda
lista.sort()
moda = None
frecuencia_max = 0
frecuencia_actual = 1
valor_actual = lista[0]
for i in range(1, len(lista)):
    if lista[i] == valor_actual:
        frecuencia_actual += 1
    else:
        if frecuencia_actual > frecuencia_max:
            frecuencia_max = frecuencia_actual
            moda = valor_actual
        frecuencia_actual = 1
        valor_actual = lista[i]
if frecuencia_actual > frecuencia_max:
    frecuencia_max = frecuencia_actual
    moda = valor_actual
print(media,mediana,moda)
