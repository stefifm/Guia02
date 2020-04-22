print("enfermos en un país")

#datos
c_pais=int(input("Cantidad total de enfermos:"))
c_ciudad=int(input("Personas en una ciudad: "))
#procesos
p_ciudad=c_ciudad*100/c_pais
#resultados
print("Porcentaje de enfermos en una ciudad en el país: ", p_ciudad)
