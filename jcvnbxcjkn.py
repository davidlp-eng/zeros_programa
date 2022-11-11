from sympy import *
import numpy as np

x = symbols('x')

t = np.arange(0.0, 3.0, 0.01)
output_t=np.zeros(len(t))
j=0

#s = t**3-9*t+3
x = symbols('x')
s = input('Func = ')
s = sympify(s)

def converter(i):
    res = s.subs(x,i)
    return res



for i in t:  

    output_t[j]= converter(i)
    j+=1

print(output_t)



