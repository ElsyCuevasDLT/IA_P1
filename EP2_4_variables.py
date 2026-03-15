print("2.4 Variables")

print()
print("2.4.1 Variables - espacios para guardar datos")
print("Una variable permite guardar información para usarla después.")
print("Cada variable tiene un nombre y un valor.")

print()
print("2.4.2 Nombres de variables")
print("Reglas básicas:")
print("Deben comenzar con una letra o con guion bajo.")
print("Pueden incluir letras, números y guion bajo.")
print("No deben tener espacios.")
print("No pueden ser palabras reservadas.")
print("Python distingue entre mayúsculas y minúsculas.")

print()
print("Ejemplos de nombres correctos:")
print("mi_variable")
print("contador")
print("total_ventas")
print("_dato")
print("m101")

print()
print("Ejemplos de nombres incorrectos:")
print("101")
print("mi variable")
print("for")

print()
print("2.4.3 Cómo crear una variable")
var = 1
print("Se creó la variable var con el valor:")
print(var)

print()
print("2.4.4 Cómo usar una variable")
x = 12
y = 6
print("Valor de x:")
print(x)
print("Valor de y:")
print(y)
print("Suma de x + y:")
print(x + y)

print()
print("Combinar texto con variables")
version = "3.12.3"
print("Versión de Python: " + version)

print()
print("2.4.5 Cómo asignar un nuevo valor a una variable")
var = 1
print("Valor inicial de var:")
print(var)

var = var + 1
print("Nuevo valor de var después de sumarle 1:")
print(var)

print()
var = 50
var = 150 + 250
print("Nuevo valor de var:")
print(var)

print()
print("2.4.6 Resolver un problema matemático simple")
print("Teorema de Pitágoras")
a = 5.0
b = 12.0
c = (a ** 2 + b ** 2) ** 0.5
print("a =", a)
print("b =", b)
print("c =", c)

print()
print("2.4.7 LAB Variables")
libros = 4
cuadernos = 7
lapices = 9

print("Cantidad de útiles:")
print(libros, cuadernos, lapices)

total_utiles = libros + cuadernos + lapices
print("Total de útiles:")
print(total_utiles)

print("Número total de útiles:", total_utiles)

print()
print("Operaciones con variables")
print("libros + cuadernos =")
print(libros + cuadernos)

print("lapices - libros =")
print(lapices - libros)

print("cuadernos * 2 =")
print(cuadernos * 2)

print("lapices / 3 =")
print(lapices / 3)

print("lapices // 3 =")
print(lapices // 3)

print()
print("2.4.8 Operadores abreviados")
x = 5
print("Valor inicial de x:")
print(x)

x += 4
print("x += 4")
print(x)

x -= 3
print("x -= 3")
print(x)

x *= 2
print("x *= 2")
print(x)

x /= 3
print("x /= 3")
print(x)

print()
pendientes = 8
print("Pendientes al inicio:")
print(pendientes)

pendientes += 1
print("Pendientes después de += 1")
print(pendientes)

print()
print("2.4.9 LAB Variables: convertidor simple")
miles = 5.25
kilometers = miles * 1.61
print(miles, "millas son", round(kilometers, 2), "kilómetros")

kilometers = 18.40
miles = kilometers / 1.61
print(kilometers, "kilómetros son", round(miles, 2), "millas")

print()
print("2.4.10 LAB Operadores y expresiones")
x = 0.0
y = 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1
print("x =", x)
print("y =", y)

print()
x = 1.0
y = 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1
print("x =", x)
print("y =", y)

print()
x = -1.0
y = 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1
print("x =", x)
print("y =", y)

print()
print("2.4.12 Cuestionario de sección")

print()
print("Pregunta 1")
var = 2
var = 3
print(var)

print()
print("Pregunta 3")
a = '2'
b = "2"
print(a + b)

print()
print("Pregunta 4")
a = 8
b = 2
a /= 2 * b
print(a)
