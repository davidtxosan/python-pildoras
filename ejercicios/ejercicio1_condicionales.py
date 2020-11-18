print("ejercicio numero mas alto")
numero1=int(input("introduce el primer numero :"))
numero2=int(input("introduce el segundo numero :"))
def DevuelveMax(num1,num2):
	if num1>num2:
		print(num1)
	elif num1<num2:
		print(num2)	
	else:
		print("los numeros son iguales")

print("el numero mas alto es: ")
DevuelveMax(numero1, numero2)