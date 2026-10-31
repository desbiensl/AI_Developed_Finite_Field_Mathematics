"""Additional checks for the revised manuscripts; not a geometric proof audit.

Python 3.10+, SymPy, and NumPy. All elliptic-curve calculations below are
exact integer modular arithmetic. The finite Fourier covariance check uses
complex floating point, with its tolerance and maximum error reported.
"""
from __future__ import annotations
from functools import lru_cache
from pathlib import Path
import json
import numpy as np
import sympy as s

p = 2**256 - 2**32 - 977
n = int('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141', 16)
G = (55066263022277343669578718895168534326250603453777594175500187360389116729240,
     32670510020758816978083085130507043184471273380659243275938904335757337482424)
Point = tuple[int, int] | None

def add(P: Point, Q: Point) -> Point:
    if P is None: return Q
    if Q is None: return P
    x,y = P; u,v = Q
    if x == u and (y+v) % p == 0: return None
    slope = ((3*x*x)*pow(2*y,-1,p) if P == Q else (v-y)*pow(u-x,-1,p)) % p
    X = (slope*slope-x-u) % p
    return X, (slope*(x-X)-y) % p

def mul(k: int, P: Point) -> Point:
    k %= n
    Q = None
    while k:
        if k & 1: Q = add(Q,P)
        P = add(P,P); k >>= 1
    return Q

def division_function(P: tuple[int,int]):
    x,y=P
    initial={0:0,1:1,2:2*y%p,3:3*x*(x**3+28)%p,
             4:4*y*(x**6+140*x**3-392)%p}
    inv2y=pow(2*y,-1,p)
    @lru_cache(maxsize=None)
    def psi(m: int) -> int:
        if m < 0: return -psi(-m)%p
        if m in initial: return initial[m]
        k=m//2
        if m & 1:
            return (psi(k+2)*pow(psi(k),3,p)-psi(k-1)*pow(psi(k+1),3,p))%p
        return (psi(k)*inv2y*(psi(k+2)*psi(k-1)**2-psi(k-2)*psi(k+1)**2))%p
    return psi

def theta(P: tuple[int,int]) -> int:
    psi=division_function(P)
    L=p-1
    return pow(psi(L)*pow(psi(L+n),-1,p)%p, pow(n*n,-1,L),p)

normalization_count=0
for d in [1,2,17]:
    P=mul(d,G)
    assert P is not None
    T=theta(P); psi=division_function(P)
    for e in [1,2,3,4,7,17,-1,-2,n-1]:
        Q=mul(e,P)
        assert Q is not None
        assert theta(Q)==pow(T,e*e,p)*psi(e)%p
        normalization_count+=1
    # The normalized Ward recurrence with independent positive indices.
    for m,r in [(4,2),(7,3),(10,4)]:
        W=lambda k: pow(T,k*k-1,p)*psi(k)%p
        assert W(m+r)*W(m-r)%p == (W(m+1)*W(m-1)*W(r)**2-W(r+1)*W(r-1)*W(m)**2)%p

# Genus-two quotient equations, as rational-function identities.
x,gamma=s.symbols('x gamma', nonzero=True)
S=gamma+1/gamma
u=x+1/x
Y2=7*(x**6-S*x**3+1)
for sign in [1,-1]:
    assert s.factor(Y2*(x+sign)**2/x**4 - 7*(u+2*sign)*(u**3-3*u-S))==0
w,y,alpha=s.symbols('w y alpha')
R=(alpha+7)/7
# w^3=(y^2-7)/(y^2-alpha-7); derive the hyperelliptic quotient.
z=(y*y-7)/(y*y-alpha-7)
assert s.factor(y*y*(z-1)**2-7*(z-1)*(R*z-1))==0

# Covariance from the actual independent-orbit coefficient vectors.
maxerr=0.0
models=[]
for N in [7,13,19,31,43]:
    lam=next(a for a in range(2,N) if pow(a,3,N)==1)
    orbit=[]; remaining=set(range(1,N))
    while remaining:
        r=min(remaining)
        pos={r, r*lam%N,r*lam*lam%N}
        neg={-v%N for v in pos}
        remaining-=pos|neg
        row=np.zeros(N)
        for v in pos: row[v]=1
        for v in neg: row[v]=-1
        orbit.append(np.fft.fft(row))
    coeff=np.array(orbit)
    cov=coeff.T @ coeff.conj()
    expected=np.zeros((N,N))
    for k in range(1,N):
        for a in [1,lam,lam*lam%N]:
            expected[k,k*a%N]=N
            expected[k,-k*a%N]=-N
    err=float(np.max(np.abs(cov-expected)))
    maxerr=max(maxerr,err)
    assert err < 1e-10
    models.append(N)

report={
    'status':'PASS',
    'intrinsic_theta_identity_exact_cases':normalization_count,
    'normalized_Ward_recurrence_exact_cases':9,
    'symbolic_quotient_identities':3,
    'orbit_covariance_group_orders':models,
    'orbit_covariance_tolerance':1e-10,
    'orbit_covariance_max_absolute_error':maxerr,
    'limitations':'These checks do not independently verify the sheaf-theoretic arguments, isogeny proof, asymptotic limit arguments, or novelty. No unknown scalar is recovered.'
}
Path(__file__).with_name('revision_identity_results.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
