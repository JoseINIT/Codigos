class cAlumno(object):
    def imprimir(self):
        print(self.control)
        print(self.nombre)



    def __init__(self, texto,elnombre):
        self.control = texto
        self.nombre= elnombre
        """@AttributeType string"""