#SETS

mi_set = {}
print(type(mi_set))

mi_set = {'mi', 'amor', 'te', 'amo'}
print(type(mi_set))

print(mi_set)
# print(mi_set[0]) tipo de error por que no tienen orden

mi_set.add('amor') #no acepta valores repetidos
print(mi_set) 

mi_set.add('juliana') # si se añadio el nuevo objeto
print(mi_set)

mi_set1 = {'mi', 'amor', 'te', 'amo'}

#funciones
mi_set.difference_update(mi_set1) #diferencia entre stes
print(mi_set)


