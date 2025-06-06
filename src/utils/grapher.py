import numpy as np 
import matplotlib.pyplot as plt 

#graficacion de las señales
def graficar_senales(t, xt, n, xn, nombre, fs):
    plt.figure()
    plt.subplots_adjust(hspace=0.65)

    plt.subplot(3, 1, 1)
    plt.plot(t, xt, '-b', lw=2)
    plt.xlabel('tiempo (s)')
    plt.ylabel('amplitud')
    plt.title(f'{nombre} - señal analógica')
    plt.grid()

    plt.subplot(3, 1, 2)
    plt.stem(n, xn, linefmt='r', markerfmt='r.', basefmt=' ')
    plt.xlabel('índice de muestra (n)')
    plt.ylabel('amplitud')
    plt.title(f'{nombre} - señal discreta')
    plt.grid()

    plt.subplot(3, 1, 3)
    plt.stem(n / fs, xn, linefmt='r', markerfmt='r.', basefmt=' ')
    plt.plot(t, xt, '-b', lw=2)
    plt.xlabel('tiempo (s)')
    plt.ylabel('amplitud')
    plt.title(f'{nombre} - señal analógica discretizada')
    plt.grid()

    plt.show()


def continuous_plotter(t, señal_modificada, titulo, subtitulo, xlabel, ylabel, señal_referencia=None):
    plt.figure()

    plt.plot(t, señal_modificada, label=subtitulo, color='blue', linewidth=2)

    if señal_referencia is not None:
        plt.plot(t, señal_referencia, '--r', lw=1, label="Referencia (A=1, f=1Hz, ϕ=0)")
    
    

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(titulo)
    plt.grid()
    plt.legend()
    plt.show()  


def discrete_plotter(n, señal_modificada, señal_referencia, título, xlabel, ylabel):
    plt.figure()
    plt.stem(n, señal_modificada, label="Señal modificada ", linefmt='b-', markerfmt='bo', basefmt="k-" )


    plt.stem(n, señal_referencia, linefmt='r', basefmt='', label="Referencia (A=1, f=1Hz, ϕ=0)")
  

  


    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(título)
    plt.grid()
    plt.legend()
    plt.show()

    