
from sympy import *
import numpy as np

def posicao_falsa(a,b,c,d,f):

    x = symbols('x')
    x0 = float(a)
    xi = float(b)
    pre = float(c)
    iter = d
    func = f
    cont = 0
    xi_1_antigo = 0
        
    while (cont<iter):

        fx0 = func.subs(x,x0)
        tx0 = teste_sinal(x0,func)

        fxi = func.subs(x,xi)
        txi = teste_sinal(xi,func)

        if cont>0:
            xi_1_antigo = xi_1

        xi_1 = ((x0 * abs(fxi)) + (xi * abs(fx0)))/((abs(fx0)) + (abs(fxi)))
        txi_1 = teste_sinal(xi_1,func)

        print('tx0: ',tx0)
        print('txi: ',txi)
        print('txi_1: ',txi_1)
        print('\n')


        if abs(xi-xi_1_antigo) < pre:
            print('Entrei')
            break

        if tx0 == txi_1:
            x0 = xi_1
        if txi == txi_1:
            xi = xi_1

        cont += 1

        print('Valor de x0: ',x0)
        print('Valor de xi: ',xi)
        print('Valor de xi_1: ',xi_1)
        print('\n')
            
    return xi_1



def teste_sinal(x_teste,func):
        
    x = symbols('x')
    f = func
    x_t = x_teste

    x_calc = f.subs(x,x_t)

    if x_calc > 0:
        return 0 

    if x_calc < 0:
        return 1

x = symbols('x')

xi_1 = posicao_falsa(2.5,3,0.0001,50,(x**3-9*x+3))


print(xi_1)




