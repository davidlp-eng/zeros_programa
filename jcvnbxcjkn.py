from sympy import *
import numpy as np

x = symbols('x')

def birge(a,b,c,d,f):
        
    def divisao(vet_func, nt, x0):

        b = np.zeros(nt)
        c = np.zeros(nt-1)

        cont = 0

        for cont in range(nt):
            if cont == 0:
                b[cont] = vet_func[cont]
            else:
                b[cont] = vet_func[cont] + b[cont - 1] * x0
            cont += 1
            
        cont = 0

        for cont in range(nt-1):
            if cont == 0:
                c[cont] = b[cont]
            else:
                c[cont] = b[cont] + c[cont - 1] * x0
            cont += 1
        return ((b[nt-1]) / (c[nt-2]))
        
    pre = c
    x0 = a
    xi = 9999999999999999.99
    iter = d
    vet_func = f
    nt = len(vet_func)

    flag = 1  
    cont = 0

    while abs(xi-x0) > pre:
        if flag == 0:
            x0 = xi
        Rr = divisao(vet_func, nt, x0)
        xi = x0 - Rr

        cont += 1
        flag = 0

        if cont == iter:
            break

    return xi

vet_func = [1,0,-9,3]

raiz = birge(2,3,0.0001,100,vet_func)

print(raiz)


