print("3.1 Cómo tomar decisiones en Python")

print()
print("3.1.1 Preguntas y respuestas")
print("Python puede comparar valores y responder con True o False.")

print()
print("Operador de igualdad ==")
print(4 == 4)
print(4 == 4.0)
print(3 == 7)

print()
print("Operador de desigualdad !=")
var = 0
print(var != 0)

var = 2
print(var != 0)

print()
print("Operador mayor que >")
print(9 > 3)
print(2 > 8)

print()
print("Operador mayor o igual que >=")
print(6 >= 6)
print(4 >= 9)

print()
print("Operador menor que <")
print(1 < 5)
print(8 < 4)

print()
print("Operador menor o igual que <=")
print(2 <= 2)
print(9 <= 1)

print()
print("Guardar respuestas en variables")
answer = 12 >= 7
print(answer)

print()
print("3.1.7 Condiciones y ejecución condicional")
x = 10

if x == 10:
    print("x es igual a 10")

if x > 5:
    print("x es mayor que 5")

if x < 10:
    print("x es menor que 10")
else:
    print("x no es menor que 10")

print()
print("if - else")
edad = 20

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print()
print("if - elif - else")
calificacion = 88

if calificacion >= 90:
    print("A")
elif calificacion >= 80:
    print("B")
elif calificacion >= 70:
    print("C")
else:
    print("Reprobado")

print()
print("Comparar 3 números")
number1 = 14
number2 = 9
number3 = 21

largest_number = number1

if number2 > largest_number:
    largest_number = number2

if number3 > largest_number:
    largest_number = number3

print("El número más grande es:", largest_number)

print()
print("Ejemplo con cadenas")
bebida = "café"

if bebida == "CAFÉ":
    print("Sí, así está escrita completamente en mayúsculas.")
elif bebida == "café":
    print("La palabra está escrita en minúsculas.")
else:
    print("Se escribió otra bebida:", bebida)

print()
print("Ejemplo de año bisiesto")
year = 2024

if year < 1582:
    print("No entra en el periodo del calendario gregoriano")
elif year % 4 != 0:
    print("Año común")
elif year % 100 != 0:
    print("Año bisiesto")
elif year % 400 != 0:
    print("Año común")
else:
    print("Año bisiesto")
