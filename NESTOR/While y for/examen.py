ahorrado=0
meses=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
for x in range(0,12):
    mes=int(input("lo que ahorraste en "+ meses[x] +" es:"))
    ahorrado=mes+ahorrado
print("lo que ahorraste en todo el año es:",ahorrado)
#Jose Daniel Ibarra Nieblas