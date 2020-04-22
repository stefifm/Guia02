____author___="Cátedra AED"

print("Precio de venta")
#Datos
precio_lista=float(input("Ingrese Precio de Lista: "))

#proceso
descuento=precio_lista*10/100
precio_contado=precio_lista-descuento
recarga=precio_lista*5/100
precio_tarjeta=precio_lista+recarga

#Resultado
print("Precio de contado es $", precio_contado)
print("Precio de tarjeta es $", precio_tarjeta)
