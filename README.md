# Matemáticas para IA

Ejercicios en **Python** y **MATLAB** de la asignatura *Matemáticas para Inteligencia Artificial*.

Universidad Tecnológica del Centro de Veracruz (UTCV) — Ingeniería en Energía y Desarrollo Sostenible.
Cuatrimestre septiembre–diciembre 2026. Docente: Dr. Oscar Isaid Pellico Sánchez.

![Matemáticas para IA](assets/BaseMatematica.png)

---

## Unidades

| # | Unidad de aprendizaje | Horas | Carpetas |
|---|---|---|---|
| I | Álgebra Lineal y Geometría Diferencial | 15 | `python/unidad-1-algebra-lineal`, `matlab/unidad-1-algebra-lineal` |
| II | Cálculo Multivariable y Optimización | 15 | `python/unidad-2-calculo-optimizacion`, `matlab/unidad-2-calculo-optimizacion` |
| III | Teoría de Grafos y Procesos Estocásticos | 15 | `python/unidad-3-grafos-estocasticos`, `matlab/unidad-3-grafos-estocasticos` |
| IV | Análisis Numérico y Transformada de Fourier | 15 | `python/unidad-4-numerico-fourier`, `matlab/unidad-4-numerico-fourier` |

Total: 60 horas (4 h/semana × 15 semanas).

## Estructura del repositorio

```
python/     ejercicios .py y notebooks, una carpeta por unidad
matlab/     scripts .m y Live Scripts, una carpeta por unidad
datos/      conjuntos de datos compartidos por los ejercicios
assets/     imágenes y material de apoyo
```

## Cómo usarlo

### Python

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
python python/unidad-1-algebra-lineal/01_operaciones_vectores.py
```

### MATLAB

Abrir MATLAB, situarse en la carpeta de la unidad y ejecutar el script:

```matlab
cd matlab/unidad-1-algebra-lineal
ej01_operaciones_vectores
```

## Convenciones

- Python: `NN_tema_descriptivo.py` con `NN` consecutivo dentro de la unidad (`01_`, `02_`, …).
- MATLAB: `ejNN_tema_descriptivo.m` — el prefijo `ej` es obligatorio porque MATLAB no admite nombres de script que empiecen con dígito.
- Cada ejercicio inicia con un comentario de encabezado: título, unidad, objetivo y fecha.
- Los datos de entrada van en `datos/`; las salidas generadas (figuras, `.mat`) no se versionan — ver `.gitignore`.
- Sin acentos ni espacios en nombres de archivo y carpeta; los acentos van en el contenido y en la documentación.

## Licencia

[MIT](LICENSE) — libre uso con atribución, pensado para material didáctico.
