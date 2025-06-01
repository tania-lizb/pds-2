"""Graficacion de Señales Analogicas y Digitales

## Descripción 
la tarea 1 se basa en generar y visualizar señales analogicas y discretas. las 4 señales se configuraron con los siguientes parametros: 
t= np.linspace(-1.0, 5.0, 1000)
n= np.arange(-40, 201)
F=2.0
fs= 40.0 hz 
ts= 1/fs 

estos parametros se utilizan para generar las siguientes señales:
1. Senoidal:  
    np.sin(2 * np.pi * F * t)
    np.sin(2 * np.pi * F * n/fs)
2. Exponencial: 
     np.exp(-2 * t) * (t >= 0)
     np.exp(-2 * n/fs) * (n >= 0) 
3. Triangular 
    sawtooth(2 * np.pi * F * t, 0.5)
    sawtooth(2 * np.pi * F * n/fs, 0.5)
4. Cuadrada (2 Hz)
    square(2 * np.pi * F * t)
    square(2 * np.pi * F * n/fs)

estas muestran cada una de las señales una subgrafica una señal analogica, señal discreta y señal discretizada.
"""

#  ESTRUCTURA DEL PROYECTO 
"""
├── main.py               
├── grapher.py            
│   └── graficar_senales() 
├── Tarea_1.py            
│   └── generar_senales()  
└── requirements.txt      
"""

# INSTALACIÓN  
def instalacion():
    """
    ## Instalación
    1. Clonar repositorio:
    ```bash
    git clone https://github.com/tu-usuario/proyecto-señales.git
    cd proyecto-señales
    ```

    2. (Opcional) Entorno virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\\Scripts\\activate   # Windows
    ```

    3. Instalar dependencias:
    ```bash
    pip install -r requirements.txt
    ```
    """

#  USO  
def uso():
    """
    ## Uso
    Opción 1 - Ejecutar directamente:
    ```bash
    python Tarea_1.py
    ```

    Opción 2 - Usar punto de entrada:
    ```bash
    python main.py
    ```

    ## Parámetros Técnicos
    - Frecuencia base: 2 Hz
    - Frecuencia muestreo: 40 Hz
    - Rango temporal: [-1, 5] segundos
    - Muestras: 241 puntos (n = -40 a 200)
    """

#  DEPENDENCIAS 
dependencias = """
- Python 3.6+
- NumPy >= 1.21.0
- SciPy >= 1.7.0
- Matplotlib >= 3.5.0

Archivo requirements.txt:
```plaintext
numpy
scipy
matplotlib