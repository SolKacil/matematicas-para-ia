# -*- coding: utf-8 -*-
"""
01 - Vectores y espacios vectoriales
Modulo 1: Algebra lineal y geometria diferencial
Objetivo: grupos, el grupo lineal general GL(n, R), los axiomas de espacio
vectorial y el criterio practico de subespacio, verificados con codigo y,
sobre todo, refutados con contraejemplos.

Referencia: Deisenroth, Faisal y Ong (2020), Mathematics for Machine Learning,
Sec. 2.4.

Nota sobre el metodo: un contraejemplo demuestra que una propiedad universal es
falsa; no hallarlo entre unas cuantas muestras no demuestra que sea verdadera.

Ejecuta el script, cambia los conjuntos y las operaciones, y vuelve a ejecutarlo.
"""

import numpy as np


def verificar_grupo(elementos, op, nombre="G"):
    """Comprueba los cuatro axiomas de grupo por enumeracion sobre un conjunto finito."""
    conjunto = list(elementos)
    pertenece = set(conjunto)

    cerradura = all(op(x, y) in pertenece for x in conjunto for y in conjunto)
    asociativa = all(op(op(x, y), z) == op(x, op(y, z))
                     for x in conjunto for y in conjunto for z in conjunto)
    neutros = [e for e in conjunto if all(op(x, e) == x == op(e, x) for x in conjunto)]
    e = neutros[0] if neutros else None

    if e is None:
        sin_inverso = conjunto
    else:
        sin_inverso = [x for x in conjunto
                       if not any(op(x, y) == e == op(y, x) for y in conjunto)]

    abeliano = all(op(x, y) == op(y, x) for x in conjunto for y in conjunto)
    es_grupo = cerradura and asociativa and e is not None and not sin_inverso

    etiqueta = "grupo abeliano" if es_grupo and abeliano else "grupo" if es_grupo else "NO es grupo"
    print(f"{nombre:>22}: cerradura={cerradura} asociativa={asociativa} neutro={e} "
          f"-> {etiqueta}")
    if sin_inverso and e is not None:
        print(f"{'':>22}  sin inverso: {sin_inverso[:5]}")
    return es_grupo


def criterio_subespacio(pertenece, muestras, escalares=(-2.0, -0.5, 0.0, 3.0), nombre="U"):
    """Aplica por muestreo las tres condiciones del criterio practico de subespacio."""
    dim = len(muestras[0])
    tiene_cero = bool(pertenece(np.zeros(dim)))

    fallo_escalar = next(((v, lam) for v in muestras for lam in escalares
                          if not pertenece(lam * np.asarray(v, dtype=float))), None)
    fallo_suma = next(((u, v) for u in muestras for v in muestras
                       if not pertenece(np.asarray(u, float) + np.asarray(v, float))), None)

    print(f"{nombre:>26}: contiene 0 = {tiene_cero}", end="")
    if fallo_escalar is not None:
        v, lam = fallo_escalar
        print(f"   falla escalar: {lam} * {np.asarray(v)}", end="")
    if fallo_suma is not None:
        u, v = fallo_suma
        print(f"   falla suma: {np.asarray(u)} + {np.asarray(v)}", end="")
    veredicto = tiene_cero and fallo_escalar is None and fallo_suma is None
    print(f"   -> {'compatible con ser subespacio' if veredicto else 'NO es subespacio'}")
    return veredicto


def main():
    np.set_printoptions(precision=4, suppress=True)

    # --- 1. Grupos finitos: verificacion exhaustiva ---
    verificar_grupo(range(5), lambda x, y: (x + y) % 5, "(Z_5, +)")
    verificar_grupo(range(5), lambda x, y: (x * y) % 5, "(Z_5, *)")
    verificar_grupo(range(1, 5), lambda x, y: (x * y) % 5, "(Z_5 sin 0, *)")

    # --- 2. Conjuntos infinitos: basta exhibir el contraejemplo ---
    print("\n(N_0, +): el inverso de 3 seria -3, que no pertenece a N_0 -> NO es grupo")
    print("(Z, .)  : el inverso de 2 seria 0.5, que no es entero      -> NO es grupo")

    A = np.array([[1.0, 2.0], [0.0, 1.0]])
    B = np.array([[2.0, 0.0], [1.0, 3.0]])
    C = np.array([[1.0, 1.0], [2.0, 0.0]])
    print(f"\n(R^2x2, .): asociativa {np.allclose((A @ B) @ C, A @ (B @ C))}, "
          f"neutro I2, pero [[1,2],[2,4]] es singular -> NO es grupo")

    # --- 3. GL(n, R): las invertibles si forman grupo, y no es abeliano ---
    print(f"\nA @ B =\n{A @ B}")
    print(f"B @ A =\n{B @ A}")
    print(f"conmutan: {np.allclose(A @ B, B @ A)}  -> GL(2, R) no es abeliano")
    print(f"cerradura: det(A@B) = {np.linalg.det(A @ B):.4f} = "
          f"det(A)*det(B) = {np.linalg.det(A) * np.linalg.det(B):.4f}")

    # Una capa lineal se puede deshacer si y solo si su matriz esta en GL(n, R).
    rng = np.random.default_rng(2)
    W = rng.normal(size=(3, 3))
    b = rng.normal(size=3)
    x = rng.normal(size=(4, 3))
    recuperado = ((x @ W + b) - b) @ np.linalg.inv(W)
    print(f"capa invertible: se recupera la entrada: {np.allclose(x, recuperado)}")

    W_sing = W.copy()
    W_sing[2, :] = W_sing[0, :]
    h = np.array([1.0, 0.0, -1.0])            # h @ W_sing = 0
    print(f"capa singular  : rango {np.linalg.matrix_rank(W_sing)} < 3, "
          f"cond = {np.linalg.cond(W_sing):.1e}, dos entradas distintas dan la misma salida: "
          f"{np.allclose(x @ W_sing, (x + h) @ W_sing)}")

    # --- 4. Axiomas de espacio vectorial ---
    u = np.array([1.0, 2.0])
    v = np.array([3.0, -1.0])
    lam, psi = 2.0, 3.0
    print(f"\ndistributividad lam(u+v)   : {np.allclose(lam * (u + v), lam * u + lam * v)}")
    print(f"distributividad (lam+psi)u : {np.allclose((lam + psi) * u, lam * u + psi * u)}")
    print(f"asociatividad   lam(psi u) : {np.allclose(lam * (psi * u), (lam * psi) * u)}")
    print(f"neutro externo  1*u == u   : {np.allclose(1.0 * u, u)}")

    # La "multiplicacion de vectores" no es una operacion de espacio vectorial.
    a = np.array([1.0, 2.0, 3.0])
    c = np.array([4.0, 0.0, -1.0])
    print(f"\nproducto interno a.T @ c = {a @ c} (escalar)   "
          f"producto externo a @ c.T -> {np.outer(a, c).shape}")

    # R^{m x n} es un espacio vectorial, equivalente a R^{mn}.
    W1 = np.arange(6.0).reshape(3, 2)
    W2 = 10 * W1
    print(f"suma de matrices == suma de los vectores aplanados: "
          f"{np.allclose((W1 + W2).ravel(), W1.ravel() + W2.ravel())}")

    # El descenso de gradiente es una operacion de espacio vectorial.
    theta = np.array([1.0, -2.0, 0.5])
    grad = np.array([0.4, 0.1, -0.3])
    print(f"theta - 0.1 * gradiente = {theta - 0.1 * grad}")

    # --- 5. Subespacios: el criterio practico ---
    print()
    criterio_subespacio(lambda p: 0 <= p[0] <= 1 and 0 <= p[1] <= 1,
                        [(1.0, 1.0), (0.5, 0.25)], nombre="A (cuadrado unitario)")
    criterio_subespacio(lambda p: np.isclose(p[1], p[0] + 1),
                        [(0.0, 1.0), (2.0, 3.0)], nombre="B (recta y = x + 1)")
    criterio_subespacio(lambda p: p[0] >= 0 and p[1] >= 0,
                        [(1.0, 1.0), (2.0, 0.5)], nombre="C (primer cuadrante)")
    criterio_subespacio(lambda p: np.isclose(p[1], 2 * p[0]),
                        [(1.0, 2.0), (-3.0, -6.0)], nombre="D (recta y = 2x)")

    # --- 6. N(A) es subespacio; el conjunto solucion de Ax = b, con b != 0, no ---
    M = np.array([[1.0, 2.0], [2.0, 4.0]])
    h1 = np.array([-2.0, 1.0])
    print(f"\nM @ (2*h1 - 5*(3*h1)) = {M @ (2 * h1 - 15 * h1)}  <- N(M) es cerrado")

    b_no_nulo = np.array([1.0, 2.0])
    x1 = np.array([1.0, 0.0])
    x2 = x1 + h1
    print(f"x1 y x2 son soluciones, pero M @ (x1 + x2) = {M @ (x1 + x2)} != {b_no_nulo}")

    # La interseccion de subespacios es subespacio; la union, no.
    print()
    criterio_subespacio(lambda p: np.isclose(p[0], 0) and np.isclose(p[1], 0),
                        [(0.0, 0.0, 1.0), (0.0, 0.0, -4.0)], nombre="U1 interseccion U2")
    criterio_subespacio(lambda p: np.isclose(p[0], 0) or np.isclose(p[1], 0),
                        [(0.0, 1.0, 0.0), (1.0, 0.0, 0.0)], nombre="U1 union U2")

    # --- 7. Subespacios en PCA: la proyeccion es lineal e idempotente ---
    rng = np.random.default_rng(4)
    direccion = np.array([2.0, 1.0]) / np.sqrt(5)
    datos = np.outer(rng.normal(scale=2.0, size=200), direccion) + 0.25 * rng.normal(size=(200, 2))
    centrados = datos - datos.mean(axis=0)
    _, s, Vt = np.linalg.svd(centrados, full_matrices=False)
    P = np.outer(Vt[0], Vt[0])
    print(f"\nprimera componente: {np.round(Vt[0], 4)}   "
          f"varianza capturada: {s[0] ** 2 / (s ** 2).sum():.1%}")
    print(f"proyeccion lineal: "
          f"{np.allclose((centrados[0] + centrados[1]) @ P, centrados[0] @ P + centrados[1] @ P)}"
          f"   idempotente P@P == P: {np.allclose(P @ P, P)}")


if __name__ == "__main__":
    main()
