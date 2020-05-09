#limpiar pantalla antes de comenzar
import os
#comando para limpiar pantalla
os.system("cls") 

calificaciones = {"Kevin":8,"Rodrigo":9,"Rodolfo":10,"Jesus":10,"Uriel":8}
print("\tLista orginal sin modificaciones\n"+str(calificaciones)+"\n")

'''
    Para mostrar los datos de una lista no hace falta realizar ningun ciclo, pero estos mismos pueden llegar
    a requerirse cuando queremos ordenar los datos, modificar los datos cuando la lista sea grande, etc.
    La forma para recorrerlos seria asi:
'''
# Este ciclo solo nos imprime las llavaes de los elementos o items de la lista
for x in calificaciones:
    print(x)

# De esta manera nos puede imprir el contenido de los elemetos sin las llaves
for x in calificaciones:
    print(calificaciones[x])

print("\n*********** ********** ************ ************** *********\n")
# Pero las formas anteriores son incorrectas ya que pueden representar un potencial peligro al momento de
# utilizarlas en un proyecto de grande, ya que la impresion no esta condicionada y podria confundir, por lo
# que se utilizan los siguientes metodos para condicionar lo que nosotros queremos que se nos muestre en
# pantalla. Por ejemplo, yo mostrare primero todas la llaves, luego el contenido de los elementos y por 
# ultimo todo el item o elemento de la lista, incluyendo su correspondiente llave.

for key in calificaciones.keys():
    # la variable key almacena solo las llaves de la lista
    print(key)
print("\n")
for value in calificaciones.values():
    # la variable value almacena los valores de cada item, sin su llave
    print(value)
print("\n")
for item in calificaciones.items():
    # la variable item almacena todo todo el elemento de la lista, incluyendo su llave
    print(item)
print("\n")