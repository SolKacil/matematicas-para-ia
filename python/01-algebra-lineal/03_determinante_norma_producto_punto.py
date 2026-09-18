# -*- coding: utf-8 -*-
"""
03 - Determinante, norma, producto punto y ortogonalidad
Modulo 1: Algebra lineal y geometria diferencial
Objetivo: las nociones de medida sobre un espacio vectorial -area y volumen
(determinante), longitud (norma), alineacion (producto punto) y perpendicularidad
(ortogonalidad)-, escritas a mano y verificadas contra NumPy.

Referencia: Deisenroth, Faisal y Ong (2020), Mathematics for Machine Learning,
Secs. 3.1-3.4 y 4.1.

Ejecuta el script, cambia los vectores y las matrices, y vuelve a ejecutarlo.
"""

import numpy as np


def det2(A):
    """Determinante de una matriz 2x2: ad - bc."""
    (a, b), (c, d) = A
    return a * d - b * c


def det3_sarrus(A):
    """Determinante 3x3 por la regla de Sarrus."""
    a = A
    return (a[0, 0] * a[1, 1] * a[2, 2] + a[0, 1] * a[1, 2] * a[2, 0]
            + a[0, 2] * a[1, 0] * a[2, 1] - a[0, 2] * a[1, 1] * a[2, 0]
            - a[0, 0] * a[1, 2] * a[2, 1] - a[0, 1] * a[1, 0] * a[2, 2])


def norma(x):
    """Norma euclidiana a partir de la definicion."""
    return np.sqrt(sum(xi ** 2 for xi in x))


def producto_punto(x, y):
    """Suma de los productos componente a componente."""
    return sum(xi * yi for xi, yi in zip(x, y))


def angulo(x, y, en_grados=True):
    """Angulo entre dos vectores, despejado del producto punto."""
    coseno = producto_punto(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))
    theta = np.arccos(np.clip(coseno, -1.0, 1.0))
    return np.degrees(theta) if en_grados else theta


def normalizar(x):
    """Vector unitario con la misma direccion."""
    return np.asarray(x, dtype=float) / np.linalg.norm(x)


def similitud_coseno(X, Y):
    """Matriz de similitudes coseno entre las filas de X y las de Y."""
    Xn = X / np.linalg.norm(X, axis=1, keepdims=True)
    Yn = Y / np.linalg.norm(Y, axis=1, keepdims=True)
    return Xn @ Yn.T


def softmax(Z, eje=-1):
    Z = Z - Z.max(axis=eje, keepdims=True)
    E = np.exp(Z)
    return E / E.sum(axis=eje, keepdims=True)


def atencion(Q, K, V):
    """Atencion por producto punto escalado: softmax(Q K^T / sqrt(d_k)) V."""
    pesos = softmax(Q @ K.T / np.sqrt(Q.shape[-1]))
    return pesos @ V, pesos


def main():
    np.set_printoptions(precision=4, suppress=True)

    # --- 1. Determinante: area con signo y criterio de singularidad ---
    A = np.array([[3.0, 1.0], [2.0, 4.0]])
    B = np.array([[1.0, 2.0], [2.0, 4.0]])
    print(f"det(A) a mano = {det2(A)}   np.linalg.det = {np.linalg.det(A):.4f}")
    print(f"area del paralelogramo de las columnas de A = {abs(det2(A))}")
    print(f"det(B) = {det2(B)} -> B singular, rango {np.linalg.matrix_rank(B)} < 2")
    print(f"intercambiar columnas invierte el signo: {det2(A[:, [1, 0]])}")

    M = np.array([[2.0, 0.0, 1.0], [1.0, 3.0, 2.0], [0.0, 1.0, 1.0]])
    print(f"\nSarrus 3x3 = {det3_sarrus(M)}   np.linalg.det = {np.linalg.det(M):.4f}")

    rng = np.random.default_rng(0)
    P, Q = rng.normal(size=(3, 3)), rng.normal(size=(3, 3))
    print(f"det(PQ) = {np.linalg.det(P @ Q):.6f} = det(P)det(Q) = "
          f"{np.linalg.det(P) * np.linalg.det(Q):.6f}")
    print(f"det(P.T) = det(P): {np.isclose(np.linalg.det(P.T), np.linalg.det(P))}")
    print(f"det(P) = producto de los autovalores: "
          f"{np.isclose(np.linalg.det(P), np.prod(np.linalg.eigvals(P)).real)}")

    # El determinante no sirve como diagnostico numerico de singularidad.
    pequena = 0.1 * np.eye(20)
    print(f"\ndet(0.1*I_20) = {np.linalg.det(pequena):.1e} pero cond = "
          f"{np.linalg.cond(pequena):.1f}: perfectamente invertible")

    # --- 2. Norma ---
    x = np.array([3.0, 4.0])
    print(f"\n||x|| a mano = {norma(x)}   np.linalg.norm = {np.linalg.norm(x)}")
    print(f"L1 = {np.linalg.norm(x, 1)}   L2 = {np.linalg.norm(x, 2)}   "
          f"Linf = {np.linalg.norm(x, np.inf)}")

    # --- 3. Producto punto: alineacion y angulo ---
    u = np.array([1.0, 0.0])
    v = np.array([1.0, 1.0])
    print(f"\nu . v = {producto_punto(u, v)}   angulo = {angulo(u, v):.1f} grados")
    print(f"x . x == ||x||^2: {producto_punto(x, x)} == {np.linalg.norm(x) ** 2}")

    for nombre, w in [("misma direccion", np.array([3.0, 0.0])),
                      ("perpendicular", np.array([0.0, 2.0])),
                      ("opuesto", np.array([-2.0, 0.0]))]:
        print(f"  {nombre:>16}: u . w = {producto_punto(u, w):>5.1f}   "
              f"angulo = {angulo(u, w):>5.1f} grados")

    # --- 4. Similitud coseno y atencion ---
    emb = np.array([[1.0, 0.2, 0.1], [0.9, 0.3, 0.15], [0.1, 1.0, 0.0], [-1.0, -0.2, -0.1]])
    print(f"\nmatriz de similitudes coseno:\n{np.round(similitud_coseno(emb, emb), 3)}")

    rng = np.random.default_rng(3)
    salida, pesos = atencion(rng.normal(size=(2, 4)), rng.normal(size=(5, 4)),
                             rng.normal(size=(5, 3)))
    print(f"\npesos de atencion (cada fila suma 1): {np.round(pesos.sum(axis=1), 6)}")
    print(f"salida de la atencion: {salida.shape}")

    # --- 5. Norma y regularizacion L2 ---
    X = rng.normal(size=(15, 8))
    y = X @ np.array([2.0, -1.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0]) + 0.1 * rng.normal(size=15)
    print()
    for lam in [0.0, 1.0, 10.0]:
        theta = np.linalg.solve(X.T @ X + lam * np.eye(8), X.T @ y)
        print(f"lambda = {lam:>5}: ||theta|| = {np.linalg.norm(theta):.3f}   "
              f"error = {np.linalg.norm(X @ theta - y) ** 2:.4f}")

    # --- 6. Ortogonalidad ---
    p, q = np.array([2.0, 3.0]), np.array([3.0, -2.0])
    print(f"\np . q = {producto_punto(p, q)} -> ortogonales ({angulo(p, q):.1f} grados)")
    print(f"x normalizado = {normalizar(x)}   norma = {np.linalg.norm(normalizar(x))}")

    R = np.array([[0.0, -1.0], [1.0, 0.0]])
    print(f"\nR ortogonal (R.T @ R == I): {np.allclose(R.T @ R, np.eye(2))}")
    print(f"R^-1 == R.T: {np.allclose(np.linalg.inv(R), R.T)}   det(R) = {np.linalg.det(R):.1f}")

    a, c = rng.normal(size=2), rng.normal(size=2)
    print(f"preserva normas   : {np.isclose(np.linalg.norm(a), np.linalg.norm(R @ a))}")
    print(f"preserva angulos  : {np.isclose(angulo(a, c), angulo(R @ a, R @ c))}")
    print(f"preserva distancias: {np.isclose(np.linalg.norm(a - c), np.linalg.norm(R @ a - R @ c))}")

    # --- 7. Ortogonalidad y estabilidad en redes profundas ---
    rng = np.random.default_rng(11)
    n, capas = 64, 60
    senal = rng.normal(size=n)
    W_gauss = rng.normal(size=(n, n)) * 0.15
    W_ort = np.linalg.qr(rng.normal(size=(n, n)))[0]

    xg = xo = senal
    for _ in range(capas):
        xg, xo = W_gauss @ xg, W_ort @ xo
    print(f"\nnorma inicial {np.linalg.norm(senal):.4f}")
    print(f"tras {capas} capas gaussianas : {np.linalg.norm(xg):.3e}")
    print(f"tras {capas} capas ortogonales: {np.linalg.norm(xo):.4f}  <- inalterada")


if __name__ == "__main__":
    main()
