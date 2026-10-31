---
title: "Primitive norm-three CM dynamics on secp256k1"
subtitle: "A sixfold quotient orbit and the scope of algebraic scalar-map obstructions"
author: ""
date: "Public mathematical research artifact | 31 October 2026"
---

**Human initiator and curator:** Louis Desbiens  
**AI mathematical research contributor:** OpenAI's ChatGPT  
**Document classification:** Public AI-developed mathematical research artifact -- independently unverified candidate results  
**Institutional affiliation:** None claimed  
**Manuscript license:** Creative Commons Attribution 4.0 International (CC BY 4.0)

**Status and reading guide.** This document records a human-initiated, substantially AI-developed mathematical investigation. The human curator directed the objectives but does not independently certify its advanced mathematical arguments. The novel claims and supplied proofs are candidate results awaiting independent specialist verification; public availability does not certify correctness, completeness or originality. This artifact investigates primitive norm-three complex multiplication, an explicit quotient map and restrictions on certain rational scalar maps. Specific secp256k1 arithmetic is accompanied by machine-rerunnable certificates; the general rigidity application, conditional correspondence arguments and any cryptographic interpretation need separate scrutiny. None of the claims constitutes a general algorithmic lower bound or an ECDLP speedup.

# Abstract

This manuscript examines the order-three automorphism of secp256k1 and a degree-three endomorphism whose scalar eigenvalue is proposed to be primitive modulo the prime group order. On the complete sixfold quotient $t=x^3$, the endomorphism induces the explicit rational map $F(t)=-(t+28)^3/(27t^2)$. The analysis includes its derivation, an exact arithmetic order certificate, a proposed single-cycle description of the quotient states, and the identity expressing $F$ as a functional square root of quotient tripling. This reframes the discrete logarithm modulo sixfold symmetry as an orbit-index problem, without giving a faster method to solve it. A proposed finite-set agreement argument derives the restricted degree bound $(n-1)/72$ for rational quotient maps implementing hidden scalar squaring. Separately, the cited classical rigidity theorem for maps into abelian varieties constrains globally rational point-output constructions on $E^r$ to affine hidden-scalar actions, subject to its hypotheses. The manuscript explores commuting quotient maps and a conditional statement about invariant correspondences; it claims neither a complete positive-characteristic centralizer classification nor a computational lower bound for arbitrary programs. The investigation combines explicit secp256k1 dynamics with established geometric theory, while submitting its new deductions for independent review.

**Keywords:** secp256k1; complex multiplication; Lattes map; primitive orbit; elliptic discrete logarithm; rational map; abelian variety.

# 1. Setting and contribution

A particularly simple endomorphism occurs within the usual $j=0$ structure of secp256k1. This article focuses on that object and the limits of operations that remain rational maps of the generic curve. The surrounding theory of efficient endomorphisms, Lattes maps, and abelian-variety rigidity is classical [1--4]. The arithmetic order certificate and explicit quotient formulas below make the specific arithmetic claims independently checkable; they do not establish historical priority for those formulas.

Let

$$
E/\mathbf F_p:\quad y^2=x^3+7,\qquad p=2^{256}-2^{32}-977.
$$

The prime order $n$ is specified in hexadecimal by concatenating the following two 32-digit words:

```
FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE
BAAEDCE6AF48A03BBFD25E8CD0364141
```

The standard base point is denoted $G$. The domain parameters and cofactor one are those of SEC 2 [1]. In particular, $E(\mathbf F_p)=\langle G\rangle$ and every nonidentity rational point has order $n$. Fix the conventional orientation of the cube roots $\beta\in\mathbf F_p$ and $\lambda\in\mathbf F_n$ by concatenating each pair of hexadecimal words below:

```
beta   = 7ae96a2b657c07106e64479eac3434e9
         9cf0497512f58995c1396c28719501ee
lambda = 5363ad4cc05c30e0a5261c028812645a
         122e22ea20816678df02967c1b23bd72
```

Here leading zeroes are immaterial. They satisfy $\beta^2+\beta+1=0$, $\lambda^2+\lambda+1=0$, and

$$
\phi(x,y)=(\beta x,y),\qquad \phi(G)=[\lambda]G.
$$

The identity on $G$ is a finite group-arithmetic check using the SEC 2 coordinates and the ordinary chord-and-tangent law. Since $G$ generates the rational group, checking it once proves the scalar action on every rational point. Its coordinates, for direct reproduction, are the following hexadecimal pairs:

```
x(G) = 79be667ef9dcbbac55a06295ce870b070
       29bfcdb2dce28d959f2815b16f81798
y(G) = 483ada7726a3c4655da4fbfc0e1108a8
       fd17b448a68554199c47d08ffb10d4b8
```

Define

$$
H=\{\pm1,\pm\lambda,\pm\lambda^2\},\qquad h=2+\lambda,\qquad M=(n-1)/6. \qquad (1.1)
$$

The letter $h$ denotes a scalar in this article, not the cofactor convention used in standards documents.

# 2. A primitive endomorphism of degree three

**Proposition 2.1.** The endomorphism

$$
\Psi=[2]+\phi=1-\phi^2
$$

is separable of degree three, acts as multiplication by $h$ on $E(\mathbf F_p)$, and satisfies

$$
\Psi^2=-[3]\phi^2. \qquad (2.1)
$$

**Proof.** The relation $1+\phi+\phi^2=0$ gives the second expression for $\Psi$. In the Eisenstein order, $N(a+b\omega)=a^2-ab+b^2$, so $N(2+\omega)=3$. Equivalently, composing $2+\phi$ with $1-\phi$ gives $[3]$, and the explicit formulas below show degree three. Since the characteristic is not three, the map is separable. Its rational scalar action follows by evaluating the endomorphism on the generator. Finally, $(2+\phi)^2=3+3\phi=-3\phi^2$. $\square$

**Proposition 2.2 (primitive scalar).** For the fixed orientation in Section 1,

$$
\operatorname{ord}_n(h)=n-1. \qquad (2.2)
$$

**Certificate.** The complete factorization is

$$
n-1=2^6\cdot3\cdot149\cdot631\cdot q_1q_2q_3. \qquad (2.3)
$$

Here the three larger prime factors are

$$
\begin{gathered}
q_1=107361793816595537,\qquad q_2=174723607534414371449,\\
q_3=341948486974166000522343609283189.
\end{gathered}
$$

The factors multiply exactly to $n-1$. Appendix A prints a complete recursive Lucas certificate, including the primality of these factors and of $n$. Its last row uses $h$ as the witness and checks

$$
h^{n-1}\equiv1\pmod n,\qquad
\gcd(h^{(n-1)/q}-1,n)=1
$$

for each distinct prime factor $q$ in (2.3). The criterion proved in the appendix implies (2.2). All certificate data are included in this article. $\square$

The certificate is a short exact computation, not an enumeration of $n-1$ points. Multiplication by a primitive element acts transitively on $\mathbf F_n^*$; consequently $\Psi$ is one cycle on the nonidentity rational points.

Changing from $\lambda$ to its conjugate is an orientation change, not a license to reuse every residue identity unchanged. The quotient map below is insensitive to multiplication of the endomorphism by a sixfold unit, but character normalizations in later work are not.

# 3. The complete sixfold quotient

**Proposition 3.1.** On nonidentity rational points, $t(P)=x(P)^3$ is a complete invariant of the $H$-orbit. Every such orbit has six elements, and there are $M$ quotient states.

**Proof.** Negation fixes $x$, and $\phi$ multiplies $x$ by $\beta$, so $t$ is invariant. If $x(Q)^3=x(P)^3$, then $x(Q)=\beta^j x(P)$ for some $j$. The curve equation gives $y(Q)=\pm y(P)$, hence $Q=\pm\phi^jP$. No nonidentity point of the prime-order group is fixed by a nontrivial element of $H$: the fixed-point conditions would force two- or three-torsion. Thus every orbit has six elements. $\square$

**Proposed Theorem 3.2 (quotient dynamics).** The map induced by $\Psi$ is

$$
x(\Psi P)=-\frac{\beta}{3}\frac{x(P)^3+28}{x(P)^2},\qquad
F(t)=-\frac{(t+28)^3}{27t^2}. \qquad (3.1)
$$

On the set of $M$ nonidentity rational quotient states, $F$ is a single cycle. As rational maps on $\mathbf P^1$,

$$
F^{\circ2}=L_3, \qquad (3.2)
$$

where $L_3$ is the map induced by multiplication by three on $E/H$.

**Proof.** Write $\Psi P=P-\phi^2P$. The joining slope is $-2y/[x(\beta^2-1)]$. Using $(\beta^2-1)^2=-3\beta^2$ and $1+\beta^2=-\beta$ in the chord formula gives the first identity in (3.1). Cubing it gives the second. The rational functions extend across their affine poles as morphisms of the projective line.

The quotient identifies scalar multiplication by the unique subgroup of order six of $\mathbf F_n^*$. Since $h$ is primitive, its class generates $\mathbf F_n^*/H$, a cyclic group of order $M$. This proves the cycle statement. Equation (2.1) differs from multiplication by three by a unit of $H$, which disappears on the quotient; this proves (3.2) as a generic rational identity, not merely a finite-set equality. $\square$

Neither $x=0$ nor an affine two-torsion point belongs to the nonidentity rational subgroup. Therefore the displayed affine denominators do not create exceptional states within this cycle.

# 4. Orbit index and hidden scalar

Let $Q=[d]G$ with $d\neq0$. There is an exponent $\kappa$ modulo $n-1$ with $d=h^\kappa$. Passing to the quotient yields

$$
t(Q)=F^\kappa(t(G)),\qquad \kappa\pmod M. \qquad (4.1)
$$

**Proposed Corollary 4.1 (exact reformulation).** Solving the quotient orbit-index problem in (4.1) determines the six candidates

$$
d_j=h^{\kappa+jM}\pmod n,\qquad 0\leq j<6. \qquad (4.2)
$$

Exactly one satisfies $[d_j]G=Q$. Conversely, knowledge of $d$ determines the target point and its quotient orbit position, although computing $\log_h d$ is itself a multiplicative discrete logarithm.

The useful computational equivalence is in the direction from a recovered quotient shift to the six checked scalar candidates. One should not assert an efficient reduction from an arbitrary scalar-output ECDLP solver to the integer orbit index without accounting for the additional finite-field logarithm $\log_h d$. The phrase "hidden shift" refers here to the orbit relation; (4.1) and (4.2) specify its exact meaning.

A collision between the two walks $F^A(t(G))$ and $F^B(t(Q))$ gives $\kappa=A-B\pmod M$. Such a relation is useful only if $A$ and $B$ are known. A compact formula for a low-norm endomorphism does not automatically provide its exponent relative to $h$.

For example, a jump induced by $a+b\phi$ has degree $a^2-ab+b^2$ and scalar $a+b\lambda$. Its primitive-orbit increment is

$$
\log_h(a+b\lambda)\pmod M,
$$

not the easily computed pair $(a,b)$. This is a known-increment bottleneck: the map and its orbit displacement are different inputs. No sub-square-root orbit-index algorithm follows from the existence of $F$.

# 5. Critical portrait and rational predecessors

The logarithmic derivative of $F$ is

$$
\frac{F'(t)}{F(t)}=\frac{t-56}{t(t+28)}.
$$

Its ramification points are $-28$ with local degree three, $0$ with local degree two, and $56$ with local degree two. Their forward portrait is

$$
-28\longmapsto0\longmapsto\infty\longmapsto\infty,
\qquad 56\longmapsto-7\longmapsto-7. \qquad (5.1)
$$

The normalized coordinate $u=-t/7$ gives

$$
\mathcal G(u)=\frac{(4-u)^3}{27u^2}. \qquad (5.2)
$$

The quotient has ramification signature $(2,3,6)$, as expected for this elliptic quotient. This places the map in the classical Lattes framework [4]; it does not by itself prove every possible positive-characteristic classification assertion.

For a finite target $v$, a predecessor solves

$$
t^3+(84+27v)t^2+2352t+21952=0.
$$

The discriminant is

$$
\Delta(v)=-(9072v)^2\,21(v+7). \qquad (5.3)
$$

For a nonidentity quotient state, $v+7$ is a nonzero square, while $-21$ is a nonsquare in the secp256k1 field; the latter follows from $\chi_2(-3)=1$ and $\chi_2(7)=-1$. Indeed $p\equiv1\pmod3$ supplies a square root of $-3$, while a square root of $7$ would give a rational point $(0,\sqrt7)$ of order three, contrary to the prime group order. The cubic is unramified there. Since the quotient cycle supplies a rational predecessor, its remaining factor is irreducible quadratic: a nonsquare discriminant excludes three rational roots. Thus one rational branch is singled out over $\mathbf F_p$, and the other two are conjugate over its quadratic extension. This arithmetic fact does not make the orbit index easy to recover; the predecessor is already the inverse of a permutation on an enormous cycle.

# 6. A degree obstruction for hidden squaring

Define $t_d=t([d]G)$ for $d\neq0$. The rule $t_d\mapsto t_{d^2}$ is well defined because multiplication of $d$ by a unit of $H$ changes $d^2$ by another unit of $H$.

**Proposed Theorem 6.1 (finite-set degree lower bound).** If a nonconstant rational function $R$ is defined on every nonidentity quotient state and satisfies

$$
R(t_d)=t_{d^2}\qquad(d\in\mathbf F_n^*),
$$

then

$$
\deg R\geq\frac{M}{12}=\frac{n-1}{72}. \qquad (6.1)
$$

**Proof.** At each of the $M$ states,

$$
R\circ F(t_d)=t_{h^2d^2}=F^{\circ2}\circ R(t_d).
$$

Writing $D=\deg R$, the two rational maps have degrees $3D$ and $9D$. They cannot be identical, because their positive degrees differ. Two distinct rational maps of degrees $a,b$ on $\mathbf P^1$ have at most $a+b$ distinct agreement points: clear their homogeneous denominators and count the zeros of the resulting nonzero homogeneous polynomial. Thus $M\leq12D$. $\square$

A constant $R$ cannot satisfy the proposed rule: the squaring map on the cyclic quotient has more than one value. The theorem therefore covers all rational candidates. It is an exact finite-field statement, but it concerns **formal degree**, not evaluation cost. For example, $F^{\circ k}$ has degree $3^k$ and a composition circuit of depth $k$. The generic point-output restriction below is a separate argument and does not use a degree-to-time inference.

# 7. Classical rigidity and point-output constructions

**Theorem 7.1 (classical).** Every rational map from an abelian variety to an abelian variety extends to a morphism and is a homomorphism followed by a translation. In particular,

$$
\mathcal F:E^r\dashrightarrow E\quad\Longrightarrow\quad
\mathcal F(P_1,\ldots,P_r)=T+\sum_{j=1}^r\alpha_j(P_j), \qquad (7.1)
$$

where $\alpha_j\in\operatorname{End}(E)$ and $T\in E$.

**Proof.** The extension theorem for maps from a smooth variety to an abelian variety [3, Theorem 3.1] extends the rational map to a morphism. Subtract its value $T$ at the origin to obtain $g$ with $g(0)=0$. The morphism $D(P,Q)=g(P+Q)-g(P)-g(Q)$ vanishes on both axes. The rigidity lemma [3, Theorem 3.4] makes it identically zero, so $g$ is a homomorphism. Restricting $g$ to each factor gives the endomorphisms $\alpha_j$, and adding the coordinate inclusions gives (7.1). If the original map is defined over the base field, uniqueness of extension and of the restrictions preserves that field of definition. $\square$

**Proposed Corollary 7.2 (hidden-scalar action).** If $\mathcal F$ is defined over $\mathbf F_p$, its action on secp256k1 rational points is

$$
(d_1,\ldots,d_r)\longmapsto c+\sum_{j=1}^rs_jd_j\pmod n. \qquad (7.2)
$$

Indeed, $T=[c]G$ and $\alpha_j(G)=[s_j]G$. Therefore no such globally rational point-output map implements $[d]G\mapsto[d^2]G$, or $([d_1]G,[d_2]G)\mapsto[d_1d_2]G$, on the whole prime-order group. These nonlinear functions cannot coincide with an affine function on that group.

The application includes any arithmetic circuit whose output coordinates satisfy the elliptic-curve equation as an identity in the generic function field of $E^r$. Its formal degree and compactness do not evade the theorem. Intermediate rational maps through auxiliary varieties also do not evade it when the final composition is genuinely a rational map $E^r\dashrightarrow E$.

This is a structural statement about one computational class. It is not a generic-group lower bound, and not a proof that a faster algorithm for ECDLP cannot exist. The generic-group theorem of Shoup [5] concerns a different model and must not be substituted for a proof about a particular coordinate representation.

# 8. What the rigidity statement does not say

## 8.1. Finite-field identities need not define generic curve maps

For a fixed finite field, exponentiation and even a multiplicative character can be expressed by polynomial coordinate functions. Thus "uses a character" is not literally the same as "is not algebraic." The decisive issue in Theorem 7.1 is whether the **point-valued output** defines a rational map on the generic curve, not whether the implementation uses multiplication or exponentiation.

For a rational affine point $Q=(a,b)$, the polynomial

$$
\delta_Q(x,y)=\bigl(1-(x-a)^{p-1}\bigr)\bigl(1-(y-b)^{p-1}\bigr)
$$

is its indicator on $\mathbf F_p^2$. Linear combinations of these indicators can interpolate arbitrary finite tables of affine output coordinates. Such outputs can lie on $E$ at all relevant rational inputs without satisfying the curve equation generically. This observation illustrates the scope limitation; it is not an efficient interpolation algorithm for an unknown discrete logarithm. Projective output coordinates can handle tables containing $O$.

Likewise, selecting roots, testing bits, comparing representatives, or branching may lead outside the generic point-output class. The theorem does not bound the information or computation obtainable from such operations.

## 8.2. Affine leaves are not running-time bounds

Suppose a branch of a program is a globally rational point-output map and agrees with hidden squaring on its assigned scalar inputs. Its scalar expression is $sd+c$, so it can agree with $d^2$ at at most two field elements. Covering all nonzero scalars therefore requires at least $(n-1)/2$ such affine pieces. If equality is required only modulo $H$, each branch gives at most twelve roots by considering $d^2=u(sd+c)$ for the six units $u$, hence at least $(n-1)/12$ pieces are needed.

These are bounds on the **number of distinct affine pieces**, under the stated branch model. They are not exponential time or circuit lower bounds. A program making $k$ binary decisions can have $2^k$ paths, and shared subcomputations may further change its representation size. Neither leaf counting nor generic-map rigidity resolves arbitrary finite-field branching complexity.

## 8.3. Squaring and multiplication

An exact hidden-squaring operation would imply hidden multiplication by polarization:

$$
[d_1d_2]G=[2^{-1}]\bigl(S(P+Q)-S(P)-S(Q)\bigr),
$$

where $P=[d_1]G$, $Q=[d_2]G$, and $S([d]G)=[d^2]G$. The inverse of two is taken modulo $n$. This identifies a useful research target, but does not assert that such an operation has been constructed.

# 9. Pairings and the field-of-definition obstruction

The arithmetic certificate in Appendix A also gives

$$
\operatorname{ord}_n(p)=M. \qquad (9.1)
$$

Appendix A verifies both $p^M=1\pmod n$ and $p^{M/q}\neq1\pmod n$ for every distinct prime divisor $q$ of $M$. The field containing a nontrivial $n$th root of unity must therefore have extension degree divisible by $M$.

The Weil pairing on two points of the same cyclic rational subgroup is trivial by alternation and bilinearity. CM endomorphisms defined over the base field keep that subgroup inside itself. Moving the outputs to an auxiliary low-dimensional variety does not change the elementary condition $n\mid p^m-1$ for a nontrivial $\mu_n$-valued pairing over $\mathbf F_{p^m}$. This is a field-of-definition obstruction for such pairings. It does not classify every possible use of auxiliary varieties or every non-pairing reduction.

# 10. Commuting quotient maps and invariant correspondences

**Proposition 10.1.** Every nonzero Eisenstein endomorphism $\alpha=a+b\phi$ induces a rational map $R_\alpha$ on $E/H$, and $R_\alpha\circ F=F\circ R_\alpha$. Multiplication of $\alpha$ by a sixfold unit does not change $R_\alpha$.

**Proof.** The function $t\circ\alpha$ is invariant under $H$, since $\alpha$ commutes with $\phi$ and negation. The invariant function field is $\mathbf F_p(t)$, so $t\circ\alpha=R_\alpha\circ t$. Commutation of $\alpha$ with $\Psi$ gives $R_\alpha F t=F R_\alpha t$. Since $t$ is dominant, the rational maps agree. Multiplication by a unit changes no quotient value. $\square$

This proves an inclusion in the rational centralizer. It is not a proof that the listed family exhausts that centralizer. A complete converse in positive characteristic requires, among other things, treatment of inseparability and of the lift from the quotient; the complex-analytic classification in [4] is not used as a substitute for that argument.

**Proposition 10.2 (a conditional correspondence statement).** Let $Z\subset E\times E$ be an irreducible projective curve with a nonconstant projection to $E$. Suppose a self-map of $Z$ induces on its smooth normalization $\widetilde Z$ a separable self-map of degree $D>1$. Then $\widetilde Z$ has genus one, and over an algebraic closure the image of $\widetilde Z$ in $E\times E$ is a translate of an elliptic subgroup.

**Proof.** Riemann--Hurwitz gives $2g-2\geq D(2g-2)$, so $g\leq1$. Genus zero is impossible: every map from $\mathbf P^1$ to an abelian variety is constant [3, Corollary 3.8]. Choose a point on the genus-one normalization as origin. Its map to $E\times E$, translated to send this origin to zero, is a homomorphism by [3, Corollary 3.6]. Its image is a one-dimensional abelian subvariety. Undoing the translation proves the claim. $\square$

For a component preserved only by an iterate, the hypothesis must be checked for that iterate. The translation need not vanish. This proposition does not classify every correspondence on the quotient line, nor does it convert a multivalued correspondence into a point-valued algorithm.

# 11. Interpretation and conclusion

The exploratory investigation used numerical evaluations to test the initial intuition behind the quotient dynamics. The cycle assertion itself follows from the complete arithmetic certificate, not from observing a long orbit. Appendix A also supplies the checks for the embedding degree and the orientation identities.

The positive object is an explicit primitive degree-three quotient dynamics. The principal restriction is the classical affine form of globally rational point-output maps. Their combination narrows a class of proposed constructions without proving a general security statement. Large formal degree, finite-field interpolation, branching, and discrete labels must be analyzed in their own computational models. No method beating the generic square-root scale is established here.

# Appendix A. Complete arithmetic certificate

This appendix gives all data needed to certify the scalar order; it does not rely on an external computation file. The prime coordinate modulus and the curve parameters are the published SEC 2 parameters. The order $n$, the three large factors of $n-1$, and every auxiliary prime used below are certified by the following elementary criterion.

**Lucas criterion.** Suppose the complete factorization $q-1=\prod t^{e_t}$ is known, every $t$ has already been proved prime, and an integer $a$ satisfies

$$
a^{q-1}\equiv1\pmod q,\qquad
\gcd(a^{(q-1)/t}-1,q)=1\quad\text{for every }t\mid q-1.
$$

Then $q$ is prime and $a$ has order $q-1$ modulo $q$. Indeed, for every prime divisor $\ell$ of $q$, the displayed conditions force the order of $a$ modulo $\ell$ to contain the full power of every prime dividing $q-1$. Thus $q-1\mid\ell-1$, so $\ell\geq q$ and $\ell=q$.

Use the parameters $n,\lambda$ of Section 1 and $h=\lambda+2$. The labels in the table mean

$$
q_1=107361793816595537,\qquad q_2=174723607534414371449,
$$
$$
q_3=341948486974166000522343609283189,
$$
$$
r_0=29047611873442575647497758179.
$$

Starting with the prime $2$, the rows are in increasing numerical order. Each row states a complete factorization and a Lucas witness. Integer multiplication, modular exponentiation, and the Euclidean algorithm verify every row. No probabilistic primality test is required.

| $q$ | Factorization of $q-1$ | Witness $a$ |
|:--|:--|:--:|
| $3$ | $2$ | $2$ |
| $5$ | $2^{2}$ | $2$ |
| $7$ | $2\cdot 3$ | $3$ |
| $11$ | $2\cdot 5$ | $2$ |
| $13$ | $2^{2}\cdot 3$ | $2$ |
| $17$ | $2^{4}$ | $3$ |
| $19$ | $2\cdot 3^{2}$ | $2$ |
| $23$ | $2\cdot 11$ | $5$ |
| $29$ | $2^{2}\cdot 7$ | $2$ |
| $37$ | $2^{2}\cdot 3^{2}$ | $2$ |
| $41$ | $2^{3}\cdot 5$ | $6$ |
| $59$ | $2\cdot 29$ | $2$ |
| $67$ | $2\cdot 3\cdot 11$ | $2$ |
| $73$ | $2^{3}\cdot 3^{2}$ | $5$ |
| $97$ | $2^{5}\cdot 3$ | $5$ |
| $109$ | $2^{2}\cdot 3^{3}$ | $6$ |
| $113$ | $2^{4}\cdot 7$ | $3$ |
| $149$ | $2^{2}\cdot 37$ | $2$ |
| $199$ | $2\cdot 3^{2}\cdot 11$ | $3$ |
| $293$ | $2^{2}\cdot 73$ | $2$ |
| $461$ | $2^{2}\cdot 5\cdot 23$ | $2$ |
| $631$ | $2\cdot 3^{2}\cdot 5\cdot 7$ | $3$ |
| $797$ | $2^{2}\cdot 199$ | $2$ |
| $1409$ | $2^{7}\cdot 11$ | $3$ |
| $1871$ | $2\cdot 5\cdot 11\cdot 17$ | $14$ |
| $2011$ | $2\cdot 3\cdot 5\cdot 67$ | $3$ |
| $2731$ | $2\cdot 3\cdot 5\cdot 7\cdot 13$ | $3$ |
| $2861$ | $2^{2}\cdot 5\cdot 11\cdot 13$ | $2$ |
| $4051$ | $2\cdot 3^{4}\cdot 5^{2}$ | $10$ |
| $9349$ | $2^{2}\cdot 3\cdot 19\cdot 41$ | $2$ |
| $16699$ | $2\cdot 3\cdot 11^{2}\cdot 23$ | $3$ |
| $28181$ | $2^{2}\cdot 5\cdot 1409$ | $2$ |
| $85831$ | $2\cdot 3\cdot 5\cdot 2861$ | $3$ |
| $120233$ | $2^{3}\cdot 7\cdot 19\cdot 113$ | $3$ |
| $305873$ | $2^{4}\cdot 7\cdot 2731$ | $3$ |
| $1627771$ | $2\cdot 3\cdot 5\cdot 29\cdot 1871$ | $3$ |
| $4681609$ | $2^{3}\cdot 3\cdot 97\cdot 2011$ | $23$ |
| $44706919$ | $2\cdot 3\cdot 797\cdot 9349$ | $6$ |
| $545358713$ | $2^{3}\cdot 41\cdot 59\cdot 28181$ | $5$ |
| $297159362677$ | $2^{2}\cdot 3^{2}\cdot 11\cdot 461\cdot 1627771$ | $2$ |
| $q_1$ | $2^{4}\cdot 16699\cdot 85831\cdot 4681609$ | $3$ |
| $q_2$ | $2^{3}\cdot 17\cdot 59\cdot 4051\cdot 120233\cdot 44706919$ | $3$ |
| $r_0$ | $2\cdot 293\cdot 305873\cdot 545358713\cdot 297159362677$ | $2$ |
| $q_3$ | $2^{2}\cdot 3^{3}\cdot 109\cdot r_0$ | $2$ |
| $n$ | $2^{6}\cdot 3\cdot 149\cdot 631\cdot q_1\cdot q_2\cdot q_3$ | $h$ |

The last row uses $h$ itself. It simultaneously proves that $n$ is prime and that $h$ has order $n-1$. Its seven proper-order tests are precisely those for the distinct factors $2,3,149,631,q_1,q_2,q_3$; in particular, the certificate is not a traversal of the curve group.

The following additional checks use the same stated parameters. They can be reproduced by the short exact-arithmetic code printed below; exponentiation is repeated squaring. Here hexadecimal strings are concatenated before conversion.

```python
from math import gcd
p = 2**256 - 2**32 - 977
n = int('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFE'
        'BAAEDCE6AF48A03BBFD25E8CD0364141', 16)
beta = int('7ae96a2b657c07106e64479eac3434e9'
           '9cf0497512f58995c1396c28719501ee', 16)
lam = int('5363ad4cc05c30e0a5261c028812645a'
          '122e22ea20816678df02967c1b23bd72', 16)
h, M = lam + 2, (n - 1) // 6
factors = [2, 3, 149, 631, 107361793816595537,
           174723607534414371449,
           341948486974166000522343609283189]
assert (beta*beta + beta + 1) % p == 0
assert (lam*lam + lam + 1) % n == 0
assert pow(h, n-1, n) == 1
for t in factors:
    assert gcd(pow(h, (n-1)//t, n)-1, n) == 1
assert pow(p, M, n) == 1
for t in factors:
    if M % t == 0:
        assert pow(p, M//t, n) != 1
assert pow(h, M, n) == (-lam*lam) % n
assert M % 3 == 1 and p % 9 == 7
assert pow((beta*pow(81, -1, p)) % p, (p-1)//3, p) == 1
assert pow(19+beta, (p-1)//3, p) == beta
assert pow((-beta*pow(3, -1, p)) % p, (p-1)//3, p) == 1
assert (n-2)**2 > (9*(3**78-1))**2*p
assert (n-2)**2 <= (9*(3**79-1))**2*p
assert (n-3**39)**2 > (6*3**39*(3**39-1))**2*p
assert (n-3**40)**2 <= (6*3**40*(3**40-1))**2*p
```

The code uses ordinary arbitrary-precision integers; negative modular exponents denote inverses. The four squared inequalities are used only with positive sides. They therefore certify, without floating-point rounding, the thresholds in the character-sum applications. These finite arithmetic certificates support the explicitly stated parameters and identities; they are not a substitute for the geometric proofs.


# Research provenance, contributions, and verification status

## Origin and development of the investigation

This mathematical investigation was initiated and directed by Louis Desbiens and developed through extensive interaction with OpenAI's ChatGPT. Louis Desbiens identified the original research questions, set the objectives, guided the investigation, assessed its progress at a conceptual level, and selected the material for public dissemination.

ChatGPT contributed substantially to mathematical exploration, including alternative formulations, derivation of algebraic identities, formulation and examination of conjectures and proposed proofs, identification of potential counterexamples and exceptional cases, design and execution of symbolic and numerical checks, organization of relevant literature, and drafting and revision of the text. These contributions went well beyond linguistic or editorial assistance.

## Attribution and scientific authorship

Louis Desbiens is identified as the **human initiator and curator**, not as an independent mathematical authority certifying the results. OpenAI's ChatGPT is identified as the **AI mathematical research contributor**, not as an accountable conventional scholarly coauthor. These designations describe the provenance without implying that the human curator personally derived or independently verified all the arguments.

## Mathematical verification status

The candidate mathematical contributions have not undergone independent specialist validation, formal proof verification, or an exhaustive originality and priority review. In particular, independent examination is needed of the complete arithmetic certificate and fixed endomorphism orientation; the quotient-cycle deduction; hypotheses and use of classical rigidity; scope of the finite-set degree obstruction and conditional correspondences. Locally displayed proofs are proposed arguments. Established results cited from public literature should be assessed separately from new deductions; neither an AI-generated proof nor a successful computational check is by itself an independently certified theorem. Individual statements may be correct, partly correct, incomplete, or incorrect.

## Responsibility and purpose of public release

Louis Desbiens assumes responsibility for the decision to release this collection and for a good-faith account of its origin, contributors and verification status. He does **not** claim to have personally established or independently certified the correctness, completeness or originality of the proposed mathematical results. The material is made available for independent examination, criticism, reproducibility and possible further development; publication does not constitute scientific endorsement. This disclosure does not eliminate ordinary responsibilities associated with distributing public material.

## Institutional independence, funding, and competing interests

No institutional affiliation or endorsement is claimed. The investigation was undertaken independently, without institutional funding or resources. No external research funding was received. The human curator reports no competing interests.

## Computational evidence and source availability

Numerical evaluations helped develop the initial intuition. The public repository contains the available scripts, archived results, and a claim-by-claim verification coverage guide. These are scoped finite arithmetic, symbolic, and numerical checks, not independent verification of the general mathematical results. Historical exploratory calculations for which independent source data are unavailable are not treated as reproducible evidence.

# References

[1] Certicom Research, *SEC 2: Recommended Elliptic Curve Domain Parameters*, version 2.0, 27 January 2010, Section 2.4.1. https://www.secg.org/sec2-v2.pdf.

[2] R. P. Gallant, R. J. Lambert, and S. A. Vanstone, "Faster point multiplication on elliptic curves with efficient endomorphisms," *CRYPTO 2001*, LNCS 2139, 190--200, 2001. DOI: 10.1007/3-540-44647-8_11. Public conference paper: <https://www.iacr.org/archive/crypto2001/21390189.pdf>. For an openly accessible treatment of endomorphisms and their arithmetic use, see [6].

[3] J. S. Milne, "Abelian varieties," in *Arithmetic Geometry*, Springer, 1986, pp. 103--150. Corrected public author version, 2 January 2022, Section 3 (Theorem 3.1, Theorem 3.4, Corollary 3.6): https://www.jmilne.org/math/xnotes/AVs.pdf.

[4] J. Milnor, *On Lattes Maps*, arXiv:math/0402147v2, 2004. https://arxiv.org/abs/math/0402147v2. Used for context on complex elliptic-quotient dynamics, not a positive-characteristic classification.

[5] V. Shoup, "Lower bounds for discrete logarithms and related problems," *EUROCRYPT 1997*, LNCS 1233, 256--266, 1997. Public author version: https://www.shoup.net/papers/dlbounds1.pdf. Its generic-group model is distinct from the restricted geometric model considered here.

[6] S. D. Galbraith, *Mathematics of Public Key Cryptography*, Cambridge University Press, 2012. Public author version and errata: https://www.math.auckland.ac.nz/~sgal018/crypto-book/crypto-book.html.
