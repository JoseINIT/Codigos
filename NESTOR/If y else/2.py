#SA DE CV JOSE IBARRA
horas=int(input("Cantidad de horas trabajadas:"))
pph=int(input("Cuanto te pagan por hora:"))
if horas>40:
    doble= horas-40
    sueldo=(40*pph)+(doble*(pph*2))
    print(sueldo)
else:
    sueldo=horas * pph
    print(sueldo)