# -*- coding: utf-8 -*-
"""
02 - Sistemas lineales: solucion general, espacio nulo y rango
Modulo 1: Algebra lineal y geometria diferencial
Objetivo: resolver A x = b describiendo el conjunto solucion completo como
x = x_p + N(A), mediante eliminacion gaussiana exacta sobre racionales: forma
escalonada reducida, base del espacio nulo por el metodo del -1, inversa por
Gauss-Jordan y rango.

Referencia: Deisenroth, Faisal y Ong (2020), Mathematics for Machine Learning,
Cap. 2, Sec. 2.3.1.

Ejecuta el script, cambia las matrices de entrada y vuelve a ejecutarlo.
"""

from fractions import Fraction

import numpy as np


# --- Impresion y conversion ---------------------------------------------------------

def fmt(x):
    """Formatea un racional: entero si el denominador es 1, con barra en caso contrario."""
    x = Fraction(x)
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def mostrar(M, titulo="", corte=None):
    """Imprime una matriz de racionales; `corte` marca la separacion de [A | b]."""
    if titulo:
        print(titulo)
    anchos = [max(len(fmt(fila[j])) for fila in M) for j in range(len(M[0]))]
    for fila in M:
        celdas = [fmt(v).rjust(anchos[j]) for j, v in enumerate(fila)]
        if corte is not None:
            celdas.insert(corte, "|")
        print("  [ " + "  ".join(celdas) + " ]")


def a_numpy(M):
    """Convierte una matriz de Fraction en un arreglo de float."""
    return np.array([[float(x) for x in fila] for fila in M])


def aumentada(A, b):
    return [list(fila) + [bi] for fila, bi in zip(A, b)]


# --- Eliminacion gaussiana exacta ---------------------------------------------------

def rref(M, trazar=False):
    """Forma escalonada reducida por Gauss-Jordan sobre racionales.

    Devuelve (R, pivotes) con `pivotes[i]` = columna del pivote de la fila i.
    """
    R = [[Fraction(x) for x in fila] for fila in M]
    m, n = len(R), len(R[0])
    pivotes, fila = [], 0

    for col in range(n):
        candidatos = [i for i in range(fila, m) if R[i][col] != 0]
        if not candidatos:                       # columna sin pivote -> variable libre
            continue

        # 1. intercambio, prefiriendo +-1 para no introducir fracciones
        i = min(candidatos, key=lambda k: (abs(R[k][col]) != 1, abs(R[k][col])))
        if i != fila:
            R[fila], R[i] = R[i], R[fila]
            if trazar:
                mostrar(R, f"R{fila + 1} <-> R{i + 1}")

        # 2. normalizacion del pivote a 1
        p = R[fila][col]
        if p != 1:
            R[fila] = [x / p for x in R[fila]]
            if trazar:
                mostrar(R, f"R{fila + 1} x 1/({fmt(p)})")

        # 3. anular el resto de la columna
        for k in range(m):
            if k != fila and R[k][col] != 0:
                factor = R[k][col]
                R[k] = [a - factor * c for a, c in zip(R[k], R[fila])]
        if trazar:
            mostrar(R, f"anular la columna {col + 1} fuera de R{fila + 1}")

        pivotes.append(col)
        fila += 1
        if fila == m:
            break

    return R, pivotes


def rango(M):
    """Numero de pivotes de la forma escalonada."""
    return len(rref(M)[1])


def nucleo_menos_uno(M):
    """Base del espacio nulo por el metodo del -1.

    Devuelve (A_tilde, base, pivotes, libres).
    """
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

    base = [[At[i][j] for i in range(n)] for j in libres]
    return At, base, pivotes, libres


def solucion_particular(A, b):
    """Solucion con las variables libres fijadas en 0; falla si el sistema es inconsistente."""
    R, piv = rref(aumentada(A, b))
    n = len(A[0])
    if piv and piv[-1] == n:
        raise ValueError("sistema inconsistente: rk(A) != rk([A|b])")
    x = [Fraction(0)] * n
    for i, j in enumerate(piv):
        x[j] = R[i][n]
    return x


def inversa_gauss_jordan(A):
    """Inversa exacta reduciendo [A | I] a [I | A^-1]; error si A es singular."""
    n = len(A)
    ident = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    R, pivotes = rref([list(fila) + ident[i] for i, fila in enumerate(A)])
    if pivotes[:n] != list(range(n)):
        raise ValueError(f"matriz singular: rk(A) = {len([j for j in pivotes if j < n])} < {n}")
    return [[R[i][n + j] for j in range(n)] for i in range(n)]


def main():
    np.set_printoptions(precision=4, suppress=True)

    # --- 1. A x es una combinacion lineal de las columnas de A ---
    A = np.array([[2.0, -1.0], [1.0, 3.0]])
    x = np.array([3.0, -2.0])
    print(f"A @ x                    = {A @ x}")
    print(f"3*c1 - 2*c2              = {3 * A[:, 0] - 2 * A[:, 1]}")

    # --- 2. Espacio nulo: N(B) = { t(-2, 1) } ---
    B = np.array([[1.0, 2.0], [2.0, 4.0]])
    print(f"\nB @ (-2, 1)              = {B @ np.array([-2.0, 1.0])}")
    print(f"columnas dependientes    : rk(B) = {np.linalg.matrix_rank(B)} < 2")

    # --- 3. Solucion general de A x = b: x = x_p + N(A) ---
    A4 = [[1, 0, 8, -4],
          [0, 1, 2, 12]]
    b4 = [42, 8]
    xp = solucion_particular(A4, b4)
    _, base, piv, libres = nucleo_menos_uno(A4)
    print(f"\nxp                       = ({', '.join(fmt(v) for v in xp)})")
    print(f"variables libres         : {[f'x{j + 1}' for j in libres]}")
    for k, v in enumerate(base, start=1):
        print(f"v{k}                       = ({', '.join(fmt(c) for c in v)})")

    A4n, b4n, xpn = a_numpy(A4), np.array(b4, dtype=float), np.array([float(v) for v in xp])
    rng = np.random.default_rng(1)
    for _ in range(3):
        lam = rng.normal(size=len(base))
        xx = xpn + sum(l * np.array([float(c) for c in v]) for l, v in zip(lam, base))
        print(f"  lambdas {np.round(lam, 3)} -> A @ x = {A4n @ xx}")

    # La solucion de norma minima es otro punto del mismo conjunto afin.
    x_min = np.linalg.lstsq(A4n, b4n, rcond=None)[0]
    print(f"lstsq (norma minima)     = {x_min}   norma {np.linalg.norm(x_min):.4f}")
    print(f"A @ (x_min - xp)         = {A4n @ (x_min - xpn)}  <- la diferencia esta en N(A)")

    # --- 4. Eliminacion gaussiana: consistencia segun el parametro a ---
    A5 = [[-2, 4, -2, -1, 4],
          [4, -8, 3, -3, 1],
          [1, -2, 1, -1, 1],
          [1, -2, 0, -3, 4]]
    print()
    for a in [-1, 0]:
        b5 = [-3, 2, 0, a]
        r_A, r_Ab = rango(A5), rango(aumentada(A5, b5))
        estado = "consistente" if r_A == r_Ab else "sin solucion"
        print(f"a = {a:>3}: rk(A) = {r_A}  rk([A|b]) = {r_Ab}  -> {estado}")

    R, _ = rref(aumentada(A5, [-3, 2, 0, -1]))
    mostrar(R, "\nRREF de [A | b] con a = -1:", corte=5)

    At, base5, piv5, libres5 = nucleo_menos_uno(A5)
    mostrar(At, "\nA tilde (metodo del -1):")
    xp5 = solucion_particular(A5, [-3, 2, 0, -1])
    print(f"\nxp = ({', '.join(fmt(v) for v in xp5)})")
    for k, v in enumerate(base5, start=1):
        vf = np.array([float(c) for c in v])
        print(f"v{k} = ({', '.join(fmt(c) for c in v)})   A @ v{k} = {a_numpy(A5) @ vf}")

    # --- 5. Rango: nulidad, invertibilidad y rango completo ---
    n_col = len(A5[0])
    print(f"\nn = {n_col}, rk(A) = {len(piv5)}, dim N(A) = {n_col - len(piv5)} "
          f"(rango-nulidad: {n_col - len(piv5) == len(base5)})")

    # --- 6. Inversa por Gauss-Jordan ---
    G = [[1, 0, 2, 0],
         [1, 1, 0, 0],
         [1, 2, 0, 1],
         [1, 1, 1, 1]]
    inv = inversa_gauss_jordan(G)
    mostrar(inv, "\nA^-1 por Gauss-Jordan:")
    print(f"coincide con np.linalg.inv: "
          f"{np.allclose(a_numpy(inv), np.linalg.inv(np.array(G, dtype=float)))}")

    try:
        inversa_gauss_jordan([[1, 2], [2, 4]])
    except ValueError as e:
        print(f"[[1,2],[2,4]] -> {e}")

    # --- 7. Rango numerico: con datos perturbados manda la tolerancia ---
    rng = np.random.default_rng(11)
    M0 = rng.normal(size=(60, 3)) @ rng.normal(size=(3, 8))     # rk exacto = 3
    print()
    for ruido in [0.0, 1e-10, 1e-2]:
        M = M0 + ruido * rng.normal(size=M0.shape)
        s = np.linalg.svd(M, compute_uv=False)
        print(f"ruido = {ruido:<7g} rk por defecto = {np.linalg.matrix_rank(M)}   "
              f"rk con tol = 1e-3*s1: {np.linalg.matrix_rank(M, tol=1e-3 * s[0])}")


if __name__ == "__main__":
    main()
