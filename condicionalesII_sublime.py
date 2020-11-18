print("testeo de la edad")
nota_alumno=int(input("Introduce tu nota,por favor : "))

if nota_alumno<5:
	print("has suspendido")
elif nota_alumno<6:
	print("suficiente")
elif nota_alumno<7:
	print("bien")
elif nota_alumno<9:
	print("notable")
elif nota_alumno<=10:
	print("sobresaliente")
else:
	print("nota incorrecta")

print("el programa ha finalizado")