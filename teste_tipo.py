from sympy import *

x = Symbol('x')

p1 = 2*x**3 - x + x**2

print(p1)

for i in range(100):
    p1 = diff(p1,x)

if p1 == 0:
    print('É um polinômio')

else:
    print('Não é um polinômio')

p1 = 2*x**3 - sin(x) + x**2

print(p1)

for i in range(100):
    p1 = diff(p1,x)

if p1 == 0:
    print('É um polinômio')

else:
    print('Não é um polinômio')