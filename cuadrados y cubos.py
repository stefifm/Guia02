____author___="Cátedra AED"

print("Cuadrados y cubos")

#datos
num1=int(input("Ingrese numero 1: "))
num2=int(input("Ingrese numero 2: "))
#procesos
suma=(2*num1**2)+(num2**2**2)
suma_cuadrado=suma-(4*num1**2-num2**2)
prom_cubos=num1**3+num2**3/3
#resultados
print("Suma de los cuadrados es: ",suma_cuadrado)
print("Promedio de los cubos es: ", prom_cubos)
