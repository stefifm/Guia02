print("Convertir Ángulo segundos a sexagesimal")

#datos
angulo_seg=int(input("Ingrese ángulo en segundos:"))

#proceso
grados=angulo_seg//3600
resto_grados=angulo_seg%3600
minutos=resto_grados//60
segundos=resto_grados%60

#resultados
print("Ángulo sexagesimal es:", grados,"º", minutos, "'", segundos, '"')
