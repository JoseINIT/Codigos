registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
miarchivo=open("registro.txt","w")
for p in registro_ultima_sesion:
    miarchivo.write(p + "\t")
miarchivo.close()
miarchivo = open("registro.txt", "r")
print(miarchivo.read())
