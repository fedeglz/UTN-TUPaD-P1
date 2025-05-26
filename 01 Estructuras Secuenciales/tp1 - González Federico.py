# González Federico
#34605567


#Ejercicio 1
print("Hola Mundo")

#Ejercicio 2
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

#Ejercicio 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar_residencia = input("Ingrese su lugar de residencial: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}")

#Ejercicio 4
radio_circulo = float(input("Ingrese su radio del circulo: "))
pi = 3.14159
area = pi * radio_circulo * radio_circulo
perimetro = 2 * radio_circulo * pi
print(f"El área del circulo es: {area}")    
print(f"El perimetro del circulo es: {perimetro}")

#Ejercicio 5
segundo = int(input("Ingrese los segundos: "))
minutos = segundo // 60
segundo_restante = segundo % 60
print(f"{segundo} segundos equivalen a {minutos} minutos y {segundo_restante} segundos")

#Ejercicio 6
num = input("Ingrese un numero: ")
for i in range(0 , 10):
    print(f"{num} x {i} = {int(num) * i}")

#Ejercicio 7
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if (num1 != 0 and num2 != 0):
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} / {num2} = {num1 / num2}")
    print(f"{num1} x {num2} = {num1 * num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
else:
    print("Error: Ingrese un numero distinto de 0.")

#Ejercicio 8
peso = float(input("Ingrese su peso: "))
altura = int(input("Ingrese su altura: "))
imc = peso / altura

print(f"su Indice de Masa Corporal es de {imc}")

#Ejercicio 9
celcius = float(input("Ingrese la temperatura en grados celcius: "))
fahrenheit = (celcius * 9/5) + 32
print (f"{celcius} grados C es = a {fahrenheit} grados F")

#Ejercicio 10
num1 = int(input("Escriba el primer número: "))
num2 = int(input("Escriba el segundo número: "))
num3 = int(input("Escriba el tercer número: "))
promedio = (num1 + num2 + num3) / 3

print(f"El promedio de los tres números es: {promedio}")



