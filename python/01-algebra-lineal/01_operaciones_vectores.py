# -*- coding: utf-8 -*-
"""
01 - Operaciones basicas con vectores y matrices
Modulo 1: Algebra lineal y geometria diferencial
Objetivo: producto punto, norma, angulo entre vectores, producto matricial,
determinante y valores/vectores propios: el vocabulario minimo con el que se
describen los datos y los pesos de un modelo.

Ejecuta el script, cambia los valores de u, v y A, y vuelve a ejecutarlo.
"""

import numpy as np


def angulo_entre(u, v):
    """Angulo en grados entre dos vectores."""
    cos = np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v))
    return np.degrees(np.arccos(np.clip(cos, -1.0, 1.0)))


def main():
    u = np.array([3.0, 4.0])
    v = np.array([1.0, 0.0])

    print(f"u = {u}")
    print(f"v = {v}")
    print(f"producto punto  : {np.dot(u, v):.4f}")
    print(f"norma de u      : {np.linalg.norm(u):.4f}")
    print(f"angulo u-v      : {angulo_entre(u, v):.2f} grados")

    A = np.array([[2.0, 1.0], [1.0, 3.0]])
    print(f"\nA =\n{A}")
    print(f"A @ u = {A @ u}")
    print(f"det(A) = {np.linalg.det(A):.4f}")

    valores, vectores = np.linalg.eig(A)
    print(f"valores propios  : {valores}")
    print(f"vectores propios :\n{vectores}")


if __name__ == "__main__":
    main()
