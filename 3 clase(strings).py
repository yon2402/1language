# strings = texto

mi_primer_string = 'mi amor te amo' # con comillas simples
mi_segundo_string = "mi amor te extraño" # con comillas dobles

# se puede concatenar

print( mi_primer_string , mi_segundo_string )
print(f'te amo mi niña {mi_segundo_string} <3' )


# string con diferentes variable

other_string = 'teamooo'
j,u,l,i,a,n,a = other_string
print(j)

# funciones
print(mi_primer_string.upper())
print(mi_primer_string.capitalize())
print(mi_primer_string.lower())
print(len (mi_primer_string))
print(mi_primer_string.find('j')) #aparece -1 por que no hay
print(mi_primer_string.count('o'))
print(mi_primer_string.upper().isupper()) #varias funciones 