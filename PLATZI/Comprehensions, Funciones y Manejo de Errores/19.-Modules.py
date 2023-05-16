#te dice el lugar en el que se ejecuta el programa
import sys
print(sys.path)
#te imprime en listas los objetos que le indiques
import re
text="mi numero de telefono es 6471247496,El codigo de mexico es +52 "
result=re.findall("[0-9]+",text)
print(result)
#te da la hora
import time
timestap=time.time()
print(timestap)
local=time.localtime()
resultado=time.asctime(local)
print(resultado)
#te dice la frecuencia de los objetos de una lista
import collections
numbers=[1,1,2,1,2,1,4,5,3,3,21]
counter=collections.Counter(numbers)
print(counter)