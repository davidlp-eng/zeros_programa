from sympy import *
import numpy as np


#x = symbols('x')

#func = x**3
func = input('Digite a funcao: ')

print("A função é: ",func)
print(type(func))

t = np.arange(0.0, 3.0, 0.001)

s = t**3

print("\nT = ",t)
print(type(t))
print("\ns = ",s)
print(type(s))


s = func.subs({'x': t}).evalf()


#print("\nT = ",t)
#print(type(t))
print("\ns = ",s)
print(type(s))

