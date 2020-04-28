#manegar las listas en python

''' 
    El metodo "extend" sirve para agrandar una lista con un dato
    EL metodo "remove" sirve para remover un dato de una lista
'''

lista = [1]
lista.append(2)

#esto agrega otra lista mas, no solo agrega los datos
#lista.append([3,4])
#esto si agrega datos a la lista ya existente pero es mejor manejar los metodos definidos por python
#lista += [3,4]

lista.extend(["tres",4])

print(lista)

#metodo para eliminar datos de lista
lista.remove("tres")

print(lista)