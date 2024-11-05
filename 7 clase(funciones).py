# FUNCIONES
# def "nombre funcion"(): syntaxis
def Juliana(nombre_1, nombre_2 ):
    print(nombre_1 + nombre_2)

Juliana('yon', 'juliana')

#ejemplo
def sum(primerN, segundoN):
    print(primerN + segundoN)
sum(24, 1)

#RETURN
def sum(primerN, segundoN = 5):
    print(primerN + segundoN)
    return primerN + segundoN
sum(24, 1)
sum(24, 4)
sum(24)