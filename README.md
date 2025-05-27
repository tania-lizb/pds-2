# Se�ales a Graficar 
 
**Se�ales a graficar:** 
- x�(t) = sin(2p�f�t): Se�al sinusoidal de frecuencia f (recomendado: f=2) 
- x�(t) = e(-2t) � u(t): Se�al exponencial, donde u(t) es la se�al escal�n unitario 
- x�(t) = tri(t, f): Se�al triangular peri�dica de frecuencia f (recomendado: f=2) 
- x4(t) = sq(t, f): Se�al cuadrada de frecuencia f (recomendado: f=2) 
 
**Dominio de tiempo:** 
- t ? [-1, 5] s (puede ajustarse seg�n la se�al) 
 
**Gr�fica de la se�al continua:** 
- Usar numpy.linspace con al menos 1000 puntos para generar t. 
- Calcular x_cont = x(t) 
- Graficar x_cont como l�nea suave 
 
**Muestreo y se�al discreta:** 
- Definir un periodo de muestreo adecuado, por ejemplo T? = 0.01�s 
- Generar n = np.arange(N) de modo que t? = n�T? cubra el mismo intervalo 
- Calcular x_disc = x(t?) 
- Superponer los puntos muestreados sobre la gr�fica continua 
 
