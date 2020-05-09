import os
os.system("cls")

# Tuplas, son listas que no se pueden editar, ni eliminar, pero podemos darle uso de manera adecuada

tupla_01 = (1,2,3)
print(tupla_01)

# si eliminar un valor de la dupla nos dara error
# pero si dentro de una dupla metemos una lista, esta podemos editarla

tupla_02 = (1,"hola",[0,1,2,3])
print("\n"+str(tupla_02))

# como podemos ver, en este caso si podemos editar los valores de una tupla, debido a que estamos editando la lista dentro de la tupla, no la tupla en si
tupla_02[2][0] = "inicio"
print("\n"+str(tupla_02))