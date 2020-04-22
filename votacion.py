____author___="Cátedra AED"

print("Votación en el congreso")

#datos
votos_favor=int(input("Ingrese votos a favor: "))
votos_contra=int(input("Ingrese votos en contra: "))
#proceso
total=votos_favor+votos_contra
porc_favor=votos_favor*100/total
porc_contra=votos_contra*100/total
#resultados
print("Porcentaje a favor", porc_favor)
print("Porcentaje en contra", porc_contra)
