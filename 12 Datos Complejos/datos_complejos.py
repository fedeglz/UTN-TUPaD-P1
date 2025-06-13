#Ejercicio 1
precios_frutas = {'Banana' : 1200, 'Anana' : 2500, 'Melon' : 3000, 'Uva' : 1450}

#Añadir frutas
#Naranja = 1200
#manzana = 1500
#Pera = 2300

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)


#Ejercicio 2
#Actualizar precios de frutas
#Banana = 1330
#Manzana = 1700
#Melon = 2800

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800

print(precios_frutas)


#Ejercicio 3
#Lista de Frutas sin precio
frutas = list(precios_frutas.keys())
print(f"Lista de frutas: {frutas}")


#Ejercicio 4
#Agenda tele
agenda = {}
for i in range(5):
    nombre = input("Ingrese el nombre: ")
    telefono = input("Ingrese el numero de telefono: ")
    agenda[nombre] = telefono

buscar = input("Ingrese el nombre a buscar: ")
if buscar in agenda:
    print(f"El numero es: {agenda[buscar]}")
else:
    print("No se encontro el nombre en la agenda")


#Ejercicio 5
frase = input("Ingrese una frase: ")
palabras = frase.lower().split()
palabras_unicas = set(palabras)
contador_palabras = {}

for palabra in palabras:
    contador_palabras[palabra] = contador_palabras.get(palabra, 0) + 1

print(f"Palbaras unicas: {palabras_unicas}")
print(f"Contador de palabras: {contador_palabras}")


#Ejercicio 6
alumnos = {}
for _ in range(3):
    nombre = input("Nombre del alumno: ")
    notas = []
    for i in range(1,4):
        nota = float(input(f"Ingrese la nota {i} de {nombre}: "))
        notas.append(nota)
    promedio = sum(notas) / len(notas)
    alumnos[nombre] = promedio

for alumno, prom in alumnos.items():
    print(f"El promedio de {alumno} es: {prom:.2f}")


#Ejercicio 7
parcial1 = {"Ana", "Luis", "Carlos", "Marta"}
parcial2 = {"Luis", "Pedro", "Marta", "Lucia"}

print("Ambos parciales:", parcial1 & parcial2)
print("Solo uno de los dos:", parcial1.symmetric_difference(parcial2))
print("Al menos uno:", parcial1 | parcial2)


#Ejercicio 8
stock = {"lapiz": 10, "goma": 5}
producto = input("Producto a consultar: ").lower()
if producto in stock:
    agregar = int(input("Cuántas unidades querés agregar?: "))
    stock[producto] += agregar
else:
    nuevo_stock = int(input("Producto nuevo. Cantidad inicial: "))
    stock[producto] = nuevo_stock
print("Stock actualizado:", stock)


#Ejercicio 9
agenda_eventos = {
    ("Lunes", "09:30"): "Reunión",
    ("Martes", "16:00"): "Clase",
}
dia = input("Ingresá el día: ")
hora = input("Ingresá la hora: ")
evento = agenda_eventos.get((dia, hora), "No hay eventos")
print("Evento:", evento)


#Ejercicio 10
paises = {"Argentina": "Buenos Aires", "Perú": "Lima", "Francia": "París", "España": "Madrid"}
capitales = {capital: pais for pais, capital in paises.items()}
print("Diccionario invertido:", capitales)
