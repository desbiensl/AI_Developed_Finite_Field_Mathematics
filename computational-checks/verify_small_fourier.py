"""Small-field consistency checks for the elliptic Fourier statements.
Requires NumPy. Enumerates prime-order models for p in {7,11,19,23}, then
selected models at larger primes. Fourier arithmetic is floating point;
autocorrelations and curve enumeration use exact integers.
"""
from pathlib import Path
from math import isqrt, sqrt
import json
import numpy as np
from verify_osculation import add

def isprime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))

def points(p,a,b):
    roots={}
    for y in range(p):roots.setdefault(y*y%p,[]).append(y)
    return [(x,y) for x in range(p) for y in roots.get((x**3+a*x+b)%p,[])]

def run_model(p,a,b):
    pts=points(p,a,b); n=len(pts)+1
    if not isprime(n) or n%2==0:return None
    G=pts[0]; P=None; f=[0]
    seen={None}
    for _ in range(1,n):
        P=add(P,G,a,p)
        assert P not in seen and P is not None
        seen.add(P)
        z=pow(P[1],(p-1)//2,p)
        assert z in [1,p-1]
        f.append(1 if z==1 else -1)
    assert add(P,G,a,p) is None
    f=np.array(f,dtype=np.int64); S=np.fft.fft(f)
    assert np.max(np.abs(S.real))<1e-8
    assert abs(S[0])<1e-8
    assert np.max(np.abs(S))<=2*sqrt(p)+1e-8
    X=S.imag/(2*sqrt(p))
    errors=[]
    from math import comb
    for r in range(1,7):
        target=comb(2*r,r)/(r+1)/4**r
        err=abs(float(np.mean(X**(2*r)))-target)
        assert err <= r/(2*sqrt(p))+1e-9
        errors.append(err)
    corr=[int(np.dot(f,np.roll(f,j))) for j in range(1,n)]
    assert max(map(abs,corr),default=0)<=2*sqrt(p)
    assert abs(float(np.mean(X*X))-(n-1)/(4*p))<1e-10
    return {'p':p,'a':a,'b':b,'n':n,'generator':G,'max_fourier_over_2sqrtp':float(np.max(np.abs(S))/(2*sqrt(p))),'max_autocorrelation':max(map(abs,corr),default=0),'raw_even_moment_errors_2_to_12':errors}

cases=[]
for p in [7,11,19,23]:
    for a in range(p):
        for b in range(p):
            if (4*a**3+27*b*b)%p:
                r=run_model(p,a,b)
                if r:cases.append(r)
for p in [43,103,211,499,1019]:
    for a,b in [(0,1),(0,7),(1,1),(2,3),(3,7),(5,11)]:
        if (4*a**3+27*b*b)%p:
            r=run_model(p,a,b)
            if r:cases.append(r)
report={'status':'PASS','design':'Fixed small-field enumeration. Only prime-order groups are tested.','model_count':len(cases),'fourier_coefficients_tested':sum(c['n'] for c in cases),'exact_nontrivial_autocorrelations_tested':sum(c['n']-1 for c in cases),'max_fourier_over_2sqrtp':max(c['max_fourier_over_2sqrtp'] for c in cases),'numpy_version':np.__version__,'cases':cases}
Path(__file__).with_name('small_fourier_results.json').write_text(json.dumps(report,indent=2))
print(json.dumps({k:v for k,v in report.items() if k!='cases'},indent=2))
