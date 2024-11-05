#CLASES

class amor:
    def __init__(self, nombre, tiempo, edad):
        self.nombre = nombre
        self.tiempo = tiempo
        self.edad = edad

    def amor(self):
        print(f'la primera persona esta enamorada de {self.nombre} ')

Persona1 = amor('juliana', 4, 18 )
persona2 = amor('yon', 4, 20)

print(f'la primera persona se llama {Persona1.nombre}, llevan en meses {Persona1.tiempo}, encontro al amor de su vida a la edad de {Persona1.edad}' )
print(f'la primera persona se llama {persona2.nombre}, llevan en meses {persona2.tiempo}, encontro al amor de su vida a la edad de {persona2.edad}' )



Persona1.amor()
persona2.amor()


        



