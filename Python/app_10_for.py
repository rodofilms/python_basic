#Se utilizara un ciclo for para recorrer toda la lista y ademas usaremos las funciones break y 
#continue para romper nuestro ciclo cuando lo requieramos

lista_numeros = [1,"dos",3,4,"cinco",6]

for numero in lista_numeros:
    if numero == 3:
        #break
        continue
    print(numero)

'''
    Ahora haremos un ejercicio para utilizar los ciclos
    * recorreremos una cadena que contenga las vocales y las imprimiremos cada una en mayusculas
'''

def mayusculas_for():
    cadena = "aeiou"
    for letra in cadena:
        print(letra.upper())
    print("Ya se imprimieron todas las vocales")
    
def mayusculas_while():
    '''
    cadena = ["a","e","i","o","u"]
    x = len(cadena)
    while x > 0:
        print(cadena[x-1].upper())
        x -=1
    '''
    vocales=["a","e","i","o","u"]
    x=0
    while x <5:
        print(vocales[x].upper())
        x+=1
    print("Ya no hay más vocales")

#llamar a las funciones
print("\n")
mayusculas_for()
print("\n")
mayusculas_while()