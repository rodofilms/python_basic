#manegar las listas en python

''' 
    El metodo append sirve para agregar un dato a la lista
'''
lista = [1,2,3,4]
#imprimir el contenido de la lista
print(lista)
#agregadar datos a la lista usando moda tradicional
lista = lista + [5,6]
print(lista)
#agregar datos a la lista usando metodos de python
lista.append(7)
print(lista)
#agregar dato de tipo string
lista.append("ocho")
#dato de tipo lista, es decir agregar una lista dentro de otra lista
lista.append([9,10])

print(lista)