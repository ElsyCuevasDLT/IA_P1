print("2.6 Interacción con el usuario")

print()
print("La función input() permite recibir datos del usuario.")

print()
nombre = input("Escribe tu nombre: ")
print("Hola", nombre)

print()
print("Ejemplo simple con input")
anything = input("Escribe algo: ")
print("Anotado:", anything)

print()
print("El resultado de input() es una cadena")
numero = input("Ingresa un número: ")
print("El valor ingresado fue:", numero)

print()
print("Conversión de tipos")

numero = input("Ingresa un número para elevarlo al cuadrado: ")
numero = int(numero)
print("El cuadrado es:", numero ** 2)

print()
print("Uso de float()")

num = float(input("Ingresa un número decimal: "))
print("El número multiplicado por 2 es:", num * 2)

print()
print("Concatenación de cadenas con +")

nombre = input("Vuelve a escribir tu nombre: ")
print("Bienvenida " + nombre)

print()
print("Replicación de cadenas con *")

texto = input("Escribe una palabra: ")
print(texto * 3)

print()
print("LAB simple de operaciones")

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

print("Suma =", a + b)
print("Resta =", a - b)
print("Multiplicación =", a * b)
print("División =", a / b)

print()
print("Ejemplo de conversión a cadena con str()")

edad = 21
print("Tengo " + str(edad) + " años")
