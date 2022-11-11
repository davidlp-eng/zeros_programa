from pathlib import Path

from sympy import *

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from matplotlib.figure import Figure
from matplotlib.backends.backend_gtk3agg import (
    FigureCanvasGTK3Agg as FigureCanvas)
import numpy as np


class Handler(object):
    def on_window1_destroy(self, widget):
        Gtk.main_quit()

    def on_plot1_destroy(self, widget):
        pass

    def on_plotar_clicked(self, button):

        

        x = symbols('x')

        func = Builder.get_object("func").get_text()


        sw = Builder.get_object("plot1")

        

        # Start of Matplotlib specific code
        figure = Figure(figsize=(8, 6), dpi=71)
        axis = figure.add_subplot()
        t = np.arange(1.0, 3.0, 0.001)
        output_t=np.zeros(len(t))
        j=0
        #s = t**3-9*t+3
        s = func
        s = sympify(s)

        for i in t:  
            res = s.subs(x,i)
            output_t[j]= res
            j+=1

        s = output_t

        axis.plot(t, s)


        axis.set_xlabel('time [s]')
        axis.set_ylabel('voltage [V]')

        canvas = FigureCanvas(figure)  # a Gtk.DrawingArea
        canvas.set_size_request(800, 600)
        sw.add(canvas)


        sw.show_all()        
 
        # End of Matplotlib specific code




Builder = Gtk.Builder()
Builder.add_from_file("mpl_with_glade3.glade")
Builder.connect_signals(Handler())
Window: Gtk.Window = Builder.get_object("window1")
Window.show_all()
Gtk.main()