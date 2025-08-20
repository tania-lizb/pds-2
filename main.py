import sys
from src.Tarea_1 import generar_senales
from src.Tarea_2 import Tarea_2
from src.Tarea_3 import senales_con_potter
from src.Tarea_4 import DAC  
from src.Examen_p1 import Examen_p1, Examen_p2

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py <tarea> [argumentos]")
    elif sys.argv[1] == "Tarea_1":
        generar_senales()
    elif sys.argv[1] == "Tarea_2":
        if len(sys.argv) >= 3:
            frecuencia = float(sys.argv[2])
            Tarea_2(frecuencia)
        else:
            print("Falta argumento de frecuencia para Tarea_2")
    elif sys.argv[1] == "Tarea_3":
        if len(sys.argv) >= 5:
            A = float(sys.argv[2])
            f = float(sys.argv[3])
            phi = float(sys.argv[4])
            senales_con_potter(A, f, phi)
        else:
            print("Uso: python main.py Tarea_3 <amplitud> <frecuencia> <fase>")
    elif sys.argv[1]== "Tarea_4":
        if len(sys.argv) >= 3: 
            bits = int(sys.argv[2])
            DAC(bits)
        else:
            print("Uso: python main.py Tarea_4 <bits>")
            
    elif sys.argv[1] == "Examen_p1":  
        Examen_p1()
    elif sys.argv[1] == "Examen_p2":  
        Examen_p2()     
    else:
        print(f"Tarea desconocida: {sys.argv[1]}")