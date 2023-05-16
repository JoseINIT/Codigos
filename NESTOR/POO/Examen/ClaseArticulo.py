class Articulo:
    def __init__(self, codigo, descripcion, precio_unitario, existencia):
        self.codigo = codigo
        self.descripcion = descripcion
        self.precio_unitario = precio_unitario
        self.existencia = existencia
    def imprimir(self):
        importelapiz = self.precio_unitario * self.existencia
        print(f"el codigo es {self.codigo}, a descripcion es {self.descripcion},el precio unitario es {self.precio_unitario}"
              f",hay en existencia {self.existencia} y el importe es {importelapiz}")
    def Lapiz(self):
        importelapiz=self.precio_unitario*self.existencia
        return (f"el codigo es {self.codigo}, a descripcion es {self.descripcion},el precio unitario es {self.precio_unitario}"
                f",hay en existencia {self.existencia} y el importe es {importelapiz}")

    def Plumas(self):
        importeplumas=self.precio_unitario*self.existencia
        return (f"el codigo es {self.codigo},la descripcion es {self.descripcion}, el precio unitario es {self.precio_unitario}"
                f", hay en existencia {self.existencia} y el importe es {importeplumas}")

    def Cuadernos(self):
        importecuadernos=self.precio_unitario*self.existencia
        return (f"el codigo es {self.codigo},la descripcion es {self.descripcion},el precio unitario es {self.precio_unitario}"
                f",hay en existencia {self.existencia} y el importe es {importecuadernos}")