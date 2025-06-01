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