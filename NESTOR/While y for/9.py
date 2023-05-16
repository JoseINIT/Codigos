import random
Mayor=0
Menor=0
for x in range(1,11):
	numero=random.randint(500,1000)
	if x==1:
		Mayor=numero
		Menor=numero
	else:
		if numero>Mayor:
			Mayor=numero
		if numero<Menor:
			Menor=numero
	print(x,'',numero)
print("el mayor es,", Mayor)
print("el menor es",Menor)
#SA DE CV JOSE IBARRA