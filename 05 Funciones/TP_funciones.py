#Ejercicio 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()


#Ejercicio 2
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre_usuario = input("ingresa su nombre: ")
saludo = saludar_usuario(nombre_usuario)
print(saludo)


#Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su residencia: ")

informacion = informacion_personal(nombre, apellido, edad, residencia)
print(informacion)


#Ejercicio 4
import math

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)
def perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = int(input("Ingrese el radio: "))

cal_area = calcular_area_circulo(radio)
cal_perm = perimetro_circulo(radio)
print(f"El Area del circulo es: {cal_area}")
print(f"El Perimetro del circulo es: {cal_perm}")


#Ejercicio 5
def segundos_a_horas(segundos):
    hora = segundos / 3600
    return hora

seg = int(input("Ingrese los segundos: "))
horas = segundos_a_horas(seg)
print(f"{seg} segundos, son {horas} horas")


#Ejercicio 6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

num_usuario = int(input("Ingrese un numero: "))
tabla_multiplicar(num_usuario)


#Ejercicio 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    mult = a * b
    div = a / b
    return(suma, resta, mult, div)

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
resultado = operaciones_basicas(num1, num2)

print(f"La suma entre {num1} y {num2} = {resultado[0]}")
print(f"La resta entre {num1} y {num2} = {resultado[1]}")
print(f"La multiplicacion entre {num1} y {num2} = {resultado[2]}")
print(f"La division entre {num1} y {num2} = {resultado[3]}")


#Ejercicio 8
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

p = float(input("Ingrese su peso: "))
a = float(input("Ingrese su altura: "))
resultado = calcular_imc(p,a)

print(f"Su IMC es: {resultado}")


#Ejercicio 9
def celcius_a_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

celc = float(input("Ingrese la temperatura en gragos Celcius: "))
fahrenheit = celcius_a_fahrenheit(celc)
print(f"{celc} grados Celcius son {fahrenheit} grados Fahrenheit.")


#Ejercicio 10
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

num1 = float(input("Ingrese el primer numaro: "))
num2 = float(input("Ingrese el segundo numaro: "))
num3 = float(input("Ingrese el tercero numaro: "))

prom = calcular_promedio(num1, num2, num3)
print(f"El promedio de {num1}, {num2} y {num3} es: {prom}")