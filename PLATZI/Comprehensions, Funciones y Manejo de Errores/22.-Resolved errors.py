import colorama
"""try:
    print(0/0)
except ZeroDivisionError as error:
    print(error)
try:
    assert 1!=1, "uno no es igual a uno"
except AssertionError as error:
    print(error)
print("hola")
age=10
try:
    if age < 18:
        raise Exception("no se permiten menores de edad")
except Exception as exo:
    print(exo)"""
#En un solo bloque
try:
    print(0/0)
    #aqui deja de correr despues de capturar el primer error
    assert 1 != 1, "uno no es igual a uno"
    age=10
    if age<18:
        raise Exception ("No se permiten menores de edad")
except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print(error)
except Exception as error:
    print(error)
print("hola mundo")