import numpy as np
import matplotlib.pyplot as plt

from .utils.grapher import continuous_plotter

def Tarea_2(frecuencia):
   
    t = np.linspace(-1.0, 5.0, 1000) 
    A = 1  # amplitud
    xt = A * np.sin(2 * np.pi * frecuencia * t)

    continuous_plotter(
        t, 
        xt, 
        titulo= f' señal sinusoide con una frecuencia de: {(frecuencia)} hz', 
        subtitulo=f'Señal generada (A=1, f={frecuencia} Hz)',
        xlabel='Tiempo (s)',
        ylabel='Amplitud'
    )
    

if __name__ == "__main__": 
    Tarea_2(frecuencia)