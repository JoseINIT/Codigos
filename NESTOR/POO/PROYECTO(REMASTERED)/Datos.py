from Personas import *
import pickle


class Datos:
    def __init__(self):
        self.lista = []

    def mostrar(self):
        print(len(self.lista))

    def agregar_lista(self, objeto):
        self.lista.append(objeto)

    def verificar(self, control):
        for persona in self.lista:
            if persona.id == control:
                print(f"La persona {persona.nombre} tiene el mismo N. de control, elige otro por favor, gracias.")
                return True
        return False

    def borrar(self, control):
        for i, persona in enumerate(self.lista):
            if persona.id == control:
                print(f"{persona.nombre} Ha sido removido con exito")
                print("-" * 50)
                self.lista.pop(i)
                return True
        return False

    def imprimirlista(self, opcion):

        if len(self.lista) > 0:
            if opcion == 1:
                print("------PROFESORES-----")
                for c in range(len(self.lista)):
                    if type(self.lista[c]) == Profesor:
                        print(self.lista[c].presentar())
            elif opcion == 2:
                print("------ADMINISTRATIVO-----")
                for c in range(len(self.lista)):
                    if type(self.lista[c]) == Administrativo:
                        print(self.lista[c].presentar())
            elif opcion == 3:
                print("------ESTUDIANTES-----")
                for c in range(len(self.lista)):
                    if type(self.lista[c]) == Estudiante:
                        print(self.lista[c].presentar())
            elif opcion == 4:
                print("------PROFESORES-----")
                for c in range(len(self.lista)):
                    if type(self.lista[c]) == Profesor:
                        print(self.lista[c].presentar())
                print("------ADMINISTRATIVO-----")
                for c in range(len(self.lista)):
                    if type(self.lista[c]) == Administrativo:
                        print(self.lista[c].presentar())
                print("------ESTUDIANTES-----")
                for c in range(len(self.lista)):
                    if type(self.lista[c]) == Estudiante:
                        print(self.lista[c].presentar())
        else:
            print("La Lista esta vacia")

    def cambiar_admin(self, control_a_cambiar):
        for persona in self.lista:
            if type(persona) == Administrativo:
                if control_a_cambiar == persona.id:
                    while True:
                        try:
                            opcion = int(input("ADMINISTRADORES\n"
                                               f"PERFIL DE {persona.nombre}\n"
                                               "[1] N. de control\n"
                                               "[2] Nombre \n"
                                               "[3] Sueldo\n"
                                               "[4] Departamento\n"
                                               "[5] Academia\n"
                                               "[6] Salir\n---"))
                        except ValueError:
                            print("Solo numeros añañin!")
                            break
                        if opcion == 1:
                            try:
                                control = int(input("Introduce el nuevo N. de control\n---"))
                                if self.verificar(control):
                                    continue
                            except ValueError:
                                print("Solo numeros añañin!")
                                break
                            persona.id = control
                        elif opcion == 2:
                            nombre1 = input("Introduce el nuevo nombre\n---")
                            persona.nombre = nombre1
                        elif opcion == 3:
                            try:
                                sueldo = int(input("Introduce el nuevo sueldo\n---"))
                            except ValueError:
                                print("Solo numeros añañin!")
                                break
                            persona.sueldo = sueldo
                        elif opcion == 4:
                            departamento = input("Introduce el nuevo departamento\n---")
                            persona.departamento = departamento
                        elif opcion == 5:
                            cargo = input("Introduce el nuevo cargo\n---")
                            persona.cargo = cargo
                        elif opcion == 6:
                            break
                        else:
                            print("opcion no valida")

    def cambiar_profesor(self, control_a_cambiar):
        for persona in self.lista:
            if type(persona) == Profesor:
                if control_a_cambiar == persona.id:
                    while True:
                        try:
                            opcion = int(input("PROFESORES\n"
                                               f"PERFIL DE {persona.nombre}\n"
                                               "[1] N. de control \n"
                                               "[2] Nombre \n"
                                               "[3] Sueldo \n"
                                               "[4] Departamento\n"
                                               "[5] Academia \n"
                                               "[6] Salir\n---"))
                        except ValueError:
                            print("Solo numeros añañin!")
                            break
                        if opcion == 1:
                            try:
                                control = int(input("Introduce el nuevo N. de control\n---"))
                                if self.verificar(control):
                                    continue
                            except ValueError:
                                print("Solo numeros añañin!")
                                break
                            persona.id = control
                        elif opcion == 2:
                            nombre1 = input("Introduce el nuevo nombre\n---")
                            persona.nombre = nombre1
                        elif opcion == 3:
                            try:
                                sueldo = int(input("Introduce el nuevo sueldo\n---"))
                            except ValueError:
                                print("Solo numeros añañin!")
                                break
                            persona.sueldo = sueldo
                        elif opcion == 4:
                            departamento = input("Introduce el nuevo departamento\n---")
                            persona.departamento = departamento
                        elif opcion == 5:
                            academia = input("Introduce la nueva academia\n---")
                            persona.academia = academia
                        elif opcion == 6:
                            break
                        else:
                            print("opcion no valida")

    def cambiar_estudiante(self, control_a_cambiar):
        for persona in self.lista:
            if type(persona) == Estudiante:
                if control_a_cambiar == persona.id:
                    while True:
                        try:
                            opcion = int(input("ESTUDIANTES\n"
                                               f"PERFIL DE {persona.nombre}\n"
                                               "[1] N. de control\n"
                                               "[2] Nombre\n"
                                               "[3] Carrera\n"
                                               "[4] Salir\n---"))
                        except ValueError:
                            print("Solo numeros añañin!")
                            break
                        if opcion == 1:
                            try:
                                control = int(input("Introduce el nuevo N. de control\n---"))
                                if self.verificar(control):
                                    continue
                            except ValueError:
                                print("Solo numeros añañin!")
                                break
                            persona.id = control
                        elif opcion == 2:
                            nombre1 = input("Introduce el nuevo nombre\n---")
                            persona.nombre = nombre1
                        elif opcion == 3:
                            carrera = input("Introduce la nueva carrera\n---")
                            persona.carrera = carrera
                        elif opcion == 4:
                            break
                        else:
                            print("opcion no valida")

    def Serializar(self):
        archivo = open("Datos", "wb")  # lo crea y Guarda la Informacion de la lista
        pickle.dump(self.lista, archivo)
        archivo.close()
        del archivo

    def DeSerializar(self):
        archivo = open("Datos", "rb")
        self.lista = pickle.load(archivo)
        archivo.close()
        del archivo
