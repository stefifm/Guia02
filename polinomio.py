____author___="Cátedra AED"

print("Polinomio de segundo grado")

#datos
a=int(input("Ingrese valor de a: "))
b=int(input("Ingrese valor de b: "))
c=int(input("Ingrese valor de c: "))
x=int(input("Ingrese valor de x: "))
#proceso
polinomio_x=(a*x**2)+(b*x)+c
discriminante=(b**2)-(4*a*c)
#resultados
print("Valor del polinomio en el punto X: ", polinomio_x)
print("Discriminante es: ", discriminante)

