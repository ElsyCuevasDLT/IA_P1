print("4.1 Funciones")

print()
print("4.1.1 ¿Por qué necesitamos funciones?")
print("Las funciones ayudan a reutilizar código.")
print("También hacen que el programa sea más ordenado y fácil de leer.")

print()
print("Ejemplo sin función")
print("Ingresa un valor:")
print("Ingresa un valor:")
print("Ingresa un valor:")

print()
print("4.1.4 Tu primera función")

def message():
    print("Ingresa un valor:")

print("Inicio del programa.")
print("Fin de la introducción.")

print()
print("Invocando la función")
print("Inicio del programa.")
message()
print("Fin del bloque.")

print()
print("Llamando la función varias veces")
message()
message()
message()

print()
print("4.1.5 Cómo funcionan las funciones")
print("Python ejecuta la función solo cuando se invoca.")

def hello():
    print("Hola")

hello()

print()
print("Función mezclada con código normal")
print("Comienza aquí.")

def saludo():
    print("Este mensaje viene desde una función")

saludo()
print("Termina aquí.")

print()
print("Usando una función para evitar repetir código")

def pedir_valor():
    print("Por favor, ingresa un valor:")

pedir_valor()
a = 10
print("a =", a)

pedir_valor()
b = 20
print("b =", b)

pedir_valor()
c = 30
print("c =", c)

print()
print("Valores finales")
print(a, b, c)

print()
print("Función con un parámetro")

def hi(name):
    print("Hola,", name)

hi("Elsy")
hi("Python")

print()
print("Prueba de sección")

print()
print("Pregunta 1")
print("input() es una función integrada")

print()
print("Pregunta 2")
print("Llamar una función antes de definirla produce NameError")

print()
print("Pregunta 3")
print("Llamar una función con argumentos incorrectos produce TypeError")
