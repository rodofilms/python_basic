#Sentencia para dar entrada a los datos a travez del teclado
'''lado=input("Ingrese la medida del lado del cuadrado:")'''
#Sentencia para convertir los datos del teclado en numeros enteros
'''lado=int(lado)'''
#las sentencias anteriores se pueden remplazar por esta
lado = int(input("Ingrese la medida del lado del cuadrado, en datos enteros: "))

#Calculo del problema
superficie=lado*lado
print("La superficie del cuadrado es:"+" "+ str(superficie))

#las variables de python pueden cambiar de tipo de dato sin previo aviso
superficie = "hola"
print(superficie)