#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Exact extension-field checks of the proposed Frobenius trace polynomial.

Finite fields are constructed as polynomial quotients.  Character sums are
aggregated by the elliptic-curve norm into the integer group ring Z[E(F_p)].
Equality of all coefficients checks all base-group characters simultaneously,
including groups that are not cyclic.  No FFT or floating-point roots of unity
are used.  These are consistency tests, not formal or independent proof audits.
"""
from __future__ import annotations
from pathlib import Path
import argparse
import json
import platform
import sympy
from itertools import product
from collections import defaultdict
from sympy import Poly, symbols, factorint

class Field:
    def __init__(self,p,m):
        if not sympy.isprime(p) or p < 5 or not isinstance(m, int) or m < 1:
            raise ValueError('Require a prime p >= 5 and an integer degree m >= 1.')
        self.p,self.m,self.q=p,m,p**m
        x=symbols('x')
        for cs in product(range(p),repeat=m):
            if cs[0] and Poly(x**m+sum(c*x**j for j,c in enumerate(cs)),x,modulus=p).is_irreducible:
                self.poly=list(cs)+[1];break
        self.digits=[tuple((a//p**j)%p for j in range(m)) for a in range(self.q)]
        self.negatives=[sum(((-c)%p)*p**j for j,c in enumerate(ds)) for ds in self.digits]
        fac=list(factorint(self.q-1))
        for g in range(2,self.q):
            if all(self.rawpow(g,(self.q-1)//ell)!=1 for ell in fac):break
        self.generator=g; self.exp=[]; self.log=[-1]*self.q
        z=1
        for k in range(self.q-1):
            assert self.log[z]==-1
            self.log[z]=k;self.exp.append(z);z=self.rawmul(z,g)
        assert z==1 and all(v>=0 for v in self.log[1:])
        self.exp*=2
    def rawmul(self,a,b):
        p,m=self.p,self.m; ds=[0]*(2*m-1)
        for i,u in enumerate(self.digits[a]):
            for j,v in enumerate(self.digits[b]):ds[i+j]=(ds[i+j]+u*v)%p
        for k in range(2*m-2,m-1,-1):
            u=ds[k]
            for j in range(m):ds[k-m+j]=(ds[k-m+j]-u*self.poly[j])%p
        return sum(ds[j]*p**j for j in range(m))
    def rawpow(self,a,n):
        b=1
        while n:
            if n&1:b=self.rawmul(a,b)
            a=self.rawmul(a,a);n//=2
        return b
    def add(self,a,b):return sum(((u+v)%self.p)*self.p**j for j,(u,v) in enumerate(zip(self.digits[a],self.digits[b])))
    def neg(self,a):return self.negatives[a]
    def sub(self,a,b):return self.add(a,self.neg(b))
    def mul(self,a,b):return self.exp[self.log[a]+self.log[b]] if a and b else 0
    def div(self,a,b):
        if not b:raise ZeroDivisionError
        return self.exp[(self.log[a]-self.log[b])%(self.q-1)] if a else 0
    def pow(self,a,n):return self.exp[(self.log[a]*n)%(self.q-1)] if a else (int(n==0))
    def scalar(self,n):return n%self.p
    def chi(self,a):return 0 if not a else (-1 if self.log[a]%2 else 1)

def add(P,Q,a,F):
    if P is None:return Q
    if Q is None:return P
    x,y=P;X,Y=Q
    if x==X:
        if F.add(y,Y)==0:return None
        s=F.div(F.add(F.mul(F.scalar(3),F.mul(x,x)),a),F.mul(F.scalar(2),y))
    else:s=F.div(F.sub(Y,y),F.sub(X,x))
    xx=F.sub(F.sub(F.mul(s,s),x),X)
    return xx,F.sub(F.mul(s,F.sub(x,xx)),y)

def points(a,b,F):
    roots=defaultdict(list)
    for y in range(F.q):roots[F.mul(y,y)].append(y)
    out=[None]
    for x in range(F.q):
        g=F.add(F.add(F.mul(F.mul(x,x),x),F.mul(a,x)),b)
        out.extend((x,y) for y in roots[g])
    return out

def conv(f,g,ps,a,F):
    h={P:0 for P in ps}
    for P in ps:
        if f[P]:
            for Q in ps:
                if g[Q]:h[add(P,Q,a,F)]+=f[P]*g[Q]
    return h

def polynomial_sm(f,m,ps,a,F):
    # c_m = (-f)*c_{m-1} + p*c_{m-2}, c_0=2 delta, c_1=-f
    c0={P:2*int(P is None) for P in ps};c1={P:-f[P] for P in ps}
    t0,t1=2,1
    if m==1:return f
    for j in range(2,m+1):
        c2=conv(f,c1,ps,a,F)
        c2={P:-c2[P]+F.q*c0[P] for P in ps}
        t2=t1-t0;c0,c1=c1,c2;t0,t1=t1,t2
    return {P:-t1*c1[P] for P in ps}

def main() -> None:
    if not __debug__:
        raise RuntimeError('Run without -O; this verification program requires assertions.')
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
        default=Path(__file__).resolve().parents[1]/'results'/'extension_results.json')
    args=parser.parse_args()
    specs=[(7,0,2,[2,3,4,5,6]), (7,1,1,[2,3]), (11,1,4,[2,3,4]),
           (19,1,1,[2,3]), (23,1,3,[2,3]), (31,0,7,[2,3]), (43,0,7,[2,3])]
    results=[]
    for p,a,b,degrees in specs:
        F0=Field(p,1); ps=points(a,b,F0)
        assert (4*a**3+27*b*b)%p and len(ps)%2 and p%4==3
        f={P:0 if P is None else F0.chi(P[1]) for P in ps}
        base_trace=p+1-len(ps)
        point_orders=[]
        for P in ps[1:]:
            Q=P;order=1
            while Q is not None:
                Q=add(Q,P,a,F0); order+=1
            point_orders.append(order)
        print(f'BASE p={p}, a={a}, b={b}, N={len(ps)}',flush=True)
        for m in degrees:
            F=Field(p,m); qs=points(a,b,F)
            # Independent check against the ordinary elliptic Frobenius recurrence.
            c0,c1=2,base_trace
            for j in range(2,m+1): c0,c1=c1,base_trace*c1-p*c0
            assert len(qs)==p**m+1-c1
            sm={P:0 for P in ps}
            for P in qs:
                N=None; R=P
                for j in range(m):
                    N=add(N,R,a,F)
                    if R is not None: R=(F.pow(R[0],p),F.pow(R[1],p))
                if N is not None: assert N[0]<p and N[1]<p
                assert N in sm
                sm[N]+=0 if P is None else F.chi(P[1])
            expected=polynomial_sm(f,m,ps,a,F0)
            assert sm==expected,(p,a,b,m,sm,expected)
            rec={'p':p,'a':a,'b':b,'base_group_order':len(ps),
                 'base_group_cyclic':max(point_orders,default=1)==len(ps),
                 'extension_degree':m,'q':F.q,'extension_group_order':len(qs),
                 'modulus_coefficients':F.poly,'primitive_element':F.generator,
                 'coefficient_equalities':len(ps),'all_passed':True,
                 'group_ring_coefficients':[{'point':P,'observed':sm[P],'predicted':expected[P]} for P in ps]}
            results.append(rec)
            print(f'  degree={m}; field={F.q}; points={len(qs)}; coefficients={len(ps)}: PASS',flush=True)
    report={'python':platform.python_version(),'sympy':sympy.__version__,
            'scope':'Exact selected extension-field tests; no formal or independent proof certification.',
            'base_models':len(specs),'extension_cases':len(results),
            'enumerated_extension_points':sum(r['extension_group_order'] for r in results),
            'group_ring_coefficient_equalities':sum(r['coefficient_equalities'] for r in results),
            'cases':results,'all_passed':True}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(f'ALL CHECKS PASSED. Results: {args.output}')

if __name__=='__main__':
    main()
