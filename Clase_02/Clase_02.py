#Desafio Listas

'''
Crea dos listas lista_1 y lista_2, con cualquier elemento que quieras. 
Realiza los siguientes puntos usando las funciones integradas ya vistas y el método slice [ : ] Imprime la lista correspondiente luego de cada punto.
Añade a la lista_1 el <int> 456789 y luego el <str> "Hola Mundo"
Luego añade a la lista_2 el <str> "Hola y adiós", y luego el <int> 5555
Genera una lista_3 con todos los elementos de la lista_1 sin considerar el último elemento [:]
Genera una lista_4 con todos los elementos de la lista_2 menos el primero y el último elemento [:]
Finalmente, genera una lista_5 con los elementos de la lista_4 y de la lista_3
'''



lista_1 = [1, 2, 3] #creo una lista con 3 elementos
lista_2 = ['a', 'b', 'c'] #creamos una lista con 3 elementos

lista_1.append(456789) #agrego un elemento a la lista
lista_1.append("Hola Mundo")#agrego un elemento a la lista
print(lista_1)#imprimo la lista

lista_2.append("Hola y adiós")#agrego un elemento a la lista
lista_2.append(5555)#
print(lista_2)#

lista_3 = lista_1[:-1]#creo una lista con todos los elementos de la lista_1 sin considerar el último elemento
print(lista_3)#imprimo la lista

lista_4 = lista_2[1:-1]#creo una lista con todos los elementos de la lista_2 menos el primero y el último elemento
print(lista_4)#

lista_5 = lista_4 + lista_3#creo una lista con los elementos de la lista_4 y de la lista_3
print(lista_5)#imprimo la lista


#Desafio Tuplas

''' Descripción de la actividad. 
A partir de una variable llamada tupla, imprimir por pantalla de forma ordenada, lo siguiente:

El último ítem de tupla
El número de ítems de tupla
La posición donde se encuentra el ítem 87 de tupla
Una lista con los últimos tres ítems de tupla
Un ítem que haya en la posición 8 de tupla
El número de veces que el ítem 7 aparece en tupla

Copia esta tupla para iniciar el ejercicio:
tupla = (8, 15, 4, 39, 5, 89, 87, 19, 7, -755, 88, 123, 2, 11, 15, 9, 355) '''

tupla = (8, 15, 4, 39, 5, 89, 87, 19, 7, -755, 88, 123, 2, 11, 15, 9, 355)

print("El último ítem de tupla:", tupla[-1])
print("El número de ítems de tupla:", len(tupla))
print("La posición donde se encuentra el ítem 87 de tupla:", tupla.index(87))
print("Una lista con los últimos tres ítems de tupla:", list(tupla[-3:]))
print("Un ítem que haya en la posición 8 de tupla:", tupla[8])
print("El número de veces que el ítem 7 aparece en tupla:", tupla.count(7))


#FIN
