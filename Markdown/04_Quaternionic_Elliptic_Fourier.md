---
title: "Quaternionic symmetry and semicircle laws for elliptic Fourier transforms"
subtitle: "The quadratic ordinate character, arithmetic components, and autocorrelation"
author: ""
date: "Public mathematical research artifact | 31 October 2026"
---

**Human initiator and curator:** Louis Desbiens  
**AI mathematical research contributor:** OpenAI's ChatGPT  
**Document classification:** Public AI-developed mathematical research artifact -- independently unverified candidate results  
**Institutional affiliation:** None claimed  
**Manuscript license:** Creative Commons Attribution 4.0 International (CC BY 4.0)

**Status and reading guide.** This document records a human-initiated, substantially AI-developed mathematical investigation. The human curator directed the objectives but does not independently certify its advanced mathematical arguments. The novel claims and supplied proofs are candidate results awaiting independent specialist verification; public availability does not certify correctness, completeness or originality. Sections 3 and 9 present proposed explicit-cover arguments for the Fourier and autocorrelation envelopes. Sections 5--8 develop proposed convolution-group, arithmetic descent and moment arguments using established literature; Section 10 presents proposed extension-field consequences. The convolution pairing, its arithmetic sign, the Frobenius-stable projector, purity and moment calculations require specialist verification. Finite Fourier evaluations are checks of particular examples, not proofs of the general statements.

# Abstract

Let $E/\mathbf F_q:y^2=x^3+ax+b$ be nonsingular, with characteristic greater than three, $q\equiv3\pmod4$, and odd group order $N$. Set $f(O)=0$ and $f(P)=\chi_q(y(P))$ otherwise. For every character $\psi$ of the elliptic-curve group, define $S_E(\psi)=\sum_P f(P)\psi(P)$. The manuscript presents a proposed explicit-cover proof of the uniform bound $|S_E(\psi)|\leq2\sqrt q$. The mechanism is the quaternion group lifting two-torsion translations to the genus-three cover $z^2=y$, together with the three-cycle action of Frobenius. The proposed identification of the associated convolution Tannaka group is $(Q_8\times SL_2)/\langle(-1,-I)\rangle$ in its four-dimensional tensor-product representation. Accounting for its arithmetic component, rather than only its connected group, is used to propose

$$
\left|\frac1N\sum_\psi\left(\frac{-iS_E(\psi)}{2\sqrt q}\right)^{2r}
-\frac{C_r}{4^r}\right|\leq\frac{r}{2\sqrt q},\qquad
C_r=\frac1{r+1}\binom{2r}{r}.
$$

The argument predicts vanishing odd moments and proposes that the full normalized Fourier spectrum tends to the radius-one semicircle law along admissible families with $q\to\infty$. A separate proposed genus-five cover argument yields the nontrivial additive-autocorrelation bound $2\sqrt q$. The proposed proofs separate the finite quaternionic symmetry from connected convolution monodromy and specify the arithmetic descent needed for the moment calculation. The consequences concern one coordinate character and do not establish general ECDLP hardness or a private-key-recovery algorithm.

**Keywords:** elliptic Fourier transform; quadratic character; quaternion group; convolution; semicircle law; arithmetic monodromy; autocorrelation.

# 1. Definitions and assumptions

Fix a short Weierstrass model
$$
E:\ y^2=g(x),\qquad g(x)=x^3+a x+b,
\qquad 4a^3+27b^2\ne0.
$$
Throughout Sections 1--9 and 11, assume
$$
\operatorname{char}k>3,\qquad q\equiv3\pmod4,\qquad N=\#E(k)\text{ odd}.
\qquad \text{(1.1)}
$$
Odd group order is enough; prime group order is not required for the Fourier theorem. The actual secp256k1 curve is an example with $a=0,b=7$. CM is useful for organizing the frequencies, but it is not needed for the main bound.

Let $\chi_q:k^*\to\{\pm1\}$ be the quadratic character. No affine rational point has $y=0$: such a point would be nonzero rational two-torsion. Consequently
$$
f(P)=\begin{cases}0,&P=O,\\ \chi_q(y(P)),&P\ne O\end{cases}
\qquad \text{(1.2)}
$$
is a well-defined real function, with $|f(P)|=1$ away from the identity.

The Fourier transform is indexed by **all characters of the elliptic-curve group**, not by additive characters of the coordinate field:
$$
S_E(\psi)=\sum_{P\in E(k)}f(P)\psi(P),
\qquad \psi\in\widehat{E(k)}.
\qquad \text{(1.3)}
$$
When $E(k)=\langle G\rangle$ has prime order $n$, this includes the discrete Fourier convention
$$
S_k=\sum_{d=0}^{n-1}f([d]G)e^{-2\pi i k d/n}.
$$
Changing the Fourier sign merely reverses the frequency labels.

Since $\chi_q(-1)=-1$,
$$
f(-P)=-f(P),\quad S_E(1)=0,\quad
S_E(\psi^{-1})=-S_E(\psi)=\overline{S_E(\psi)}.
\qquad \text{(1.4)}
$$
Thus all Fourier sums are purely imaginary. Put
$$
Y_\psi=\frac{-iS_E(\psi)}{\sqrt q},\qquad
X_\psi=\frac{Y_\psi}{2}.
\qquad \text{(1.5)}
$$
The eventual compact support is $[-2,2]$ for $Y$, and $[-1,1]$ for $X$.

## 1.1 The special CM bookkeeping

For $a=0$, $q\equiv1\pmod3$, choose $\beta^3=1$, $\beta\ne1$. Then
$$
\phi(x,y)=(\beta x,y)
$$
preserves every predicate depending only on $y$. In a prime-order group, writing $\phi(G)=[\lambda]G$ gives
$$
f([\lambda d]G)=f([d]G),\qquad
S_{\lambda k}=S_k,\qquad S_{-k}=-S_k.
\qquad \text{(1.6)}
$$
There are $(n-1)/6$ equal-magnitude frequency orbits.

**Sign-selection warning.** Selecting one representative from each sixfold orbit preserves every even spectral moment, but does not canonically preserve a signed distribution. One could deliberately choose the positive member of every sign pair. A theorem about the signed semicircle distribution must use the full character set, or the explicitly symmetrized list containing both $X$ and $-X$ for each orbit. An arbitrary choice of one signed representative cannot be used to define the signed measure in the theorem.


# 2. The genus-three cover and its quaternionic symmetry

Let $C$ be the smooth projective normalization of
$$
z^2=y,\qquad y^2=g(x),
$$
so affinely
$$
C:\ z^4=g(x).
\qquad \text{(2.1)}
$$
Write $\pi:C\to E$ for the degree-two map and $\iota(x,z)=(x,-z)$ for its deck involution.

Over $\bar k$, the roots $r_1,r_2,r_3$ of $g$ give the nonzero two-torsion points $T_r=(r,0)$. The divisor
$$
\operatorname{div}(y)=\sum_{r:g(r)=0}(T_r)-3(O)
\qquad \text{(2.2)}
$$
has odd valuations exactly at $E[2]$. Thus $C/E$ has four simple quadratic branch points. Riemann--Hurwitz gives
$$
2g(C)-2=2(2g(E)-2)+4,
\qquad g(C)=3.
\qquad \text{(2.3)}
$$

## Lemma 2.1. Explicit lifts of two-torsion translations

For a root $r$, set $d_r=g'(r)=3r^2+a\ne0$. Translation by $T_r$ has formulas
$$
x(P+T_r)=r+\frac{d_r}{x(P)-r},
\qquad
y(P+T_r)=-\frac{d_r}{(x(P)-r)^2}y(P).
\qquad \text{(2.4)}
$$
Choose $c_r\in\bar k$ with $c_r^2=-d_r$. Then
$$
\sigma_r(x,z)=\left(r+\frac{d_r}{x-r},\frac{c_r}{x-r}z\right)
\qquad \text{(2.5)}
$$
lifts this translation and satisfies $\sigma_r^2=\iota$.

**Proof.** Substituting (2.4) verifies the square of the new $z$-coordinate. After translating twice, the product of the two multipliers on $z$ is
$$
\frac{c_r^2}{d_r}=-1.
$$
These rational formulas extend to the smooth projective curve. The translation formulas follow from the chord through $P$ and $(r,0)$. $\square$

There are two lifts of each of the four two-torsion translations. They form an order-eight group whose six noncentral elements all have order four. Consequently
$$
\widetilde{E[2]}\simeq Q_8,
\qquad
1\to\langle\iota\rangle\to Q_8\to E[2]\to1.
\qquad \text{(2.6)}
$$
This is an ordinary finite-group statement; no experimental input is used.

## Lemma 2.2. Frobenius acts by an order-three automorphism on this $Q_8$

Because $N$ is odd, Frobenius fixes no nonzero point of $E[2]$. Its permutation of the three nonzero points is therefore a three-cycle. The induced automorphism of $Q_8$ is also of order three: under
$$
\operatorname{Aut}(Q_8)\simeq S_4\longrightarrow S_3,
$$
the preimages of three-cycles are three-cycles. In particular, this is not a claim that Frobenius acts trivially on the quaternion group.

For the original $j=0$ setting, one can choose $c_r=\delta r$, $\delta^2=-3\in k$, and the cyclic permutation is visible directly in (2.5). The general argument does not need this specialization.


# 3. The uniform Fourier bound

## Proposed Theorem A
Under (1.1), for every $\psi\in\widehat{E(k)}$, including the trivial character,
$$
\boxed{|S_E(\psi)|\le2\sqrt q.}
\qquad \text{(3.1)}
$$

The proof uses the Weil theorem for smooth projective curves, together with an explicit construction making all actions compatible. It does not assume the later $SL_2$ result.

## 3.1 A concrete simultaneous cover for all characters

Let
$$
\mathsf L=\operatorname{Frob}_q-[1]:E\to E
$$
be the Lang isogeny. It is finite etale of degree $N$, with constant deck group $\Gamma=E(k)$. Form the fiber product
$$
\widetilde C=C\times_{E,\mathsf L}E.
\qquad \text{(3.2)}
$$
It is smooth and connected. Connectedness follows, for example, because a nontrivial quadratic function-field extension cannot become trivial after an odd-degree extension. The map $\widetilde C\to C$ is etale of degree $N$, and the map $\widetilde C\to E$ on the second factor is quadratic with $4N$ branch points. Hence
$$
g(\widetilde C)=2N+1.
\qquad \text{(3.3)}
$$

The Lang map is invertible on $E[2]$, since its kernel has odd order. For $T\in E[2]$, let $U_T\in E[2]$ be the unique point such that $\mathsf L(U_T)=T$. A lifted translation acts on the fiber product by
$$
(c,R)\longmapsto(\sigma_T(c),R+U_T).
\qquad \text{(3.4)}
$$
Together with the deck involution these give a genuine $Q_8$-action. It commutes with $\Gamma$, and the construction is Frobenius-compatible. The group law is exact: $T\mapsto U_T$ is an additive inverse to the Lang map on $E[2]$, so the product of two such lifts has the same central cocycle as the original quaternion lifts. A deck translation by $\gamma\in\Gamma$ changes only $R$, and hence commutes with each lift. Frobenius commutes with the Lang map and sends $U_T$ to $U_{F_qT}$, giving arithmetic compatibility.

Equivalently, in character-sheaf language, choose the unique character $\theta$ with $\theta^2=\psi$. The rigidified Lang character sheaves satisfy
$$
\mathcal L_\psi\simeq[2]^*\mathcal L_\theta.
\qquad \text{(3.5)}
$$
The right side has its canonical $E[2]$-linearization, which lifts to $Q_8$ on $C$. This is the same construction in a smaller notation.

## 3.2 Each character contributes a four-dimensional anti-invariant space

Work with $\overline{\mathbf Q}_\ell$-coefficients, for $\ell\ne\operatorname{char}k$, and fix an embedding of the relevant coefficient field into $\mathbf C$. In the $(-1)$-eigenspace of $\iota$ on $H^1(\widetilde C)$, the $\psi$-isotypic component has dimension four.

One elementary dimension check is as follows. An etale $\Gamma$-cover of a genus-three curve has
$$
H^1(\widetilde C)\simeq4\operatorname{Reg}_\Gamma\oplus2\mathbf1
$$
as a $\Gamma$-representation. This follows from the fixed-point trace formula: a nonidentity deck translation has no fixed points and therefore trace two on $H^1$. The $\iota$-invariant part is $H^1(E)$, on which all translations act trivially, accounting for $2\mathbf1$. Thus the anti-invariant part is $4\operatorname{Reg}_\Gamma$.

Write its $\psi$-component as $V_\psi$. Equivalently,
$$
V_\psi=H^1(C_{\bar k},\pi^*\mathcal L_\psi)^-,
\qquad \dim V_\psi=4.
\qquad \text{(3.6)}
$$
This formulation also handles $\psi=1$: one must use the minus part, not the entire six-dimensional $H^1(C)$.

The dimension can also be read without an equivariant fixed-point argument. The local system $\mathcal K_y\otimes\mathcal L_\psi$ on $E\setminus E[2]$ has four tame nontrivial local monodromies and no geometric invariants. The unramified twist changes none of them. The genus-one Euler-characteristic formula gives $\dim H_c^1=4$, while $H_c^0=H_c^2=0$. The Kummer anti-invariant part identifies this group with $V_\psi$.

At a rational unbranched point, the difference between the two quadratic-cover eigenspace traces is $\chi_q(y(P))$. At each branch point the anti-invariant stalk is zero. Thus the prescribed values, including $f(O)=0$, agree with the middle-extension trace; no omitted endpoint correction is present.

With the Lang eigenspace convention chosen so the trace function is $\psi$, the trace formula is
$$
S_E(\psi)=-\operatorname{Tr}(F_q\mid V_\psi).
\qquad \text{(3.7)}
$$
Using the opposite Frobenius/eigenspace convention replaces $\psi$ by $\psi^{-1}$, without altering any bound or distribution below.

## 3.3 Quaternionic multiplicity and the Frobenius trace

The central involution of $Q_8$ acts as $-I$ on $V_\psi$. Of the irreducible characteristic-zero representations of $Q_8$, only its unique two-dimensional representation $\rho$ has this central character. Hence
$$
V_\psi\simeq\rho\otimes W_\psi,
\qquad \dim W_\psi=2.
\qquad \text{(3.8)}
$$

Choose a finite-order matrix $A\in SL_2$ implementing the Frobenius three-cycle on $\rho(Q_8)$. In quaternion notation one may take, up to sign and inverse,
$$
A=\frac{1+I+J+K}{2},\qquad I^2=J^2=K^2=IJK=-1.
\qquad \text{(3.9)}
$$
For example, take $I=\operatorname{diag}(i,-i)$, $J=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$, and $K=IJ$. Direct multiplication gives $\det A=1$, $A^3=-I_2$, and the eight numbers $\operatorname{tr}(A\rho(u))$, $u\in Q_8$, consist of four $+1$ and four $-1$. The inverse three-cycle and an inner quaternionic conjugation have the same absolute trace property.

It has $|\operatorname{tr}A|=1$. Schur's lemma gives
$$
F_q\mid V_\psi=A\otimes B_\psi
\qquad \text{(3.10)}
$$
for a two-dimensional operator $B_\psi$. All eigenvalues on $V_\psi$ have absolute value $\sqrt q$, by the Weil theorem applied to the smooth projective cover. Since the eigenvalues of $A$ are roots of unity, the two eigenvalues of $B_\psi$ also have absolute value $\sqrt q$. Therefore
$$
|S_E(\psi)|=|\operatorname{tr}A|\,|\operatorname{tr}B_\psi|
\le2\sqrt q.
$$
This completes the proposed proof of Theorem A. $\square$

**Interpretation.** The four-dimensional space does not simply lose two dimensions. It is a tensor product of a finite two-dimensional quaternionic factor and a two-dimensional multiplicity factor. Frobenius has trace of absolute value one on the former.


# 4. The geometric convolution object

Let $U=E\setminus E[2]$, $j:U\to E$ be the open inclusion, and let $\mathcal K_y$ be the quadratic Kummer local system associated with $y$. Define
$$
\mathcal A=j_{!*}\mathcal K_y[1].
\qquad \text{(4.1)}
$$
All four local monodromies are $-1$, so the middle extension has zero stalk at each branch point. Its trace function is $-f$. It is geometrically simple, of generic rank one and Tannakian dimension
$$
\chi(E,\mathcal A)=4.
\qquad \text{(4.2)}
$$
It has property P: after tensoring by any lisse rank-one sheaf on $E$, global cohomology vanishes outside degree zero. Indeed the nontrivial ramification prevents global sections of the underlying local system or its dual; on the proper curve only the middle cohomology survives.

We use the semisimple elliptic-convolution category described in [CDRS, Proposition 1.2.2]. Convolution is derived pushforward along addition; the unit is $\delta_O$, duality is $[-1]^*D$, and the fiber functor is global degree-zero cohomology. Its dimension is Euler characteristic. These are established inputs, not new claims of this manuscript.

For precision, two further consequences of that framework are used. If $\operatorname{rk}$ denotes generic local-system rank and $\chi$ denotes Tannakian dimension, then

$$
\operatorname{rk}(K*L)=\operatorname{rk}(K)\chi(L)+\chi(K)\operatorname{rk}(L).
$$

This is [CDRS, Lemma 1.2.4]. It can be seen on a generic addition fiber: the singular sets of the two factors are disjoint, the elliptic curve has Euler characteristic zero, and each factor's local Euler defects are multiplied by the other's generic rank. Summing the defects gives the formula.

An object with finite Tannaka group is a direct sum of torsion-point skyscrapers [CDRS, Lemma 1.2.5]. To recall the reason, if its dimension is $d$ and its rank is $r$, the rank formula makes the rank of its $m$th convolution power equal to $md^{m-1}r$. Finite monodromy allows only finitely many irreducible constituents, so their ranks give a bound $Cd^m$. Letting $m$ grow forces $r=0$. A rank-zero perverse object is punctual, and a skyscraper at a point of infinite order would generate infinitely many distinct translates, contrary to finite monodromy. These arguments clarify the inputs behind the component-group calculation.

The word **monodromy** below means the convolution Tannaka group. The ordinary local monodromy of $\mathcal K_y$ is only a finite quadratic group. We are not constructing an ordinary rank-two lisse sheaf on an algebraic variety whose rational points are all the characters $\psi$; those characters naturally parameterize fiber functors instead [FFK].


# 5. The connected geometric group is $SL_2$

## Proposed Theorem B
For the geometric convolution group $G$ generated by $\mathcal A$, the identity component acts on the multiplicity space $W$ as the standard representation of $SL_2$:
$$
G^\circ\simeq SL_2,\qquad V\vert_{G^\circ}\simeq W\oplus W.
\qquad \text{(5.1)}
$$

## 5.1 Translation stabilizer

The lifted translations prove $t_T^*\mathcal A\simeq\mathcal A$ for every $T\in E[2]$. Conversely, any translation stabilizing $\mathcal A$ must preserve its singular set $E[2]$, hence belongs to $E[2]$. Thus
$$
\operatorname{Stab}(\mathcal A)=E[2].
\qquad \text{(5.2)}
$$

For each $T$, the isomorphism $\mathcal A*\delta_T\simeq\mathcal A$ yields a self-twist operator $A_T$ on the four-dimensional fiber $V$. Their multiplication is the quaternion extension already computed. If $\varepsilon_T$ is the finite character associated with $\delta_T$,
$$
A_Tg=\varepsilon_T(g)gA_T.
\qquad \text{(5.3)}
$$
The finite characters are trivial on $G^\circ$, so $G^\circ$ centralizes this $Q_8$. Consequently it acts only on $W$ in $V=\rho\otimes W$.

## 5.2 Exact commutant dimension

The representation $\operatorname{End}_{G^\circ}(V)$ factors through the finite component group. By [CDRS, Lemma 1.2.5], every object with finite convolution group is a sum of torsion skyscrapers. Therefore its simple constituents are one-dimensional characters attached to $\delta_T$.

The multiplicity of the character attached to $T$ in $\operatorname{End}(V)$ is
$$
\dim\operatorname{Hom}_G(V\otimes\varepsilon_T,V).
$$
Since $V$ is irreducible, this is one when $t_T^*\mathcal A\simeq\mathcal A$, and zero otherwise. Thus
$$
\dim\operatorname{End}_{G^\circ}(V)=4.
\qquad \text{(5.4)}
$$
But
$$
\operatorname{End}_{G^\circ}(V)
=\operatorname{End}(\rho)\otimes\operatorname{End}_{G^\circ}(W).
$$
Hence $\operatorname{End}_{G^\circ}(W)$ consists of scalars. Semisimplicity then makes $W$ absolutely irreducible.

## 5.3 Self-duality excludes the torus

Geometrically, $\mathcal A\simeq\mathcal A^\vee$: the local system is quadratic, and replacing $y$ by $-y$ changes it only by a geometrically constant factor. Thus $W\simeq W^\vee$.

An irreducible self-dual two-dimensional representation preserves either a symmetric or an alternating form. If symmetric, its connected image lies in $SO_2$, a torus, which cannot act absolutely irreducibly on a two-dimensional space over an algebraically closed field. Therefore its form is alternating, and the image lies in $Sp_2=SL_2$.

The image is connected and reductive. A proper connected reductive subgroup of $SL_2$ is a torus or the trivial group, again incompatible with irreducibility. The representation is faithful because the original Tannaka representation is faithful. Hence the image is exactly $SL_2$, completing the proposed proof of Theorem B. $\square$


# 6. The full geometric group and the arithmetic sign

Identifying $G^\circ$ is not by itself an equidistribution theorem. The finite component matters here.

## 6.1 The symmetric convolution form

Choose $i\in\bar k$ with $i^2=-1$. On $C$,
$$
\nu(x,z)=(x,iz)
$$
lifts inversion on $E$, and $\nu^2=\iota$. On $V=H^1(C)^-$, put $J=\nu^*$. Then $J^2=-I$.

The cup-product pairing $\langle\ ,\ \rangle$ is alternating. Define
$$
B(v,w)=\langle v,Jw\rangle.
\qquad \text{(6.1)}
$$
Since $J$ preserves cup product and $J^{-1}=-J$,

$$
B(w,v)=\langle w,Jv\rangle
=-\langle Jv,w\rangle
=-\langle v,J^{-1}w\rangle=B(v,w).
$$

Nondegeneracy follows because both cup product and $J$ are nondegenerate. To identify the pairing in the convolution category, restrict the addition fiber over $O$ to the anti-diagonal $(P,-P)$. Evaluation there pairs a local-system fiber with the inverse-point dual fiber. The lift $\nu$ identifies the inverse-point fiber with the original fiber, and integration over $E$ is cup product. Thus the fiber of this evaluation is exactly $\langle v,Jw\rangle$ up to a nonzero scalar. It is therefore the convolution duality pairing, not merely an unrelated bilinear form on cohomology, and is $G$-invariant. The quaternion lifts commute with $\nu$, so they preserve $B$ too. In $V=\rho\otimes W$, this form is the tensor product of alternating forms on $\rho$ and $W$.

Because $q\equiv3\pmod4$, Frobenius sends $\nu$ to $\nu^{-1}$. Thus
$$
B(F_qv,F_qw)=-q\,B(v,w).
\qquad \text{(6.2)}
$$
Multiplying Frobenius by $i/\sqrt q$ makes it orthogonal. This is the arithmetic reason for the imaginary normalization in (1.5), not a cosmetic rotation of a plot.

## 6.2 Full geometric group

The normalizer in $O(V,B)$ of $I_\rho\otimes SL_2(W)$ is
$$
\bigl(SL_2(\rho)\times SL_2(W)\bigr)/\langle(-I,-I)\rangle.
\qquad \text{(6.3)}
$$
Indeed all automorphisms of $SL_2$ are inner; after removing the action on $W$, a normalizing operator lies in $GL(\rho)$. Preservation of the tensor-product form gives (6.3).

Every irreducible representation of the finite group $G/G^\circ$ is one-dimensional, again by the finite-object lemma and torsion skyscrapers. Thus $G/G^\circ$ is abelian. Its faithful projective image in $PGL_2(\rho)$ is a finite abelian group, hence cyclic or Klein four. A cyclic image preserves two lines in $\rho$, making $V$ reducible as a $G$-representation. Therefore the image is Klein four. Its inverse image in $SL_2(\rho)$ is quaternionic, giving
$$
\boxed{
G\simeq
(Q_8\times SL_2)/\langle(-1,-I)\rangle.
}
\qquad \text{(6.4)}
$$

There are two roles for $Q_8$: geometric self-twist operators, and the finite factor of the full convolution group. Their projective images agree. One way to check this is that (5.3) makes the component group centralize the projective self-twist Klein four; its centralizer in $PGL_2$ is that same Klein four.

## 6.3 The Frobenius component

The normalized arithmetic Frobenius acts as
$$
\mathfrak F=A\otimes B_0,
\qquad A\in SL_2(\rho),\quad B_0\in SL_2(W),
\qquad \text{(6.5)}
$$
with $A$ inducing the three-cycle on $Q_8$. The normalization (6.2) ensures $\det B_0=1$.

The finite extension generated by $Q_8$ and $A$ is the binary tetrahedral group. Crucially,
$$
\operatorname{tr}(A\rho(u))\in\{1,-1\}
\qquad(u\in Q_8).
\qquad \text{(6.6)}
$$
Thus the relevant arithmetic component has the same trace distribution as a single $SU(2)$ factor, although the full geometric representation has dimension four.


# 7. Catalan moments with an explicit error term

## Proposed Theorem C
Under (1.1), for every integer $r\ge1$,
$$
\boxed{
\left|\frac1N\sum_{\psi\in\widehat{E(k)}}X_\psi^{2r}
-\frac{C_r}{4^r}\right|
\le\frac{r}{2\sqrt q},
\qquad C_r=\frac1{r+1}\binom{2r}{r}.
}
\qquad \text{(7.1)}
$$
All odd moments are zero. The constant in (7.1) is uniform in the curve and field, but intentionally far from optimized.

## 7.1 A useful stronger simplification: the square has a rank-two trace model

Normalize the perverse sheaf arithmetically by
$$
\mathcal M=\mathcal A\otimes\text{constant}(i/\sqrt q).
\qquad \text{(7.2)}
$$
It is pure of weight zero; its trace function is $-if(P)/\sqrt q$, and its elliptic Fourier transform is $Y_\psi$.

Let $\mathcal B$ be the object corresponding to the representation
$$
\mathbf1_{Q_8}\otimes(W\otimes W)
=\mathbf1\oplus(\mathbf1_{Q_8}\otimes\operatorname{Sym}^2W).
$$
The quaternion identity $\rho\otimes\rho=\bigoplus_{T\in E[2]}\varepsilon_T$ gives
$$
\mathcal M*\mathcal M
\simeq_{\bar k}\bigoplus_{T\in E[2]}\delta_T*\mathcal B.
\qquad \text{(7.3)}
$$
There is a canonical way to put the required arithmetic structure on $\mathcal B$. In $\rho\otimes\rho$, the trivial quaternionic character is $\bigwedge^2\rho$. Its projector is the average of the diagonal $Q_8$-action. Frobenius normalizes this action, so the projector is Frobenius-stable. On its one-dimensional image, Frobenius acts by $\det A=1$. The induced operator on the remaining factor is therefore exactly $B_0\otimes B_0$, not an unspecified constant twist. This gives $\mathcal B$ its descended Weil structure. The other three projectors are permuted in a three-cycle. All statements may be made after Weil semisimplification, which changes no trace function.

The $T=O$ summand is Frobenius-stable. Frobenius cyclically permutes the other three summands. Their total trace at every $k$-rational point is therefore zero. Consequently
$$
t_{\mathcal M*\mathcal M}(P)=t_{\mathcal B}(P)
\quad\text{for every }P\in E(k).
\qquad \text{(7.4)}
$$
This is a trace-function identity over the stated field, not a geometric isomorphism between $\mathcal M*\mathcal M$ and $\mathcal B$.

The elliptic convolution rank formula [CDRS, Lemma 1.2.4] gives
$$
\operatorname{rk}(\mathcal M*\mathcal M)=8.
$$
All four translates in (7.3) have the same generic rank. Thus
$$
\boxed{\operatorname{rk}(\mathcal B)=2,\qquad\chi(\mathcal B)=4.}
\qquad \text{(7.5)}
$$
In fact $\mathcal B=\delta_O\oplus\mathcal B_2$, where $\mathcal B_2$ has generic rank two and Tannakian dimension three. The punctual factor has arithmetic eigenvalue one because $\det A=\det B_0=1$.

Fourier transformation of (7.4) now yields
$$
\widehat{t_{\mathcal B}}(\psi)=Y_\psi^2.
\qquad \text{(7.6)}
$$
This rank-two **trace model for the square** makes the error bound much better than the estimate obtained by applying a rank bound to $\mathcal M^{*2r}$ directly.

## 7.2 Moments and the punctual contribution

Fourier orthogonality gives
$$
\frac1N\sum_\psi Y_\psi^{2r}
=t_{\mathcal B^{*r}}(O).
\qquad \text{(7.7)}
$$
This identity also follows directly by expanding the product of Fourier sums: averaging the character of a sum gives one exactly when that sum is $O$, and zero otherwise. Convolution of trace functions agrees with proper sheaf convolution by the trace formula.

The geometric representation of $\mathcal B^{*r}$ is $W^{\otimes2r}$, with the finite quaternionic factor trivial. Its invariants have dimension
$$
\dim(W^{\otimes2r})^{SL_2}=C_r.
$$
For completeness, the invariant dimension follows from the elementary weight decomposition of tensor powers of the standard two-dimensional representation. The multiplicity of its highest-weight-zero constituent is the weight-zero multiplicity minus the weight-two multiplicity:

$$
\binom{2r}{r}-\binom{2r}{r-1}
=\frac{1}{r+1}\binom{2r}{r}=C_r.
$$

Nontrivial punctual constituents would be nontrivial finite characters. None occurs here, because the finite factor in $W^{\otimes2r}$ is trivial. Thus every punctual constituent is supported at $O$, and there is no additional finite-support contribution hidden in the rank estimate.

Arithmetic Frobenius acts through $B_0\in SL_2(W)$, and so acts trivially on these invariants. Therefore the punctual $\delta_O$ contribution in (7.7) is exactly $C_r$, with no unknown phase.

Equivalently, working directly with $V=\rho\otimes W$, the finite factor contributes
$$
\frac18\sum_{u\in Q_8}\operatorname{tr}(A\rho(u))^{2r}=1.
\qquad \text{(7.8)}
$$
This calculation explains why identifying connected $SL_2$ alone would not determine the limiting law.

## 7.3 Bound the remaining stalk

The rank formula
$$
\operatorname{rk}(K*L)
=\operatorname{rk}(K)\chi(L)+\chi(K)\operatorname{rk}(L)
$$
and (7.5) imply
$$
\operatorname{rk}(\mathcal B^{*r})=2r4^{r-1}.
\qquad \text{(7.9)}
$$

Proper convolution preserves purity, and property P keeps the convolution perverse. A nonpunctual pure weight-zero middle extension on a curve has its local-system stalk in degree $-1$, with eigenvalues of absolute value at most $q^{-1/2}$. Its stalk dimension is at most its generic rank. The total nonpunctual contribution at $O$ therefore has absolute value at most
$$
2r4^{r-1}/\sqrt q.
$$
Divide (7.7) by $4^r$ to obtain
$$
\left|\frac1N\sum_\psi X_\psi^{2r}-\frac{C_r}{4^r}\right|
\le\frac{r}{2\sqrt q}.
$$
Odd moments vanish exactly by (1.4). This completes the proposed proof of Theorem C. $\square$

## 7.4 A Chebyshev form of the estimate

There is an alternative useful formulation. Let $U_m$ be the Chebyshev polynomial of the second kind, so
$$
U_m(\cos\theta)=\frac{\sin((m+1)\theta)}{\sin\theta}.
$$
For even $m>0$, the representation $\mathbf1_{Q_8}\otimes\operatorname{Sym}^mW$ defines a nonpunctual simple object. On the arithmetic component its Fourier trace is $U_m(X_\psi)$. Its generic rank is
$$
\frac{m(m+1)(m+2)}{12}.
\qquad \text{(7.10)}
$$
Here is a direct rank calculation, avoiding an implicit differentiation convention. Write $R_m$ for the rank of the object attached to $\operatorname{Sym}^mW$, for even $m$. One has $R_0=0$ and $R_2=2$. The character identity

$$
\operatorname{Sym}^2W\otimes\operatorname{Sym}^mW
=\operatorname{Sym}^{m+2}W\oplus\operatorname{Sym}^mW\oplus\operatorname{Sym}^{m-2}W
$$

for even $m\geq2$, together with the rank formula, gives

$$
R_{m+2}=2(m+1)+2R_m-R_{m-2}.
$$

Induction gives (7.10). Only even powers descend with trivial quaternionic factor, which is why the statement is restricted to even $m$. For a character-twisted fiber the sign of the finite-factor trace can change $Y_\psi$ to its negative, but $U_m$ is even for even $m$, so the stated Fourier trace is unaffected.

There is no punctual invariant contribution for $m>0$, hence
$$
\left|\frac1N\sum_\psi U_m(X_\psi)\right|
\le\frac{m(m+1)(m+2)}{12\sqrt q}
\quad(m>0\text{ even}).
\qquad \text{(7.11)}
$$
The average is exactly zero for odd $m$, by symmetry. This expresses the approach to semicircle orthogonality directly and can support a later quantitative CDF-discrepancy analysis.

## 7.5. Scope of the estimate

For each fixed moment order the error tends to zero uniformly in the curve as $q\to\infty$. This establishes a limiting distribution, not a finite-field assertion that every empirical moment equals a Catalan number. The constants need not describe the typical size of an individual finite-field discrepancy. No independent-sampling assumption is used.

# 8. The semicircle law and correct normalization

The radius-one semicircle probability measure is
$$
d\mu_{\mathrm{sc}}(x)=\frac2\pi\sqrt{1-x^2}\,\mathbf1_{[-1,1]}(x)\,dx.
\qquad \text{(8.1)}
$$
Its even moments are $C_r/4^r$, and its odd moments vanish. By Theorem A all empirical measures are supported on $[-1,1]$. Theorem C, polynomial approximation on a compact interval, and uniqueness of the moment problem imply:

## Proposed Corollary 8.1
Along any sequence of curves satisfying (1.1), with $q\to\infty$,
$$
\frac1{\#E(\mathbf F_q)}
\sum_{\psi\in\widehat{E(\mathbf F_q)}}\delta_{X_\psi}
\Longrightarrow\mu_{\mathrm{sc}}.
\qquad \text{(8.2)}
$$
This does not assume that prime-order curves form an infinite family: odd group order suffices. For example, starting with an admissible curve, extension degrees congruent to $1$ or $5\pmod6$ remain admissible.

In particular, the bound is asymptotically sharp: along any such family, $\max_\psi |S_E(\psi)|/(2\sqrt q)\to1$, since every fixed neighborhood of either endpoint has positive limiting semicircle mass.

This conclusion uses the explicit arithmetic component and uniform moment proof above. It is not a blind application of an equidistribution theorem requiring equality of geometric and arithmetic groups. The distinction is treated in the general framework [FFK, Chapter 4].

## 8.1 Parseval fixes the second moment

Exactly,
$$
\sum_\psi|S_E(\psi)|^2=N\sum_P|f(P)|^2=N(N-1).
$$
Thus
$$
\frac1N\sum_\psi X_\psi^2=\frac{N-1}{4q}.
\qquad \text{(8.3)}
$$
Since $S_E(1)=0$, averaging only over nontrivial characters gives
$$
\frac1{N-1}\sum_{\psi\ne1}X_\psi^2=\frac{N}{4q}.
\qquad \text{(8.4)}
$$
On a prime-order CM curve with group order greater than three, the same is true for one representative per sixfold frequency orbit, for even moments. Consequently the second moment is a normalization identity, not independent evidence for an $SU(2)$ distribution.

## 8.2 Variance standardization

For a cyclic prime-order group, the variance-standardized variable on nontrivial frequencies is $X/\sqrt{n/(4p)}=-iS/\sqrt n$. Its limiting even moments are the Catalan numbers $C_r$. At finite size the exact Parseval scale differs from $1/4$, so raw and variance-standardized moments should not be mixed in a proof or figure caption.

## 8.3 No independence claim

The theorem makes no assertion that distinct Fourier coefficients are independent random variables. Statistical tests assuming independent and identically distributed samples are therefore not justified by this result. A signed empirical distribution from arbitrarily selected CM representatives is additionally subject to the sign-selection warning in Section 1.1.


# 9. A second theorem: the autocorrelation envelope

## Proposed Theorem D
Under (1.1), for every $T\in E(k)$ with $T\ne O$,
$$
\boxed{
\left|\sum_{P\in E(k)}f(P)f(P+T)\right|\le2\sqrt q.
}
\qquad \text{(9.1)}
$$

**Proof.** Consider the smooth projective normalization
$$
D_T:\ w^2=y(P)y(P+T).
\qquad \text{(9.2)}
$$
The two branch sets $E[2]$ and $E[2]-T$ are disjoint: otherwise $T\in E[2]$, impossible for a nonzero rational point when $N$ is odd. Thus there are eight quadratic branch points, and $g(D_T)=5$.

For $S\in E[2]$, let $c_S(P)$ be the multiplier on $z$ in its quaternion lift on $C$. Translation lifts to $D_T$ by
$$
(P,w)\longmapsto
(P+S,c_S(P)c_S(P+T)w).
\qquad \text{(9.3)}
$$
The two quaternionic cocycle signs multiply to $+1$. These lifts therefore form an honest group $E[2]$, not $Q_8$, and commute with the quadratic deck involution. They are Frobenius-compatible because $T$ is rational. The $E[2]$-action is free, so the quotient $D_T/E[2]$ has genus two.

The resulting degree-eight abelian cover of $E/E[2]\simeq E$ has group $E[2]\times C_2$. Its deck-minus cohomology decomposes into four two-dimensional spaces, indexed by the four characters of $E[2]$. Equivalently, these are the quadratic two-branch local system downstairs tensored with the four unramified characters of the isogeny $[2]$; each has Euler characteristic $-2$.

Each minus-character local system downstairs is ramified at exactly two points: the images of the two disjoint $E[2]$-orbits. Tensoring by any of the four unramified characters leaves that ramification unchanged. Its $H^0$ and $H^2$ vanish, and the tame Euler formula gives dimension two in $H^1$. This proves the dimension assertion without an assumed splitting of a generic genus-five Jacobian. At $O$ and $-T$ the trace is zero, as is $f(P)f(P+T)$; at every other rational point the quadratic-cover trace is the product of the two characters.

Frobenius cycles the three nontrivial $E[2]$-characters, so their direct sum has trace zero. Only the trivial $E[2]$-character sector contributes, and it is two-dimensional and pure of weight one. The trace formula identifies the negative of this trace with the sum in (9.1), giving the bound. $\square$

Thus the Fourier and additive-autocorrelation envelopes have related but distinct geometric explanations. The autocorrelation result was not assumed in the Fourier proof.


# 10. Extension fields and arithmetic phases

This section records an additional consequence of the full arithmetic-component calculation. It is not needed for the base-field theorems.

Fix a curve over an admissible $\mathbf F_q$. For extension degree $d\ge1$, put $Q=q^d$, use the quadratic character of $\mathbf F_Q$ extended by $\chi_Q(0)=0$, set the value at $O$ to zero, and define $S_{d,\psi}$ over $E(\mathbf F_Q)$. The natural normalization inherited from (7.2) is
$$
X_{d,\psi}=\frac{-i^d S_{d,\psi}}{2q^{d/2}}.
\qquad \text{(10.1)}
$$
This is real: for odd $d$ the sum is imaginary; for even $d$ it is real.

In the finite factor, arithmetic Frobenius is $A^d$. The invariant trace is
$$
\frac18\sum_{u\in Q_8}\operatorname{tr}(A^d\rho(u))^{2r}
=\begin{cases}
1,&3\nmid d,\\
4^{r-1},&3\mid d.
\end{cases}
\qquad \text{(10.2)}
$$
The first line uses the binary tetrahedral three-cycle coset. In the second, $A^d\in Q_8$, and the standard quaternion representation has traces $2,-2,0,0,0,0,0,0$.

The same convolution proof therefore gives limiting laws, as extension sizes tend to infinity along the indicated subsequences:
$$
\begin{cases}
\mu_{\mathrm{sc}},&3\nmid d,\\
\displaystyle\frac34\delta_0+\frac14\mu_{{\mathrm{sc}},2},&3\mid d,
\end{cases}
\qquad \text{(10.3)}
$$
where $\mu_{{\mathrm{sc}},2}$ is the radius-two semicircle law. Without using the rank-two simplification, the rank of $\mathcal M^{*2r}$ gives the safe extension-field error bound $2r4^{r-1}/\sqrt Q$ for these raw even moments. When $3\nmid d$, the rank-two simplification applies again and improves this to $r/(2\sqrt Q)$.

There is an elementary check on the atom at zero. Over a degree divisible by three, the quaternion lifts and all two-torsion points are rational. Formula (2.4) then shows that the quadratic ordinate predicate is invariant under $E[2]$. Its Fourier transform is consequently supported only on characters trivial on $E[2]$: at least three quarters of all Fourier coefficients vanish **exactly**. For every character, the original four-branch Kummer system with its unramified character twist has first cohomology of dimension four. The ordinary Weil bound therefore gives $|S|\le4\sqrt Q$, without assuming that a character has a square root in the even-order character group.

One extra step is needed to deduce a signed limiting law over even extension degrees. When $d$ is even, $f$ is even under inversion, so its odd spectral moments are not forced to vanish by (1.4). Instead, for every odd integer $j\geq1$, $W^{\otimes j}$ has no $SL_2$-invariants. There is no punctual part in $\mathcal M^{*j}$, and its rank is $j4^{j-1}$. The same weight estimate gives

$$
\left|\frac{1}{\#E(\mathbf F_Q)}\sum_\psi X_{d,\psi}^{\,j}\right|
\leq\frac{j\,2^{j-2}}{\sqrt Q}. \qquad (10.4)
$$

Thus odd moments tend to zero even on those subsequences. For even moments, (10.2) and the invariant dimension $C_r$ give $C_r/4^r$ when $3\nmid d$ and $C_r/4$ when $3\mid d$. These are exactly the moments of the two measures in (10.3). The bound $|X_{d,\psi}|\leq2$, valid in every extension, gives a common compact support, so convergence of all moments proves the stated weak limits. When $3\nmid d$, the Frobenius three-cycle and the rank-two trace reduction remain available, giving the sharper support $[-1,1]$ and the sharper even-moment error already stated.

This illustrates why connected $SL_2$ alone is not the correct statement of the distribution theorem. Arithmetic components can produce different laws over different extension degrees.


# 11. Consequences for the original scalar-information question

These are consequences for one specific observable, not lower bounds for arbitrary private-key-recovery algorithms.

## 11.1 Fourier incompressibility

Assume the group is cyclic of prime order $n$. Its Fourier energy is
$$
\sum_k|S_k|^2=n(n-1).
$$
By Theorem A, any set of $s$ frequencies carries energy at most $4qs$. Hence a Fourier-supported approximation capturing a fraction $\eta$ of the total energy needs
$$
\boxed{s\ge\eta\,\frac{n(n-1)}{4q}.}
\qquad \text{(11.1)}
$$
For $n\sim q$, this is linear in $n$. This is an approximation statement in the Fourier basis, not an unrestricted circuit or query lower bound.

## 11.2 Canonical scalar parity and affine reparameterization

Let $f_d=f([d]G)$, $f_0=0$, and let $a(d)=(-1)^d$ on the canonical representatives $0\le d<n$. Its discrete Fourier transform satisfies
$$
|\widehat a(k)|=\frac1{|\cos(\pi k/n)|}.
\qquad \text{(11.2)}
$$
An elementary harmonic-sum estimate gives
$$
\sum_{k=1}^{n-1}|\widehat a(k)|\le n(2+\log n).
\qquad \text{(11.3)}
$$
For completeness, pair $k$ with $n-k$, write the distance from $n/2$ as $j-1/2$, and use $\sin x\ge2x/\pi$ on $[0,\pi/2]$. The remaining sum is bounded by $2+\log n$.

For any known $u\ne0,v\pmod n$, the Fourier magnitudes of $d\mapsto f_{ud+v}$ are a permutation of those of $f$. Fourier inversion, (3.1), and (11.3) imply
$$
\boxed{
\left|\frac1{n-1}\sum_{d=1}^{n-1}(-1)^d f([ud+v]G)\right|
\le\frac{2\sqrt q(2+\log n)+1}{n-1}.
}
\qquad \text{(11.4)}
$$
The $+1$ accommodates removing the $d=0$ term; it is unnecessary when $v=0$. The zero Fourier mode vanishes because $f$ is odd.

Thus every fixed affine-query version of this particular Legendre predicate has only square-root-times-logarithmic direct parity correlation. The theorem does **not** rule out arbitrary adaptive combinations of many queries, other predicates, high-degree functions, or quantum algorithms.


# 12. Numerical motivation and mathematical scope

The exploratory investigation used numerical evaluations to test and refine the initial intuition about the quadratic ordinate character. They motivated the comparison between a uniform square-root Fourier envelope and semicircle moments. No software-specific calculation, unarchived numerical array, or fitted distribution is intended as an input to the proposed proofs.

The second moment is fixed by Parseval, so it cannot by itself distinguish the semicircle law from another variance-matched model. Likewise, selecting arbitrary signs from sixfold frequency orbits changes a signed empirical distribution. Theorems C and Corollary 8.1 use the full character set and make neither of these substitutions. They do not treat the coefficients as independent random observations.

The principal mathematical ingredients are an explicit cover, its quaternionic translation symmetry, the arithmetic three-cycle, and the elliptic-convolution framework of [CDRS] and [FFK]. The finite factor is essential both to the constant two in the pointwise envelope and to the extension-field phases. The absolute bound and autocorrelation bound have independent cover arguments, whereas the limiting law also uses the convolution duality and the descended rank-two trace model.

The framework itself is established literature. The candidate contribution proposed in this investigation is the explicit ordinate-character example and its deductions. A claim of priority for this collection would require a separate comprehensive literature investigation. The application bounds concern one observable and are not lower bounds for arbitrary ECDLP algorithms.

# Research provenance, contributions, and verification status

## Origin and development of the investigation

This mathematical investigation was initiated and directed by Louis Desbiens and developed through extensive interaction with OpenAI's ChatGPT. Louis Desbiens identified the original research questions, set the objectives, guided the investigation, assessed its progress at a conceptual level, and selected the material for public dissemination.

ChatGPT contributed substantially to mathematical exploration, including alternative formulations, derivation of algebraic identities, formulation and examination of conjectures and proposed proofs, identification of potential counterexamples and exceptional cases, design and execution of symbolic and numerical checks, organization of relevant literature, and drafting and revision of the text. These contributions went well beyond linguistic or editorial assistance.

## Attribution and scientific authorship

Louis Desbiens is identified as the **human initiator and curator**, not as an independent mathematical authority certifying the results. OpenAI's ChatGPT is identified as the **AI mathematical research contributor**, not as an accountable conventional scholarly coauthor. These designations describe the provenance without implying that the human curator personally derived or independently verified all the arguments.

## Mathematical verification status

The candidate mathematical contributions have not undergone independent specialist validation, formal proof verification, or an exhaustive originality and priority review. In particular, independent examination is needed of the compatible-cover and quaternionic actions; convolution duality and its arithmetic sign; convolution Tannaka group identification; the Frobenius-stable projector and purity estimate; the moment and extension-degree calculations. Locally displayed proofs are proposed arguments. Established results cited from public literature should be assessed separately from new deductions; neither an AI-generated proof nor a successful computational check is by itself an independently certified theorem. Individual statements may be correct, partly correct, incomplete, or incorrect.

## Responsibility and purpose of public release

Louis Desbiens assumes responsibility for the decision to release this collection and for a good-faith account of its origin, contributors and verification status. He does **not** claim to have personally established or independently certified the correctness, completeness or originality of the proposed mathematical results. The material is made available for independent examination, criticism, reproducibility and possible further development; publication does not constitute scientific endorsement. This disclosure does not eliminate ordinary responsibilities associated with distributing public material.

## Institutional independence, funding, and competing interests

No institutional affiliation or endorsement is claimed. The investigation was undertaken independently, without institutional funding or resources. No external research funding was received. The human curator reports no competing interests.

## Computational evidence and source availability

Numerical evaluations helped develop the initial intuition. The public repository contains the available scripts, archived results, and a claim-by-claim verification coverage guide. These are scoped finite arithmetic, symbolic, and numerical checks, not independent verification of the general mathematical results. Historical exploratory calculations for which independent source data are unavailable are not treated as reproducible evidence.

# References and dependency map

[CDRS] B. Collas, M. Dettweiler, S. Reiter, and W. Sawin, "Monodromy of elliptic curve convolution, seven-point sheaves of $G_2$-type and motives of Beauville type," *Journal fuer die reine und angewandte Mathematik* 784 (2022), 1--26. DOI: 10.1515/crelle-2021-0070. Public version: https://arxiv.org/abs/1803.05883v2. Numbering used here is from that version: Proposition 1.2.2 (the semisimple property-P convolution category), Lemma 1.2.4 (generic-rank formula), Lemma 1.2.5 (finite objects), and the argument of Lemma 1.2.6 (translation self-twists and the connected component). Only these algebraic statements, not the subsequent complex-analytic discussion, are used over finite fields.

[Deligne] P. Deligne, "La conjecture de Weil. II," *Publications Mathematiques de l'IHES* 52 (1980), 137--252. DOI: 10.1007/BF02684780. Public text: https://www.numdam.org/item/PMIHES_1980__52__137_0/. The purity and weight estimates used in Sections 4--10 are standard inputs; no new general purity theorem is asserted.

[FFK] A. Forey, J. Fresan, and E. Kowalski, *Arithmetic Fourier transforms over finite fields: generic vanishing, convolution, and equidistribution*, arXiv:2109.11961v6, 8 September 2025. Public version: https://arxiv.org/abs/2109.11961v6. Chapters 3--4 supply the general Tannakian and equidistribution context. The explicit moment proof in Section 7 treats the arithmetic component directly rather than invoking equidistribution from a connected-group identification alone.

[Milne] J. S. Milne, *Elliptic Curves*, second edition, World Scientific, 2021. Public author version: https://www.jmilne.org/math/Books/EC2.pdf. Used for finite-field elliptic curves, divisors, coverings, and the classical curve Weil bound in the explicit-cover arguments.

[SEC2] Certicom Research, *SEC 2: Recommended Elliptic Curve Domain Parameters*, version 2.0, 27 January 2010, Section 2.4.1. https://www.secg.org/sec2-v2.pdf. The secp256k1 parameters provide a motivating example, not an additional hypothesis of the general theorem.
