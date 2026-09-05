# -*- coding: utf-8 -*-
"""
02 - Suma, producto por escalar y multiplicacion
Modulo 1: Algebra lineal y geometria diferencial
Objetivo: suma de vectores y de matrices, producto por escalar, los tres
productos entre vectores (punto, elemento a elemento y externo) y la
multiplicacion de matrices, escrita a mano y verificada contra NumPy.

Ejecuta el script, cambia los vectores y las matrices, y vuelve a ejecutarlo.
"""

import numpy as np


def multiplicar_a_mano(A, B):
    """Producto matricial siguiendo la definicion c[i,j] = suma_k a[i,k]*b[k,j]."""
    n, m = A.shape
    m2, p = B.shape
    if m != m2:
        raise ValueError(f"no se puede multiplicar {A.shape} por {B.shape}")

    C = np.zeros((n, p))
    for i in range(n):
        for j in range(p):
            for k in range(m):
                C[i, j] += A[i, k] * B[k, j]
    return C


def capa_densa(X, W, b):
    """Una capa densa con ReLU: producto de matrices, suma del sesgo y activacion."""
    return np.maximum(0.0, X @ W + b)


def main():
    np.set_printoptions(precision=4, suppress=True)

    # --- 1. Suma de vectores: componente a componente, misma dimension ---
    u = np.array([3.0, 1.0])
    v = np.array([1.0, 4.0])
    print(f"u = {u}")
    print(f"v = {v}")
    print(f"u + v = {u + v}")
    print(f"u - v = {u - v}")

    # --- 2. Producto por escalar: estira, encoge o voltea ---
    print(f"\n2 * u    = {2 * u}   norma {np.linalg.norm(2 * u):.4f}")
    print(f"-1.5 * u = {-1.5 * u}   norma {np.linalg.norm(-1.5 * u):.4f}")

    # Suma y escalar juntos: un paso de descenso de gradiente.
    pesos = np.array([1.0, -2.0, 0.5])
    grad = np.array([0.4, 0.1, -0.3])
    print(f"\npesos - 0.1*gradiente = {pesos - 0.1 * grad}")

    # --- 3. Los tres productos entre vectores ---
    a = np.array([1.0, 2.0, 3.0])
    b = np.array([4.0, 0.0, -1.0])
    print(f"\na = {a}")
    print(f"b = {b}")
    print(f"producto punto      : {np.dot(a, b)}  (un escalar)")
    print(f"elemento a elemento : {a * b}  (ojo: * NO es el producto punto)")
    print(f"producto externo    : forma {np.outer(a, b).shape}")
    print(np.outer(a, b))

    # --- 4. Suma de matrices: misma forma, elemento a elemento ---
    A = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
    B = np.array([[10.0, 20.0], [30.0, 40.0], [50.0, 60.0]])
    print(f"\nA + B =\n{A + B}")

    # Broadcasting: sumar un vector a todas las filas (asi se aplica el sesgo).
    lote = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
    sesgo = np.array([100.0, 200.0, 300.0])
    print(f"\nlote + sesgo =\n{lote + sesgo}")

    # --- 5. Matriz por escalar ---
    print(f"\n3 * A =\n{3 * A}")

    # --- 6. Multiplicacion de matrices: (n x m)(m x p) = (n x p) ---
    M = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])      # 2x3
    N = np.array([[7.0, 8.0], [9.0, 10.0], [11.0, 12.0]])  # 3x2
    print(f"\nM {M.shape} @ N {N.shape} -> {(M @ N).shape}")
    print(f"a mano =\n{multiplicar_a_mano(M, N)}")
    print(f"numpy  =\n{M @ N}")
    print(f"iguales: {np.allclose(multiplicar_a_mano(M, N), M @ N)}")

    # El orden importa: AB no es BA.
    R = np.array([[0.0, -1.0], [1.0, 0.0]])   # rotacion de 90 grados
    S = np.array([[3.0, 0.0], [0.0, 1.0]])    # estirar 3x en horizontal
    print(f"\nR @ S =\n{R @ S}")
    print(f"S @ R =\n{S @ R}")
    print(f"son iguales? {np.allclose(R @ S, S @ R)}")

    # --- 7. Todo junto: una capa densa Y = XW + b ---
    np.random.seed(0)
    X = np.array([[0.5, 2.0, -1.0], [1.0, 0.0, 3.0],
                  [-2.0, 1.5, 0.5], [0.0, -1.0, 1.0]])   # 4 muestras x 3 rasgos
    W = np.random.randn(3, 2)                            # 3 entradas -> 2 neuronas
    sesgo_capa = np.array([0.1, -0.2])
    salida = capa_densa(X, W, sesgo_capa)
    print(f"\nX {X.shape} @ W {W.shape} + b -> salida {salida.shape}")
    print(salida)


if __name__ == "__main__":
    main()
