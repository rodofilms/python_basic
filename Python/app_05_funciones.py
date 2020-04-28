#Entrada de datos
nota1=int(input("Ingrese primer nota: "))
nota2=int(input("Ingrese segunda nota: "))
nota3=int(input("Ingrese tercer nota: "))
#print solo para dar estitica al programa
print("\n")

def suma(nota1,nota2,nota3):
    suma = nota1 + nota2 + nota3
    #imprimir datos
    print(str(suma)+"\n")

def promedio(nota1,nota2,nota3):
    #Calcular promedio
    prom=(nota1+nota2+nota3)/3

    #Ejersicio para probar los diferentes tipos de condiciones
    if nota1 == 1 or nota2 == 1 or nota3 == 1:
        print("Reprobado por materia")
    elif prom>=7:
        print("Promocionado")
    else:
        if prom>=4:
            print("Regular")
        else:
            print("Reprobado")

suma(nota1,nota2,nota3)
promedio(nota1,nota2,nota3)