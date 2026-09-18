# Cómo contribuir

Este repositorio es material didáctico abierto. Toda aportación que ayude a que alguien
entienda mejor un concepto es bienvenida: no hace falta ser experto.

## Qué aporta más

- **Correcciones**: errores de matemáticas, de código o de redacción.
- **Ejercicios nuevos** dentro de los cuatro módulos existentes.
- **Explicaciones**: comentarios que aclaren *por qué* se hace un paso, no solo *qué* hace.
- **Datos de ejemplo** pequeños y de licencia libre, en `datos/`.

## Reglas para un ejercicio

1. Un archivo por concepto. Que corra solo, sin depender de otros scripts.
2. Encabezado obligatorio: título, módulo y objetivo en una línea.
3. Solo dependencias que ya estén en `requirements.txt`; si necesitas otra, dilo en el pull request.
4. Nombres de archivo sin acentos ni espacios (`03_descenso_gradiente.py`).
   Los acentos van en el contenido.
5. Que imprima resultados legibles. El objetivo es que quien lo ejecute vea de inmediato
   qué pasó y pueda compararlo con lo que esperaba.
6. Prefiere lo explícito a lo ingenioso: aquí el código se lee más veces de las que se ejecuta.

## Notebooks

[`python/01-algebra-lineal/00_propiedades_matrices.ipynb`](python/01-algebra-lineal/00_propiedades_matrices.ipynb)
es la plantilla: cópialo y sustituye el contenido. La estructura que sigue todo notebook es:

1. **Insignia de Colab** en la primera línea, apuntando a la ruta del propio notebook:
   `https://colab.research.google.com/github/SolKacil/matematicas-para-ia/blob/main/<ruta>.ipynb`
2. **Portada**: título, módulo, por qué el tema importa en IA, qué vas a poder hacer al
   terminar, qué se da por sabido y cómo usar el notebook.
3. **Celda de imports** al inicio, con solo lo que esté en `requirements.txt`.
4. **Secciones numeradas**: explicación en markdown (con LaTeX entre `$…$`) y luego el código.
   Donde se pueda, implementa la operación a mano *y* con la biblioteca, y compara las dos.
5. **Una gráfica** cuando ayude a ver la idea, no de adorno.
6. **Tu turno**: ejercicios sin respuestas, con una celda vacía para resolverlos.
7. **Resumen** en tabla, y enlaces al documento de la sesión, al notebook
   siguiente y al README.

Antes de enviarlo: *Restart & Run All*, y guarda con las salidas incluidas, para que quien lo
lea en GitHub vea los resultados sin ejecutar nada.

## Notebooks que acompañan a un documento del curso

Los notebooks de `python/01-algebra-lineal` desarrollan, uno a uno, los documentos
`Matematicas_para_IA_NN.pdf` de la Unidad I. Si aportas uno nuevo de esa serie, conserva la
correspondencia: el número del notebook es el del documento, las secciones siguen su orden y
la sección **Tu turno** recoge sus ejercicios propuestos. El registro es formal, sin
analogías, y cada bloque de aplicación en IA va rotulado como *Lectura en aprendizaje
automático*.

## Flujo

1. Haz un fork y crea una rama descriptiva (`ejercicio-svd`, `fix-angulo-vectores`).
2. Ejecuta tu script antes de enviarlo y comprueba la salida.
3. Abre un pull request explicando qué concepto cubre y a quién le sirve.

## Dudas y sugerencias

Abre un *issue*. También valen las preguntas del tipo «este tema no se entiende»:
sirven para saber qué falta explicar mejor.
