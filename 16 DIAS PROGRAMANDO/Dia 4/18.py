capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
for pais,capi in zip(paises,capitales):
    print(f"La capital de {pais} es {capi}")