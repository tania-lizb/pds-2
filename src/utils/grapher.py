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

##Examen_p1


def analisis_espectro_frec(tiempo, señal, frecuencias, magnitudes, titulo_senal, titulo_espectro, xlim=None):
    """Grafica señal en el tiempo y su espectro de frecuencias"""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
    
    # Señal en el tiempo
    ax1.plot(tiempo, señal, 'b-', linewidth=2)
    ax1.set_xlabel('Tiempo (s)')
    ax1.set_ylabel('Amplitud')
    ax1.set_title(titulo_senal)
    ax1.grid(True)

    # Espectro de frecuencia
    ax2.plot(frecuencias, magnitudes, 'r-', linewidth=2)
    ax2.set_xlabel('Frecuencia (Hz)')
    ax2.set_ylabel('Magnitud')
    ax2.set_title(titulo_espectro)
    ax2.grid(True)
    if xlim is not None:
        ax2.set_xlim(0, xlim)

    plt.tight_layout()
    plt.show()


def imprimir_en_consolaPT1(delta_f, N, fs, picos):
    print("Analisis Espectral Parte 1 Transformada Discreta de Fourier")
    print(f"Resolución en frecuencia Δf: {delta_f:.4f} Hz")
    print(f"Número de muestras: {N}")
    print(f"Frecuencia de muestreo fs: {fs} Hz")
    print("\nPicos espectrales encontrados:")
    for i, (freq, mag) in enumerate(picos[:5], 1):
        print(f"  Pico {i}: {freq:.4f} Hz - Amplitud: {mag:.6f}")


def imprimir_en_consolaPT2(delta_f, N, fs, frecuencia_ruido, amplitud_ruido, picos_limpia, picos_con_ruido):
    print("Analisis Espectral con Ruido Parte 2 Transformada Discreta de Fourier")
    print(f"Resolución en frecuencia Δf: {delta_f:.4f} Hz")
    print(f"Número de muestras: {N}")
    print(f"Frecuencia de muestreo fs: {fs} Hz")
    print(f"Frecuencia de ruido añadido: {frecuencia_ruido} Hz")
    print(f"Amplitud de ruido: {amplitud_ruido}")
    print("\nPicos en señal limpia:")
    for i, (freq, mag) in enumerate(picos_limpia[:5], 1):
        print(f"  Pico {i}: {freq:.2f} Hz - Amplitud: {mag:.6f}")
    print("\nPicos en señal con ruido:")
    for i, (freq, mag) in enumerate(picos_con_ruido[:5], 1):
        print(f"  Pico {i}: {freq:.2f} Hz - Amplitud: {mag:.6f}")