import numpy as np
from scipy.signal import find_peaks
from .utils.grapher import continuous_plotter, discrete_plotter, analisis_espectro_frec, imprimir_en_consolaPT1, imprimir_en_consolaPT2

def mi_DFT(x):
    return np.fft.fft(x)

def encontrar_picos(magnitudes, frecuencias, umbral=0.01):
    indices_picos, _ = find_peaks(magnitudes, height=umbral)
    return [(frecuencias[idx], magnitudes[idx]) for idx in indices_picos]

def analizar_espectro_pt1(fm=0.5, fc=8.0, m=0.5, fs=80.0, duracion=10.0):
    n = np.arange(int(fs * duracion))
    t = n / fs
    senal_tiempo = (1 + m * np.cos(2 * np.pi * fm * t)) * np.sin(2 * np.pi * fc * t)
    
    X = mi_DFT(senal_tiempo)
    N = len(n)
    magnitudes = np.abs(X) / N
    frecuencias = np.arange(N) * fs / N
    delta_f = fs / N

    picos = encontrar_picos(magnitudes[:N//2], frecuencias[:N//2])

    imprimir_en_consolaPT1(delta_f, N, fs, picos)
    analisis_espectro_frec(t, senal_tiempo, frecuencias[:N//2], magnitudes[:N//2], 
                          f'Señal: x(t) = [1 + {m}·cos(2π·{fm}·t)]·sin(2π·{fc}·t)', 
                          f'Espectro (Δf = {delta_f:.4f} Hz)', xlim=20)

    return {'senal_tiempo': senal_tiempo, 'frecuencias': frecuencias, 'magnitudes': magnitudes, 'picos': picos}

def analizar_espectro_pt2(f1=8.0, f2=20.0, amplitud_ruido=0.3, frecuencia_ruido=60.0, fs=256.0, duracion=6.0):
    N = int(fs * duracion)
    n = np.arange(N)
    t = n / fs

    senal_limpia = np.sin(2 * np.pi * f1 * t) + 0.15 * np.sin(2 * np.pi * f2 * t)
    ruido = amplitud_ruido * np.sin(2 * np.pi * frecuencia_ruido * t)
    senal_con_ruido = senal_limpia + ruido

    X_limpia, X_con_ruido = mi_DFT(senal_limpia), mi_DFT(senal_con_ruido)
    magnitudes_limpia, magnitudes_con_ruido = np.abs(X_limpia) / N, np.abs(X_con_ruido) / N
    frecuencias = np.arange(N) * fs / N
    delta_f = fs / N

    picos_limpia = encontrar_picos(magnitudes_limpia[:N//2], frecuencias[:N//2])
    picos_con_ruido = encontrar_picos(magnitudes_con_ruido[:N//2], frecuencias[:N//2])

    imprimir_en_consolaPT2(delta_f, N, fs, frecuencia_ruido, amplitud_ruido, picos_limpia, picos_con_ruido)
    
    analisis_espectro_frec(t, senal_limpia, frecuencias[:N//2], magnitudes_limpia[:N//2], 
                          f'Señal limpia', f'Espectro (Δf = {delta_f:.4f} Hz)', xlim=100)
    analisis_espectro_frec(t, senal_con_ruido, frecuencias[:N//2], magnitudes_con_ruido[:N//2], 
                          f'Señal con ruido', f'Espectro (Δf = {delta_f:.4f} Hz)', xlim=100)

    return {'senal_limpia': senal_limpia, 'senal_con_ruido': senal_con_ruido, 'frecuencias': frecuencias}

def Examen_p1():
    return {'parte1': analizar_espectro_pt1()}

def Examen_p2():
    return {'parte2': analizar_espectro_pt2()}