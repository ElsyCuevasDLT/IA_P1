print("3.2 Bucles en Python")

print()
print("3.2.1 Bucle while")
counter = 3
while counter > 0:
    print("Dentro del while:", counter)
    counter -= 1
print("Fuera del while")

print()
print("Contar pares e impares")
odd_numbers = 0
even_numbers = 0

number = 1
while number <= 6:
    if number % 2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1
    number += 1

print("Impares:", odd_numbers)
print("Pares:", even_numbers)

print()
print("3.2.2 while con número mayor")
largest_number = -999999999
numbers = [8, 13, 2, 27, -1]
i = 0

while numbers[i] != -1:
    if numbers[i] > largest_number:
        largest_number = numbers[i]
    i += 1

print("El número más grande es:", largest_number)

print()
print("3.2.5 Bucle for")
for i in range(5):
    print("Valor de i:", i)

print()
print("range con inicio y fin")
for i in range(3, 9):
    print(i)

print()
print("range con tres argumentos")
for i in range(1, 10, 4):
    print(i)

print()
print("Potencias de 3")
power = 1
for expo in range(5):
    print("3 ^", expo, "=", power)
    power *= 3

print()
print("3.2.8 break")
for letter in "python":
    if letter == "h":
        break
    print(letter)

print()
print("continue")
for letter in "python":
    if letter == "h":
        continue
    print(letter)

print()
print("3.2.10 Filtro de vocales")
user_word = "Mariana"
user_word = user_word.upper()

for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    print(letter)

print()
print("Filtro de vocales con acumulación")
user_word = "murcielago"
user_word = user_word.upper()
word_without_vowels = ""

for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    word_without_vowels += letter

print(word_without_vowels)

print()
print("3.2.12 while con else")
n = 0
while n != 3:
    print(n)
    n += 1
else:
    print(n, "else")

print()
print("3.2.13 for con else")
for i in range(3):
    print(i)
else:
    print(i, "else")

print()
print("3.2.14 Altura de una pirámide")
blocks = 10
height = 0
layer = 1

while blocks >= layer:
    blocks -= layer
    height += 1
    layer += 1

print("La altura de la pirámide es:", height)

print()
print("3.2.15 Hipótesis de Collatz")
c0 = 11
steps = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1
    print(c0)
    steps += 1

print("pasos =", steps)
