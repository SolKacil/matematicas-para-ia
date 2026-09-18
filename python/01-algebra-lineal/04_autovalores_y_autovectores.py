# -*- coding: utf-8 -*-
"""
04 - Autovalores y autovectores
Modulo 1: Algebra lineal y geometria diferencial
Objetivo: la definicion A v = lambda v, el polinomio caracteristico
det(A - lambda I) = 0, los autovectores como espacio nulo de A - lambda I, las
propiedades de las matrices simetricas y ortogonales, la diagonalizacion
A = P D P^-1 y el metodo de la potencia.

Referencia: Deisenroth, Faisal y Ong (2020), Mathematics for Machine Learning,
Secs. 4.1-4.4.

Ejecuta el script, cambia las matrices de entrada y vuelve a ejecutarlo.
"""

from fractions import Fraction

import numpy as np
import sympy as sp


def rref(M):
    """Forma escalonada reducida en aritmetica racional exacta (notebook 02)."""
    R = [[Fraction(x) for x in fila] for fila in M]
    m, n = len(R), len(R[0])
    pivotes, fila = [], 0
    for col in range(n):
        candidatos = [i for i in range(fila, m) if R[i][col] != 0]
        if not candidatos:
            continue
        i = min(candidatos, key=lambda k: (abs(R[k][col]) != 1, abs(R[k][col])))
        R[fila], R[i] = R[i], R[fila]
        p = R[fila][col]
        if p != 1:
            R[fila] = [x / p for x in R[fila]]
        for k in range(m):
            if k != fila and R[k][col] != 0:
                f = R[k][col]
                R[k] = [a - f * c for a, c in zip(R[k], R[fila])]
        pivotes.append(col)
        fila += 1
        if fila == m:
            break
    return R, pivotes


def nucleo_menos_uno(M):
    """Base del espacio nulo por el metodo del -1 (notebook 02)."""
    R, pivotes = rref(M)
    n = len(M[0])
    libres = [j for j in range(n) if j not in pivotes]
    At = [[Fraction(0)] * n for _ in range(n)]
    for i, j in enumerate(pivotes):
        At[j] = R[i][:]
    for j in libres:
        f = [Fraction(0)] * n
        f[j] = Fraction(-1)
        At[j] = f
    return [[At[i][j] for i in range(n)] for j in libres]


def espacio_propio(A, autovalor):
    """Base del espacio propio de un autovalor: el nucleo de A - lambda I."""
    n = len(A)
    desplazada = [[Fraction(A[i][j]) - (Fraction(autovalor) if i == j else 0)
                   for j in range(n)] for i in range(n)]
    return nucleo_menos_uno(desplazada)


def representante(vec):
    """Reescala un autovector para que su primera entrada no nula valga 1."""
    primera = next(x for x in vec if x != 0)
    return [x / primera for x in vec]


def polinomio_caracteristico(A):
    """Polinomio caracteristico simbolico y sus raices."""
    lam = sp.symbols("lambda")
    M = sp.Matrix(A)
    poli = sp.expand((M - lam * sp.eye(M.shape[0])).det())
    return poli, sp.solve(sp.Eq(poli, 0), lam)


def metodo_potencia(A, x0, iteraciones=8):
    """Itera x <- A x; devuelve (iteracion, x, normalizado, cociente de Rayleigh)."""
    x = np.asarray(x0, dtype=float)
    historial = []
    for k in range(1, iteraciones + 1):
        x = A @ x
        historial.append((k, x.copy(), x / np.abs(x).max(), (x @ (A @ x)) / (x @ x)))
    return historial


def main():
    np.set_printoptions(precision=4, suppress=True)

    # --- 1. Definicion: A v = lambda v ---
    A = np.array([[4.0, 1.0], [2.0, 3.0]])
    v, w = np.array([1.0, 1.0]), np.array([1.0, 0.0])
    print(f"A @ v = {A @ v} = 5 * v = {5 * v}  -> v es autovector")
    print(f"A @ w = {A @ w}, que no es multiplo de w = {w}  -> w no lo es")

    # --- 2. Polinomio caracteristico ---
    poli, raices = polinomio_caracteristico([[4, 1], [2, 3]])
    print(f"\npolinomio caracteristico: {poli}")
    print(f"factorizado: {sp.factor(poli)}   autovalores: {raices}")

    # --- 3. Autovectores: el nucleo de A - lambda I, en aritmetica exacta ---
    for lam_val in [5, 2]:
        for vec in espacio_propio([[4, 1], [2, 3]], lam_val):
            canonico = representante(vec)
            vf = np.array([float(x) for x in canonico])
            print(f"lambda = {lam_val}: v = ({', '.join(str(x) for x in canonico)})   "
                  f"A @ v = {A @ vf} = {lam_val} * v")

    valores, vectores = np.linalg.eig(A)
    print(f"\nnp.linalg.eig -> autovalores {valores}, autovectores normalizados:\n{vectores}")

    # --- 4. Matrices simetricas: autovalores reales y autovectores ortogonales ---
    S = np.array([[2.0, 1.0], [1.0, 2.0]])
    for lam_val in [3, 1]:
        for vec in espacio_propio([[2, 1], [1, 2]], lam_val):
            print(f"lambda = {lam_val}: v = ({', '.join(str(x) for x in representante(vec))})")
    print(f"(1,1) . (1,-1) = {np.array([1.0, 1.0]) @ np.array([1.0, -1.0])} -> ortogonales")

    rng = np.random.default_rng(0)
    for n in [3, 5]:
        X = rng.normal(size=(n, n))
        Msim = X + X.T
        _, V = np.linalg.eigh(Msim)
        print(f"n = {n}: autovalores reales {np.allclose(np.linalg.eigvals(Msim).imag, 0)}, "
              f"autovectores ortonormales {np.allclose(V.T @ V, np.eye(n))}")

    # --- 5. Matrices ortogonales: todos los autovalores tienen modulo 1 ---
    print()
    for grados in [30.0, 90.0]:
        t = np.radians(grados)
        Rot = np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])
        val = np.linalg.eigvals(Rot)
        print(f"rotacion de {grados:>5.1f} grados: autovalores {np.round(val, 4)}   "
              f"modulos {np.round(np.abs(val), 6)}")

    # --- 6. Diagonalizacion y potencias ---
    P = np.array([[1.0, 1.0], [1.0, -2.0]])
    D = np.diag([5.0, 2.0])
    print(f"\nP D P^-1 == A: {np.allclose(P @ D @ np.linalg.inv(P), A)}")

    val_s, P_s = np.linalg.eigh(S)
    print(f"caso simetrico: P ortogonal {np.allclose(P_s.T @ P_s, np.eye(2))}, "
          f"P D P.T == S: {np.allclose(P_s @ np.diag(val_s) @ P_s.T, S)}")

    k = 12
    print(f"A^{k} = P D^{k} P^-1: "
          f"{np.allclose(np.linalg.matrix_power(A, k), P @ np.diag(np.diag(D) ** k) @ np.linalg.inv(P))}")

    # El radio espectral decide el comportamiento a largo plazo.
    print()
    for nombre, Mat in [("estable", np.array([[0.5, 0.1], [0.0, 0.3]])),
                        ("inestable", np.array([[1.2, 0.1], [0.0, 0.9]]))]:
        radio = max(abs(np.linalg.eigvals(Mat)))
        normas = [np.linalg.norm(np.linalg.matrix_power(Mat, j)) for j in [1, 10, 50]]
        print(f"{nombre:>10}: radio espectral {radio:.2f}   ||M^k|| k=1,10,50: {np.round(normas, 4)}")

    # --- 7. PCA: autovectores de la matriz de covarianza ---
    rng = np.random.default_rng(3)
    base = rng.normal(size=(300, 2)) @ np.array([[2.5, 0.0], [0.0, 0.6]])
    t = np.radians(30)
    giro = np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])
    datos = base @ giro.T
    centrados = datos - datos.mean(axis=0)
    cov = (centrados.T @ centrados) / (len(centrados) - 1)
    val_pca, vec_pca = np.linalg.eigh(cov)
    orden = np.argsort(val_pca)[::-1]
    val_pca, vec_pca = val_pca[orden], vec_pca[:, orden]
    print(f"\nautovalores de la covarianza: {np.round(val_pca, 4)}")
    print(f"componentes principales (columnas):\n{np.round(vec_pca, 4)}")
    print(f"varianza explicada por la primera: {val_pca[0] / val_pca.sum():.1%}")

    # --- 8. Metodo de la potencia ---
    print(f"\n{'iter':>4} | {'x_k':>22} | {'normalizado':>18} | {'lambda estimado':>16}")
    for k, xk, norm, ray in metodo_potencia(A, [1.0, 0.0]):
        print(f"{k:>4} | {str(np.round(xk, 1)):>22} | {str(np.round(norm, 3)):>18} | {ray:>16.6f}")
    print("converge al autovector dominante (1, 1) con autovalor 5")


if __name__ == "__main__":
    main()
