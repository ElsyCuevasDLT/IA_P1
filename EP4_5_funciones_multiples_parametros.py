print("4.5 Funciones con múltiples parámetros")

print()
print("4.5.1 Cálculo del IMC")

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
    return weight / height ** 2

print(bmi(58.0, 1.62))

def lb_to_kg(lb):
    return lb * 0.45359237

def ft_and_inch_to_m(ft, inch=0.0):
    return ft * 0.3048 + inch * 0.0254

print(lb_to_kg(1))
print(ft_and_inch_to_m(1, 1))
print(ft_and_inch_to_m(5))

print(bmi(weight=lb_to_kg(140), height=ft_and_inch_to_m(5, 4)))

print()
print("4.5.2 Triángulos")

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

print(is_a_triangle(3, 4, 5))
print(is_a_triangle(1, 1, 3))

def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
    return b ** 2 == a ** 2 + c ** 2

print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(2, 3, 4))

def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)

print(area_of_triangle(6.0, 8.0, 10.0))

print()
print("4.5.3 Factoriales")

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1

    product = 1
    for i in range(2, n + 1):
        product *= i
    return product

for n in range(1, 6):
    print(n, factorial_function(n))

print()
print("4.5.4 Números de Fibonacci")

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum

for n in range(1, 10):
    print(n, "->", fib(n))

print()
print("4.5.5 Recursividad")

def fib_rec(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib_rec(n - 1) + fib_rec(n - 2)

for n in range(1, 8):
    print(n, "->", fib_rec(n))

def factorial_rec(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_rec(n - 1)

for n in range(1, 6):
    print(n, factorial_rec(n))

print()
print("Prueba de sección")

print()
print("Pregunta 1")
print("Esa función entra en recursión infinita porque no tiene condición de terminación")

print()
print("Pregunta 2")
def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)

print(fun(25))
