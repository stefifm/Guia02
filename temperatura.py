print("Temperaturas en deposito quimico")

#datos
T1=int(input("Cargue Temperatura 1: "))
T2=int(input("Cargue Temperatura 2: "))
T3=int(input("Cargue Temperatura 3: "))
#proceso
prom1=(T1+T2+T3)/3
prom2=(T1+T2+T3)//3
#resultados
print("Promedio decimal: ",prom1)
print("Promedio entero: ",prom2)
