"""class Persona:
    def __init__(self,persona,edad):
        self.persona=persona
        self.edad=edad
    def saluda(self,otra_persona):
        return f"Hola {otra_persona.nombre}, me llamo {self.persona} "
#uso
david=Persona("david",12)
marta=Persona("marta",12)
david.saluda(marta)"""
class Persona:
    def __init__(self, persona, edad):
        self.persona = persona
        self.edad = edad

    def saluda(self, otra_persona):
        return f"Hola {otra_persona.persona}, me llamo {self.persona}"


# uso
david = Persona("David", 12)
marta = Persona("Marta", 12)
print(david.saluda(marta))  # Hola Marta, me llamo David
