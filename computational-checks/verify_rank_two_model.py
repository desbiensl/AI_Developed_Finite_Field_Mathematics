#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Exact checks of the proposed elliptic trace model, not a proof audit.

Default coverage: every nonsingular short Weierstrass model over primes 5..43
whose rational group has odd order, and every nonidentity rational shift.
The program uses no floating-point character sums.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import platform
import sympy as s

Point = tuple[int, int] | None


def chi(value: int, p: int) -> int:
    value %= p
    if value == 0:
        return 0
    return 1 if pow(value, (p - 1) // 2, p) == 1 else -1


def add(P: Point, Q: Point, a: int, p: int) -> Point:
    if P is None:
        return Q
    if Q is None:
        return P
    x, y = P
    X, Y = Q
    if x == X:
        if (y + Y) % p == 0:
            return None
        slope = (3*x*x + a) * pow(2*y, -1, p) % p
    else:
        slope = (Y-y) * pow(X-x, -1, p) % p
    z = (slope*slope-x-X) % p
    return z, (slope*(x-z)-y) % p


def symbolic_checks() -> dict:
    x, u, a, b, z, q, t = s.symbols('x u a b z q t')
    g = x**3 + a*x + b
    c = u**3 + a*u + b
    d = 3*u*u + a
    D = -4*a**3 - 27*b*b
    quartic = (x-u)*g
    cubic = c*z**3 + d*z*z + 3*u*z + 1
    monic_cubic = x**3 + d*x*x + 3*u*c*x + c*c
    assert s.factor(s.discriminant(quartic, x) - D*c*c) == 0
    assert s.factor(s.discriminant(cubic, z) - D) == 0
    assert s.factor(s.discriminant(monic_cubic, x) - c*c*D) == 0
    assert s.factor(z**4*quartic.subs(x, u+1/z)-cubic) == 0
    assert s.factor(d*d-9*u*c-(a*a-3*a*u*u-9*b*u)) == 0
    # The chord identity does not require substitution of the curve equation.
    xp,xq,yp,yq=s.symbols('xp xq yp yq')
    assert s.factor(((yp+yq)/(xp-xq))**2-((yp-yq)/(xp-xq))**2-4*yp*yq/(xp-xq)**2)==0
    I2=s.eye(2)
    I=s.diag(s.I,-s.I)
    J=s.Matrix([[0,1],[-1,0]])
    K=I*J
    A=(I2+I+J+K)/2
    assert A.det()==1 and A.trace()==1 and A**3==-I2
    mats=[s.eye(4),s.kronecker_product(I,I),s.kronecker_product(J,J),s.kronecker_product(K,K)]
    signs=[(1,1,1,1),(1,1,-1,-1),(1,-1,1,-1),(1,-1,-1,1)]
    projectors=[sum((sg*M for sg,M in zip(ss,mats)),s.zeros(4))/4 for ss in signs]
    for n,P in enumerate(projectors):
        assert P*P==P and P.rank()==1
        for j,Q in enumerate(projectors):
            if n!=j: assert P*Q==s.zeros(4)
    AA=s.kronecker_product(A,A)
    assert s.simplify(AA*projectors[0]-projectors[0])==s.zeros(4)
    perm=[]
    for P in projectors:
        Q=s.simplify(AA*P*AA.inv())
        perm.append(next(j for j,R in enumerate(projectors) if Q==R))
    assert perm[0]==0 and all(perm[j]!=j for j in range(1,4))
    omega=s.Matrix([[0,1],[-1,0]])
    r0,r1,r2,r3=s.symbols('r0:4')
    R=s.Matrix([[r0,r1],[r2,r3]])
    assert s.simplify(R.T*omega*R-R.det()*omega)==s.zeros(2)
    B=s.Matrix([[0,q],[1,t]]) # trace t, determinant -q
    F=s.kronecker_product(A,B)
    target=x**4-t*x**3+(t*t+q)*x*x+q*t*x+q*q
    assert s.factor(F.charpoly(x).as_expr()-target)==0
    return {
        'quartic_discriminant':'PASS', 'birational_cubic_model':'PASS',
        'cubic_discriminants':'PASS', 'j_invariant_numerator':'PASS',
        'chord_identity':'PASS','quaternion_intertwiner':'PASS',
        'four_projectors':'PASS', 'frobenius_projector_permutation':perm,
        'invariant_line_frobenius_eigenvalue':1,
        'alternating_form_multiplier_identity':'PASS',
        'four_dimensional_characteristic_polynomial':'PASS'
    }


def finite_checks(max_prime: int) -> dict:
    per_prime=[]
    examples=[]
    digest=hashlib.sha256()
    total_models=total_shifts=0
    for p0 in s.primerange(5,max_prime+1):
        p=int(p0); models=shifts=0
        roots={x:[] for x in range(p)}
        for y in range(p): roots[y*y%p].append(y)
        for a in range(p):
            for b in range(p):
                if (4*a**3+27*b*b)%p==0:
                    continue
                values=[(x**3+a*x+b)%p for x in range(p)]
                if 0 in values: # rational two-torsion, hence even group order
                    continue
                points=[None]+[(x,y) for x,v in enumerate(values) for y in roots[v]]
                assert len(points)%2==1
                f={P:0 if P is None else chi(P[1],p) for P in points}
                assert sum(v*v for v in f.values())==len(points)-1
                for T in points[1:]:
                    u,v=T
                    correlation=sum(f[P]*f[add(P,T,a,p)] for P in points)
                    tau=-1-sum(chi((x-u)*values[x],p) for x in range(p))
                    tau_cubic=-sum(chi(v*v*z**3+(3*u*u+a)*z*z+3*u*z+1,p) for z in range(p))
                    assert correlation==-chi(-1,p)*tau,(p,a,b,T,correlation,tau)
                    assert tau==tau_cubic,(p,a,b,T,tau,tau_cubic)
                    assert tau*tau<=4*p
                    digest.update(f'{p},{a},{b},{u},{v},{correlation},{tau}\n'.encode())
                    if p==31 and a==0 and b==7 and len(examples)<6:
                        examples.append({'p':p,'a':a,'b':b,'T':T,'N':len(points),'correlation':correlation,'elliptic_trace':tau,'H_group_order':p+1-tau})
                    shifts+=1
                models+=1
        per_prime.append({'prime':p,'epsilon':chi(-1,p),'curve_models':models,'nonzero_shifts':shifts})
        total_models+=models;total_shifts+=shifts
        print(f'p={p}: {models} models; {shifts} shifts: PASS',flush=True)
    return {'max_prime':max_prime,'curve_models':total_models,'nonzero_shifts':total_shifts,
            'q_3_mod_4_models':sum(v['curve_models'] for v in per_prime if v['epsilon']==-1),
            'q_3_mod_4_shifts':sum(v['nonzero_shifts'] for v in per_prime if v['epsilon']==-1),
            'per_prime':per_prime,'examples':examples,'ordered_test_data_sha256':digest.hexdigest(),
            'arithmetic':'exact integers and modular arithmetic; no floating point','all_passed':True}


def main() -> None:
    if not __debug__:
        raise RuntimeError('Run without -O: this verification program requires assertions.')
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-prime',type=int,default=43)
    parser.add_argument('--output',type=Path,default=Path(__file__).resolve().parents[1]/'results'/'rank_two_results.json')
    args=parser.parse_args()
    if args.max_prime<5:
        parser.error('--max-prime must be at least 5')
    report={'python':platform.python_version(),'sympy':s.__version__,
            'scope':'Consistency tests for the accompanying proposed derivations; not independent proof verification.',
            'symbolic':symbolic_checks(),'finite_fields':finite_checks(args.max_prime)}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(f'ALL CHECKS PASSED. Results: {args.output}')

if __name__=='__main__':
    main()
