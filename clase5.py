print("Ángulos solo en grados, minutos y segundos")

#Datos
grados= int(input("Ingrese ángulo en grados: "))
minutos= int(input("Ingrese ángulo en minutos: "))
segundos= int(input("Ingrese ángulo en segundos: "))

#proceso
minutos_grados=minutos/60
segundos_grados=segundos/3600
angulo_grados=grados+minutos_grados+segundos_grados

grados_min=grados*60
seg_min=segundos/60
angulo_min=minutos+grados_min+seg_min

grados_seg=grados*3600
min_seg=minutos*60
angulo_seg=segundos+grados_seg+min_seg

#resultado
print("Angulo grados es:", angulo_grados)
print("Angulo en minutos es:", angulo_min)
print("Angulo en segundos es:", angulo_seg)
