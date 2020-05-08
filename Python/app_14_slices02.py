#limpiar pantalla antes de comenzar
import os
#comando para limpiar pantalla
os.system ("cls") 

numeros = [1,2,3,4,5,6,7,8,9,10,11,25,87,68,15,23,47]
print(str(numeros)+"\n")

# ahora vamos a eliminar los elementos "1,2,3" y los elemtos "8,9,10"

del numeros[0:4]
print(str(numeros)+"\n")
del numeros[3:6]
print(str(numeros)+"\n")

# ahora vamos a volver a colocar los elementos "8,9,10" en el mismo lugar donde estaban

numeros[2:3] = [8,9,10]
print(str(numeros)+"\n")

# ahora vamos a remplazar los elementos "15,23" por "80,80"

numeros[9:11] = [80,80]
print(str(numeros)+"\n")