temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(temperatura-32)*(5/9) for temperatura in temperatura_fahrenheit]
print(grados_celsius)