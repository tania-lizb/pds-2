# PDS tareas 1 a 4 


### **Tarea_1: Generación de Señales Básicas**

Genera 4 tipos de señales (sinusoidal, exponencial, triangular, cuadrada) en versión **analógica** y **discreta**, mostrando su relación.

* **Ecuaciones utilizadas**:
  - Sinusoidal: $x(t) = \sin(2\pi F t)$
  - Exponencial: $x(t) = e^{-2t} \cdot u(t)$
  - Triangular: $\text{sawtooth}(2\pi F t, \text{width}=0.5)$
  - Cuadrada: $\text{square}(2\pi F t)$

* **Parámetros**:
  - Frecuencia (F): 2 Hz
  - Tiempo analógico: -1.0 a 5.0 s (1000 muestras)
  - Muestreo discreto: $f_s = 40$ Hz, $n = -40$ a $200$

* **Para ejecutar**:
   ```bash
   python main.py Tarea_1



### **Tarea_2: Señal senoidal continua** 

Genera una señal senoidal continua ajustable por frecuencia.

* **Ecuaciones utilizadas**:
   - x(t) = A \cdot \sin(2\pi f t)

* **Parámetros**:
  - Frecuencia (F): 1, 2, 5 hz (introducida por el usuario)
  - Tiempo: -1.0 a 5.0 s (1000 muestras)

* **Para ejecutar**:
   ```bash
   python main.py Tarea_2 <frecuencia>
   ejemplo 
   python main.py Tarea_2 2.5



### **Tarea_3: **

Compara dos señales sinusoides con parametros personalizados 

* **Ecuaciones utilizadas**:
  - continua: x(t) = A \cdot \sin(2\pi f t + \phi)
  - discreta: x[n] = A \cdot \sin(2\pi f n T_s + \phi)

* **Parámetros**:
  - ts=0.01 s
  - Tiempo: 0 a 5.0 s (1000 muestras)
  - Muestreo discreto: n= -50, 250

* **Para ejecutar**:
   ```bash
   python main.py Tarea_3 <amplitud> <frecuencia> <fase_en_radianes>
   ejemplo 
   python main.py Tarea_3 1.5 2 0.785

### **Tarea_4: simulacion DAC**

simula un convertidor digital-analogico de N bits calculando resolucion y tamaño del paso 

* **Parámetros**:
  - Niveles :  2^N
  - Paso: VFS/(2^N - 1)
  - Resolucion: 100 / (2^N - 1) %

* **Para ejecutar**:
   ```bash
   python main.py Tarea_4 <bits>
   ejemplo
   python main.py Tarea_4 8

