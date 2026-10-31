#!/usr/bin/env python3
"""Exact-arithmetic checks for the exploratory elliptic-osculation manuscript.

Python 3.10+; standard library only. No network, private keys, or external data.
Run: python verify_osculation.py --output validation_results.json
All curve coordinates and polynomial coefficients are reduced modulo p.
Polynomial coefficient lists are in ascending order. None denotes infinity.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import platform
from pathlib import Path
from typing import Optional

Point = Optional[tuple[int, int]]

def inv(a: int, p: int) -> int:
    if a % p == 0:
        raise ZeroDivisionError('Non-invertible field element')
    return pow(a, -1, p)

def trim(a: list[int], p: int) -> list[int]:
    a = [x % p for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a or [0]

def sub(a: list[int], b: list[int], p: int) -> list[int]:
    n = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else 0) -
                 (b[i] if i < len(b) else 0) for i in range(n)], p)

def mul(a: list[int], b: list[int], p: int) -> list[int]:
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] = (c[i+j] + x*y) % p
    return trim(c, p)

def evaluate(a: list[int], x: int, p: int) -> int:
    r = 0
    for v in reversed(a):
        r = (r*x+v) % p
    return r

def add(P: Point, Q: Point, A: int, p: int) -> Point:
    if P is None:
        return Q
    if Q is None:
        return P
    x, y = P
    u, v = Q
    if x == u and (y+v) % p == 0:
        return None
    s = ((3*x*x+A)*inv(2*y, p) if P == Q else
         (v-y)*inv(u-x, p)) % p
    w = (s*s-x-u) % p
    return (w, (s*(x-w)-y) % p)

def negate(P: Point, p: int) -> Point:
    return None if P is None else (P[0], -P[1] % p)

def scalar(k: int, P: Point, A: int, p: int) -> Point:
    if k < 0:
        return scalar(-k, negate(P, p), A, p)
    Q = None
    while k:
        if k & 1:
            Q = add(Q, P, A, p)
        P = add(P, P, A, p)
        k >>= 1
    return Q

def coeffs(P: tuple[int, int], A: int, B: int, p: int, M: int) -> list[int]:
    a, b = P
    if (b*b-a*a*a-A*a-B) % p:
        raise ValueError('Point is not on the curve')
    if b == 0:
        raise ValueError('The local x parameter requires a nonzero ordinate')
    f = [b*b % p, (3*a*a+A) % p, 3*a % p, 1]
    c = [b]
    z = inv(2*b, p)
    for k in range(1, M+1):
        rhs = f[k] if k < 4 else 0
        c.append((rhs-sum(c[i]*c[k-i] for i in range(1, k)))*z % p)
    return c

def residual(P: tuple[int, int], A: int, p: int, c: list[int], m: int) -> list[int]:
    a, b = P
    f = [b*b % p, (3*a*a+A) % p, 3*a % p, 1]
    F = sub(mul(c[:m+1], c[:m+1], p), f, p)
    assert all(v == 0 for v in F[:m+1]), ('contact', P, m)
    assert c[m] != 0
    assert len(F) == 2*m+1
    return F[m+1:]

def split_roots(h: list[int], p: int) -> Optional[list[int]]:
    """Return all roots with multiplicity only if h splits over F_p."""
    h = trim(h, p)
    roots: list[int] = []
    for r in range(p):
        while len(h) > 1 and evaluate(h, r, p) == 0:
            d = len(h)-1
            q = [0]*d
            q[-1] = h[-1]
            for j in range(d-2, -1, -1):
                q[j] = (h[j+1]+r*q[j+1]) % p
            assert (h[0]+r*q[0]) % p == 0
            h = trim(q, p)
            roots.append(r)
    return roots if len(h) == 1 else None

def nullvector(matrix: list[list[int]], p: int) -> list[int]:
    """Check one-dimensional nullspace and return its normalized generator."""
    M = [[v % p for v in row] for row in matrix]
    rows, cols = len(M), len(M[0])
    pivots: list[int] = []
    r = 0
    for col in range(cols):
        k = next((j for j in range(r, rows) if M[j][col]), None)
        if k is None:
            continue
        M[r], M[k] = M[k], M[r]
        s = inv(M[r][col], p)
        M[r] = [v*s % p for v in M[r]]
        for j in range(rows):
            if j != r and M[j][col]:
                s = M[j][col]
                M[j] = [(v-s*w) % p for v, w in zip(M[j], M[r])]
        pivots.append(col)
        r += 1
        if r == rows:
            break
    free = [j for j in range(cols) if j not in pivots]
    assert len(free) == 1, ('nullity', rows, cols, pivots)
    v = [0]*cols
    v[free[0]] = 1
    for row, col in enumerate(pivots):
        v[col] = -M[row][free[0]] % p
    return v

def rr_check(P: tuple[int, int], A: int, B: int, p: int, n: int,
             c: list[int]) -> tuple[bool, bool]:
    """Construct U+V*y in L((n+1)O-nP), and check its norm and residual."""
    N = n+1
    du, dv = N//2, (N-3)//2
    columns = [[int(i == j) for i in range(n)] for j in range(du+1)]
    columns += [[c[i-j] if i >= j else 0 for i in range(n)]
                for j in range(dv+1)]
    assert len(columns) == N
    v = nullvector([list(row) for row in zip(*columns)], p)
    U, V = trim(v[:du+1], p), trim(v[du+1:], p)
    a, b = P
    f = [b*b % p, (3*a*a+A) % p, 3*a % p, 1]
    F = sub(mul(U, U, p), mul(mul(V, V, p), f, p), p)
    assert all(z == 0 for z in F[:n])
    target = negate(scalar(n, P, A, p), p)
    if target is None:
        assert len(F) == n+1 and F[n]
        return True, False
    assert len(F) == n+2 and F[n+1]
    t = -F[n]*inv(F[n+1], p) % p
    assert (a+t) % p == target[0]
    denominator = evaluate(V, t, p)
    if denominator:
        assert -evaluate(U, t, p)*inv(denominator, p) % p == target[1]
    else:
        assert target == negate(P, p), ('zero denominator residual', P, n, target)
    return False, denominator == 0

def check_point(P: tuple[int, int], A: int, B: int, p: int,
                counts: dict[str, int], small: bool) -> dict:
    c = coeffs(P, A, B, p, 12)
    a, b = P
    counts['points'] += 1
    psi3 = (3*a**4+6*A*a*a+12*B*a-A*A) % p
    psi4 = 4*b*(a**6+5*A*a**4+20*B*a**3-5*A*A*a*a-
                 4*A*B*a-8*B*B-A**3) % p
    assert c[2] == psi3*inv(8*b**3, p) % p
    assert c[3] == -psi4*inv(64*b**6, p) % p
    counts['division_polynomial_pairs'] += 1
    if c[2]:
        t = (1-2*c[1]*c[2])*inv(c[2]*c[2], p) % p
        R = ((a+t) % p, evaluate(c[:3], t, p))
        assert R == negate(scalar(3, P, A, p), p)
        counts['tripling'] += 1
    else:
        assert scalar(3, P, A, p) is None
        counts['three_torsion'] += 1
    if c[3]:
        s = c[2]*inv(c[3], p) % p
        lam = (c[2]*s-c[1]) % p
        x4 = (lam*lam-2*a+2*s) % p
        mu = (b+c[2]*(c[2]*c[2]+2*c[1]*c[3])*inv(c[3]*c[3], p)) % p
        y4 = (lam*(x4-a)+mu) % p
        assert (x4, y4) == scalar(4, P, A, p)
        counts['quadrupling'] += 1
    else:
        assert scalar(4, P, A, p) is None
        counts['four_torsion'] += 1
    for m in range(2, 11):
        if not c[m]:
            counts['zero_leading_coefficients'] += 1
            continue
        H = residual(P, A, p, c, m)
        trace_t = -H[-2]*inv(H[-1], p) % p
        expected = ((1-2*c[1]*c[2])*inv(c[2]*c[2], p) if m == 2
                    else -2*c[m-1]*inv(c[m], p)) % p
        assert trace_t == expected
        counts['residual_polynomials'] += 1
        if small and m <= 6:
            roots = split_roots(H, p)
            if roots is not None:
                S = None
                for t in roots:
                    R = ((a+t) % p, evaluate(c[:m+1], t, p))
                    assert (R[1]**2-R[0]**3-A*R[0]-B) % p == 0
                    S = add(S, R, A, p)
                assert S == negate(scalar(m+1, P, A, p), p)
                counts['split_divisor_sums'] += 1
    for n in range(2, 13):
        torsion, zero_denominator = rr_check(P, A, B, p, n, c)
        counts['rr_systems'] += 1
        counts['rr_torsion_cases'] += int(torsion)
        counts['rr_zero_y_denominator'] += int(zero_denominator)
    return {'point': list(P), 'c0_to_c3': c[:4],
            'triple': scalar(3, P, A, p), 'quadruple': scalar(4, P, A, p)}

def empty_counts() -> dict[str, int]:
    return {k: 0 for k in ['points','division_polynomial_pairs','tripling','quadrupling',
                           'three_torsion','four_torsion','zero_leading_coefficients',
                           'residual_polynomials','split_divisor_sums','rr_systems',
                           'rr_torsion_cases','rr_zero_y_denominator']}

def main() -> int:
    if not __debug__:
        raise RuntimeError("Run without -O: the validation checks use assertions.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', default='validation_results.json')
    args = parser.parse_args()
    primes = [5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
    models = [(0,7),(2,3),(1,1),(0,1)]
    small_counts = empty_counts()
    curves = 0
    examples = []
    for p in primes:
        seen = set()
        for aa, bb in models:
            A, B = aa % p, bb % p
            if (A,B) in seen or (4*A**3+27*B**2) % p == 0:
                continue
            seen.add((A,B))
            curves += 1
            for a in range(p):
                for b in range(1, p):
                    if (b*b-a*a*a-A*a-B) % p == 0:
                        check_point((a,b), A, B, p, small_counts, True)
                        if p == 101 and A == 0 and B == 7:
                            c = coeffs((a,b), A, B, p, 3)
                            if c[3]:
                                H = residual((a,b), A, p, c, 3)
                                roots = split_roots(H, p)
                                if roots is not None and len(set(roots)) == 2 and len(examples) < 4:
                                    examples.append({'P':[a,b], 'c':c, 'H_t':H,
                                      'residual_points': [[(a+t)%p,evaluate(c,t,p)] for t in roots],
                                      'four_P':scalar(4,(a,b),A,p),
                                      'minus_four_P':negate(scalar(4,(a,b),A,p),p)})
    p = 2**256-2**32-977
    order = int('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141',16)
    G = (int('79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798',16),
         int('483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8',16))
    assert scalar(order, G, 0, p) is None
    sec_counts = empty_counts()
    sec_examples = []
    scalars = list(range(1,65)) + [2**128+1, order-2, order-1]
    for k in scalars:
        P = scalar(k,G,0,p)
        assert P is not None
        record = check_point(P,0,7,p,sec_counts,False)
        if k == 1:
            sec_examples.append(record)
    result = {'status':'PASS', 'python':platform.python_version(),
       'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'small_fields': {'primes':primes,'model_seeds':models,'distinct_nonsingular_models':curves,
                        'counts':small_counts},
       'secp256k1':{'scalars':scalars,'counts':sec_counts,'generator_record':sec_examples[0]},
       'small_examples':examples,
       'limits':['Tests are not a proof.','Divisor group sums are checked directly only when residuals split over the base field.',
                 'No discrete logarithm is recovered; all secp256k1 input scalars are deliberately known.',
                 'Group-law and osculation checks use different formulas but are maintained in one implementation.']}
    Path(args.output).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
