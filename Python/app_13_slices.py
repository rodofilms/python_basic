#los Slices sirven para trabajar por rebadas algunas partes de codigo de python
#Por Ejemplo: En un lista tenemos un idice que nos indica la posicion de los elementos de la lista,
#por lo cual podemos recorrerlas usando una variable como indice para recorrer los elementos de la lista,
#pero con con los slices podemos recorrer los elementos de la lista y tambien hacerlo a trozos / rebanadas

#limpiar pantalla antes de comenzar
import os
#comando para limpiar pantalla
os.system ("cls") 


''' Creamos una lista para empezar con el ejemplo '''

numeros = [0,1,2,3,4,5,6,7,8,9,10]
print(numeros)

# mostramos un elemento de la lista de forma convencional
print(numeros[4])

# ahora mostraremos un rango de elementos en la lista usando un slice 
print(numeros[2:5])

# ahora mostraremos un rango de elementos en la lista usando un slice pero usando saltos entre ellas
print(numeros[2:9:2])

''' 
    Ahora una aclaracion, los slices tienen inicio y fin asi como tambien los pasos que este da
    es decir podemos mostrar un rango determinado de elementos y condicionarlos para que estos 
    se muestren de 2 en 2, 3 en 3, etc.
'''