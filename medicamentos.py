____author___="Cátedra AED"

print("Precio de medicamentos")

#datos
medicamento=float(input("Ingrese precio de medicamento $"))
#procesos
descuento=medicamento*35/100
precio_final=medicamento-descuento
#resultados
print("Pecio actual $", medicamento)
print("Monto del descuento $", descuento)
print("Monto final a pagar $", precio_final)
