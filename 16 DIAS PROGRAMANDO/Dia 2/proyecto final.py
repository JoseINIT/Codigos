#comisiones
nombre=input("Cual es tu nombre:")
generado=float(input("Cuanto son tus ventas totales:"))
comision=generado*13/100
print(f"Tu {nombre} haz generado {round(comision,2)}$")