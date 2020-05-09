#limpiar pantalla antes de comenzar
import os
#comando para limpiar pantalla
os.system("cls") 

'''
    En esta seccion veremos como utilizar diccionarios en python, ya que son listas comunes pero con un indicador visible
    en cada elemento, para ubicar rapidamente los elementos de la lista.
'''
# Vamos a declarar un lista comun para notar la diferencia
lista_comun_calificaciones = [10,9,8,5]
print(str(lista_comun_calificaciones)+"\n")
# Vamos a declarar una lista con diccionario
lista_diccionario_calificaciones = {"Rodolfo":10,"Kevin":9,"Adrian":8,"Nike":5}
print(str(lista_diccionario_calificaciones)+"\n")
# En esta forma podemos visualizar cualquier elemento de la lista, ya que solo tenemos que poner su indicador
# para que podamos visualizarlo. Ejemplo, veremos la calificacion de Kevin 
print(str(lista_diccionario_calificaciones["Kevin"])+"\n")
# Ahora vamos a cambiar la calificacion de Kevin por un 7
lista_diccionario_calificaciones["Kevin"] = 7
print(str(lista_diccionario_calificaciones)+"\n")

'''
    Al igual que las listas, los diccionarios tienen un metodo para ser creados, el cual
    se llama "dict()"
'''

lista_calificaciones_nueva = dict([["Kevin",7],["Maria",10],["Manuel",8],["luis",10]])
print(str(lista_calificaciones_nueva)+"\n")

###########################################################################################
print("###########################################################################################\n")
'''
    Tambien en las listas diccionarios podemos usar las funciones de eliminar y actualizar
    "del" y "update"
'''
del lista_calificaciones_nueva["Maria"]
print(str(lista_calificaciones_nueva)+"\n")
# Actualizamos la calificacion de kevin y al mismo tiempo actualizamos la lista agregando otro elemento
lista_calificaciones_nueva.update({"Kevin":10,"Emanuel":10})
print(str(lista_calificaciones_nueva)+"\n")
