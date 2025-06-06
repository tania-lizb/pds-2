import numpy as np
from src.utils.grapher import discrete_plotter, continuous_plotter

def senales_con_potter(A,f,ϕ):
    
    t = np.linspace(0, 5.0, 1000)  

    xt_modificada = A * np.sin(2 * np.pi * f * t + ϕ) # señal color azul en grafica
    xt_referencia = 1.0 * np.sin(2 * np.pi * 1.0 * t + 0) #señal color rojo en grafica
    
    continuous_plotter(t, xt_modificada, f"señal continua (A={A}, f={f} Hz, ϕ={ϕ}rad)", "señal modificada", "tiempo [s]", "Amplitud", xt_referencia)    


    ts = 0.01
    n = np.arange(-50, 250) 
    tn= n * ts
    
    xn_modificada = A * np.sin(2 * np.pi * f * tn + ϕ)
    xn_referencia = 1.0 * np.sin(2 * np.pi * 1.0 * tn + 0)
    

    discrete_plotter(
    n, 
    xn_modificada, 
    xn_referencia, 
    f'señal discreta (A={A}, f={f} Hz, ϕ={ϕ} rad)', 
    "Índice de muestra (n)", 
    "Amplitud"
)

#if __name__ == "__main__":
 #   import sys
  #  if len(sys.argv) != 4:
   #     print("Uso: python main.py tarea_3 <amplitud> <frecuencia> <fase>")
    #    sys.exit(1)
    #A, f, ϕ = map(float, sys.argv[1:4])
    #senales_con_potter(A,f,ϕ)