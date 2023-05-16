from Datos import *
from pathlib import Path

lista = Datos()


def buscar_persona():
    while True:
        try:
            opcion = int(input("-----BUSCAR PERSONA-----\n"
                               "[1] PROFESORES\n"
                               "[2] ADMINISTRATIVO\n"
                               "[3] ESTUDIANTES\n"
                               "[4] Consulta General\n"
                               "[5] Salir\n---"))
        except ValueError:
            print("Solo numeros añañin!")
            opcion = 0
        lista.imprimirlista(opcion)
        if opcion == 5:
            break
        try:
            otra = int(input("Desea buscar una persona otra vez?\n"
                             "[1] Si\n"
                             "[Cualquier otra tecla] No\n---"))
        except ValueError:
            print("Solo numeros añañin!")
            otra = None
        if otra == 1:
            print("Ingresa datos")
            print("-" * 50)
        else:
            break


def estudiante():
    while True:
        try:
            control = int(input("Introduce tu N. de control\n---"))
            if lista.verificar(control):
                continue
        except ValueError:
            print("Solo numeros añañin!")
            break
        nombre = input("Introduce tu nombre\n---")
        carrera = input("Introduce tu carrera\n---")
        estud = Estudiante(control, nombre, carrera)
        try:
            guardar = int(input("¿Quieres guardar el estudiante?\n"
                                "[1] Si\n"
                                "[Cualquier otro numero] No\n---"))
            print("-" * 50)
        except ValueError:
            print("Solo numeros añañin!")
            guardar = 0
        if guardar == 1:
            lista.agregar_lista(estud)
            print("Se guardo el estudiante")
            print("-" * 50)
        else:
            print("No se guardo el estudiante.")
        try:
            otro = int(input("¿Quieres guardar otro?\n"
                             "[1] Si\n"
                             "[Cualquier otro numero] No\n---"))
            print("-" * 50)
        except ValueError:
            print("Solo numeros añañin!")
            otro = 0
        if otro != 1:
            break


def profesor():
    while True:
        try:
            control = int(input("Introduce tu N. de control\n---"))
            if lista.verificar(control):
                continue
        except ValueError:
            print("Solo numeros añañin!")
            continue
        nombre = input("Introduce tu nombre\n---")
        try:
            sueldo = int(input("Introduce tu sueldo\n---"))
        except ValueError:
            print("Solo numeros añañin!")
            continue
        departamento = input("Introduce tu departamento\n---")
        academia = input("Introduce tu academia\n---")
        prof = Profesor(control, nombre, sueldo, departamento, academia)
        try:
            guardar = int(input("¿Quieres guardar el profesor?\n"
                                "[1] Si\n"
                                "[Cualquier otro numero] No\n---"))
            print("-" * 50)
        except ValueError:
            print("No se registro el profesor!")
            print("-" * 50)
            break
        if guardar == 1:
            lista.agregar_lista(prof)
            print("Se guardo el profesor")
            print("-" * 50)
        else:
            print("No se guardo el profesor.")
        try:
            otro = int(input("¿Quieres guardar otro?\n"
                             "[1] Si\n"
                             "[Cualquier otro numero] No\n---"))
            print("-" * 50)

        except ValueError:
            print("Solo numeros añañin!")
            continue
        if otro != 1:
            break


def administracion():
    while True:
        try:
            control = int(input("Introduce tu N. de control\n---"))
            if lista.verificar(control):
                continue
        except ValueError:
            print("Solo numeros añañin!")
            break
        nombre = input("Introduce tu nombre\n---")
        try:
            sueldo = int(input("Introduce tu sueldo\n---"))
        except ValueError:
            print("Solo numeros añañin!")
            break
        departamento = input("Introduce tu departamento de trabajo\n---")
        cargo = input("Introduce tu cargo\n---")
        admin = Administrativo(control, nombre, sueldo, departamento, cargo)
        try:
            guardar = int(input("¿Quieres guardar el personal administrativo??\n"
                                "[1] Si\n"
                                "[Cualquier otro numero] No\n---"))
            print("-" * 50)
        except ValueError:
            print("Solo numeros añañin!")
            break
        if guardar == 1:
            lista.agregar_lista(admin)
            print("Se guardo el administrativo")
            print("-" * 50)
        else:
            print("No se guardo el administrativo.")
        try:
            otro = int(input("¿Quieres guardar otro?\n"
                             "[1] Si\n"
                             "[Cualquier otro numero] No\n---"))
            print("-" * 50)
        except ValueError:
            print("Solo numeros añañin!")
            break
        if otro != 1:
            break


def bajas():
    while True:
        try:
            opcion = int(input("-----BAJAS-----\n"
                               "[1] Dar de baja\n"
                               "[2] Salir\n---"))
        except ValueError:
            break
        if opcion == 1:
            try:
                control_a_eliminar = int(input("Numero de control a eliminar\n---"))
                if lista.borrar(control_a_eliminar):
                    pass
            except ValueError:
                print("Solo numeros añañin!")
            else:
                print("El N. de control no se encuentra")
                print("-" * 50)
        elif opcion == 2:
            break
        try:
            otra = int(input("Desea dar de baja otra vez?\n"
                             "[1] Si\n"
                             "[Cualquier otra tecla] No\n---"))
        except ValueError:
            print("Solo numeros añañin!")
            continue
        if otra == 1:
            print("Ingresa datos")
        else:
            break


def altas():
    while True:
        try:
            op = int(input("-----ALTAS-----\n"
                           "[1] Estudiante\n"
                           "[2] Profesor\n"
                           "[3] Administrativo\n"
                           "[4] Salir\n---"))
        except ValueError:
            print("Solo numeros añañin!")
            op = 5
        if op == 1:
            print("----ESTUDIANTE----")
            estudiante()
        if op == 2:
            print("----PROFESOR----")
            profesor()
        if op == 3:
            print("----ADMINISTRATIVO----")
            administracion()
        elif op == 4:
            break


def cambios():
    while True:
        try:
            opcion_a_cambiar = int(input("-----CAMBIOS-----\n"
                                         "[1] Administrativo\n"
                                         "[2] Profesor\n"
                                         "[3] Estudiante\n"
                                         "[4] Salir\n---"))
        except ValueError:
            print("Solo numeros añañin!")
            opcion_a_cambiar = 0
        if opcion_a_cambiar == 1:
            control_a_cambiar = int(input("Introduce el N. de control a cambiar\n---"))
            lista.cambiar_admin(control_a_cambiar)
        elif opcion_a_cambiar == 2:
            control_a_cambiar = int(input("Introduce el N. de control a cambiar\n---"))
            lista.cambiar_profesor(control_a_cambiar)
        elif opcion_a_cambiar == 3:
            control_a_cambiar = int(input("Introduce el N. de control a cambiar\n---"))
            lista.cambiar_estudiante(control_a_cambiar)
        elif opcion_a_cambiar == 4:
            break
        else:
            print("Opcion no valida")
            continue
        try:
            otra = int(input("Desea buscar una hacer otro cambio otra vez?\n"
                             "[1] Si\n"
                             "[Cualquier otra tecla] No\n---"))
        except ValueError:
            print("Solo numeros añañin!")
            otra = None
        if otra == 1:
            print("Ingresa datos")
        else:
            break


def main():
    numero = 0
    if Path('Datos').is_file():  # verifica si el archivo existe
        lista.DeSerializar()  # recupera la inforamcion de la lista
    else:
        print('Es la primera ves se creara al fian el Archivo Binario DatosNestor')
    while numero != 5:
        lista.mostrar()
        try:
            numero = int(input("*****Menu Principal*****\n"
                               "[1] Altas\n"
                               "[2] Bajas\n"
                               "[3] Cambios\n"
                               "[4] Consultas\n"
                               "[5] Salir\n---"))
        except ValueError:
            print("Solo numeros añañin!")
        if numero != 5:
            if numero == 1:
                altas()

            elif numero == 2:
                bajas()

            elif numero == 3:
                cambios()

            elif numero == 4:
                buscar_persona()

            else:
                print("Opcion no valida")

        else:
            lista.Serializar()
            print("Salir de la aplicacion")


if __name__ == "__main__":
    main()
