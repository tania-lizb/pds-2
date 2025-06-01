import sys 
import numpy as np
from scipy.signal import square, sawtooth
from src.utils.grapher import graficar_senales

#definicion de los parametros a utilizat

def generar_senales():

    t = np.linspace(-1.0, 5.0, 1000)
    F = 2
    n = np.arange(-40, 201)
    fs = 40.0
    ts = 1.0 / fs
    tn = n * ts

    señales ={
       "Sinusoidal": (np.sin(2 * np.pi * F * t), np.sin(2 * np.pi * F * n / fs)),
        "Exponencial": (np.exp(-2 * t) * (t >= 0), np.exp(-2 * n / fs) * (n >= 0)),
        "Triangular": (sawtooth(2 * np.pi * F * t, width=0.5), sawtooth(2 * np.pi * F * n / fs, width=0.5)),
        "Cuadrada": (square(2 * np.pi * F * t), square(2 * np.pi * F * n / fs))  
    }

    for nombre, (xt, xn) in señales.items():
        graficar_senales(t, xt, n, xn, nombre, fs)  

if __name__ == "__main__":
    generar_senales()













   ## x1_t = np.sin(2 * np.pi * F * t)
   ## x1_n = np.sin(2 * np.pi * F * n / fs)
   ## x2_t = np.exp(-2 * t) * (t >= 0)
   ## x2_n = np.exp(-2 * tn) * (tn >= 0)
   ## x3_t = sawtooth(2 * np.pi * F * t, width=0.5)
   ## x3_n = sawtooth(2 * np.pi * F * n / fs, width=0.5)
   ## x4_t = square(2 * np.pi * F * t)
   ## x4_n = square(2 * np.pi * F * n / fs) ##

   ## print(f'ts = {ts} segundos')

   ## graficar_senales(t, x1_t, n, x1_n, "Gráfica senoidal")
   ## graficar_senales(t, x2_t, n, x2_n, "Gráfica exponencial")
   ## graficar_senales(t, x3_t, n, x3_n, "Gráfica triangular")
   ## graficar_senales(t, x4_t, n, x4_n, "Gráfica cuadrada")

##if __name__ == "__main__":
##    graficar_senales() ##