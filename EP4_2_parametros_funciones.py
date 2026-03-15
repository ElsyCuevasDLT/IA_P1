print("4.2 Parámetros en funciones")

print()
print("Función con un parámetro")

def message(number):
    print("Ingresa un número:", number)

message(2)
message(8)

print()
print("Variable y parámetro con el mismo nombre")

def show(number):
    print("Dentro de la función:", number)

number = 1234
show(9)
print("Fuera de la función:", number)

print()
print("Función con dos parámetros")

def message2(what, number):
    print("Ingresa", what, "número", number)

message2("folio", 11)
message2("precio", 5)

print()
print("Argumentos posicionales")

def my_function(a, b, c):
    print(a, b, c)

my_function(1, 2, 3)

print()
print("Argumentos con palabra clave")

def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

introduction(first_name="Elsy", last_name="Cuevas")
introduction(last_name="Ramírez", first_name="Laura")

print()
print("Mezcla de argumentos")

def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

adding(1, 2, 3)
adding(3, c=1, b=2)

print()
print("Valores por defecto")

def intro_default(first_name, last_name="López"):
    print("Hola, mi nombre es", first_name, last_name)

intro_default("Andrea")
intro_default("María", "Pérez")
intro_default(first_name="Diana")

print()
print("Dos valores por defecto")

def intro_full(first_name="Ana", last_name="López"):
    print("Hola, mi nombre es", first_name, last_name)

intro_full()
intro_full(last_name="Torres")

print()
print("Prueba de sección")

print()
print("Pregunta 1")
def intro(a="James Bond", b="Bond"):
    print("Mi nombre es", b + ".", a + ".")

intro()

print()
print("Pregunta 2")
def intro(a="James Bond", b="Bond"):
    print("Mi nombre es", b + ".", a + ".")

intro(b="Sean Connery")

print()
print("Pregunta 3")
def intro(a, b="Bond"):
    print("Mi nombre es", b + ".", a + ".")

intro("Susan")

print()
print("Pregunta 4")
print("def add_numbers(a, b=2, c):")
print("Ese código es incorrecto")
print("porque c no puede ir después de un parámetro con valor por defecto")
