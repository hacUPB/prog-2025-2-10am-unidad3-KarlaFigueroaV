print("Ingresa tu nombre y apellido")
nombre = input ()
print("Bienvenido: ")
print(nombre)
#Opción 2
print("Bienvenido: ", nombre)
#Calcular el IMC de esa persona
#Leer peso, altura
peso = input ("Ingresa tu peso en kg: ")
peso = float(peso)
altura = input ("Ingresa tu talla en metros: ")
altura = float(altura)
#Cálculos
imc = peso/altura**2
#Mostrar imc
print("Tu IMC = ", imc)
