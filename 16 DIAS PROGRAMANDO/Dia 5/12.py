n=[100,125,1256,65436]
def cantidad_pares(n):
    suma=0
    for d in n:
        if d%2==0:
            suma+=1
        else:
            pass
    return suma
print(cantidad_pares(n))