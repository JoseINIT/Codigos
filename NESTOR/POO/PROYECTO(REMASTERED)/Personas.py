class Persona:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre


class Estudiante(Persona):
    def __init__(self, id, nombre, carrera):
        super().__init__(id, nombre)
        self.carrera = carrera

    def presentar(self):
        return f"ID: {self.id} | Nombre: {self.nombre} | Carrera: {self.carrera}"


class Empleado(Persona):
    def __init__(self, id, nombre, sueldo, departamento):
        super().__init__(id, nombre)
        self.sueldo = sueldo
        self.departamento = departamento


class Administrativo(Empleado):
    def __init__(self, id, nombre, sueldo, departamento, cargo):
        super().__init__(id, nombre, sueldo, departamento)
        self.cargo = cargo

    def presentar(self):
        return f"ID: {self.id} | Nombre: {self.nombre} | Sueldo: {self.sueldo} | Departamento: {self.departamento} | " \
               f"Cargo: {self.cargo}"


class Profesor(Empleado):
    def __init__(self, id, nombre, sueldo, departamento, academia):
        super().__init__(id, nombre, sueldo, departamento)
        self.academia = academia

    def presentar(self):
        return f"ID: {self.id} | Nombre: {self.nombre} | Sueldo: {self.sueldo} | Departamento: {self.departamento} | " \
               f"Academia: {self.academia}"
