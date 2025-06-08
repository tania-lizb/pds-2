import numpy as np
from src.utils.grapher import continuous_plotter

def DAC(bits):

    VFS = 5.0
    niveles = 2 ** bits
    paso = VFS / (niveles - 1)
    resolucion = 100 / (niveles - 1)

    entrada_dig= np.arange(niveles)
    salida_anlog= entrada_dig * paso 

    print("\nResultados DAC: ")
    print(f"Bits: {bits}")
    print(f"Niveles: {niveles}")
    print(f"Tamaño del paso: {paso:.4f} V")
    print(f"Resolucion: {resolucion:.4f} %")

    
    titulo = f"Salida Analogica del DAC de {bits} bits"

    continuous_plotter(entrada_dig, salida_anlog, titulo, "Salida del DAC", "Entrada Digital", "Voltaje de Salida en V")
