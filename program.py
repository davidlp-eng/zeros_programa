import gi
from sympy import *
import math

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from gi.repository import Gtk
from matplotlib.figure import Figure
from matplotlib.backends.backend_gtk3agg import (
    FigureCanvasGTK3Agg as FigureCanvas)
import numpy as np
#import matplotlib as plt

class Handler(object):
    def __init__(self):
        pass

    def on_main_window_detroy(self, Window):
        Gtk.main_quit()

    def on_calcular_clicked(self, Button):
        x = symbols('x')


        x_0 = sympify(Builder.get_object("x0_value").get_text())
        x_i = sympify(Builder.get_object("xi_value").get_text())
        precisao = sympify(Builder.get_object("ep").get_text())
        iter = sympify(Builder.get_object("iter").get_text())
        bis = Builder.get_object("bisecao").get_active()
        pos = Builder.get_object("pos_falsa").get_active()
        nw = Builder.get_object("new_rap").get_active()
        bir = Builder.get_object("bier_juv").get_active()
        func = Builder.get_object("func").get_text()
        func = sympify(func)
        bis_vet_resul = []
        pf_vet_resul = []
        nw_vet_resul = []
        bir_vet_resul = []


        if bis == True:
            bis_vet_resul = self.bissecao(x_0,x_i,precisao,iter,func)
        else:
            Builder.get_object("resul_bis").set_text('')
            Builder.get_object("pre_bis").set_text('')
            Builder.get_object("n_iter_bis").set_text('')
        if pos == True:
            pf_vet_resul = self.posicao_falsa(x_0,x_i,precisao,iter,func)
        else:
            Builder.get_object("resul_pos_f").set_text('')
            Builder.get_object("pre_pos_f").set_text('')
            Builder.get_object("n_iter_pos_f").set_text('') 
        if nw == True:
            nw_vet_resul = self.newton(x_0,x_i,precisao,iter,func)
        else:
            Builder.get_object("resul_nr").set_text('')
            Builder.get_object("pre_nr").set_text('')
            Builder.get_object("n_iter_nr").set_text('')
        if bir == True:
            i = 0
            test_poly = func

            for i in range(30):
                test_poly = diff(test_poly,x)

            if test_poly != 0:
                Builder.get_object("resul_bier").set_text('')
                Builder.get_object("pre_bier").set_text('')
                Builder.get_object("n_iter_bier").set_text('')

            else:
                vet_func = Poly(func)
                vet_func = vet_func.all_coeffs()
                bir_vet_resul = self.birge(x_0,x_i,precisao,iter,vet_func)
        else:
            Builder.get_object("resul_bier").set_text('')
            Builder.get_object("pre_bier").set_text('')
            Builder.get_object("n_iter_bier").set_text('')

        self.plotar_2(bis_vet_resul,pf_vet_resul,nw_vet_resul,bir_vet_resul)
 

    def bissecao(self,a,b,c,d,f):
        x = symbols('x')
        x0 = float(a)
        xi = float(b)
        pre = float(c)
        iter = d
        cont = 0
        func = f
        bis_vet_resul = []

        while (cont<iter):

            xi_1 = (x0 + xi) / 2
            bis_vet_resul.append(xi_1)
            
            tx0 = self.teste_sinal(x0,func)
            txi = self.teste_sinal(xi,func)
            txi_1 = self.teste_sinal(xi_1,func)

            if tx0 == txi_1:
                x0 = xi_1
            if txi == txi_1:
                xi = xi_1
            cont += 1

            if abs((xi-x0)) < pre:
                break


        Builder.get_object("resul_bis").set_text(str(xi_1))
        Builder.get_object("pre_bis").set_text(str(abs(xi-x0)))
        Builder.get_object("n_iter_bis").set_text(str(cont))

        return bis_vet_resul
    
    def posicao_falsa(self,a,b,c,d,f):

        x = symbols('x')
        x0 = float(a)
        xi = float(b)
        pre = float(c)
        iter = d
        func = f
        cont = 0
        pf_vet_resul = []
        
        while (cont<iter):

            fx0 = func.subs(x,x0)
            tx0 = self.teste_sinal(x0,func)

            fxi = func.subs(x,xi)
            txi = self.teste_sinal(xi,func)

            xi_1 = ((x0 * abs(fxi)) + (xi * abs(fx0))) / ((abs(fx0)) + (abs(fxi)))
            pf_vet_resul.append(xi_1)
            txi_1 = self.teste_sinal(xi_1,func)

            if tx0 == txi_1:
                x0 = xi_1
            if txi == txi_1:
                xi = xi_1

            cont += 1

            if abs((xi-x0)) < pre:
                break

        Builder.get_object("resul_pos_f").set_text(str(xi_1))
        Builder.get_object("pre_pos_f").set_text(str(abs(xi-x0)))
        Builder.get_object("n_iter_pos_f").set_text(str(cont))    

        return pf_vet_resul

    def newton(self,a,b,c,d,f):
        x = symbols('x')
        xi = float(b)
        pre = float(c)
        iter = d
        cont = 0
        func = f
        nw_vet_resul = []

        while (cont<iter):

            f_xi = func.subs(x,xi)
            fl_xi = diff(func,x)
            fl_xi = fl_xi.subs(x,xi)

            xi_1 = float(xi - (f_xi/fl_xi))
            cont +=1
            nw_vet_resul.append(xi_1)

            if abs((xi-xi_1)) < pre:
                break

            xi = xi_1

        Builder.get_object("resul_nr").set_text(str(xi_1))
        Builder.get_object("pre_nr").set_text(str(abs(xi-xi_1)))
        Builder.get_object("n_iter_nr").set_text(str(cont))

        return nw_vet_resul

    def birge(self,a,b,c,d,f):
        
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
        bir_vet_resul = []

        while abs(xi-x0) > pre:
            if flag == 0:
                x0 = xi
            Rr = divisao(vet_func, nt, x0)
            xi = x0 - Rr
            bir_vet_resul.append(xi)

            cont += 1
            flag = 0

            if cont == iter:
                break

        Builder.get_object("resul_bier").set_text(str(xi))
        Builder.get_object("pre_bier").set_text(str(abs(xi-x0)))
        Builder.get_object("n_iter_bier").set_text(str(cont))

        return bir_vet_resul


    def teste_sinal(self, x_teste,func):
        
        x = symbols('x')
        f = func
        x_t = x_teste

        x_calc = f.subs(x,x_t)

        if x_calc > 0:
            return 0 

        if x_calc < 0:
            return 1


    def on_plot1_destroy(self, widget):
        pass

    def on_plotar_clicked(self, button):

        x = symbols('x')

        func = Builder.get_object("func").get_text()

        x0_plot = float(Builder.get_object("x0_plot").get_text())
        xi_plot = float(Builder.get_object("xi_plot").get_text())


        sw = Builder.get_object("plot1")


        figure = Figure(figsize=(8, 6), dpi=71)
        axis = figure.add_subplot()
        t = np.arange(x0_plot, xi_plot, 0.001)
        output_t=np.zeros(len(t))
        j=0
 
        s = func
        s = sympify(s)

        for i in t:  
            res = s.subs(x,i)
            output_t[j]= res
            j+=1

        s = output_t

        axis.plot(t, s)


        axis.set_xlabel('x')
        axis.set_ylabel('y')

        canvas = FigureCanvas(figure)  
        canvas.set_size_request(800, 600)
        sw.add(canvas)
        sw.show_all()      

    def plotar_2(self,a,b,c,d):
        bis = a
        pf = b
        nw = c
        bir = d

        sw = Builder.get_object("plot2")

        figure = Figure(figsize=(8, 8), dpi=71)

        x_val = np.arange(0, len(bis), 1)
        axs = figure.add_subplot(2,2,1) #.title.set_text('Bisseccao')
        axs.plot(x_val,bis)

        x_val = np.arange(0, len(pf), 1)
        axs = figure.add_subplot(2,2,2) #.title.set_text('Posicao Falsa')
        axs.plot(x_val,pf)

        x_val = np.arange(0, len(nw), 1)
        axs = figure.add_subplot(2,2,3) #.title.set_text('Newton Raphson')
        axs.plot(x_val,nw)

        x_val = np.arange(0, len(bir), 1)
        axs = figure.add_subplot(2,2,4) #.title.set_text('Bierge Vieta')
        axs.plot(x_val,bir)


        canvas = FigureCanvas(figure)  
        canvas.set_size_request(800, 600)
        sw.add(canvas)
        sw.show_all()  


 

Builder = Gtk.Builder()
Builder.add_from_file("projeto_feira.glade")
Builder.connect_signals(Handler())
Window: Gtk.Window = Builder.get_object("main_window")
Window.show_all()
Gtk.main()
