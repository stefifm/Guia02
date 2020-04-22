____author___="Cátedra AED"

print("Rinde de un campo agrícola")

#datos
largo=int(input("Ingrese largo de parcela: "))
ancho=int(input("Ingrese ancho de la parcela: "))
#proceso
area_parcela=largo*ancho
rinde=area_parcela*2/10
#resultado
print("Quintales para producir", rinde)
