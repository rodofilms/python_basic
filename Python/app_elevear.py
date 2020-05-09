#limpiar pantalla antes de comenzar
import os
#comando para limpiar pantalla
os.system("cls") 

num = int(input("Dame un numero: "))
pot = int(input("\nPotencia para elevar: "))

x = 0
resultado = 1

while x < pot:
    resultado = resultado * num
    x = x + 1

print("\n\tResultado: "+str(resultado)+"\n")