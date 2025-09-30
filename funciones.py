# Sección de las funciones
def suma(a, b):
	resultado = a + b
	return resultado

def resta(a, b):
	res = a - b
	return res

def max(num1, num2):
	if num1 > num2:
		maximo = num1
	else:
		maximo = num2
	return maximo
	

# Sección para el programa principal
#Llamando a la función
numero1 = 5
numero2 = 3
# Las variables pertenecen al contexto donde fueron creadas
a = 1000
b = 5000
resultado_suma = suma(numero1, numero2)
print(f"{numero1} + {numero2} = {resultado_suma}")
print(suma(9898,564))
suma(45, 78)

res_resta = resta(a, b)
print(res_resta)
	
print(max(56,98))

texto = "La Universidad Pontificia Bolivariana se encuentra en el barrio Laureles de Medellín"
x = texto.find("Laureles")
print = (x)