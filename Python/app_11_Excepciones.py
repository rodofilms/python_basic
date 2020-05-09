# Aprenderemos el manejo de excepciones, para ello practicaremoa con una suma de datos

#limpiar pantalla antes de comenzar
import os
#comando para limpiar pantalla
os.system("cls") 

# Estrunctura try catch tipica 
try:
    n1 = int(input("Dame un numero: "))
    n2 = int(input("Dame otro numero: "))
except ValueError as identifier:
    print("Ese no es un numero")
else:
    suma = n1 + n2
    print("La suma es: "+ str(suma))

