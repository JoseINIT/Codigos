#SA DE CV JOSE IBARRA
traje=int(input("precio del traje:"))
if traje>2500:
    costo= traje- traje* 15/100
    print("el costo es:",costo)
else:
    costo = traje - traje * 8 / 100
    print("el costo es:", costo)