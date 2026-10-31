"""Exact review-stage checks. These do not verify geometric or complexity proofs."""
import json
from pathlib import Path
from math import prod
import sympy as s
from verify_prime_certificate import verify

p=2**256-2**32-977
n=int('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141',16)
lam=int('5363ad4cc05c30e0a5261c028812645a122e22ea20816678df02967c1b23bd72',16)
beta=int('7ae96a2b657c07106e64479eac3434e99cf0497512f58995c1396c28719501ee',16)
h=lam+2; M=(n-1)//6
G=(55066263022277343669578718895168534326250603453777594175500187360389116729240,32670510020758816978083085130507043184471273380659243275938904335757337482424)
factors={2:6,3:1,149:1,631:1,107361793816595537:1,174723607534414371449:1,341948486974166000522343609283189:1}

def add(P,Q):
    if P is None:return Q
    if Q is None:return P
    x,y=P; u,v=Q
    if x==u and (y+v)%p==0:return None
    m=((3*x*x)*pow(2*y,-1,p) if P==Q else (v-y)*pow(u-x,-1,p))%p
    z=(m*m-x-u)%p
    return z,(m*(x-z)-y)%p

def mul(k,P):
    k%=n; Q=None
    while k:
        if k&1:Q=add(Q,P)
        P=add(P,P); k//=2
    return Q

def F(t):return -(t+28)**3*pow(27*t*t,-1,p)%p

def char3(v):return pow(v%p,(p-1)//3,p)

def psi3(P):
    x,_=P; return 3*x*(x**3+28)%p

base=Path(__file__).parent
proof_count=verify(base/'prime_certificate.json')
assert prod(q**e for q,e in factors.items())==n-1
assert (lam*lam+lam+1)%n==0 and (beta*beta+beta+1)%p==0
assert pow(h,n-1,n)==1
h_res={str(q):str(pow(h,(n-1)//q,n)) for q in factors}
assert all(int(v)!=1 for v in h_res.values())
assert pow(7,n-1,n)==1 and all(pow(7,(n-1)//q,n)!=1 for q in factors)
assert pow(p,M,n)==1
p_res={str(q):str(pow(p,M//q,n)) for q in factors if M%q==0}
assert all(int(v)!=1 for v in p_res.values())
assert pow(h,M,n)==(-lam*lam)%n
assert M%3==1 and p%9==7
assert char3(beta*pow(81,-1,p))==1
assert char3(-beta*pow(3,-1,p))==1
assert char3(19+beta)==beta
assert pow(-21%p,(p-1)//2,p)==p-1
scalar_cases=list(range(1,33))+[2**128+1,n-2,n-1]
for d in scalar_cases:
    P=mul(d,G); x,y=P
    phi=(beta*x%p,y)
    assert phi==mul(lam,P)
    Q=add(mul(2,P),phi)
    assert Q==mul(h,P)
    assert Q[0]==(-beta*(x**3+28)*pow(3*x*x,-1,p))%p
    t=pow(x,3,p)
    assert F(t)==pow(Q[0],3,p)
    assert F(F(t))==pow(mul(3,P)[0],3,p)
    assert len({pow(mul(u,P)[0],3,p) for u in [1,n-1,lam,-lam,lam*lam,-lam*lam]})==1
    R=psi3(Q)*pow(psi3(P),-1,p)%p
    f=(t**3-672*t*t+2352*t+21952)%p
    assert R==beta*f*pow(81*t**3,-1,p)%p
    assert char3(R)==char3(f)
    PM=mul(pow(h,M,n),P)
    assert char3(psi3(PM))==beta*char3(psi3(P))%p
x,u=s.symbols('x u')
f=s.Poly(x**3-672*x*x+2352*x+21952,x)
assert s.discriminant(f)==5334336**2
r,b=s.symbols('r b')
alpha=224+84*r+s.Rational(12,7)*(18-b)*r*r
root_test=alpha**3-672*alpha**2+2352*alpha+21952
root_test=s.rem(s.expand(root_test),r**3-(19+b),r)
root_test=s.rem(s.expand(root_test),b*b+b+1,b)
assert s.expand(root_test)==0
inv=x**3+(84+27*u)*x*x+2352*x+21952
assert s.factor(s.discriminant(inv,x)+(9072*u)**2*21*(u+7))==0
fp=s.Poly(f.as_expr(),x,modulus=p)
a=s.Poly(x,x,modulus=p); result=s.Poly(1,x,modulus=p); k=p
while k:
    if k&1:result=(result*a).rem(fp)
    a=(a*a).rem(fp); k//=2
assert s.gcd(result-s.Poly(x,x,modulus=p),fp).degree()==0
recurrence={str(k):(9*(3**k-1))**2*p < (n-2)**2 for k in [77,78,79]}
words={str(k):(n-3**k)>0 and (n-3**k)**2 > (6*3**k*(3**k-1))**2*p for k in [38,39,40]}
assert recurrence=={'77':True,'78':True,'79':False}
assert words=={'38':True,'39':True,'40':False}
report={'status':'PASS','prime_certificates':proof_count,'known_scalar_cases':len(scalar_cases),'primitive_order_h':str(n-1),'embedding_degree':str(M),'h_order_residues':h_res,'p_order_residues':p_res,'h_to_M':hex(pow(h,M,n)),'scalar_7_primitive':True,'cubic_extension_root_formula':True,'cubic_atom_irreducible':True,'cubic_atom_discriminant':str(5334336**2),'recurrence_excluded_for_length':recurrence,'every_word_sufficient_bound_for_length':words,'limits':'Exact arithmetic checks, not an independent verification of the geometric proofs or original experiments.'}
(base/'cm_eds_results.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
