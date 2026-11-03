# Exact elliptic Frobenius traces for ordinate-character autocorrelation

*Public AI-developed mathematical research artifact -- independently unverified candidate results*  
**Edition:** 2 November 2026  
**License:** CC BY 4.0 (manuscripts and documentation)

## Abstract

For a nonsingular elliptic curve $E/\mathbf F_q:y^2=x^3+ax+b$ in characteristic greater than three with odd rational group order, let $f(O)=0$ and $f(P)=\chi_q(y(P))$. For each nonidentity $T=(u,v)$, the manuscript proposes the exact identity 

$$
\sum_{P\in E(\mathbf F_q)}f(P)f(P+T)
 =-\chi_q(-1)\left(q+1-\#H_T(\mathbf F_q)\right),
\quad H_T:w^2=(x-u)(x^3+ax+b).
$$

 The formula is derived from the chord identity, the invertibility of multiplication by two on the rational group, an exceptional midpoint, and the two rational points at infinity on the quartic. Hasse's theorem then supplies the bound $2\sqrt q$. The same identity gives exact finite Fourier-energy and trace-sum formulas, and a cubic family whose $j$-invariant is explicit. These deductions are distinct from the more advanced, still-unverified convolution and semicircle claims in the associated Article IV.

**Human initiator and curator:** Louis Desbiens\
**AI mathematical research contributor:** OpenAI's ChatGPT\
**Document classification:** Public AI-developed mathematical research artifact\
**Institutional affiliation:** None claimed\
**Manuscript license:** Creative Commons Attribution 4.0 International (CC BY 4.0)

**Verification and provenance notice.** The exact identity and its proposed proof were developed through human-initiated, AI-assisted mathematical exploration. Although the proof uses elementary group-law and point-counting arguments and is supported by exact checks, the human curator does not claim independent specialist certification, mathematical originality, or proof verification. The displayed claims invite independent examination and correction.

**Keywords:** elliptic curves over finite fields; quadratic character; autocorrelation; Frobenius trace; finite Fourier transform; complex multiplication.

# Definitions, assumptions, and provenance of inputs

The question is whether the autocorrelation of the quadratic ordinate character on an odd-order elliptic-curve group is a trace of a concrete auxiliary elliptic curve. The result below is elementary and does not use a proposed convolution-group classification. The new derivation is offered as a candidate contribution for independent examination.

Let $k=\mathbf F_q$, $\operatorname{char}k>3$, and 

$$
E:y^2=g(x),\qquad g(x)=x^3+ax+b,\qquad
 D=-4a^3-27b^2\ne0.
$$

 Let $O$ be the identity and suppose $N=\#E(k)$ is odd. Extend the quadratic character by $\chi_q(0)=0$, and set 

$$
f(O)=0,\quad f(P)=\chi_q(y(P))\ (P\ne O),\quad
 \varepsilon=\chi_q(-1),\quad a_E=q+1-N.
$$

 Then $E[2](k)=\{O\}$, $g$ has no root in $k$, and multiplication by two is a bijection of $E(k)$. In particular $f(P)^2=1$ away from $O$. Define 

$$
\begin{aligned}
 C_E(T)&=\sum_{P\in E(k)} f(P)f(P+T),\\
 (f*f)(T)&=\sum_{P\in E(k)} f(P)f(T-P),\\
 S(\psi)&=\sum_{P\in E(k)}f(P)\psi(P).
\end{aligned}
$$

 Here $\psi$ ranges over characters of the elliptic-curve group, not additive characters of the coordinate field. Since $f(-P)=\varepsilon f(P)$, 

$$
(f*f)(T)=\varepsilon C_E(T),\qquad C_E(O)=N-1.
$$

 The autocorrelation identity holds for either value of $\varepsilon$. When $q\equiv3\pmod4$, $\varepsilon=-1$, and the spectrum is purely imaginary; when $q\equiv1\pmod4$, $\varepsilon=1$, and it is real.

The established inputs are the ordinary elliptic group law, elementary finite-field character sums, and Hasse's theorem. The proposed identity is not attributed to any reference as a previously established theorem; the sources cite only these standard inputs and the known finite Fourier convolution formula.

# An elementary elliptic model for the autocorrelation


**Proposed Proposition 2.1**. *For $T=(u,v)\in E(k)\setminus\{O\}$, let $H_T$ be the smooth projective completion of 

$$
H_T:\quad w^2=(x-u)g(x).
$$

 This is a genus-one curve with rational points, hence an elliptic curve after a choice of identity. If 

$$
a_{H_T}=q+1-\#H_T(k),
$$

 then 

$$
\boxed{(f*f)(T)=-a_{H_T},\qquad
 C_E(T)=-\varepsilon a_{H_T}.}
$$

 In particular, for $q\equiv3\pmod4$, one has $C_E(T)=a_{H_T}$.*


*Proposed proof.* Since $T$ is not two-torsion, $g(u)=v^2\ne0$. The quartic in (equation 2.1) has four distinct roots over $\bar k$, so its smooth completion has genus one. Its leading coefficient is one, giving two $k$-rational points at infinity. It also has the rational point $(u,0)$.

Fix $P\in E(k)$, put $Q=T-P$ and $R=P-Q=2P-T$. For distinct abscissas the chord formulas give 

$$
x(P-Q)-x(P+Q)
 =\frac{4y(P)y(Q)}{(x(P)-x(Q))^2}.
$$

 Indeed the difference of the squared slopes is $((y(P)+y(Q))^2-(y(P)-y(Q))^2)/(x(P)-x(Q))^2$. Therefore, at nonexceptional points, 

$$
f(P)f(Q)=\chi_q(x(R)-u).
$$

 The map $P\mapsto R=2P-T$ is a bijection of $E(k)$.

There are exactly three exceptional inputs. If $P=O$ or $P=T$, the product is zero, and $R=-T$ or $R=T$, respectively; the right side is also zero. If $P=Q=T/2$, then $R=O$ and the product is $f(T/2)^2=1$. There are no other equal-abscissa cases: $Q=-P$ would imply $T=O$. Consequently 

$$
\begin{aligned}
 (f*f)(T)
 &=1+\sum_{R\in E(k)\setminus\{O\}}\chi_q(x(R)-u)\\
 &=1+\sum_{x\in k}(1+\chi_q(g(x)))\chi_q(x-u)\\
 &=1+\sum_{x\in k}\chi_q((x-u)g(x)).
\end{aligned}
$$

 The sum of $\chi_q(x-u)$ over $k$ is zero. On the other hand, 

$$
\#H_T(k)=q+2+\sum_{x\in k}\chi_q((x-u)g(x)).
$$

 Combining (the displayed convolution calculation) and (equation 2.9) gives $(f*f)(T)=-a_{H_T}$; equation (equation 1.6) gives the correlation identity. Both the $+1$ in (the displayed convolution calculation) and the two points at infinity are essential. ◻


**Proposed Corollary 2.2**. *Under the hypotheses of Section 1, 

$$
|C_E(T)|\le2\sqrt q\qquad(T\in E(k)\setminus\{O\}).
$$

*


*Proposed deduction.* Apply Hasse's theorem to the elliptic curve $H_T$ in Proposition [1](#prop:trace){reference-type="ref" reference="prop:trace"}. Hasse's theorem is an established input [@Sutherland Theorem 7.3]. ◻

This is a bound on the autocorrelation, not a bound on each individual Fourier coefficient. The Fourier envelope in Article IV involves additional covering-space arguments.

# Computable equations and a worked example

The quartic has a useful cubic model. Set $s=1/(x-u)$ and $z=w/(x-u)^2$. Then 

$$
z^2=v^2s^3+(3u^2+a)s^2+3us+1.
$$

 Writing $c=g(u)=v^2$ and $d=g'(u)=3u^2+a$, the substitution $X=cs$, $Y=cz$ gives 

$$
Y^2=X^3+dX^2+3ucX+c^2.
$$

 Its Weierstrass discriminant and $j$-invariant are 

$$
\begin{aligned}

 \Delta(H_T)&=16c^2D\ne0,\\
 j(H_T)&=\frac{256(a^2-3au^2-9bu)^3}{g(u)^2D}.
\end{aligned}
$$

 These follow by expansion of the standard cubic discriminant and $c_4$ formulas. The accompanying symbolic checker verifies the polynomial identities, not their geometric interpretation.

For $E/\mathbf F_{31}:y^2=x^3+7$, one has $N=21$. Take $T=(1,15)$. Then 

$$
H_T:\quad z^2=8s^3+3s^2+3s+1.
$$

 Exact enumeration gives $\#H_T(\mathbf F_{31})=27$, hence $a_{H_T}=5$. Directly summing the 21 terms of $C_E(T)$ also gives $5$. For $T=(0,10)$, the corresponding values are $\#H_T=39$ and $C_E(T)=a_{H_T}=-7$. These are examples over a toy field, not secp256k1 point counts.

For $a=0$, the formula simplifies to 

$$
j(H_T)=\frac{6912b\,u^3}{(u^3+b)^2}.
$$

 Thus in the $j=0$ setting this auxiliary family is naturally expressed in the sixfold quotient coordinate $u^3$ used elsewhere in the project. This algebraic observation does not by itself establish an isogeny relation along the primitive CM orbit or an algorithm for recovering a hidden scalar.

# Exact finite Fourier consequences

These identities use only finite Fourier analysis, not a sheaf or monodromy theorem. Continue with the convention $S(\psi)=\sum_{P\in E(k)}f(P)\psi(P)$ and $C_E(T)=\sum_{P}f(P)f(P+T)$.


**Proposed Proposition 4.1** (Proposed spectral trace identity). *For every character $\psi$ of $E(k)$, 

$$
\boxed{\left|S(\psi)\right|^2
 =(N-1)-\varepsilon\sum_{T\ne O}
 a_{H_T}\,\psi(T).}
$$

 In particular, the right-hand side is real and nonnegative, although this is not obvious term by term.*


*Proposed proof.* A finite Fourier transform sends the correlation function to a squared modulus: 

$$
\sum_{T\in E(k)}C_E(T)\psi(T)=|S(\psi)|^2.
$$

 Indeed, replacing $Q=P+T$ separates the double sum into $S(\psi)\overline{S(\psi)}$, because $f$ is real-valued. Now substitute $C_E(O)=N-1$ and $C_E(T)=-\varepsilon a_{H_T}$ for $T\ne O$. ◻


**Proposed Corollary 4.2** (Proposed trace-sum identities). *Writing $m=\sum_{P\in E(k)}f(P)$, one has 

$$
\boxed{\sum_{T\ne O}a_{H_T}
 =-\varepsilon\bigl(m^2-(N-1)\bigr).}
$$

 In the $q\equiv3\pmod4$ case, $m=0$, and hence 

$$
\boxed{\sum_{T\ne O}a_{H_T}=-(N-1),\qquad
\frac1{N-1}\sum_{T\ne O}a_{H_T}=-1.}
$$

*


*Proposed proof.* Set $\psi=1$ in equation (equation 4.1). In the odd predicate case, the terms indexed by $P$ and $-P$ cancel, so $m=0$. ◻

## The square model is explicit on rational parameters

In the setting $q\equiv3\pmod4$, normalize $Y_\psi=-iS(\psi)/\sqrt q$ and define a function 

$$
b(T)=\begin{cases}
  a_{H_T}/q,&T\ne O,\\[2pt]
  (N-1)/q,&T=O.
 \end{cases}
$$

 The already proved finite identities give 

$$
\boxed{\sum_{T\in E(k)} b(T)\psi(T)=Y_\psi^2.}
$$

 This is a literal equality of finite functions for every odd-order $E(k)$. It does not, on its own, construct a rank-two *sheaf*, or establish the proposed convolution Tannaka group, higher moment bounds, or semicircle equidistribution in Article IV.

At the identity, the inverse Fourier formula recovers the exact Parseval second moment 

$$
\frac1N\sum_\psi\left(\frac{-iS(\psi)}{2\sqrt q}\right)^2
 =\frac{N-1}{4q}.
$$

 In particular, agreement with the second semicircle moment is forced up to the group-order normalization and is not independent evidence for the distribution.

# Scope, exceptional cases, and reproducible arithmetic

The assumption that $N$ is odd ensures both that the map $P\mapsto2P-T$ is bijective and that a nonzero rational shift $T=(u,v)$ has $v\ne0$. If rational two-torsion exists, $H_T$ can degenerate and the displayed proof does not apply as stated. The identity does not assume $N$ is prime, that $E(k)$ is cyclic, or that $q$ itself is prime. No large-field ECDLP calculation is claimed.

The companion program `verify_rank_two_model.py` tests the character identity, curve point counts, the quartic--cubic change of variables and the Hasse bound in exact arithmetic. The archived run covers every nonsingular odd-order curve model over primes $5$ through $43$: $2{,}744$ models and $93{,}640$ nonidentity shifts. These are all tested *models*, not all isomorphism classes or all finite fields. Script assertions are not a machine-checked general proof or a substitute for an independent specialist review.

The specific quartic-to-cubic and $j$-invariant identities are computationally useful because the curve $H_T$ can be counted with ordinary elliptic-curve software and allows the exact correlations to be reproduced without enumerating all the products $f(P)f(P+T)$ for every shift. That is an algorithmic route to checking the identity; no general speedup for recovering secret elliptic scalars follows.

# Conclusions and independent-verification request

The central proposal is the exact identification of the nonzero-shift ordinate-character autocorrelation with an auxiliary elliptic Frobenius trace. Its proof is short enough to examine independently: verify the chord relation, the three exceptional input cases, the rational points at infinity, and the relation between correlation and convolution for the sign $\chi_q(-1)$.

The resulting Hasse envelope, spectral trace identity, and trace-sum mean require no sheaf theory. The more advanced identification of the same elliptic family with a Frobenius-stable convolution projector is discussed in Article IV and its technical companion; those additional geometric statements remain proposed.

The research provenance, absence of independent proof certification, and CC BY 4.0 reuse terms are part of this public release.

# Research provenance, status, and rights {#research-provenance-status-and-rights .unnumbered}

Louis Desbiens initiated and curated the mathematical investigation. OpenAI's ChatGPT contributed substantive derivations, equation verification procedures and prose beyond editorial assistance. Neither participant independently certifies all mathematical claims; ChatGPT is not an accountable conventional human coauthor. No institutional affiliation or endorsement is claimed. No institutional resources or external funding were used, and no competing interests are reported. This manuscript and its editable source are offered under CC BY 4.0 to the extent of rights controlled by the curator; the associated Python checkers are under MIT. This is a public research artifact, not an independently validated theorem or a priority claim.


9

A. V. Sutherland, *18.783 Elliptic Curves, Lecture 7: Point counting*, MIT, 22 February 2022, Theorem 7.3 and the quadratic-character point-count formula.\
<https://math.mit.edu/classes/18.783/2022/LectureNotes7.pdf> J. S. Milne, *Lectures on Etale Cohomology*, version 2.21, 22 March 2013. Sections 14, 17--20, 22, 24--29 supply the curve cohomology, base change, Kunneth, duality and trace-formula background.\
<https://www.jmilne.org/math/CourseNotes/LEC.pdf> N. M. Katz, *Elliptic convolution, $G_2$, and elliptic surfaces*, Sections 1--2. Fourier-convolution identities, property P, and character-twisted fiber functors.\
<https://web.math.princeton.edu/~nmk/laumon15.pdf> B. Collas, M. Dettweiler, S. Reiter and W. Sawin, *Monodromy of elliptic curve convolution, seven-point sheaves of $G_2$-type and motives of Beauville type*, arXiv:1803.05883v2 (2018), Proposition 1.2.2 and Lemmas 1.2.4--1.2.6.\
<https://arxiv.org/abs/1803.05883> P. Deligne, *La conjecture de Weil. II*, Publications Mathematiques de l'IHES 52 (1980), 137--252. Standard weight and purity framework used in the semisimple geometric interpretation, not a source of the explicit formulas derived here.\
<https://www.numdam.org/item/PMIHES_1980__52__137_0/>
