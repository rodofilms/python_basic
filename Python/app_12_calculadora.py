''' Este es un mini proyecto, para poner en práctica los conocimientos de todas las unidades vistas hasta ahora '''

#limpiar pantalla antes de comenzar
import os
#comando para limpiar pantalla
os.system ("cls") 

###############################################################################
#Variables Globales
bandera = True

#Funciones del proyecto
def restar():
    n1 = int(input("Dame el primer numero: "))
    n2 = int(input("Dame el segundo numero: "))
    resta = n1 - n2
    print("\nEl resultado es: "+str(resta))
    print("\n")

def multiplicar():
    n1 = int(input("Dame el primer numero: "))
    n2 = int(input("Dame el segundo numero: "))
    producto = n1 * n2
    print("\nEl resultado es: "+str(producto))
    print("\n")

def dividir():
    n1 = int(input("Dame el primer numero: "))
    n2 = int(input("Dame el segundo numero: "))
    dividir = n1 / n2
    print("\nEl resultado es: "+str(dividir))
    print("\n")

def sumar():
    n1 = int(input("Dame el primer numero: "))
    n2 = int(input("Dame el segundo numero: "))
    suma = n1 + n2
    print("\nEl resultado es: "+str(suma))
    print("\n")


print("Bienvenido a la Calculadora")
print("Estas son las operaciones que puede realizar: \n")

while bandera != False:
    print("1 - Suma\n2 - Resta")
    print("3 - Multiplicar\n4 - Dividir")
    print("5 - Salir\n")

    try:
        entrada = int(input("Que operacion realizara: "))
    except ValueError as identifier:
        print("\nEse no es un numero\n")
    else:
        if entrada == 1:
            os.system ("cls")
            sumar()
        elif entrada == 2:
            os.system ("cls")
            restar()
        elif entrada == 3:
            os.system ("cls")
            multiplicar()
        elif entrada == 4:
            os.system ("cls")
            dividir()
        elif entrada == 5:
            bandera = False
            break
        else:
            print("\Operación no Valida\n")
            break
        
