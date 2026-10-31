"""Symbolic checks only: no elliptic-curve enumeration or statistical simulation."""
import sympy as s
x, r, aa = s.symbols('x r aa')
bb = -r**3-aa*r
D = 3*r*r+aa
xp = r + D/(x-r)
y2 = x**3+aa*x+bb
assert s.factor(D**2*y2/(x-r)**4 - (xp**3+aa*xp+bb)) == 0
I2 = s.eye(2)
I = s.diag(s.I,-s.I)
J = s.Matrix([[0,1],[-1,0]])
K = I*J
qs = [I2,-I2,I,-I,J,-J,K,-K]
A = (I2+I+J+K)/2
assert A.det() == 1
assert s.simplify(A**3) == -I2
traces = [s.simplify(s.trace(A*u)) for u in qs]
assert all(t in [-1,1] for t in traces)
for order in range(1,13):
    value = s.simplify(sum(t**order for t in traces)/8)
    assert value == (1 if order % 2 == 0 else 0)
for ext in range(1,7):
    for rr in range(1,7):
        value = s.simplify(sum(s.trace(A**ext*u)**(2*rr) for u in qs)/8)
        assert value == (4**(rr-1) if ext % 3 == 0 else 1)
t = s.symbols('t')
for m in range(2,14,2):
    char = s.chebyshevu(m,t/2)
    rank = s.diff(char,t).subs(t,2)/2
    assert rank == s.Rational(m*(m+1)*(m+2),12)
for rr in range(1,7):
    total = 0
    for j in range(rr+1):
        multiplicity = s.binomial(2*rr,rr-j) - (s.binomial(2*rr,rr-j-1) if rr-j-1 >= 0 else 0)
        m=2*j
        total += multiplicity*s.Rational(m*(m+1)*(m+2),12)
    assert total == 2*rr*4**(rr-1)
print('General two-torsion translation identity: PASS')
print('Quaternion intertwiner determinant, order, coset traces: PASS')
print('Even/odd finite-factor moment traces through order 12: PASS')
print('Extension-degree phase traces for degrees 1..6: PASS')
print('Symmetric-power rank formulas through degree 12: PASS')
print('Improved moment-rank identity through moment 12: PASS')
print('These checks do not verify the geometric or sheaf-theoretic arguments.')
