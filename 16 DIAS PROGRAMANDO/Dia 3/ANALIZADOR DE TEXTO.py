
texto=input("pon tu texto:")
texto.lower()
l1=input("Primera letra:")
l1.lower()
l2=input("Segunda letra:")
l2.lower()
l3=input("Tercera letra:")
l3.lower()
c1=texto.count(l1)
c2=texto.count(l2)
c3=texto.count(l3)
print(f"La letra {l1} se repite {c1}")
print(f"La letra {l2} se repite {c2}")
print(f"La letra {l3} se repite {c3}")
c4=c1+c2+c3
separado=texto.split()
separado1=separado
separado1.reverse()
textoinvertido="".join(separado1)
reverso=separado.reverse()
inverso=texto[::-1]
variable=texto.find("python")
python=[]
python.append(variable)
bool= variable == 0
print("Esta es la cantidad de palabras que hay en tu texto:",len(separado))
print("Cantidad de veces que se repiten las letras que pusiste en el texto:",c4)
print("La primera letra es:",texto[0],"y la ultima letra es",texto[-1])
print("Orden inverso:",inverso)
print(f"Si ordenamos tu texto al revés va a decir: '{textoinvertido}'")
print("La palabra python esta en el texto?",bool)
