---
title: "Polynomial and rational osculation on elliptic curves"
subtitle: "Residual divisors, coordinate traces, and genus-one reduction"
author: ""
date: "Public mathematical research artifact | 31 October 2026"
---

**Human initiator and curator:** Louis Desbiens  
**AI mathematical research contributor:** OpenAI's ChatGPT  
**Document classification:** Public AI-developed mathematical research artifact -- independently unverified candidate results  
**Institutional affiliation:** None claimed  
**Manuscript license:** Creative Commons Attribution 4.0 International (CC BY 4.0)

**Status and reading guide.** This document records a human-initiated, substantially AI-developed mathematical investigation. The human curator directed the objectives but does not independently certify its advanced mathematical arguments. The novel claims and supplied proofs are candidate results awaiting independent specialist verification; public availability does not certify correctness, completeness or originality. This artifact develops polynomial and rational contact constructions and distinguishes residual group sums from coordinate traces. Classical divisor theory, the genus-one Picard group and Riemann--Roch are cited inputs, not claimed inventions. The local formulas, mixed-contact conventions, multiplicity arguments and exceptional cases should receive specialist review. Sampled osculation checks are available but do not certify the general divisor results.

# Abstract

Higher-order contact curves extend the geometry of the chord-and-tangent law, but they do not generally leave a single residual point. For a nonsingular short Weierstrass curve and an affine point with nonzero ordinate, this manuscript distinguishes the group sum of a residual divisor from the ordinary sum of its abscissae. The proposed analysis shows that an order-$d$ polynomial contact, with nonvanishing leading coefficient and $d\geq3$, leaves a divisor of degree $d-2$ whose group sum is $-[d]P$. Its coordinate trace obeys a separate Vieta identity, including an essential exception at $d=3$. The manuscript presents formulas for tripling and quadrupling, a finite-field counterexample to the coordinate-trace shortcut, and a discussion of classical genus-one Mumford reduction. A complementary Riemann--Roch construction using $A-By$ is proposed to leave exactly one residual point. Formal coefficient recurrences avoid factorial divisions in positive characteristic. The proposed proofs address multiplicities and torsion exceptions. These constructions concern known multiples and divisor invariants, not recovery of an unknown scalar. No novelty is claimed for the classical divisor theory, Riemann--Roch theorem, or Cantor reduction on which the treatment depends.

**Keywords:** elliptic curve; osculation; residual divisor; Vieta identity; Mumford representation; rational contact; finite field.

# 1. Introduction

The chord-and-tangent law turns an intersection divisor into a group sum. Replacing a line by a higher-degree graph is natural, but the number of remaining intersections changes. The central issue is therefore not whether higher contact exists: it is which invariant of its residual divisor represents the desired multiple.

We develop a self-contained comparison between polynomial contact, divisor reduction, and a rational contact construction with one residual point. The group law, the identification $E\simeq\operatorname{Pic}^0(E)$, Riemann--Roch, and genus-one Cantor reduction are classical [1--3]. Our purpose is to derive the concrete formulas with their hypotheses and explain exactly why a coordinate-trace shortcut fails. No new group law or general inversion algorithm is asserted.

The exploratory investigation used numerical evaluations to test and refine the initial intuition and to check low-order identities. The conclusions below rest on the displayed arguments, not on those evaluations. All nonstandard constructions and conventions needed to read the paper are defined here.

# 2. Local coefficients without factorials

Let $k$ be a field of characteristic different from two and three, and let

$$
E:\quad y^2=C(x)=x^3+Ax+B,\qquad 4A^3+27B^2\neq0.
$$

Write $O$ for the point at infinity and $P=(a,b)\in E(k)$, with $b\neq0$. A point in parentheses denotes a divisor; $[d]P$ denotes group multiplication. Put $z=x-a$. The formal implicit-function theorem gives a unique branch

$$
S(z)=\sum_{j\geq0}c_jz^j,\qquad c_0=b,\qquad S(z)^2=C(a+z).
$$

**Lemma 2.1 (coefficient recurrence).** Write $C(a+z)=\sum g_jz^j$, where $g_0=b^2$, $g_1=3a^2+A$, $g_2=3a$, $g_3=1$, and $g_j=0$ for $j>3$. Then, for $m\geq1$,

$$
2b c_m=g_m-\sum_{j=1}^{m-1}c_jc_{m-j}. \qquad (2.1)
$$

**Proof.** In the coefficient of $z^m$ in $S^2$, the two terms involving the unknown $c_m$ sum to $2bc_m$. All remaining terms involve coefficients already determined. Since $2b$ is invertible, the recurrence determines the branch uniquely. Conversely, its coefficients make $S^2-C$ vanish identically. $\square$

In particular,

$$
c_1=\frac{3a^2+A}{2b},\qquad c_2=\frac{3a-c_1^2}{2b},\qquad c_3=\frac{1-2c_1c_2}{2b}. \qquad (2.2)
$$

In characteristic zero, $c_j=S^{(j)}(0)/j!$. In characteristic $p$, that interpretation is valid for $j<p$, but (2.1) remains meaningful for all indices. It is therefore the coefficient recurrence, rather than unrestricted ordinary differentiation, that should be used in finite-field implementations.

# 3. The residual-divisor theorem

For an integer $d\geq3$, define

$$
f_{d-1}(z)=\sum_{j=0}^{d-1}c_jz^j.
$$

**Proposed Theorem 3.1 (polynomial contact).** Assume $c_{d-1}\neq0$. There is a polynomial

$$
H_d(z)=\frac{f_{d-1}(z)^2-C(a+z)}{z^d},\qquad \deg H_d=d-2, \qquad (3.1)
$$

and an effective affine divisor $D$, defined over $k$, such that

$$
\operatorname{div}(y-f_{d-1}(x-a))=d(P)+D-(2d-2)(O). \qquad (3.2)
$$

The residual points, counted with multiplicity over an algebraic closure, have coordinates $(a+z,f_{d-1}(z))$ for the roots $z$ of $H_d$. Their group sum satisfies

$$
\Sigma_E(D)=-[d]P. \qquad (3.3)
$$

For $d\geq4$, their coordinate trace is

$$
\operatorname{Tr}_x(D)=\sum_{R\in D}x(R)=(d-2)a-2\frac{c_{d-2}}{c_{d-1}}. \qquad (3.4)
$$

**Proof.** Formal contact implies that $f_{d-1}-S$ is divisible by $z^d$, while $f_{d-1}+S$ has constant term $2b\neq0$. Hence their product is divisible by $z^d$. The numerator in (3.1) has degree $2d-2$ and leading coefficient $c_{d-1}^2$, proving its stated degree.

The functions $x$ and $y$ have pole orders two and three at $O$. Since $d\geq3$, the pole order of $y-f_{d-1}$ is exactly $2d-2$. Removing the prescribed $d$ zeros at $P$ leaves an effective divisor of degree $d-2$, proving (3.2). If contact is greater than $d$, some of that divisor remains supported at $P$.

At a residual point with nonzero ordinate, the other factor $y+f_{d-1}$ is a unit, so the polynomial multiplicity agrees with the intersection multiplicity. If the residual ordinate is zero, nonsingularity gives $C'(x)\neq0$. The derivative of $f_{d-1}^2-C$ is then nonzero, so this root in $x$ is simple; the zero of $y-f_{d-1}$ in the local parameter $y$ is also simple. This accounts for every multiplicity, without assuming rational or distinct residual points.

A principal degree-zero divisor has zero group sum under $E\simeq\operatorname{Pic}^0(E)$ [1]. Applying this criterion to (3.2) proves (3.3). For $d\geq4$, the two highest coefficients in the numerator of (3.1) are $c_{d-1}^2$ and $2c_{d-1}c_{d-2}$; the cubic $C$ does not affect them. Vieta's formula gives the sum of the $z$-roots as $-2c_{d-2}/c_{d-1}$. Adding $a$ for each of the $d-2$ roots proves (3.4). $\square$

The distinction between (3.3) and (3.4) is essential. The first is an equality in an elliptic-curve group; the second is an equality in the coordinate field. In general,

$$
\operatorname{Tr}_x(D)\neq x(\Sigma_E(D)).
$$

Where ordinary derivatives are valid, writing $D_j=S^{(j)}(0)$ converts (3.4) to the derivative identity

$$
\operatorname{Tr}_x(D)=(d-2)a-2(d-1)\frac{D_{d-2}}{D_{d-1}},\qquad d\geq4. \qquad (3.5)
$$

If $c_{d-1}=0$, neither the displayed residual degree nor divisions by that coefficient may be retained. The actual polynomial degree and pole divisor must be recomputed. Some low-order degree drops are exactly torsion phenomena, as described next.

# 4. Doubling, tripling, and quadrupling

## 4.1. The tangent and the exceptional tripling term

The tangent line has slope $c_1$, and the usual group law gives

$$
x([2]P)=c_1^2-2a.
$$

The line has pole order three, so doubling must not be forced into the pole-order formula $2d-2$ used above. For tripling, $d=3$ and the residual polynomial is linear:

$$
H_3(z)=(2c_1c_2-1)+c_2^2z.
$$

If $c_2\neq0$, its point is $-[3]P$ and

$$
x([3]P)=a-\frac{2c_1}{c_2}+\frac1{c_2^2},\qquad y([3]P)=-f_2(x([3]P)-a). \qquad (4.1)
$$

Equivalently,

$$
x([3]P)=a-\frac{4D_1}{D_2}+\frac4{D_2^2}.
$$

The extra $1/c_2^2$ term is caused by the coefficient of $z^3$ in $C(a+z)$. Omitting it is precisely why the general trace formula cannot be used at $d=3$.

**Lemma 4.1 (low-order exceptions).** Under the standing hypotheses, $c_2=0$ if and only if $[3]P=O$, and $c_3=0$ if and only if $[4]P=O$.

**Proof.** If $c_2=0$, the tangent has contact at least three and pole order three, so its divisor is $3(P)-3(O)$. Conversely, a function with that divisor lies in the span of $1,x,y$. Its $y$ coefficient is nonzero, since a nonzero linear polynomial in $x$ cannot vanish to order three at this point. After normalization, it is the tangent, forcing $c_2=0$.

If $c_3=0$, (2.2) gives $2c_1c_2=1$, so the quadratic osculant has degree two, contact at least four, and pole order four. Its divisor is $4(P)-4(O)$. Conversely, a function with that divisor lies in the span of $1,x,y,x^2$ and must have nonzero $y$ coefficient. Normalization identifies it with the quadratic contact function and forces $c_3=0$. $\square$

These exceptions agree with the familiar division polynomials. In particular,

$$
\psi_3(a)=3a^4+6Aa^2+12Ba-A^2,\qquad c_2=\frac{\psi_3(a)}{8b^3}. \qquad (4.2)
$$

## 4.2. Quadrupling without splitting the residual quadratic

For $d=4$ and $c_3\neq0$,

$$
H_4(z)=c_3^2z^2+2c_2c_3z+(c_2^2+2c_1c_3). \qquad (4.3)
$$

Reduce $f_3$ modulo $H_4$. The remainder is $\mu z+\nu$, where

$$
\mu=\frac{c_2^2}{c_3}-c_1,\qquad
\nu=b+\frac{c_2(c_2^2+2c_1c_3)}{c_3^2}. \qquad (4.4)
$$

This line contains the two residual points, including their multiplicities. Since their sum is $-[4]P$, its third intersection is **$[4]P$**, not its negative. Vieta's formula for the line therefore gives

$$
x([4]P)=\left(c_1-\frac{c_2^2}{c_3}\right)^2-2a+\frac{2c_2}{c_3}, \qquad (4.5)
$$

$$
y([4]P)=\mu\bigl(x([4]P)-a\bigr)+\nu.
$$

The slope in (4.4) is specified to remove the sign ambiguity that a squared-slope formula alone leaves unresolved. In derivative notation, (4.5) becomes

$$
x([4]P)=\left(D_1-\frac{3D_2^2}{2D_3}\right)^2-2a+\frac{6D_2}{D_3}.
$$

No factorization of $H_4$ is needed. The formula remains valid for a repeated root or a nonsplit quadratic, because polynomial reduction respects the residual divisor scheme.

## 4.3. A finite-field counterexample to the trace shortcut

On $E/\mathbf F_{101}:y^2=x^3+7$, take $P=(4,24)$. The first four local coefficients are

$$
(c_0,c_1,c_2,c_3)=(24,1,36,89).
$$

The residual quadratic is $60+45z+43z^2$. Its residual points are $(51,67)$ and $(64,64)$, while $[4]P=(50,75)$. Thus

$$
51+64=14\pmod{101},\qquad x([4]P)=50.
$$

The residual group sum is $(50,26)=-[4]P$. This example demonstrates the distinction directly: the divisor relation holds exactly and the proposed coordinate-sum shortcut fails.

# 5. Genus-one Mumford reduction

The full residual divisor, unlike its coordinate trace, contains enough information to recover the multiple. Represent an effective divisor on the graph $y=V(x)$ by a monic polynomial $U$, with $\deg V<\deg U$ and

$$
U\mid V^2-C.
$$

The pair $(U,V)$ represents the degree-zero class of that divisor minus $(\deg U)(O)$. Starting from contact data in the local coordinate gives $U=z^d$ and $V=f_{d-1}$.

**Proposition 5.1 (reduction step).** For such a semireduced pair of degree greater than one, define

$$
U_{\mathrm{new}}=\operatorname{monic}\left(\frac{V^2-C}{U}\right),\qquad
V_{\mathrm{new}}=-V\bmod U_{\mathrm{new}}. \qquad (5.1)
$$

The new pair represents the same divisor class. Iteration terminates with degree at most one and represents $[d]P$ for the initial contact pair.

**Proof.** The zeros of $y-V$ comprise the divisor represented by $(U,V)$ and its residual divisor. Their total group sum is zero, as the poles are supported at $O$. The negative of the residual divisor therefore represents the original class. Negation changes the ordinate from $V$ to $-V$, which is exactly the second operation in (5.1). Taking the monic quotient records its abscissae.

If $r=\deg U\geq3$, the quotient degree is at most $2r-2-r=r-2$. If $r=2$, the cubic term of $C$ makes the quotient degree one. Degree drops only accelerate termination. At degree zero the class is $O$; at degree one its unique point is obtained from the root of $U$ and $V$ evaluated there. The starting class is $d(P)-d(O)$, hence its group representative is $[d]P$. This is the genus-one specialization of the classical reduction construction [2,3]. $\square$

An implementation must reduce $V$ modulo $U$ after each step, use exact field arithmetic, and allow degree-zero output. For the point in Section 4.3, order-eight contact has degree path $8,6,4,2,1$.

## 5.1. Mixed contacts and inverse steps

The same method applies to a prescribed effective divisor $D=\sum m_i(P_i)$ with pairwise distinct abscissae and nonzero ordinates. At each $P_i$, take the local branch with that ordinate and impose $V\equiv S_i\pmod{(x-x(P_i))^{m_i}}$. The Chinese remainder theorem supplies a unique $V$ of degree less than $\deg U$, where $U=\prod_i(x-x(P_i))^{m_i}$. Then $U\mid V^2-C$, and Proposition 5.1 returns $\sum_i[m_i]P_i$. Opposite pairs must first be cancelled in the group; a two-torsion point is represented with multiplicity at most one after cancellation. These restrictions are the meaning of a semireduced divisor in this model.

Reduction is not an injective transformation of polynomial data. Given a reduced pair $(U_1,V_1)$, a predecessor must have

$$
V=-V_1+U_1W
$$

for an unspecified polynomial $W$, followed by $U=(V^2-C)/U_1$ and the appropriate monic normalization. The missing quotient $W$ is not determined by the reduced point. For example, every nonvertical line through a fixed affine point produces a residual quadratic divisor with the same reflected group sum. Thus reversing a remainder step introduces choices; decreasing polynomial degree during reduction is not decreasing the represented scalar.

# 6. Rational contact with a single residual point

Polynomial graphs impose an unnecessary restriction if the aim is to leave a single residual point. The complete space of functions with a bounded pole at $O$ contains both polynomial terms and terms involving $y$.

**Proposed Theorem 6.1 (Riemann--Roch contact).** For $m\geq2$, the $k$-vector space

$$
L((m+1)(O)-m(P))
$$

has dimension one. Every nonzero element $h$ has divisor

$$
\operatorname{div}(h)=m(P)+(R)-(m+1)(O),\qquad R=-[m]P. \qquad (6.1)
$$

If $R=O$, one copy of $O$ cancels and the actual pole order is $m$.

**Proof.** The defining divisor has degree one. Riemann--Roch on a genus-one curve gives dimension equal to the degree for every divisor of positive degree [1]. For a nonzero section, the divisor obtained by adding $(m+1)(O)-m(P)$ is effective of degree one. It is a $k$-rational point $R$. The principal-divisor group-sum criterion gives $[m]P+R=O$. $\square$

The functions $1,x,x^2,\ldots,y,xy,x^2y,\ldots$ have pole orders $0,2,4,\ldots,3,5,7,\ldots$. Therefore $h$ can be written in the local coordinate as

$$
h=A_m(z)-B_m(z)y,
$$

$$
2\deg A_m\leq m+1,\qquad 2\deg B_m\leq m-2. \qquad (6.2)
$$

There are $m+1$ coefficients. The condition

$$
A_m-B_mS\equiv0\pmod{z^m} \qquad (6.3)
$$

is a homogeneous linear system with a one-dimensional solution space. This is a Pade-type contact system. Its degree patterns are consequences of the pole filtration, not guesses from numerical examples.

**Proposed Corollary 6.2 (norm identity).** If $[m]P\neq O$, then for some $\kappa\in k^*$,

$$
N_m(z)=A_m(z)^2-C(a+z)B_m(z)^2
       =\kappa z^m(z-z_m), \qquad (6.4)
$$

$$
z_m=x([m]P)-a.
$$

If $[m]P=O$, the norm has the corresponding lower degree and is proportional to $z^m$.

**Proof.** Let $\pi_x:E\to\mathbf P^1$ be the degree-two map defined by $x$. The field norm is $h\bar h=A_m^2-CB_m^2$, and the divisor of a norm is the pushforward of the divisor of the function. Over an algebraic closure, pushing (6.1) forward gives

$$
\operatorname{div}_{\mathbf P^1}(N_m)
=m(a)+(x(R))-(m+1)(\infty).
$$

Consequently $N_m$ is the displayed polynomial up to a nonzero constant. This argument also covers a two-torsion residual point: pushforward counts its divisor multiplicity, rather than multiplying it by the ramification index of $x$. If $R=P$ or $R=-P$, the two roots in the coordinate line coincide and the answer is $\kappa z^{m+1}$. If $R=O$, cancellation in (6.1) gives $m(a)-m(\infty)$ and the norm is $\kappa z^m$. $\square$

The norm forgets the residual ordinate. Recovering it by $A_m/B_m$ is legitimate only where the denominator is nonzero. At a common zero of the coefficient polynomials, direct evaluation or local cancellation is required. These cases must not be erased from an implementation test suite.

# 7. Logarithmic derivatives and the scalar-extraction limitation

Away from the roots of (6.4), differentiation gives

$$
\frac{N_m'(z)}{N_m(z)}=\frac{m}{z}+\frac1{z-z_m},\qquad
m=z\left(\frac{N_m'(z)}{N_m(z)}-\frac1{z-z_m}\right). \qquad (7.1)
$$

This identity correctly recovers the multiplication index already used to construct the contact data. It is not an inversion algorithm for $Q=[m]P$: the coefficients of $A_m$ and $B_m$, the order of the linear system, and the norm itself depend on the unknown index. In characteristic $p$, the displayed $m$ is moreover its image in the coordinate field, not automatically a canonical scalar modulo a distinct group order $n$.

There is also an orientation-sensitive logarithmic derivative. For $h=A-By$, let $\bar h=A+By$ and differentiate along the curve. Direct algebra gives

$$
J_h=\frac{d}{dx}\log\frac{h}{\bar h}
=\frac{2C(A'B-AB')-AB C'}{y(A^2-CB^2)}. \qquad (7.2)
$$

It changes sign under $P\mapsto-P$, unlike the norm $A^2-CB^2$. That makes it compatible with an odd scalar label, but compatibility is not predictive power. No statistical or computational advantage follows from the sign identity alone.

More generally, constructing degree-$O(m)$ contact data should not be described as a large-scalar algorithm of complexity polynomial in $\log m$. A separate complexity analysis would be needed to justify such a claim. Ordinary multiplication by a known scalar already uses a short addition chain; no improvement over it is established here.

# 8. A direct verification procedure

Every formula in this note can be checked without a specialized implementation. Given a nonsingular curve, an affine point $P=(a,b)$ with $b\neq0$, and a known small index, first generate the coefficients using (2.1). Form $f_{d-1}^2-C$ and divide by $z^d$ exactly. Its degree and two leading coefficients check (3.1) and (3.4); the special linear remainder at $d=3$ checks (4.1). Apply (5.1), and compare the final point with independently computed chord-and-tangent multiplication.

For rational contact, solve the homogeneous system (6.3), form $A_m^2-CB_m^2$, and compare the residual abscissa with $x([m]P)$. Include inputs with $[m]P=O$, increased contact, and nonsplit residual polynomials. These tests are useful for detecting arithmetic or transcription errors but do not prove a statement for every index or field. The exact example of Section 4.3 is part of the paper and requires no external dataset.

# 9. Conclusion

Higher contact provides a valid geometric representation of known elliptic multiples, but its residual divisor must be interpreted in the group law. A coordinate trace is a useful symmetric invariant, not the coordinate of that group sum. Genus-one reduction restores the correct multiple, while the full Riemann--Roch space supplies a genuine single-residual construction. The logarithmic-derivative identity is a diagnostic of a known contact order, not evidence of private-key recovery. The contribution of this note is a precise synthesis and reproducible treatment of the osculation constructions; a claim of original multiplication theory would require a separate literature investigation.

# Research provenance, contributions, and verification status

## Origin and development of the investigation

This mathematical investigation was initiated and directed by Louis Desbiens and developed through extensive interaction with OpenAI's ChatGPT. Louis Desbiens identified the original research questions, set the objectives, guided the investigation, assessed its progress at a conceptual level, and selected the material for public dissemination.

ChatGPT contributed substantially to mathematical exploration, including alternative formulations, derivation of algebraic identities, formulation and examination of conjectures and proposed proofs, identification of potential counterexamples and exceptional cases, design and execution of symbolic and numerical checks, organization of relevant literature, and drafting and revision of the text. These contributions went well beyond linguistic or editorial assistance.

## Attribution and scientific authorship

Louis Desbiens is identified as the **human initiator and curator**, not as an independent mathematical authority certifying the results. OpenAI's ChatGPT is identified as the **AI mathematical research contributor**, not as an accountable conventional scholarly coauthor. These designations describe the provenance without implying that the human curator personally derived or independently verified all the arguments.

## Mathematical verification status

The candidate mathematical contributions have not undergone independent specialist validation, formal proof verification, or an exhaustive originality and priority review. In particular, independent examination is needed of divisor multiplicities and non-split residual divisors; exceptional contact orders and torsion cases; the rational-contact norm and divisor pushforward; distinguishing scalar-index identities from inversion procedures. Locally displayed proofs are proposed arguments. Established results cited from public literature should be assessed separately from new deductions; neither an AI-generated proof nor a successful computational check is by itself an independently certified theorem. Individual statements may be correct, partly correct, incomplete, or incorrect.

## Responsibility and purpose of public release

Louis Desbiens assumes responsibility for the decision to release this collection and for a good-faith account of its origin, contributors and verification status. He does **not** claim to have personally established or independently certified the correctness, completeness or originality of the proposed mathematical results. The material is made available for independent examination, criticism, reproducibility and possible further development; publication does not constitute scientific endorsement. This disclosure does not eliminate ordinary responsibilities associated with distributing public material.

## Institutional independence, funding, and competing interests

No institutional affiliation or endorsement is claimed. The investigation was undertaken independently, without institutional funding or resources. No external research funding was received. The human curator reports no competing interests.

## Computational evidence and source availability

Numerical evaluations helped develop the initial intuition. The public repository contains the available scripts, archived results, and a claim-by-claim verification coverage guide. These are scoped finite arithmetic, symbolic, and numerical checks, not independent verification of the general mathematical results. Historical exploratory calculations for which independent source data are unavailable are not treated as reproducible evidence.

# References

[1] J. S. Milne, *Elliptic Curves*, second edition, World Scientific, 2021. Public author version: https://www.jmilne.org/math/Books/EC2.pdf.

[2] D. G. Cantor, "Computing in the Jacobian of a hyperelliptic curve," *Mathematics of Computation* 48 (177), 95--101, 1987. DOI: 10.1090/S0025-5718-1987-0866101-0. The genus-one specialization is proved in Section 5 here; an openly accessible account of the general method is also provided in [3].

[3] S. D. Galbraith, *Mathematics of Public Key Cryptography*, Cambridge University Press, 2012. Public author version and errata: https://www.math.auckland.ac.nz/~sgal018/crypto-book/crypto-book.html.
