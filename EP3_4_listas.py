print("3.4 Listas")

print()
print("3.4.1 Crear una lista")
numbers = [12, 7, 9, 3, 1]
print(numbers)

print()
print("3.4.2 Indexación de listas")
print("Primer elemento:", numbers[0])
print("Último elemento:", numbers[4])

numbers[0] = 200
print("Lista modificada:", numbers)

numbers[1] = numbers[4]
print("Copiando el quinto elemento al segundo:", numbers)

print()
print("3.4.3 Acceso y longitud")
print(numbers)
print("Longitud de la lista:", len(numbers))

print()
print("3.4.4 Eliminar elementos")
del numbers[1]
print("Lista después de eliminar:", numbers)
print("Nueva longitud:", len(numbers))

print()
print("3.4.5 Índices negativos")
print("Último elemento:", numbers[-1])
print("Penúltimo elemento:", numbers[-2])

print()
print("3.4.6 Fundamentos de listas")
shopping_list = ["pan", "leche", "huevos", "fruta", "agua"]
shopping_list[2] = input("Escribe un producto para reemplazar el tercero de la lista: ")
del shopping_list[-1]
print("Longitud de la lista:", len(shopping_list))
print(shopping_list)

print()
print("3.4.8 append() e insert()")
my_list = []

for i in range(5):
    my_list.append(i + 1)

print("Con append:", my_list)

my_list.insert(0, 100)
print("Con insert al inicio:", my_list)

print()
print("3.4.9 Recorrer lista y sumar")
my_list = [6, 2, 9, 4, 5]
total = 0

for i in my_list:
    total += i

print("Suma total:", total)

print()
print("3.4.10 Intercambiar elementos")
my_list = [6, 2, 9, 4, 5]
my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]
print("Lista invertida manualmente:", my_list)

print()
print("Invertir con for")
my_list = [6, 2, 9, 4, 5]
length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print("Lista invertida con for:", my_list)

print()
print("3.4.11 Serie favorita")
serie = []

serie.append("Temporada 1")
serie.append("Temporada 2")
serie.append("Temporada 3")

for i in range(2):
    nuevo_elemento = input("Agrega un elemento a la lista: ")
    serie.append(nuevo_elemento)

print("Lista actual:", serie)

del serie[3]
del serie[3]

serie.insert(0, "Inicio")
print("Lista final:", serie)

print()
print("Quiz de sección")

print()
print("Pregunta 1")
lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
del lst[0]
lst.append(1)
print(lst)

print()
print("Pregunta 2")
lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0

for number in lst:
    add += number
    lst_2.append(add)

print(lst_2)

print()
print("Pregunta 4")
lst = [1, [2, 3], 4]
print(lst[1])
print(len(lst))
