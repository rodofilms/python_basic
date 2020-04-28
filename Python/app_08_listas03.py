'''
    Metodos split y join, dividir y juntar ... estos son metodos de la clase cadena, no de la lista
'''
lista = ["Godzilla es poderoso"]
print(lista)

lista = ["Godzilla es poderoso".split()]
print(lista)
#ahora probamos usando una cadena sin espacios y usando la "," como delimitador
lista = ["Godzilla,es,poderoso".split(",")]
print(lista)
#como podemos ver nos genera la misma lista que formamos arriba usando el espacio como delimitador
#el metodo split nos sirve para separar una cadena dependiendo de su delimitador, es cual podemos definir pasandolo como parametro a split

cadena = "godzilla es: "
lista_cadena = ["poderoso","como","el","sol"]
print(cadena+", ".join(lista_cadena))

#el metodo join usa la lo que escribamos en la cadena anterior, como delimitador para juntar la lista

''' MOSTRAR INDICES '''
#Mostramos el indice del caracter que queramos de una cadena o lista
print(cadena.index(":"))
print(lista_cadena.index("el"))