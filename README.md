# Matemáticas para Inteligencia Artificial

Las matemáticas que hay debajo de la IA, explicadas con código que puedes ejecutar.
Cada tema viene resuelto en **Python** y en **MATLAB/Octave**, con scripts cortos, comentados y autocontenidos.

Material abierto y gratuito. No necesitas estar inscrito en ningún lado: clona el repositorio y empieza.

![Matemáticas para IA](assets/BaseMatematica.png)

---

## ¿Para quién es esto?

- Quien aprende IA por su cuenta y se topa con la pared del álgebra lineal o el cálculo.
- Quien programa modelos pero quiere entender qué pasa dentro del `fit()`.
- Quien estudia una ingeniería o una carrera técnica y busca ejemplos que sí corran.
- Quien enseña estos temas y quiere ejercicios listos para adaptar (la licencia lo permite).

**Lo que se da por sabido:** álgebra de bachillerato y nociones básicas de programación.
Lo demás se construye desde cero en los propios scripts.

## Ruta de aprendizaje

Los módulos están pensados para seguirse en orden, pero cada script funciona por separado.

### 1 · Álgebra lineal y geometría diferencial
Vectores, matrices, normas, producto punto, determinantes, valores y vectores propios,
descomposiciones y transformaciones. Es el lenguaje en el que se escriben los datos y los pesos de una red.

| Notebook | Abrir sin instalar nada |
|---|---|
| [01 · Operaciones con vectores y matrices](python/01-algebra-lineal/01_operaciones_vectores.ipynb) | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SolKacil/matematicas-para-ia/blob/main/python/01-algebra-lineal/01_operaciones_vectores.ipynb) |

📁 [`python/01-algebra-lineal`](python/01-algebra-lineal) · [`matlab/01-algebra-lineal`](matlab/01-algebra-lineal)

### 2 · Cálculo multivariable y optimización
Derivadas parciales, gradiente, regla de la cadena, matrices jacobiana y hessiana, descenso de gradiente.
Aquí está el motor del entrenamiento: retropropagación y minimización de la función de pérdida.
📁 [`python/02-calculo-optimizacion`](python/02-calculo-optimizacion) · [`matlab/02-calculo-optimizacion`](matlab/02-calculo-optimizacion)

### 3 · Teoría de grafos y procesos estocásticos
Grafos, matrices de adyacencia, recorridos, cadenas de Markov y probabilidad aplicada.
La base de las redes neuronales de grafos, los sistemas de recomendación y el aprendizaje por refuerzo.
📁 [`python/03-grafos-y-procesos-estocasticos`](python/03-grafos-y-procesos-estocasticos) · [`matlab/03-grafos-y-procesos-estocasticos`](matlab/03-grafos-y-procesos-estocasticos)

### 4 · Análisis numérico y transformada de Fourier
Error numérico, interpolación, integración, raíces, series y transformada de Fourier (DFT/FFT).
Indispensable para trabajar señales, audio, imágenes y series de tiempo.
📁 [`python/04-analisis-numerico-y-fourier`](python/04-analisis-numerico-y-fourier) · [`matlab/04-analisis-numerico-y-fourier`](matlab/04-analisis-numerico-y-fourier)

## Empezar

### Sin instalar nada: Google Colab

Cada notebook lleva arriba un botón **Open in Colab**. Le das clic y el material se abre y se
**ejecuta en tu navegador**, gratis, sin instalar Python ni nada. Es la forma más rápida de
empezar y la recomendada si estás aprendiendo.

### En tu computadora: Python

```bash
git clone https://github.com/SolKacil/matematicas-para-ia.git
cd matematicas-para-ia

python -m venv .venv
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # Linux / macOS

pip install -r requirements.txt
python python/01-algebra-lineal/01_operaciones_vectores.py
```

### En tu computadora: MATLAB o GNU Octave

Los scripts `.m` están escritos para correr igual en MATLAB y en [GNU Octave](https://octave.org),
que es libre y gratuito, por si no tienes licencia de MATLAB.

```matlab
cd matlab/01-algebra-lineal
ej01_operaciones_vectores
```

## Cómo estudiar con este repositorio

1. Lee el encabezado del script: dice qué concepto trabaja y qué deberías obtener.
2. Ejecútalo tal cual y compara la salida con lo que esperabas.
3. Cambia los números de entrada y vuelve a correrlo. Ahí es donde se aprende.
4. Reescribe la parte central sin usar la función de la biblioteca (tu propio producto punto,
   tu propio descenso de gradiente) y verifica que coincida con la versión de NumPy o MATLAB.

## Estructura

```
python/     notebooks .ipynb (con teoría) y scripts .py, una carpeta por módulo
matlab/     scripts .m compatibles con Octave, una carpeta por módulo
datos/      conjuntos de datos que comparten los ejercicios
assets/     imágenes y material de apoyo
```

## Convenciones

- Python: `NN_tema_descriptivo.py` y `NN_tema_descriptivo.ipynb`, con `NN` consecutivo dentro
  del módulo (`01_`, `02_`, …). El notebook explica el tema; el script es el mismo contenido
  reducido a lo ejecutable.
- MATLAB/Octave: `ejNN_tema_descriptivo.m` — el prefijo `ej` es obligatorio porque MATLAB no admite
  nombres de script que empiecen con dígito.
- Cada ejercicio abre con un encabezado: título, módulo y objetivo.
- Los datos de entrada van en `datos/`; las salidas generadas (figuras, `.mat`) no se versionan.
- Sin acentos ni espacios en los nombres de archivo y carpeta; los acentos van en el contenido.

## Contribuir

Se aceptan correcciones, ejercicios nuevos, traducciones y mejoras a las explicaciones.
Lee [CONTRIBUTING.md](CONTRIBUTING.md) — es corto.

## Licencia y autoría

[MIT](LICENSE): puedes usar, copiar, modificar y redistribuir el material, incluso en cursos propios,
conservando el aviso de atribución.

Escrito y mantenido por **Dr. Oscar Isaid Pellico Sánchez**, docente de ingeniería.
El contenido nace de un curso universitario que imparto, reordenado aquí para que sirva a cualquiera.
