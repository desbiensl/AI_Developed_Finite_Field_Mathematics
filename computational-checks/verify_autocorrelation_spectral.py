#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Exact finite-group checks for the standalone autocorrelation identity.

These are finite examples, not independent proof certification.  For each
nonsingular short Weierstrass model with odd rational group order over
primes 5 <= p <= max_prime (default 23), test the exact trace and group
algebra equalities, both chi(-1)=+1 and chi(-1)=-1 where available.
Requires Python 3.10+ and sympy, with assertions enabled.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import platform
import sympy as sp


def chi(x:int,p:int)->int:
    t=x%p
    if t==0:return 0
    return 1 if pow(t,(p-1)//2,p)==1 else -1


def add(P,Q,a:int,p:int):
    if P is None:return Q
    if Q is None:return P
    x,y=P;u,v=Q
    if x==u:
        if (y+v)%p==0:return None
        k=(3*x*x+a)*pow(2*y,-1,p)%p
    else:
        k=(v-y)*pow(u-x,-1,p)%p
    z=(k*k-x-u)%p
    return z,(k*(x-z)-y)%p


def run(max_prime:int)->dict:
    if not __debug__:raise RuntimeError('Assertions must be enabled')
    counts={'models':0,'shifts':0,'q3_models':0,'q1_models':0,'per_prime':[]}
    dig=hashlib.sha256()
    for p_sym in sp.primerange(5,max_prime+1):
        p=int(p_sym); model=shift=0
        square_roots={u:[] for u in range(p)}
        for v in range(p): square_roots[v*v%p].append(v)
        for a in range(p):
            for b in range(p):
                if (4*a*a*a+27*b*b)%p==0:continue
                g=[(x*x*x+a*x+b)%p for x in range(p)]
                if 0 in g:continue
                E=[None]+[(x,y) for x,gx in enumerate(g) for y in square_roots[gx]]
                N=len(E);assert N%2==1
                f={P:0 if P is None else chi(P[1],p) for P in E}
                eps=chi(-1,p)
                m=sum(f.values())
                traces={}
                csum=0
                fstar={}
                for T in E:
                    cor=sum(f[P]*f[add(P,T,a,p)] for P in E)
                    # Written separately for clarity and compatibility with identity.
                    neg=lambda P:None if P is None else(P[0],(-P[1])%p)
                    conv=sum(f[P]*f[add(T,neg(P),a,p)] for P in E)
                    assert conv==eps*cor
                    fstar[T]=conv
                    if T is None:
                        assert cor==N-1
                    else:
                        u,v=T
                        trace=-1-sum(chi((x-u)*g[x],p) for x in range(p))
                        assert cor==-eps*trace
                        assert trace*trace<=4*p
                        traces[T]=trace
                        shift+=1
                    csum+=cor
                assert csum==m*m
                assert sum(fstar.values())==m*m
                assert sum(traces.values())==-eps*(m*m-(N-1))
                if eps==-1:
                    assert m==0 and sum(traces.values())==-(N-1)
                # The squared Fourier identity is the group ring equality:
                # C(T)=epsilon * (f*f)(T), already checked at every T.
                dig.update(f'{p}:{a}:{b}:{N}:{m}:{sum(traces.values())}\n'.encode())
                model+=1
        counts['per_prime'].append({'p':p,'models':model,'shifts':shift})
        counts['models']+=model;counts['shifts']+=shift
        if p%4==3:counts['q3_models']+=model
        else:counts['q1_models']+=model
        print(f'p={p}: {model} models; {shift} nonzero shifts: PASS',flush=True)
    counts['digest']=dig.hexdigest()
    counts['all_assertions_passed']=True
    counts['method']='Exact integer arithmetic on each enumerated rational group; no floating-point Fourier transform'
    counts['software']={'python':platform.python_version(),'sympy':sp.__version__}
    return counts

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--max-prime',type=int,default=23)
    ap.add_argument('--output',type=Path,default=Path(__file__).resolve().parent/'autocorrelation_spectral_results.json')
    o=ap.parse_args()
    o.output.parent.mkdir(parents=True,exist_ok=True)
    result=run(o.max_prime)
    o.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print('PASS',result['models'],'models',result['shifts'],'shifts')
