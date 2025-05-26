# Ejercicio 1
def factorial_recursivo(x):
    return 1 if x == 0 else x * factorial_recursivo(x - 1)

def mostrar_factorial():
    num = int(input("Introduce un número para calcular su factorial: "))
    
    if num < 1:
        print("El número debe ser mayor o igual a 1.")
        return
    
    for i in range(1, num + 1):
        print(f"El factorial de {i} es: {factorial_recursivo(i)}")

if __name__ == "__main__":
    mostrar_factorial()


# Ejercicio 2
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
def mostrar_fibonacci():
    num = int(input("Introduce un número para calcular su serie de Fibonacci: "))
    
    if num < 0:
        print("El número debe ser mayor o igual a 0.")
        return
    
    for i in range(num + 1):
        print(f"Fibonacci({i}) = {fibonacci(i)}")

if __name__ == "__main__":
    mostrar_fibonacci()


# Ejercicio 3
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
    
def mostrar_potencia():
    base= int(input("Introduce la base: "))
    exponente = int(input("Introduce el exponente: "))

    if exponente < 0:
        print("El exponente debe ser mayor o igual a 0.")
        return
    print(f"{base} elevado a {exponente} es: {potencia(base, exponente)}")
if __name__ == "__main__":
    mostrar_potencia()


# Ejercicio 4
def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"    
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
    
def mostrar_decimal_a_binario():
    num = int(input("Introduce un número decimal: "))
    
    if num < 0:
        print("El número debe ser mayor o igual a 0.")
        return
    print(f"El número {num} en binario es: {decimal_a_binario(num)}")

if __name__ == "__main__":
    mostrar_decimal_a_binario()


# Ejercicio 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

def polindromo():
    palabra = input("Ingrese una palabra sin espacios y sin tildes: ").lower()
    
    if es_palindromo(palabra):
        print(f"La palabra '{palabra}' es un palíndromo.")
    else:
        print(f"La palabra '{palabra}' no es un palíndromo.")

if __name__ == "__main__":
    polindromo()


# Ejercicio 6
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)
    
def mostrar_suma_digitos():
    num = int(input("Introduce un número entero positivo: "))

    if num < 0:
        print("El número debe ser mayor o igual a 0.")
        return mostrar_suma_digitos()
    else:
        print(f"La suma de los dígitos de {num} es: {suma_digitos(num)}")

if __name__ == "__main__":
    mostrar_suma_digitos()


# Ejercicio 7
def contar_bloques(n):
    if n == 0:
        return 0
    else:
        return 1 + contar_bloques(n - 1)
    
def calculo_bloques():
    bloques = int(input("Ingrese la cantidad de bloques: "))

    if bloques < 1:
        print("La cantidad de bloques debe ser mayor o igual a 1.")
        return calculo_bloques()
    else:
        print(f"La cantidad de bloques necesarios para construir una pirámide con {bloques} bloques es: {contar_bloques(bloques)}")

if __name__ == "__main__":
    calculo_bloques()


# Ejercicio 8
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    elif numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)
    
def mostrar_cant_veses():
    numero = int(input("Ingrese un número entero positivo: "))
    digito = int(input("Ingrese el dígito a contar (0-9): "))

    if numero < 0 or not (0 <= digito <= 9):
        print("El número debe ser positivo y el dígito debe estar entre 0 y 9.")
        return mostrar_cant_veses()
    else:
        cantidad = contar_digito(numero, digito)
        print(f"El dígito {digito} aparece {cantidad} veces en el número {numero}.")

if __name__ == "__main__":
    mostrar_cant_veses()

