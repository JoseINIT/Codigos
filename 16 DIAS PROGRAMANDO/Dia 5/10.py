def todos_positivos(lista):
    for n in lista:
        if n>0:
            return True
        else:
            pass
    return False
print(todos_positivos([400,200,-122]))