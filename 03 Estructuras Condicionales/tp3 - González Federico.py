#González Federico
#34605567

#Ejercicio 1
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad")


#Ejercicio 2
nota = int(input("Ingrese su nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Reprobado")


#Ejercicio 3
numero = int(input("Ingrese un numero Par : "))

if numero % 2 == 0:
    print("Ha ingresado un numero Par")
else:
    print("Por favor ingresa un numero Par")


#Ejercicio 4
edad = int(input("Ingrese un edad: "))

if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")


#Ejercicio 5
contrasenia = input("Ingrese una contraseña: ")

if len(contrasenia) >= 8 and len(contrasenia) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor ingrese una contraseña entre 8 a 14 caracteres")


#Ejercicio 6
import random
from statistics import mode, median, mean

numero_aleatorio = [random.randint(1, 100) for i in range(50)]

moda = mode(numero_aleatorio)
mediana = median(numero_aleatorio)
media = mean(numero_aleatorio)

if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("El número aleatorio tiene una distribución normal")


#Ejercicio 7
frase = input("Ingrese una frase o palabra: ")
ultimo_caracter = frase[-1].lower()

if ultimo_caracter in "a e i o u":
    resultado = frase + "!" 
    print(resultado) 
else:
    print(frase)


#Ejercicio 8
nombre = input("Ingrese su nombre: ")
numero = input("Ingrese una opcion (1, 2, 3)")

if numero == "1":
    nombre_transformado = nombre.upper()
elif numero == "2":
    nombre_transformado = nombre.lower()
elif numero == "3":
    nombre_transformado = nombre.title()
else:
    nombre_transformado = "Opcion invalida"
    print("Ingrese una opcion valida (1, 2, 3)")

print(nombre_transformado)



#Ejercicio 9
magnitud = float(input("Ingrese la magnitud del trerremoto: "))

if magnitud < 3:
    categoria = "Muy leve (imperceptible)"
elif magnitud >= 3 and magnitud < 4:
    categoria = "Leve (perceptible)"
elif magnitud >= 4 and magnitud < 5:
    categoria = "Moderado (sentido por personas, pero generalmente no causa daños)"
elif magnitud >= 5 and magnitud < 6:
    categoria = "Fuerte (puede causar daños en estructuras debiles)"
elif magnitud >= 6 and magnitud < 7:
    categoria = "Muy fuerte (causa daños significativos)"
else:
    categoria = "Extremo (puede causar grandes daños a gran escala)"

print (f"La magnitud {magnitud} en la escala de Ritcher es clasificada como: {categoria}")


#Ejercicio 10
hemisferio = input("Ingrese en que hemisferio se encuentra N/S: ")
mes = int(input("Ingrese el mes (1 - 12)"))
dia = int(input("Ingrese el dia (1 - 31)"))

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes == 1 and dia <= 20) or (mes == 2 and dia <= 20) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 20) or (mes == 5 and dia <= 20) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 20) or (mes == 8 and dia <= 20) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (mes == 10 and dia <= 20) or (mes == 11 and dia <= 20) or (mes == 12 and dia <= 20):
        estacion = "Otoño"
    else:
        estacion = "Fecha invalida"

elif hemisferio == "S":
        if (mes == 6 and dia >= 21) or (mes == 7 and dia <= 20) or (mes == 8 and dia <= 20) or (mes == 9 and dia <= 20):
            estacion = "Invierno"
        elif (mes == 9 and dia >= 21) or (mes == 10 and dia <= 20) or (mes == 11 and dia <= 20) or (mes == 12 and dia <= 20):
            estacion = "Primavera"
        elif (mes == 12 and dia >= 21) or (mes == 1 and dia <= 20) or (mes == 2 and dia <= 20) or (mes == 3 and dia <= 20):
            estacion = "Verano"
        elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 20) or (mes == 5 and dia <= 20) or (mes == 6 and dia <= 20):
            estacion = "Otoño"
        else:
            estacion = "Fecha inválida"
else:
    estacion = "Hemisferio invalido"
print (f"La estacion en el hemisferio {hemisferio} es: {estacion}")

