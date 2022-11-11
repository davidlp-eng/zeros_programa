import gi
from sympy import *

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from gi.repository import Gtk
from matplotlib.figure import Figure
from matplotlib.backends.backend_gtk3agg import (
    FigureCanvasGTK3Agg as FigureCanvas)
import numpy as np

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


        if bis == True:
            self.bissecao(x_0,x_i,precisao,iter,func)
        if pos == True:
            self.posicao(x_0,x_i,precisao,iter,func)
        if nw == True:
            self.newton(x_0,x_i,precisao,iter,func)
        if bir == True:
            self.birge(x_0,x_i,precisao,iter,func)
 


    def bissecao(self,a,b,c,d,f):
        x = symbols('x')
        x0 = a
        xi = b
        pre = c
        iter = d
        cont = 0
        func = f

        print(pre)
        print()
        
        while (cont<iter):

            xi_1 = float((x0 + xi) / 2)
            x_teste = float(x0)
            tx0 = self.teste_sinal(x_teste,func)
            x_teste = float(xi)
            txi = self.teste_sinal(x_teste,func)
            x_teste = float(xi_1)
            txi_1 = self.teste_sinal(x_teste,func)
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

        return None
    
    def posicao(self,a,b,c,d,f):
        pass

    def newton(self,a,b,c,d,f):
        pass

    def birge(self,a,b,c,d,f):
        pass


    def teste_sinal(self, x_teste,func):
        
        x = symbols('x')
        f = func

        x_calc = f.subs(x,x_teste)

        if x_calc > 0:
            return 0 

        elif x_calc < 0:
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
 

Builder = Gtk.Builder()
Builder.add_from_file("projeto_feira.glade")
Builder.connect_signals(Handler())
Window: Gtk.Window = Builder.get_object("main_window")
Window.show_all()
Gtk.main()
