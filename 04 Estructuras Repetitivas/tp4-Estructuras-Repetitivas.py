# Ejercicio 1

for i in range(101):
    print(i)

# Ejercicio 2
num = input("Ingrese un nro entero: ")
contador = 0

for i in num:
    if i.isdigit():
        contador += 1
print(f"El numero {num} contiene {contador} digitos")

# Ejercicio 3
num1 = int(input("Ingrese el 1er valor: "))
num2 = int(input("Ingrese el 2do valor: "))
suma = 0

if num1 > num2:
    num1, num2 == num2, num1
    
for i in range(num1 + 1, num2):
    suma += i
print(f"La suma entre {num1} y {num2} es: {suma}")


# Ejercicio 4
print("Ingrese un numero entero para sumar. Ingrese el 0 para finalizar")
suma = 0
while True:
    num = int(input("Ingrese un numero entero: "))
    if num == 0:
        break

    suma += num
print(f"La suma acumulada es: {suma}")


# Ejercicio 5
import random

print ("Elige un nro entre 0 y 9, e intenta adivinarlo!")
nro_aleatorio = random.randint(0,9)
intentos = 0

while True:
    intento = int(input("Ingresa un nro: "))
    intentos += 1

    if intento < 0 or intento > 9:
        print("Por favor, ingresa un número entre 0 y 9.")
    elif intento < nro_aleatorio:
        print("Demasiado bajo. Intenta de nuevo.")
    elif intento > nro_aleatorio:
        print("Demasiado alto. Intenta de nuevo.")
    else:
        print(f"¡Felicidades! Has adivinado el número {nro_aleatorio} en {intentos} intentos.")
        break


# Ejercicio 6
for num in range(100, -1, -1):
    if num % 2 == 0:
        print(num)


# Ejercicio 7
num = int(input("Ingrese un numero entero: "))

if num < 0:
    print("Por favor ingrese un nro entero positivo: ")
else:
    suma = 0

    for i in range(1, num + 1):
        suma += i
        
    print(f"La suma entre 0 y {num} es: {suma}")


# Ejercicio 8
cant_nro = 100
contador_pares = 0
contador_impares = 0
contador_negativos = 0
contador_positivos = 0

print(f"Ingrese {cant_nro} números enteros:")

for i in range(cant_nro):
    numero = int(input(f"Número {i + 1}: "))    
    
    if numero % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1
    
    
    if numero < 0:
        contador_negativos += 1
    elif numero > 0:
        contador_positivos += 1


print(f"Números pares: {contador_pares}")
print(f"Números impares: {contador_impares}")
print(f"Números negativos: {contador_negativos}")
print(f"Números positivos: {contador_positivos}")


# Ejercicio 9
cant_nro = 100
suma = 0

print(f"Ingrese {cant_nro} números enteros:")

for i in range(cant_nro):
    numero = int(input(f"Número {i + 1}: "))
    suma += numero  

media = suma / cant_nro

print(f"La media de los {cant_nro} números ingresados es: {media}")


# Ejercico 10
num = input("Ingrese un numero entero: ")
num_invertido = num[::-1]
print(f"El nro invertido es: {num_invertido}")