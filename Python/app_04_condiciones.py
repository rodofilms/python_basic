#Entrada de datos
nota1=int(input("Ingrese primer nota:"))
nota2=int(input("Ingrese segunda nota:"))
nota3=int(input("Ingrese tercer nota:"))
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