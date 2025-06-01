"""
## GRAFICACION DE SEÑALES ANALOGAS Y DISCRETAS

## Descripción
La Tarea 1 genera y visualiza señales analógicas y discretas con los parámetros:
t = np.linspace(-1.0, 5.0, 1000)
n = np.arange(-40, 201)
F = 2.0  # Hz
fs = 40.0  # Hz
ts = 1/fs
estas muestran cada una de las señales una subgrafica una señal analogica, señal discreta y señal discretizada.
"""

# ============== Señales implementadas ==============
def mostrar_senales():
    """
    Señales implementadas:
    1. Senoidal:
       Analógica: np.sin(2 * np.pi * F * t)
       Discreta: np.sin(2 * np.pi * F * n/fs)
    
    2. Exponencial:
       Analógica: np.exp(-2 * t) * (t >= 0)
       Discreta: np.exp(-2 * n/fs) * (n >= 0)
    
    3. Triangular:
       Analógica: sawtooth(2 * np.pi * F * t, 0.5)
       Discreta: sawtooth(2 * np.pi * F * n/fs, 0.5)
    
    4. Cuadrada (2 Hz):
       Analógica: square(2 * np.pi * F * t)
       Discreta: square(2 * np.pi * F * n/fs)
    """

# ============== Estructura del proyecto ==============
estructura = """
├── main.py  
├── src/  
│   ├── utils/  
│   │   └── grapher.py  
│   └── tarea1.py
└── requirements.txt
"""

# ============== Requisitos ==============
requisitos = """
- Python 3.8+
- Bibliotecas:
  - numpy
  - matplotlib
  - scipy
Requisitos en requirements.txt
"""

# ============== Instalación ==============
def instalacion():
    """
    1. Clonar repositorio:
    ```bash
    git clone https://github.com/tania-lizb/pds-2
    cd pds-2
    ```

    2. (Opcional) Entorno virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\\Scripts\\activate  # Windows
    ```

    3. Instalar dependencias:
    ```bash
    pip install -r requirements.txt
    ```
    """

# ============== Uso ==============
def uso():
    """
    Ejecutar la Tarea 1:
    ```bash
    python main.py
    ```

    Genera gráficas de:
    1. Sinusoidal: x₁(t) = sin(2πft)
    2. Exponencial: x₂(t) = e^(–2t)·u(t)
    3. Triangular: x₃(t) = tri(t,f)
    4. Cuadrada: x₄(t) = sq(t,f)
    """

