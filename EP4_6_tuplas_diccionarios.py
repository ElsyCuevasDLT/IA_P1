print("4.6 Tuplas y diccionarios")

print()
print("4.6.1 Tipos de secuencia y mutabilidad")
print("Las listas son mutables")
print("Las tuplas son inmutables")

print()
print("4.6.2 Tuplas")
tuple_1 = (2, 4, 6, 8)
tuple_2 = 1.0, 1.5, 2.0, 2.5

print(tuple_1)
print(tuple_2)

print()
print("Tupla vacía")
empty_tuple = ()
print(empty_tuple)

print()
print("Tupla de un solo elemento")
one_element_tuple_1 = (1,)
one_element_tuple_2 = 1.,
print(one_element_tuple_1)
print(one_element_tuple_2)

print()
print("Acceso a elementos de una tupla")
my_tuple = (5, 10, 15, 20)
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:3])

print()
print("Recorrer una tupla")
for elem in my_tuple:
    print(elem)

print()
print("Operaciones con tuplas")
print(len(my_tuple))
print(my_tuple + (25,))
print((1, 2, 3) * 3)
print(10 in my_tuple)
print(30 not in my_tuple)

print()
print("Intercambio de tuplas")
var = 123
t1 = (1,)
t2 = (2,)
t3 = (3, var)

t1, t2, t3 = t2, t3, t1
print(t1, t2, t3)

print()
print("4.6.3 Diccionarios")
dictionary = {"rojo": "red", "azul": "blue", "verde": "green"}
phone_numbers = {"casa": 3312345678, "trabajo": 3323456789}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

print()
print("Acceso a valores del diccionario")
print(dictionary["rojo"])
print(phone_numbers["trabajo"])

print()
print("Uso de in y not in")
words = ["rojo", "amarillo", "verde"]

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "no está en el diccionario")

print()
print("4.6.4 Métodos de diccionarios")
for key in dictionary.keys():
    print(key, "->", dictionary[key])

print()
for spanish, english in dictionary.items():
    print(spanish, "->", english)

print()
for english in dictionary.values():
    print(english)

print()
print("Modificar valores")
dictionary["rojo"] = "dark red"
print(dictionary)

print()
print("Agregar nuevas claves")
dictionary["negro"] = "black"
print(dictionary)

dictionary.update({"blanco": "white"})
print(dictionary)

print()
print("Eliminar claves")
del dictionary["azul"]
print(dictionary)

dictionary.popitem()
print(dictionary)

print()
print("Ordenar claves")
for key in sorted(dictionary.keys()):
    print(key, "->", dictionary[key])

print()
print("4.6.5 Tuplas y diccionarios juntos")
school_class = {}

school_class["Ana"] = (9, 8, 10)
school_class["Luis"] = (7, 9, 8)

for name in sorted(school_class.keys()):
    total = 0
    counter = 0
    for grade in school_class[name]:
        total += grade
        counter += 1
    print(name, ":", total / counter)

print()
print("Prueba de sección")

print()
print("Pregunta 1")
my_tup = (1, 2, 3)
print(my_tup[2])

print()
print("Pregunta 2")
tup = 1, 2, 3
a, b, c = tup
print(a * b * c)

print()
print("Pregunta 3")
tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)
print(duplicates)

print()
print("Pregunta 4")
d1 = {"Andrea Ruiz": "A", "María Soto": "B+"}
d2 = {"Luisa Torres": "A", "Paola Díaz": "C"}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)

print()
print("Pregunta 5")
my_list = ["car", "Ford", "flower", "Tulip"]
t = tuple(my_list)
print(t)

print()
print("Pregunta 6")
colors = (("green", "#008000"), ("blue", "#0000FF"))
colors_dictionary = dict(colors)
print(colors_dictionary)

print()
print("Pregunta 7")
my_dictionary = {"A": 1, "B": 2}
copy_my_dictionary = my_dictionary.copy()
my_dictionary.clear()
print(copy_my_dictionary)

print()
print("Pregunta 8")
colors = {
    "blanco": (255, 255, 255),
    "gris": (128, 128, 128),
    "rojo": (255, 0, 0),
    "verde": (0, 128, 0)
}

for col, rgb in colors.items():
    print(col, ":", rgb)
