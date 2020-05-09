#limpiar pantalla antes de comenzar
import os
#comando para limpiar pantalla
os.system("cls") 

def mientras_while():
    n = int(input("Hasta que numero deseas listar: "))
    x = 1
    while x<=n:
        print(x)
        x = x + 1
        #x+=1

#funcion para teclear 10 numeros y calcular suma y promedio
def promedio():
    lista_valor = []
    x = 1
    suma = 0
    while x <= 10:
        valor = int(input("dato "+str(x)+": "))
        lista_valor.append(valor)
        suma = suma + valor
        x += 1
    
    #promedio
    promedio = suma/10
    #imprimir datos
    print("\n")
    y = 0
    while y < 5:
        #se utiliza el metodo "srt" porque mezclamos un valor entero con string y se debe coventir a string lo que esta en entero
        print(str(lista_valor[y]) +"\t"+ str(lista_valor[y+1]))
        y+=1
    
    print("\nSuma: "+str(suma))
    print("Promedio: "+str(promedio))
    
    

promedio()
print("\n")