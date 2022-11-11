
from sympy import *
import numpy as np

x = symbols('x')

s = input('Func = ')

s = sympify(s)
res = s.subs(x,2)

print(res)




