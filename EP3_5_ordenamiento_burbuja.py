print("3.5 Ordenamiento de listas: algoritmo burbuja")

print()
print("Lista original")
my_list = [14, 3, 9, 1, 7]
print(my_list)

print()
print("Una pasada del algoritmo")
for i in range(len(my_list) - 1):
    if my_list[i] > my_list[i + 1]:
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)

print()
print("Burbuja completa")
my_list = [14, 3, 9, 1, 7]
swapped = True

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("Lista ordenada:", my_list)

print()
print("Usando sort()")
my_list = [14, 3, 9, 1, 7]
my_list.sort()
print(my_list)

print()
print("Usando reverse()")
lst = [2, 4, 1, 5, 3]
print("Original:", lst)
lst.reverse()
print("Invertida:", lst)

print()
print("Quiz de sección")

print()
print("Pregunta 1")
lst = ["M", "R", "A", "Z"]
lst.sort()
print(lst)

print()
print("Pregunta 2")
a = 5
b = 2
c = 4

lst = [a, c, b]
lst.sort()
print(lst)

print()
print("Pregunta 3")
a = "A"
b = "B"
c = "C"
d = " "

lst = [a, b, c, d]
lst.reverse()
print(lst)
