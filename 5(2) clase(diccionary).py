# DICCIONARIOS

mi_diccionary= {'nombre' : 'juliana',  
                'Situacion': 'casada no oficial con yon', 
                '¿hasta cuando?': 'para siempre'}
print(type(mi_diccionary))

print(mi_diccionary['nombre'])
print(mi_diccionary['Situacion'])
print(mi_diccionary['¿hasta cuando?'])

#FUNCIONES DICT
print(mi_diccionary.keys()) #imprime todas las llaves
print(mi_diccionary.values()) #imprime todos los valores

#se puede cambiar de dict a lista o a tupla
mi_diccionary = list(mi_diccionary)
print(type(mi_diccionary))