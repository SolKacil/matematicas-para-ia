# Cómo contribuir

Este repositorio es material didáctico abierto. Toda aportación que ayude a que alguien
entienda mejor un concepto es bienvenida: no hace falta ser experto.

## Qué aporta más

- **Correcciones**: errores de matemáticas, de código o de redacción.
- **Ejercicios nuevos** dentro de los cuatro módulos existentes.
- **La versión que falta**: muchos temas están solo en Python o solo en MATLAB.
- **Explicaciones**: comentarios que aclaren *por qué* se hace un paso, no solo *qué* hace.
- **Datos de ejemplo** pequeños y de licencia libre, en `datos/`.

## Reglas para un ejercicio

1. Un archivo por concepto. Que corra solo, sin depender de otros scripts.
2. Encabezado obligatorio: título, módulo y objetivo en una línea.
3. Solo dependencias que ya estén en `requirements.txt`; si necesitas otra, dilo en el pull request.
4. Nombres de archivo sin acentos ni espacios (`03_descenso_gradiente.py`,
   `ej03_descenso_gradiente.m`). Los acentos van en el contenido.
5. Que imprima resultados legibles. El objetivo es que quien lo ejecute vea de inmediato
   qué pasó y pueda compararlo con lo que esperaba.
6. Prefiere lo explícito a lo ingenioso: aquí el código se lee más veces de las que se ejecuta.

## Flujo

1. Haz un fork y crea una rama descriptiva (`ejercicio-svd`, `fix-angulo-vectores`).
2. Ejecuta tu script antes de enviarlo y comprueba la salida.
3. Abre un pull request explicando qué concepto cubre y a quién le sirve.

## Dudas y sugerencias

Abre un *issue*. También valen las preguntas del tipo «este tema no se entiende»:
sirven para saber qué falta explicar mejor.
