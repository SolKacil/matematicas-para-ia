# -*- coding: utf-8 -*-
"""
00 - Propiedades de matrices: suma, multiplicacion, identidad y transpuesta
Modulo 1: Algebra lineal y geometria diferencial
Objetivo: las cuatro operaciones basicas sobre matrices, sus condiciones de
forma y sus propiedades, escritas a mano y verificadas contra NumPy.

Referencia: Deisenroth, Faisal y Ong (2020), Mathematics for Machine Learning,
Sec. 2.2.

Ejecuta el script, cambia las matrices de entrada y vuelve a ejecutarlo.
"""

import numpy as np


def multiplicar(A, B):
    """Producto matricial a partir de la definicion c[i,j] = sum_p a[i,p]*b[p,j]."""
    m, n = A.shape
    n2, k = B.shape
    if n != n2:
        raise ValueError(f"formas incompatibles: {A.shape} por {B.shape}")

    C = np.zeros((m, k))
    for i in range(m):
        for j in range(k):
            for p in range(n):
                C[i, j] += A[i, p] * B[p, j]
    return C


def es_simetrica(A):
    """Una matriz es simetrica si es cuadrada y coincide con su transpuesta."""
    return A.ndim == 2 and A.shape[0] == A.shape[1] and np.allclose(A, A.T)


def bloque_residual(x, W, b):
    """Conexion residual y = x + F(x): la identidad es el comportamiento por defecto."""
    return x + np.maximum(0.0, x @ W + b)


def main():
    np.set_printoptions(precision=4, suppress=True)

    # --- 1. Forma: primero filas, despues columnas ---
    A = np.array([[1.0, 2.0, 3.0],
                  [4.0, 5.0, 6.0]])
    print(f"A =\n{A}")
    print(f"forma {A.shape}: {A.shape[0]} filas, {A.shape[1]} columnas")

    # --- 2. Suma: entrada por entrada, misma forma ---
    A2 = np.array([[1.0, 2.0], [3.0, 4.0]])
    B2 = np.array([[5.0, 0.0], [1.0, 2.0]])
    C2 = np.array([[2.0, -1.0], [0.0, 3.0]])
    print(f"\nA + B =\n{A2 + B2}")
    print(f"conmutativa: {np.allclose(A2 + B2, B2 + A2)}   "
          f"asociativa: {np.allclose((A2 + B2) + C2, A2 + (B2 + C2))}")

    try:
        A + A.T                                   # (2,3) + (3,2)
    except ValueError as e:
        print(f"sumar (2,3) con (3,2) -> {e}")

    # --- 3. Producto por escalar ---
    lam, psi = 3.0, -2.0
    print(f"\n3 * A2 =\n{lam * A2}")
    print(f"distributiva: {np.allclose((lam + psi) * C2, lam * C2 + psi * C2)}")

    # --- 4. Producto matricial: (m,n)(n,k) = (m,k) ---
    A4 = np.array([[1.0, 2.0], [3.0, 4.0]])
    B4 = np.array([[2.0, 0.0], [1.0, 2.0]])
    print(f"\na mano =\n{multiplicar(A4, B4)}")
    print(f"numpy  =\n{A4 @ B4}")
    print(f"iguales: {np.allclose(multiplicar(A4, B4), A4 @ B4)}")

    # El orden importa: AB no es BA.
    print(f"\nB @ A =\n{B4 @ A4}")
    print(f"AB == BA: {np.allclose(A4 @ B4, B4 @ A4)}  <- en general, no")

    # Y '*' no es '@': el asterisco es el producto de Hadamard.
    print(f"\nA * B (Hadamard) =\n{A4 * B4}")
    print(f"A @ B (matricial) =\n{A4 @ B4}")

    # Propiedades.
    D4 = np.array([[1.0, 2.0], [0.0, 1.0]])
    print(f"\nasociativa   (A@B)@C == A@(B@C): {np.allclose((A4 @ B4) @ C2, A4 @ (B4 @ C2))}")
    print(f"distributiva (A+B)@C == A@C+B@C: {np.allclose((A4 + B4) @ C2, A4 @ C2 + B4 @ C2)}")
    print(f"distributiva A@(C+D) == A@C+A@D: {np.allclose(A4 @ (C2 + D4), A4 @ C2 + A4 @ D4)}")

    # --- 5. Identidad: el neutro del producto ---
    print(f"\nI @ A == A: {np.allclose(np.eye(2) @ A4, A4)}   "
          f"A @ I == A: {np.allclose(A4 @ np.eye(2), A4)}")

    rng = np.random.default_rng(0)
    x = rng.normal(size=(4, 3))
    W = rng.normal(size=(3, 3)) * 0.1
    print(f"bloque residual con W = 0 es la identidad: "
          f"{np.allclose(bloque_residual(x, np.zeros((3, 3)), np.zeros(3)), x)}")

    # --- 6. Transpuesta: (AB)^T = B^T A^T, con el orden invertido ---
    print(f"\nA.T =\n{A.T}  (forma {A.T.shape})")
    print(f"(A.T).T == A         : {np.allclose(A.T.T, A)}")
    print(f"(A+B).T == A.T + B.T : {np.allclose((A4 + B4).T, A4.T + B4.T)}")
    print(f"(A@B).T == B.T @ A.T : {np.allclose((A4 @ B4).T, B4.T @ A4.T)}")
    print(f"(A@B).T == A.T @ B.T : {np.allclose((A4 @ B4).T, A4.T @ B4.T)}  <- falso")

    # Matrices simetricas: X^T X lo es siempre.
    X = rng.normal(size=(6, 3))
    print(f"\n[[2,1],[1,2]] simetrica: {es_simetrica(np.array([[2.0, 1.0], [1.0, 2.0]]))}")
    print(f"X.T @ X simetrica      : {es_simetrica(X.T @ X)}  (forma {(X.T @ X).shape})")
    print(f"X @ X.T simetrica      : {es_simetrica(X @ X.T)}  (forma {(X @ X.T).shape})")

    # --- 7. La transpuesta en la propagacion hacia atras ---
    W = rng.normal(size=(4, 3))
    x = rng.normal(size=4)
    grad_y = rng.normal(size=3)
    print(f"\nadelante: W.T @ x -> {(W.T @ x).shape}   atras: W @ grad_y -> {(W @ grad_y).shape}")
    print(f"grad_W = outer(x, grad_y) -> {np.outer(x, grad_y).shape}, igual que W {W.shape}")

    # --- 8. Promediar modelos: una suma de matrices ---
    replicas = [rng.normal(size=(2, 2)) for _ in range(4)]
    print(f"\npromedio de 4 modelos =\n{sum(replicas) / len(replicas)}")


if __name__ == "__main__":
    main()
