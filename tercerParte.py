#tercera parte: descuentos por cantidad.
n=0
fecha=''
tb=5.0
costtal=0.0

#solicitud de datos al usuario:
n=int(input('Ingresa la cantidad de boletas a comprar:' ))
fecha=input("La boleta es para finde semana?(si o no)")
# condicional para fecha:
if fecha=='si':
  costtal=tb*1.20
else:
  costtal=tb

#Proceso segun elección de Palco:
palco=input("Escribe A, B, C, según el palco:")
if palco=='A':
  costtal+=tb*.1  #costtal= costtal + tb*.1
elif palco=='B':
  costtal+=tb*.05

#proceso de descuentos por cantidad boletas
if n>=5 and n<=10:
  costtal=costtal*.9
print("El costo total a pagar:", round(costtal*n,2))