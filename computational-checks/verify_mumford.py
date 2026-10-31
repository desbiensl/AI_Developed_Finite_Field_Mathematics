"""Exact genus-one reduction checks; standard library only."""
from pathlib import Path
import json
from verify_osculation import trim, sub, mul, coeffs, scalar, evaluate

def divmodp(a,b,p):
    a=trim(a,p); b=trim(b,p)
    if b==[0]:raise ZeroDivisionError('Zero polynomial')
    q=[0]*max(1,len(a)-len(b)+1)
    while a!=[0] and len(a)>=len(b):
        j=len(a)-len(b); c=a[-1]*pow(b[-1],-1,p)%p; q[j]=c
        a=sub(a,[0]*j+[c*v%p for v in b],p)
    return trim(q,p),a

def reduce_point(P,A,B,p,d):
    x,y=P; C=[y*y%p,(3*x*x+A)%p,3*x%p,1]
    u=[0]*d+[1]; v=coeffs(P,A,B,p,d-1); path=[d]
    while len(u)>2:
        z,r=divmodp(sub(mul(v,v,p),C,p),u,p)
        assert r==[0] and z!=[0]
        z=[c*pow(z[-1],-1,p)%p for c in z]
        assert len(z)<len(u)
        _,v=divmodp([-c%p for c in v],z,p)
        u=z; path.append(len(u)-1)
    if len(u)==1:Q=None
    else:
        root=-u[0]*pow(u[1],-1,p)%p
        Q=((x+root)%p,evaluate(v,root,p))
    assert Q==scalar(d,P,A,p)
    return path

count=0
for p in [7,11,19,31]:
    for A,B in [(0,7),(1,1),(2,3)]:
        if (4*A**3+27*B*B)%p==0:continue
        for x in range(p):
            for y in range(1,p):
                if (y*y-x**3-A*x-B)%p==0:
                    for d in range(2,25):reduce_point((x,y),A,B,p,d);count+=1
p=2**256-2**32-977
G=(55066263022277343669578718895168534326250603453777594175500187360389116729240,32670510020758816978083085130507043184471273380659243275938904335757337482424)
big=0
for k in range(1,18):
    P=scalar(k,G,0,p)
    for d in range(2,25):reduce_point(P,0,7,p,d);big+=1
example=reduce_point((4,24),0,7,101,8)
report={'status':'PASS','small_field_reduction_cases':count,'secp256k1_reduction_cases':big,'contact_orders':[2,24],'example_p101_P4_24_d8_degree_path':example,'limits':'Exact modular-arithmetic consistency checks, not an independent proof audit.'}
Path(__file__).with_name('mumford_results.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
