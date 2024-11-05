# LISTAS
mi_lista = [ 'amor' ,24,False,6,'te', 'amo', 'amo', 'amo']
print(type(mi_lista))

print(mi_lista)
print(mi_lista[0]) #imprimir 1 solo valor

#funciones a la lista
mi_lista.append('niña') #agregar objeto
print(mi_lista)

mi_lista.insert(1, 'te adoro')#agregar objeto en una posicion       
print(mi_lista)

mi_lista.remove(24) #remover un pnjeto
print(mi_lista)

mi_lista.pop(2) #remover un objeto utiliando la poscion 
print(mi_lista)

print(mi_lista.pop(2)) #nos devuelve lo que se borro
print(mi_lista)

print(mi_lista.count('amo'))

mi_lista.reverse()#lista al reves
print(mi_lista)

mi_lista.clear() #limpiar o dejar vacia la lista
print(mi_lista)