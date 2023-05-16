def conversor(tipo_pesos,dolar):
    pesosmexicanos= float(input("Cuantos dinero " + tipo_pesos + " tienes:"))
    conversion = pesosmexicanos/dolar
    conversion = round(conversion,2)
    conversion = str(conversion)
    print("Tienes $",conversion+ " dolares")

menu="""
Bienvenido al conversor de monedas 👍😁

1.-Pesos Mexicanos
2.-Euros
3.-Yuanes
4.-Yenes
5.-Pesos Argentinos

Elige una opcion:
"""
opcion=int(input(menu))
if opcion == 1:
        conversor("Mexicanos",20.21)
elif opcion == 2:
        conversor("Euros",1.0324)
elif opcion == 3:
        conversor("Yuanes",7.19)
elif opcion == 4:
        conversor("Yenes",144.42)
elif opcion == 5:
        conversor("Argentinos",146.88)
else:
        print("Escribe una opcion valida don pendejo.")