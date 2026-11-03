# Quaternionic symmetry and semicircle laws for elliptic Fourier transforms

*Public AI-developed mathematical research artifact -- independently unverified candidate results*  
**Edition:** 2 November 2026  
**License:** CC BY 4.0 (manuscripts and documentation)

**Human initiator and curator:** Louis Desbiens\
**AI mathematical research contributor:** OpenAI's ChatGPT\
**Document classification:** Public AI-developed mathematical research artifact -- independently unverified candidate results\
**Institutional affiliation:** None claimed\
**Manuscript license:** Creative Commons Attribution 4.0 International (CC BY 4.0)

**Status and reading guide.** This document records a human-initiated, substantially AI-developed mathematical investigation. The human curator directed the objectives but does not independently certify its advanced mathematical arguments. The novel claims and supplied proofs are candidate results awaiting independent specialist verification; public availability does not certify correctness, completeness or originality. Section 3 presents the proposed explicit-cover Fourier envelope. Section 9 develops an elementary exact elliptic-trace identity for the autocorrelation, giving its envelope through the classical Hasse bound. Sections 5--8 develop proposed convolution-group, arithmetic descent and moment arguments using established literature; Section 10 presents proposed extension-field consequences. The augmented inversion pairing, its arithmetic sign, the Frobenius-stable projector, the geometric comparison, and especially the convolution-group and higher-moment calculations require independent specialist verification. Finite Fourier evaluations are checks of particular examples, not proofs of the general statements.

# Abstract

Let $E/\mathbf F_q:y^2=x^3+ax+b$ be nonsingular, with characteristic greater than three, $q\equiv3\pmod4$, and odd group order $N$. Set $f(O)=0$ and $f(P)=\chi_q(y(P))$ otherwise. For every character $\psi$ of the elliptic-curve group, define $S_E(\psi)=\sum_P f(P)\psi(P)$. The manuscript presents a proposed explicit-cover proof of the uniform bound $|S_E(\psi)|\leq2\sqrt q$. The mechanism is the quaternion group lifting two-torsion translations to the genus-three cover $z^2=y$, together with the three-cycle action of Frobenius. The proposed identification of the associated convolution Tannaka group is $(Q_8\times SL_2)/\langle(-1,-I)\rangle$ in its four-dimensional tensor-product representation. Accounting for its arithmetic component, rather than only its connected group, is used to propose

$$\left|\frac1N\sum_\psi\left(\frac{-iS_E(\psi)}{2\sqrt q}\right)^{2r}
-\frac{C_r}{4^r}\right|\leq\frac{r}{2\sqrt q},\qquad
C_r=\frac1{r+1}\binom{2r}{r}.$$

The argument predicts vanishing odd moments and proposes that the full normalized Fourier spectrum tends to the radius-one semicircle law along admissible families with $q\to\infty$. For a nonzero shift $T=(u,v)$, an elementary proposed identity identifies the autocorrelation with the Frobenius trace of the auxiliary elliptic curve $H_T:w^2=(x-u)(x^3+ax+b)$, up to the sign $-\chi_q(-1)$. It gives the autocorrelation bound $2\sqrt q$ by the established Hasse theorem. The new explicit Lang-cover inversion pairing and diagonal two-torsion projector strengthen the proposed rank-two model independently of the full convolution-group classification. The latter classification, the higher moments and the semicircle law still await specialist review. The consequences concern one coordinate character and do not establish general ECDLP hardness or a private-key-recovery algorithm.

**Keywords:** elliptic Fourier transform; quadratic character; quaternion group; convolution; semicircle law; arithmetic monodromy; autocorrelation.

# 1. Definitions and assumptions

Fix a short Weierstrass model $$E:\ y^2=g(x),\qquad g(x)=x^3+a x+b,
\qquad 4a^3+27b^2\ne0.$$ Throughout Sections 1--9 and 11, assume $$\operatorname{char}k>3,\qquad q\equiv3\pmod4,\qquad N=\#E(k)\text{ odd}.
\qquad \text{(1.1)}$$ Odd group order is enough; prime group order is not required for the Fourier theorem. The actual secp256k1 curve is an example with $a=0,b=7$. CM is useful for organizing the frequencies, but it is not needed for the main bound.

Let $\chi_q:k^*\to\{\pm1\}$ be the quadratic character. No affine rational point has $y=0$: such a point would be nonzero rational two-torsion. Consequently $$f(P)=\begin{cases}0,&P=O,\\ \chi_q(y(P)),&P\ne O\end{cases}
\qquad \text{(1.2)}$$ is a well-defined real function, with $|f(P)|=1$ away from the identity.

The Fourier transform is indexed by **all characters of the elliptic-curve group**, not by additive characters of the coordinate field: $$S_E(\psi)=\sum_{P\in E(k)}f(P)\psi(P),
\qquad \psi\in\widehat{E(k)}.
\qquad \text{(1.3)}$$ When $E(k)=\langle G\rangle$ has prime order $n$, this includes the discrete Fourier convention $$S_k=\sum_{d=0}^{n-1}f([d]G)e^{-2\pi i k d/n}.$$ Changing the Fourier sign merely reverses the frequency labels.

Since $\chi_q(-1)=-1$, $$f(-P)=-f(P),\quad S_E(1)=0,\quad
S_E(\psi^{-1})=-S_E(\psi)=\overline{S_E(\psi)}.
\qquad \text{(1.4)}$$ Thus all Fourier sums are purely imaginary. Put $$Y_\psi=\frac{-iS_E(\psi)}{\sqrt q},\qquad
X_\psi=\frac{Y_\psi}{2}.
\qquad \text{(1.5)}$$ The eventual compact support is $[-2,2]$ for $Y$, and $[-1,1]$ for $X$.

## 1.1 The special CM bookkeeping

For $a=0$, $q\equiv1\pmod3$, choose $\beta^3=1$, $\beta\ne1$. Then $$\phi(x,y)=(\beta x,y)$$ preserves every predicate depending only on $y$. In a prime-order group, writing $\phi(G)=[\lambda]G$ gives $$f([\lambda d]G)=f([d]G),\qquad
S_{\lambda k}=S_k,\qquad S_{-k}=-S_k.
\qquad \text{(1.6)}$$ There are $(n-1)/6$ equal-magnitude frequency orbits.

**Sign-selection warning.** Selecting one representative from each sixfold orbit preserves every even spectral moment, but does not canonically preserve a signed distribution. One could deliberately choose the positive member of every sign pair. A theorem about the signed semicircle distribution must use the full character set, or the explicitly symmetrized list containing both $X$ and $-X$ for each orbit. An arbitrary choice of one signed representative cannot be used to define the signed measure in the theorem.

# 2. The genus-three cover and its quaternionic symmetry

Let $C$ be the smooth projective normalization of $$z^2=y,\qquad y^2=g(x),$$ so affinely $$C:\ z^4=g(x).
\qquad \text{(2.1)}$$ Write $\pi:C\to E$ for the degree-two map and $\iota(x,z)=(x,-z)$ for its deck involution.

Over $\bar k$, the roots $r_1,r_2,r_3$ of $g$ give the nonzero two-torsion points $T_r=(r,0)$. The divisor $$\operatorname{div}(y)=\sum_{r:g(r)=0}(T_r)-3(O)
\qquad \text{(2.2)}$$ has odd valuations exactly at $E[2]$. Thus $C/E$ has four simple quadratic branch points. Riemann--Hurwitz gives $$2g(C)-2=2(2g(E)-2)+4,
\qquad g(C)=3.
\qquad \text{(2.3)}$$

## Lemma 2.1. Explicit lifts of two-torsion translations

For a root $r$, set $d_r=g'(r)=3r^2+a\ne0$. Translation by $T_r$ has formulas $$x(P+T_r)=r+\frac{d_r}{x(P)-r},
\qquad
y(P+T_r)=-\frac{d_r}{(x(P)-r)^2}y(P).
\qquad \text{(2.4)}$$ Choose $c_r\in\bar k$ with $c_r^2=-d_r$. Then $$\sigma_r(x,z)=\left(r+\frac{d_r}{x-r},\frac{c_r}{x-r}z\right)
\qquad \text{(2.5)}$$ lifts this translation and satisfies $\sigma_r^2=\iota$.

**Proof.** Substituting (2.4) verifies the square of the new $z$-coordinate. After translating twice, the product of the two multipliers on $z$ is $$\frac{c_r^2}{d_r}=-1.$$ These rational formulas extend to the smooth projective curve. The translation formulas follow from the chord through $P$ and $(r,0)$. $\square$

There are two lifts of each of the four two-torsion translations. They form an order-eight group whose six noncentral elements all have order four. Consequently $$\widetilde{E[2]}\simeq Q_8,
\qquad
1\to\langle\iota\rangle\to Q_8\to E[2]\to1.
\qquad \text{(2.6)}$$ This is an ordinary finite-group statement; no experimental input is used.

## Lemma 2.2. Frobenius acts by an order-three automorphism on this $Q_8$

Because $N$ is odd, Frobenius fixes no nonzero point of $E[2]$. Its permutation of the three nonzero points is therefore a three-cycle. The induced automorphism of $Q_8$ is also of order three: under $$\operatorname{Aut}(Q_8)\simeq S_4\longrightarrow S_3,$$ the preimages of three-cycles are three-cycles. In particular, this is not a claim that Frobenius acts trivially on the quaternion group.

For the original $j=0$ setting, one can choose $c_r=\delta r$, $\delta^2=-3\in k$, and the cyclic permutation is visible directly in (2.5). The general argument does not need this specialization.

# 3. The uniform Fourier bound

## Proposed Theorem A

Under (1.1), for every $\psi\in\widehat{E(k)}$, including the trivial character, $$\boxed{|S_E(\psi)|\le2\sqrt q.}
\qquad \text{(3.1)}$$

The proof uses the Weil theorem for smooth projective curves, together with an explicit construction making all actions compatible. It does not assume the later $SL_2$ result.

## 3.1 A concrete simultaneous cover for all characters

Let $$\mathsf L=\operatorname{Frob}_q-[1]:E\to E$$ be the Lang isogeny. It is finite etale of degree $N$, with constant deck group $\Gamma=E(k)$. Form the fiber product $$\widetilde C=C\times_{E,\mathsf L}E.
\qquad \text{(3.2)}$$ It is smooth and connected. Connectedness follows, for example, because a nontrivial quadratic function-field extension cannot become trivial after an odd-degree extension. The map $\widetilde C\to C$ is etale of degree $N$, and the map $\widetilde C\to E$ on the second factor is quadratic with $4N$ branch points. Hence $$g(\widetilde C)=2N+1.
\qquad \text{(3.3)}$$

The Lang map is invertible on $E[2]$, since its kernel has odd order. For $T\in E[2]$, let $U_T\in E[2]$ be the unique point such that $\mathsf L(U_T)=T$. A lifted translation acts on the fiber product by $$(c,R)\longmapsto(\sigma_T(c),R+U_T).
\qquad \text{(3.4)}$$ Together with the deck involution these give a genuine $Q_8$-action. It commutes with $\Gamma$, and the construction is Frobenius-compatible. The group law is exact: $T\mapsto U_T$ is an additive inverse to the Lang map on $E[2]$, so the product of two such lifts has the same central cocycle as the original quaternion lifts. A deck translation by $\gamma\in\Gamma$ changes only $R$, and hence commutes with each lift. Frobenius commutes with the Lang map and sends $U_T$ to $U_{F_qT}$, giving arithmetic compatibility.

Equivalently, in character-sheaf language, choose the unique character $\theta$ with $\theta^2=\psi$. The rigidified Lang character sheaves satisfy $$\mathcal L_\psi\simeq[2]^*\mathcal L_\theta.
\qquad \text{(3.5)}$$ The right side has its canonical $E[2]$-linearization, which lifts to $Q_8$ on $C$. This is the same construction in a smaller notation.

## 3.2 Each character contributes a four-dimensional anti-invariant space

Work with $\overline{\mathbf Q}_\ell$-coefficients, for $\ell\ne\operatorname{char}k$, and fix an embedding of the relevant coefficient field into $\mathbf C$. In the $(-1)$-eigenspace of $\iota$ on $H^1(\widetilde C)$, the $\psi$-isotypic component has dimension four.

One elementary dimension check is as follows. An etale $\Gamma$-cover of a genus-three curve has $$H^1(\widetilde C)\simeq4\operatorname{Reg}_\Gamma\oplus2\mathbf1$$ as a $\Gamma$-representation. This follows from the fixed-point trace formula: a nonidentity deck translation has no fixed points and therefore trace two on $H^1$. The $\iota$-invariant part is $H^1(E)$, on which all translations act trivially, accounting for $2\mathbf1$. Thus the anti-invariant part is $4\operatorname{Reg}_\Gamma$.

Write its $\psi$-component as $V_\psi$. Equivalently, $$V_\psi=H^1(C_{\bar k},\pi^*\mathcal L_\psi)^-,
\qquad \dim V_\psi=4.
\qquad \text{(3.6)}$$ This formulation also handles $\psi=1$: one must use the minus part, not the entire six-dimensional $H^1(C)$.

The dimension can also be read without an equivariant fixed-point argument. The local system $\mathcal K_y\otimes\mathcal L_\psi$ on $E\setminus E[2]$ has four tame nontrivial local monodromies and no geometric invariants. The unramified twist changes none of them. The genus-one Euler-characteristic formula gives $\dim H_c^1=4$, while $H_c^0=H_c^2=0$. The Kummer anti-invariant part identifies this group with $V_\psi$.

At a rational unbranched point, the difference between the two quadratic-cover eigenspace traces is $\chi_q(y(P))$. At each branch point the anti-invariant stalk is zero. Thus the prescribed values, including $f(O)=0$, agree with the middle-extension trace; no omitted endpoint correction is present.

With the Lang eigenspace convention chosen so the trace function is $\psi$, the trace formula is $$S_E(\psi)=-\operatorname{Tr}(F_q\mid V_\psi).
\qquad \text{(3.7)}$$ Using the opposite Frobenius/eigenspace convention replaces $\psi$ by $\psi^{-1}$, without altering any bound or distribution below.

## 3.3 Quaternionic multiplicity and the Frobenius trace

The central involution of $Q_8$ acts as $-I$ on $V_\psi$. Of the irreducible characteristic-zero representations of $Q_8$, only its unique two-dimensional representation $\rho$ has this central character. Hence $$V_\psi\simeq\rho\otimes W_\psi,
\qquad \dim W_\psi=2.
\qquad \text{(3.8)}$$

Choose a finite-order matrix $A\in SL_2$ implementing the Frobenius three-cycle on $\rho(Q_8)$. In quaternion notation one may take, up to sign and inverse, $$A=\frac{1+I+J+K}{2},\qquad I^2=J^2=K^2=IJK=-1.
\qquad \text{(3.9)}$$ For example, take $I=\operatorname{diag}(i,-i)$, $J=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$, and $K=IJ$. Direct multiplication gives $\det A=1$, $A^3=-I_2$, and the eight numbers $\operatorname{tr}(A\rho(u))$, $u\in Q_8$, consist of four $+1$ and four $-1$. The inverse three-cycle and an inner quaternionic conjugation have the same absolute trace property.

It has $|\operatorname{tr}A|=1$. Schur's lemma gives $$F_q\mid V_\psi=A\otimes B_\psi
\qquad \text{(3.10)}$$ for a two-dimensional operator $B_\psi$. All eigenvalues on $V_\psi$ have absolute value $\sqrt q$, by the Weil theorem applied to the smooth projective cover. Since the eigenvalues of $A$ are roots of unity, the two eigenvalues of $B_\psi$ also have absolute value $\sqrt q$. Therefore $$|S_E(\psi)|=|\operatorname{tr}A|\,|\operatorname{tr}B_\psi|
\le2\sqrt q.$$ This completes the proposed proof of Theorem A. $\square$

**Interpretation.** The four-dimensional space does not simply lose two dimensions. It is a tensor product of a finite two-dimensional quaternionic factor and a two-dimensional multiplicity factor. Frobenius has trace of absolute value one on the former.

# 4. The geometric convolution object

Let $U=E\setminus E[2]$, $j:U\to E$ be the open inclusion, and let $\mathcal K_y$ be the quadratic Kummer local system associated with $y$. Define $$\mathcal A=j_{!*}\mathcal K_y[1].
\qquad \text{(4.1)}$$ All four local monodromies are $-1$, so the middle extension has zero stalk at each branch point. Its trace function is $-f$. It is geometrically simple, of generic rank one and Tannakian dimension $$\chi(E,\mathcal A)=4.
\qquad \text{(4.2)}$$ It has property P: after tensoring by any lisse rank-one sheaf on $E$, global cohomology vanishes outside degree zero. Indeed the nontrivial ramification prevents global sections of the underlying local system or its dual; on the proper curve only the middle cohomology survives.

We use the semisimple elliptic-convolution category described in \[CDRS, Proposition 1.2.2\]. Convolution is derived pushforward along addition; the unit is $\delta_O$, duality is $[-1]^*D$, and the fiber functor is global degree-zero cohomology. Its dimension is Euler characteristic. These are established inputs, not new claims of this manuscript.

For precision, two further consequences of that framework are used. If $\operatorname{rk}$ denotes generic local-system rank and $\chi$ denotes Tannakian dimension, then

$$\operatorname{rk}(K*L)=\operatorname{rk}(K)\chi(L)+\chi(K)\operatorname{rk}(L).$$

This is \[CDRS, Lemma 1.2.4\]. It can be seen on a generic addition fiber: the singular sets of the two factors are disjoint, the elliptic curve has Euler characteristic zero, and each factor's local Euler defects are multiplied by the other's generic rank. Summing the defects gives the formula.

An object with finite Tannaka group is a direct sum of torsion-point skyscrapers \[CDRS, Lemma 1.2.5\]. To recall the reason, if its dimension is $d$ and its rank is $r$, the rank formula makes the rank of its $m$th convolution power equal to $md^{m-1}r$. Finite monodromy allows only finitely many irreducible constituents, so their ranks give a bound $Cd^m$. Letting $m$ grow forces $r=0$. A rank-zero perverse object is punctual, and a skyscraper at a point of infinite order would generate infinitely many distinct translates, contrary to finite monodromy. These arguments clarify the inputs behind the component-group calculation.

The word **monodromy** below means the convolution Tannaka group. The ordinary local monodromy of $\mathcal K_y$ is only a finite quadratic group. We are not constructing an ordinary rank-two lisse sheaf on an algebraic variety whose rational points are all the characters $\psi$; those characters naturally parameterize fiber functors instead \[FFK\].

# 5. The connected geometric group is $SL_2$

## Proposed Theorem B

For the geometric convolution group $G$ generated by $\mathcal A$, the identity component acts on the multiplicity space $W$ as the standard representation of $SL_2$: $$G^\circ\simeq SL_2,\qquad V\vert_{G^\circ}\simeq W\oplus W.
\qquad \text{(5.1)}$$

## 5.1 Translation stabilizer

The lifted translations prove $t_T^*\mathcal A\simeq\mathcal A$ for every $T\in E[2]$. Conversely, any translation stabilizing $\mathcal A$ must preserve its singular set $E[2]$, hence belongs to $E[2]$. Thus $$\operatorname{Stab}(\mathcal A)=E[2].
\qquad \text{(5.2)}$$

For each $T$, the isomorphism $\mathcal A*\delta_T\simeq\mathcal A$ yields a self-twist operator $A_T$ on the four-dimensional fiber $V$. Their multiplication is the quaternion extension already computed. If $\varepsilon_T$ is the finite character associated with $\delta_T$, $$A_Tg=\varepsilon_T(g)gA_T.
\qquad \text{(5.3)}$$ The finite characters are trivial on $G^\circ$, so $G^\circ$ centralizes this $Q_8$. Consequently it acts only on $W$ in $V=\rho\otimes W$.

## 5.2 Exact commutant dimension

The representation $\operatorname{End}_{G^\circ}(V)$ factors through the finite component group. By \[CDRS, Lemma 1.2.5\], every object with finite convolution group is a sum of torsion skyscrapers. Therefore its simple constituents are one-dimensional characters attached to $\delta_T$.

The multiplicity of the character attached to $T$ in $\operatorname{End}(V)$ is $$\dim\operatorname{Hom}_G(V\otimes\varepsilon_T,V).$$ Since $V$ is irreducible, this is one when $t_T^*\mathcal A\simeq\mathcal A$, and zero otherwise. Thus $$\dim\operatorname{End}_{G^\circ}(V)=4.
\qquad \text{(5.4)}$$ But $$\operatorname{End}_{G^\circ}(V)
=\operatorname{End}(\rho)\otimes\operatorname{End}_{G^\circ}(W).$$ Hence $\operatorname{End}_{G^\circ}(W)$ consists of scalars. Semisimplicity then makes $W$ absolutely irreducible.

## 5.3 Self-duality excludes the torus

Geometrically, $\mathcal A\simeq\mathcal A^\vee$: the local system is quadratic, and replacing $y$ by $-y$ changes it only by a geometrically constant factor. Thus $W\simeq W^\vee$.

An irreducible self-dual two-dimensional representation preserves either a symmetric or an alternating form. If symmetric, its connected image lies in $SO_2$, a torus, which cannot act absolutely irreducibly on a two-dimensional space over an algebraically closed field. Therefore its form is alternating, and the image lies in $Sp_2=SL_2$.

The image is connected and reductive. A proper connected reductive subgroup of $SL_2$ is a torus or the trivial group, again incompatible with irreducibility. The representation is faithful because the original Tannaka representation is faithful. Hence the image is exactly $SL_2$, completing the proposed proof of Theorem B. $\square$

# 6. The full geometric group and the arithmetic sign

Identifying $G^\circ$ is not by itself an equidistribution theorem. The finite component matters here.

## 6.1 The symmetric convolution form

Choose $i\in\bar k$ with $i^2=-1$. On $C$, $$\nu(x,z)=(x,iz)$$ lifts inversion on $E$, and $\nu^2=\iota$. On $V=H^1(C)^-$, put $J=\nu^*$. Then $J^2=-I$.

The cup-product pairing $\langle\ ,\ \rangle$ is alternating. Define $$B(v,w)=\langle v,Jw\rangle.
\qquad \text{(6.1)}$$ Since $J$ preserves cup product and $J^{-1}=-J$,

$$B(w,v)=\langle w,Jv\rangle
=-\langle Jv,w\rangle
=-\langle v,J^{-1}w\rangle=B(v,w).$$

Nondegeneracy follows because both cup product and $J$ are nondegenerate. To identify the pairing in the convolution category, restrict the addition fiber over $O$ to the anti-diagonal $(P,-P)$. Evaluation there pairs a local-system fiber with the inverse-point dual fiber. The lift $\nu$ identifies the inverse-point fiber with the original fiber, and integration over $E$ is cup product. Thus the fiber of this evaluation is exactly $\langle v,Jw\rangle$ up to a nonzero scalar. It is therefore the convolution duality pairing, not merely an unrelated bilinear form on cohomology, and is $G$-invariant. The quaternion lifts commute with $\nu$, so they preserve $B$ too. In $V=\rho\otimes W$, this form is the tensor product of alternating forms on $\rho$ and $W$.

Because $q\equiv3\pmod4$, Frobenius sends $\nu$ to $\nu^{-1}$. Thus $$B(F_qv,F_qw)=-q\,B(v,w).
\qquad \text{(6.2)}$$ Multiplying Frobenius by $i/\sqrt q$ makes it orthogonal. This is the arithmetic reason for the imaginary normalization in (1.5), not a cosmetic rotation of a plot.

### 6.1a. Inversion pairing on every character-twisted space

The preceding pairing must be checked on each individual twisted space, not only on the cohomology of the original genus-three curve. On the simultaneous Lang cover from Section 3.1, define $$\widetilde\nu(c,R)=(\nu(c),-R),\qquad
 \nu(x,z)=(x,\zeta z),\quad\zeta^2=-1.$$ This geometric lift squares to the deck involution and conjugates a Lang-deck translation by $\gamma$ to its inverse. It commutes with the lifted two-torsion translations: their auxiliary points $U_T\in E[2]$ satisfy $-U_T=U_T$. For $V_\psi=H^1(\widetilde C)^{-}_{\psi}$, cup product pairs $V_\psi$ with $V_{\psi^{-1}}$. The induced operator $J=\widetilde\nu^*$ interchanges these spaces, and $J^2=-I$. Consequently $$b_\psi(v,w)=\langle v,Jw\rangle$$ is a nondegenerate symmetric $Q_8$-invariant form on $V_\psi$. Because $q\equiv3\pmod4$, Frobenius conjugates $\nu$ to $\nu^{-1}$. Hence $FJ=-JF$ on the deck-anti-invariant part and $$\boxed{b_\psi(Fv,Fw)=-q\,b_\psi(v,w).}
 \tag{N.1}$$ As $V_\psi\simeq\rho\otimes W_\psi$, the form is the tensor product of alternating forms on the two quaternionic and multiplicity factors. Choosing the three-cycle intertwiner $A\in SL_2$ with $\operatorname{tr}A=1$ and $F=A\otimes B_\psi$, the multiplier on the second alternating form is $\det B_\psi$. Thus the proposed cohomological construction determines, not merely bounds, $$\boxed{\det B_\psi=-q,\qquad
 U_\psi=\frac{iB_\psi}{\sqrt q}\in SL_2,\qquad
 \operatorname{tr}U_\psi=\frac{-iS_E(\psi)}{\sqrt q}.}
 \tag{N.2}$$ Here $i$ in the coefficient field and $\zeta$ in the geometric base field are separate choices. The proof does not require the proposed full convolution-group identification in Section 6.2. An independent expert must still review all Weil-action conventions, including their effect on the trivial character space.

## 6.2 Full geometric group

The normalizer in $O(V,B)$ of $I_\rho\otimes SL_2(W)$ is $$\bigl(SL_2(\rho)\times SL_2(W)\bigr)/\langle(-I,-I)\rangle.
\qquad \text{(6.3)}$$ Indeed all automorphisms of $SL_2$ are inner; after removing the action on $W$, a normalizing operator lies in $GL(\rho)$. Preservation of the tensor-product form gives (6.3).

Every irreducible representation of the finite group $G/G^\circ$ is one-dimensional, again by the finite-object lemma and torsion skyscrapers. Thus $G/G^\circ$ is abelian. Its faithful projective image in $PGL_2(\rho)$ is a finite abelian group, hence cyclic or Klein four. A cyclic image preserves two lines in $\rho$, making $V$ reducible as a $G$-representation. Therefore the image is Klein four. Its inverse image in $SL_2(\rho)$ is quaternionic, giving $$\boxed{
G\simeq
(Q_8\times SL_2)/\langle(-1,-I)\rangle.
}
\qquad \text{(6.4)}$$

There are two roles for $Q_8$: geometric self-twist operators, and the finite factor of the full convolution group. Their projective images agree. One way to check this is that (5.3) makes the component group centralize the projective self-twist Klein four; its centralizer in $PGL_2$ is that same Klein four.

## 6.3 The Frobenius component

The normalized arithmetic Frobenius acts as $$\mathfrak F=A\otimes B_0,
\qquad A\in SL_2(\rho),\quad B_0\in SL_2(W),
\qquad \text{(6.5)}$$ with $A$ inducing the three-cycle on $Q_8$. The normalization (6.2) ensures $\det B_0=1$.

The finite extension generated by $Q_8$ and $A$ is the binary tetrahedral group. Crucially, $$\operatorname{tr}(A\rho(u))\in\{1,-1\}
\qquad(u\in Q_8).
\qquad \text{(6.6)}$$ Thus the relevant arithmetic component has the same trace distribution as a single $SU(2)$ factor, although the full geometric representation has dimension four.

### 6.3a. Characteristic polynomial and extension-character checks

Put $s=S_E(\psi)$. The determinant and trace calculation in (N.2) predicts the following characteristic polynomial of four-dimensional Frobenius: $$\boxed{\det(Z-F\mid V_\psi)
 =Z^4+sZ^3+(s^2+q)Z^2-qsZ+q^2.}
\tag{N.3}$$ For the extension character obtained by composing $\psi$ with the elliptic-curve norm $E(\mathbf F_{q^m})\to E(\mathbf F_q)$, let $S_m(\psi)$ be the corresponding ordinate-character sum. It follows formally from $S_m=-\operatorname{Tr}(F^m\mid V_\psi)$ that $$\boxed{S_2(\psi)=s^2+2q,\qquad S_3(\psi)=-2s^3-6qs.}
\tag{N.4}$$ These formulas do *not* compare arbitrary unrelated characters on the extension groups. They provide falsifiable predictions tested in the accompanying technical evidence manuscript; finite tests are not a general cohomological proof.

# 7. Catalan moments with an explicit error term

## Proposed Theorem C

Under (1.1), for every integer $r\ge1$, $$\boxed{
\left|\frac1N\sum_{\psi\in\widehat{E(k)}}X_\psi^{2r}
-\frac{C_r}{4^r}\right|
\le\frac{r}{2\sqrt q},
\qquad C_r=\frac1{r+1}\binom{2r}{r}.
}
\qquad \text{(7.1)}$$ All odd moments are zero. The constant in (7.1) is uniform in the curve and field, but intentionally far from optimized.

## 7.1 A Frobenius-stable rank-two square model

This section uses a geometric diagonal projector and an explicit auxiliary elliptic family; its construction is proposed independently of the full convolution-group classification. For every nonzero rational parameter $T=(u,v)$, let $H_T:w^2=(x-u)g(x)$ be the auxiliary elliptic curve of Section 9. The exact trace-function identity can also be proved directly from Section 9 by elementary character sums. The sheaf-level identification and its singular fibers are more demanding and still require an expert review.

### 7.1a. A diagonal two-torsion projector

A projector on a vector space is not automatically an endomorphism of a sheaf. The following construction addresses that distinction directly.

Let $\mathcal A=(\pi_*\overline{\mathbf Q}_{\ell})^-[1]=j_{!*}\mathcal K_y[1]$ and $$\mathcal M=\mathcal A\otimes\operatorname{const}(i/\sqrt q),\qquad \mathcal K=\mathcal M*\mathcal M.$$ The notation $\operatorname{const}(c)$ denotes a geometrically constant rank-one Weil object on which the chosen Frobenius acts by $c$. The trace function of $\mathcal M$ is $-if/\sqrt q$. The local monodromy of $\mathcal K_y$ is nontrivial at every point of $E[2]$. Twisting by a lisse rank-one sheaf on $E$ preserves this ramification, so the underlying sheaf and its dual have no global invariants. Their cohomology on the proper curve is concentrated in degree one. Thus $\mathcal A$ and $\mathcal M$ have property P. The published convolution formalism makes $\mathcal K$ perverse with property P; purity and geometric semisimplicity apply to this geometric construction \[Katz; CDRS; Deligne\].

On $C\times C$, the diagonal automorphism $(\sigma_T,\sigma_T)$ preserves the sum map $$s:C\times C\longrightarrow E,\qquad(c_1,c_2)\longmapsto\pi(c_1)+\pi(c_2),$$ because $2T=O$. Select the $(-1,-1)$-eigensummand for the two deck involutions in $Rs_*\overline{\mathbf Q}_{\ell}[2]$. This is the unnormalized convolution $\mathcal A*\mathcal A$. On this summand the central diagonal involution acts trivially; the diagonal $Q_8$ action therefore factors through $H=E[2]$. Changing the sign of a lift $\sigma_T$ has no effect on this action, since it inserts the central involution in both factors.

If $D_T$ denotes the resulting operator, define $$\label{eq:projector}
 \boxed{e_0=\frac14\sum_{T\in E[2]}D_T,\qquad
 \mathcal B=\operatorname{im}(e_0:\mathcal K\to\mathcal K).}$$ This is a genuine convolution endomorphism, not only a fiber-functor calculation. Frobenius sends $D_T$ to $D_{FT}$, so $e_0$ is Frobenius-stable and its image has a specified Weil structure. Idempotents split in the semisimple perverse setting \[CDRS\].

Geometrically the other three character projectors of $H$ are cyclically permuted by Frobenius. At a $k$-rational point, the operator on their direct sum has zero trace in every cohomological degree. It follows that $$\label{eq:tracefunction}
 \boxed{t_{\mathcal B}(T)=t_{\mathcal K}(T)
       =-\frac{(f*f)(T)}q=\frac{C_E(T)}q
       \quad(T\in E(k)).}$$ This is a base-field trace-function identity, not a geometric isomorphism $\mathcal K\simeq\mathcal B$. Over extensions with degree divisible by three the other sectors no longer have to cancel.

On global cohomology the projector is the average of the diagonal quaternion action on $\rho\otimes\rho$, tensored with the identity on $W\otimes W$. Its invariant line is $\bigwedge^2\rho$. Frobenius acts there by $\det A=1$, so the induced operator is exactly $U_\psi\otimes U_\psi$. Thus no unspecified scalar twist remains in the descended square model. Its Tannakian dimension is four.

### 7.1b. The explicit genus-two quotient and elliptic family

Fix a geometric parameter $T\notin E[2]$ and write $Q=T-P$. The relevant anti-invariant cohomology of the addition fiber can be represented by $$D_T^{\mathrm{conv}}:\quad w^2=y(P)y(Q),\qquad P+Q=T.$$ There are eight branch points, so this double cover of $E$ has genus five. A diagonal two-torsion translation acts as $$\label{eq:diag}
 (P,w)\longmapsto
 \left(P+T_r,-\frac{d_r}{(x(P)-r)(x(Q)-r)}w\right).$$ The action is free, since a nonzero translation fixes no point of the base elliptic curve. Its quotient has genus two by Riemann--Hurwitz.

The quotient is explicit. Put $$\label{eq:quotient}
 R=P-Q=2P-T,\qquad h=\frac{2w}{x(P)-x(Q)}.$$ Both are invariant under [\[eq:diag\]](#eq:diag){reference-type="eqref" reference="eq:diag"}. Indeed $x(P)-x(Q)$ is multiplied by exactly the same factor as $w$. Equation (9.3) yields $$\label{eq:genus2}
 Z_T:\quad h^2=x(R)-u,\qquad y(R)^2=g(x(R)).$$ For generic $(R,h)$ there are four choices of $P$ with $2P-T=R$, and $w$ is then fixed by [\[eq:quotient\]](#eq:quotient){reference-type="eqref" reference="eq:quotient"}. Thus this is the full degree-four quotient, not merely an invariant map. Writing $Y=y(R)$, the genus-two equation is $$Y^2=(h^2+u)^3+a(h^2+u)+b.$$ It has the deck involution $(h,Y)\mapsto(-h,Y)$ with quotient $E$, and the hyperelliptic involution $(h,Y)\mapsto(h,-Y)$. The quotient by their product is exactly $$(X,W)=(h^2+u,hY),\qquad H_T:\quad W^2=(X-u)g(X).$$ The hyperelliptic involution acts by $-1$ on $H^1(Z_T)$. Therefore pullback from $H_T$ identifies its two-dimensional $H^1$ with the anti-invariant part for $Z_T\to E$. This proves the generic rank-two assertion by an explicit curve correspondence.

Over the open parameter set $E\setminus E[2]$, the restriction of $\mathcal B$ is consequently $$\label{eq:localfamily}
 \left(R^1h_*\overline{\mathbf Q}_{\ell}\otimes\operatorname{const}(-1/q)\right)[1],$$ where here $h$ denotes the smooth projective family with fibers $H_T$. The shift contributes a minus sign to stalk traces, which explains why [\[eq:localfamily\]](#eq:localfamily){reference-type="eqref" reference="eq:localfamily"} has trace $+a_{H_T}/q$, not $-a_{H_T}/q$.

**Two different rank-two objects.** The multiplicity space $W_\psi$ is indexed by an elliptic-group character and can have cyclotomic coefficients. The rank-two local system in [\[eq:localfamily\]](#eq:localfamily){reference-type="eqref" reference="eq:localfamily"} is indexed by a point $T$ and comes from an actual elliptic-curve family. Their roles are related by convolution and Fourier transformation; they must not be identified. In particular, this argument does not say that the original $S(\psi)$ is an integer elliptic-curve trace.

### 7.1c. Origin stalk, punctual correction, and Parseval

The generic rank alone does not fix the value of $t_{\mathcal B}$ at the identity. That value is needed for the moment calculation.

On the addition fiber over $O$, the product of quadratic functions is $y(P)y(-P)=-y(P)^2$. Its Kummer local system is geometrically constant, with Frobenius scalar $-1$, on $U=E\setminus E[2]$. Multiplying by the normalization $(i/\sqrt q)^2=-1/q$ leaves scalar $1/q$. The $E[2]$ action is the ordinary translation action after this trivialization.

The compact-support exact sequence is $$\label{eq:openexact}
 0\longrightarrow\overline{\mathbf Q}_{\ell}\longrightarrow\overline{\mathbf Q}_{\ell}^{E[2]}
 \longrightarrow H_c^1(U,\overline{\mathbf Q}_{\ell})
 \longrightarrow H^1(E,\overline{\mathbf Q}_{\ell})\longrightarrow0.$$ The permutation representation $\overline{\mathbf Q}_{\ell}^{E[2]}$ is regular. Taking $E[2]$ invariants kills its reduced regular part, while translations act trivially on $H^1(E)$. Also $H_c^2(U)=\overline{\mathbf Q}_{\ell}(-1)$ has Frobenius eigenvalue $q$. Proper base change then gives $$\label{eq:originstalk}
 H^{-1}(\mathcal B_O)\simeq H^1(E)\otimes\operatorname{const}(1/q),\qquad
 H^0(\mathcal B_O)\simeq\overline{\mathbf Q}_{\ell}\quad\text{with eigenvalue }+1.$$ Thus $$\label{eq:origintrace}
 \boxed{t_{\mathcal B}(O)=1-\frac{a_E}{q}=\frac{N-1}{q}.}$$ This determines the arithmetic sign of the punctual contribution without using the proposed full group.

At a nonzero geometric $S\in E[2]$, the coefficient trivialization instead carries the nontrivial character $T\mapsto e_2(T,S)$ of $E[2]$, where $e_2$ is the commutator pairing of the quaternion extension. To see the sign, describe the normalization of the addition fiber using the graph of $\sigma_S\nu$. Conjugation by a diagonal lift $\sigma_T$ multiplies this graph map by the central commutator $e_2(T,S)$. Hence the invariant projector kills the top compact-support group there. There is no punctual invariant summand at such an $S$. The only possible singular addition parameters are in $E[2]$, so, in the pure semisimple category, $$\label{eq:Bdecomp}
 \mathcal B\simeq\delta_O\oplus\mathcal L[1],$$ where $\mathcal L[1]$ denotes the middle extension of the rank-two local system in [\[eq:localfamily\]](#eq:localfamily){reference-type="eqref" reference="eq:localfamily"}. Its generic rank is two and its Tannakian dimension is three. No irreducibility or full monodromy classification of this summand is needed for the trace identity established here.

There is a separate geometric check of its behavior at $O$. Put $z=1/u$ and rescale the quartic coordinate by $w'=uw/v$. Near the parameter $O$, $$\label{eq:limit}
 (w')^2=\frac{z x-1}{1+az^2+bz^3}\,g(x).$$ At $z=0$ this becomes $(w')^2=-g(x)$, the quadratic $(-1)$-twist of $E$. The homogeneous branch divisor remains reduced, so this gives good reduction of the genus-one family at $O$. Its trace is $-a_E$, and the normalizing factor and perverse sign in [\[eq:localfamily\]](#eq:localfamily){reference-type="eqref" reference="eq:localfamily"} give $-a_E/q$, agreeing with [\[eq:origintrace\]](#eq:origintrace){reference-type="eqref" reference="eq:origintrace"} after the $+1$ punctual term.

Finally define $Y_\psi=-iS(\psi)/\sqrt q$. Fourier transformation of [\[eq:tracefunction\]](#eq:tracefunction){reference-type="eqref" reference="eq:tracefunction"} gives $$\label{eq:square}
 \boxed{\widehat{t_{\mathcal B}}(\psi)=Y_\psi^2.}$$ At the identity, Fourier orthogonality gives $$\frac1N\sum_\psi Y_\psi^2=t_{\mathcal B}(O)=\frac{N-1}{q}.$$ After $X_\psi=Y_\psi/2$, this is the exact second moment $(N-1)/(4q)$. The check is sensitive to the sign, the two points at infinity in the quartic, and the punctual contribution.

### 7.1d. Relation to the proposed tensor-invariant calculation

The original representation-theoretic proposal remains relevant to higher moments: $\rho\otimes\rho$ decomposes into the four characters of $E[2]$, and the invariant projector picks out the geometric summand associated with $W\otimes W$. In the proposed full convolution group, this further decomposes as $$\mathbf1\oplus\operatorname{Sym}^2W.
\tag{N.9}$$ The geometric construction gives a rank-two trace model for the *square* and a punctual correction at the identity. It does not, by itself, establish connected $SL_2$, the higher tensor-invariant dimensions, or a uniform Catalan-moment error. Those stronger statements remain conditional on the separate arguments of Sections 5--8 and require independent specialist examination.

## 7.2 Moments and the punctual contribution

Fourier orthogonality gives $$\frac1N\sum_\psi Y_\psi^{2r}
=t_{\mathcal B^{*r}}(O).
\qquad \text{(7.7)}$$ This identity also follows directly by expanding the product of Fourier sums: averaging the character of a sum gives one exactly when that sum is $O$, and zero otherwise. Convolution of trace functions agrees with proper sheaf convolution by the trace formula.

The geometric representation of $\mathcal B^{*r}$ is $W^{\otimes2r}$, with the finite quaternionic factor trivial. Its invariants have dimension $$\dim(W^{\otimes2r})^{SL_2}=C_r.$$ For completeness, the invariant dimension follows from the elementary weight decomposition of tensor powers of the standard two-dimensional representation. The multiplicity of its highest-weight-zero constituent is the weight-zero multiplicity minus the weight-two multiplicity:

$$\binom{2r}{r}-\binom{2r}{r-1}
=\frac{1}{r+1}\binom{2r}{r}=C_r.$$

Nontrivial punctual constituents would be nontrivial finite characters. None occurs here, because the finite factor in $W^{\otimes2r}$ is trivial. Thus every punctual constituent is supported at $O$, and there is no additional finite-support contribution hidden in the rank estimate.

Arithmetic Frobenius acts through $B_0\in SL_2(W)$, and so acts trivially on these invariants. Therefore the punctual $\delta_O$ contribution in (7.7) is exactly $C_r$, with no unknown phase.

Equivalently, working directly with $V=\rho\otimes W$, the finite factor contributes $$\frac18\sum_{u\in Q_8}\operatorname{tr}(A\rho(u))^{2r}=1.
\qquad \text{(7.8)}$$ This calculation explains why identifying connected $SL_2$ alone would not determine the limiting law.

## 7.3 Bound the remaining stalk

The rank formula $$\operatorname{rk}(K*L)
=\operatorname{rk}(K)\chi(L)+\chi(K)\operatorname{rk}(L)$$ and (7.5) imply $$\operatorname{rk}(\mathcal B^{*r})=2r4^{r-1}.
\qquad \text{(7.9)}$$

Proper convolution preserves purity, and property P keeps the convolution perverse. A nonpunctual pure weight-zero middle extension on a curve has its local-system stalk in degree $-1$, with eigenvalues of absolute value at most $q^{-1/2}$. Its stalk dimension is at most its generic rank. The total nonpunctual contribution at $O$ therefore has absolute value at most $$2r4^{r-1}/\sqrt q.$$ Divide (7.7) by $4^r$ to obtain $$\left|\frac1N\sum_\psi X_\psi^{2r}-\frac{C_r}{4^r}\right|
\le\frac{r}{2\sqrt q}.$$ Odd moments vanish exactly by (1.4). This completes the proposed proof of Theorem C. $\square$

## 7.4 A Chebyshev form of the estimate

There is an alternative useful formulation. Let $U_m$ be the Chebyshev polynomial of the second kind, so $$U_m(\cos\theta)=\frac{\sin((m+1)\theta)}{\sin\theta}.$$ For even $m>0$, the representation $\mathbf1_{Q_8}\otimes\operatorname{Sym}^mW$ defines a nonpunctual simple object. On the arithmetic component its Fourier trace is $U_m(X_\psi)$. Its generic rank is $$\frac{m(m+1)(m+2)}{12}.
\qquad \text{(7.10)}$$ Here is a direct rank calculation, avoiding an implicit differentiation convention. Write $R_m$ for the rank of the object attached to $\operatorname{Sym}^mW$, for even $m$. One has $R_0=0$ and $R_2=2$. The character identity

$$\operatorname{Sym}^2W\otimes\operatorname{Sym}^mW
=\operatorname{Sym}^{m+2}W\oplus\operatorname{Sym}^mW\oplus\operatorname{Sym}^{m-2}W$$

for even $m\geq2$, together with the rank formula, gives

$$R_{m+2}=2(m+1)+2R_m-R_{m-2}.$$

Induction gives (7.10). Only even powers descend with trivial quaternionic factor, which is why the statement is restricted to even $m$. For a character-twisted fiber the sign of the finite-factor trace can change $Y_\psi$ to its negative, but $U_m$ is even for even $m$, so the stated Fourier trace is unaffected.

There is no punctual invariant contribution for $m>0$, hence $$\left|\frac1N\sum_\psi U_m(X_\psi)\right|
\le\frac{m(m+1)(m+2)}{12\sqrt q}
\quad(m>0\text{ even}).
\qquad \text{(7.11)}$$ The average is exactly zero for odd $m$, by symmetry. This expresses the approach to semicircle orthogonality directly and can support a later quantitative CDF-discrepancy analysis.

## 7.5. Scope of the estimate

For each fixed moment order the error tends to zero uniformly in the curve as $q\to\infty$. This establishes a limiting distribution, not a finite-field assertion that every empirical moment equals a Catalan number. The constants need not describe the typical size of an individual finite-field discrepancy. No independent-sampling assumption is used.

# 8. The semicircle law and correct normalization

The radius-one semicircle probability measure is $$d\mu_{\mathrm{sc}}(x)=\frac2\pi\sqrt{1-x^2}\,\mathbf1_{[-1,1]}(x)\,dx.
\qquad \text{(8.1)}$$ Its even moments are $C_r/4^r$, and its odd moments vanish. By Theorem A all empirical measures are supported on $[-1,1]$. Theorem C, polynomial approximation on a compact interval, and uniqueness of the moment problem imply:

## Proposed Corollary 8.1

Along any sequence of curves satisfying (1.1), with $q\to\infty$, $$\frac1{\#E(\mathbf F_q)}
\sum_{\psi\in\widehat{E(\mathbf F_q)}}\delta_{X_\psi}
\Longrightarrow\mu_{\mathrm{sc}}.
\qquad \text{(8.2)}$$ This does not assume that prime-order curves form an infinite family: odd group order suffices. For example, starting with an admissible curve, extension degrees congruent to $1$ or $5\pmod6$ remain admissible.

In particular, the bound is asymptotically sharp: along any such family, $\max_\psi |S_E(\psi)|/(2\sqrt q)\to1$, since every fixed neighborhood of either endpoint has positive limiting semicircle mass.

This conclusion uses the explicit arithmetic component and uniform moment proof above. It is not a blind application of an equidistribution theorem requiring equality of geometric and arithmetic groups. The distinction is treated in the general framework \[FFK, Chapter 4\].

## 8.1 Parseval fixes the second moment

Exactly, $$\sum_\psi|S_E(\psi)|^2=N\sum_P|f(P)|^2=N(N-1).$$ Thus $$\frac1N\sum_\psi X_\psi^2=\frac{N-1}{4q}.
\qquad \text{(8.3)}$$ Since $S_E(1)=0$, averaging only over nontrivial characters gives $$\frac1{N-1}\sum_{\psi\ne1}X_\psi^2=\frac{N}{4q}.
\qquad \text{(8.4)}$$ On a prime-order CM curve with group order greater than three, the same is true for one representative per sixfold frequency orbit, for even moments. Consequently the second moment is a normalization identity, not independent evidence for an $SU(2)$ distribution.

## 8.2 Variance standardization

For a cyclic prime-order group, the variance-standardized variable on nontrivial frequencies is $X/\sqrt{n/(4p)}=-iS/\sqrt n$. Its limiting even moments are the Catalan numbers $C_r$. At finite size the exact Parseval scale differs from $1/4$, so raw and variance-standardized moments should not be mixed in a proof or figure caption.

## 8.3 No independence claim

The theorem makes no assertion that distinct Fourier coefficients are independent random variables. Statistical tests assuming independent and identically distributed samples are therefore not justified by this result. A signed empirical distribution from arbitrarily selected CM representatives is additionally subject to the sign-selection warning in Section 1.1.

# 9. Exact autocorrelation as an elliptic Frobenius trace {#autocorrelation-elliptic-trace}

## Proposed Theorem D (stronger exact statement)

The following identity holds in a more general setting than (1.1): allow any finite field $k=\mathbf F_q$ of characteristic greater than three and any nonsingular short Weierstrass curve with $N$ odd. Let $\varepsilon=\chi_q(-1)$. For $T=(u,v)\in E(k)\setminus\{O\}$, let $H_T$ be the smooth projective genus-one curve $$H_T:\quad w^2=(x-u)(x^3+ax+b),\qquad
 a_{H_T}=q+1-\#H_T(k).
\tag{9.1}$$ Then the proposed exact identity is $$\boxed{C_E(T):=\sum_{P\in E(k)}f(P)f(P+T)
 =-\varepsilon\,a_{H_T}.}
\tag{9.2}$$ In the standing case $q\equiv3\pmod4$, $\varepsilon=-1$, so $C_E(T)=a_{H_T}$ exactly. The known Hasse bound therefore gives $\lvert C_E(T)\rvert\le2\sqrt q$. This route does not depend on the proposed convolution Tannaka group.

**Proposed elementary proof.** Because $N$ is odd, the multiplication-by-two map on $E(k)$ is bijective and $E(k)$ has no nonzero rational two-torsion. Set $Q=T-P$ and $R=P-Q=2P-T$. When $P,Q$ are distinct with nonzero finite ordinates, the addition formulas give $$x(P-Q)-x(P+Q)
=\frac{4y(P)y(Q)}{(x(P)-x(Q))^2}.
\tag{9.3}$$ It follows that $f(P)f(Q)=\chi_q(x(R)-u)$ away from the exceptional inputs. For $P=O$ or $P=T$, both sides vanish. At the unique midpoint $P=Q=T/2$, the left side contributes one, and $R=O$, so the right side is not an affine evaluation. No other collision of abscissas is possible, since $Q=-P$ would imply $T=O$. Consequently the bijection $P\mapsto R$ yields $$\begin{aligned}
(f*f)(T)&=1+\sum_{R\in E(k)\setminus\{O\}}
  \chi_q(x(R)-u)\\
 &=1+\sum_{x\in k}\chi_q((x-u)g(x)).
\end{aligned}
\tag{9.4}$$ Here the term $\sum_x\chi_q(x-u)=0$ has been removed. The quartic has four distinct roots because $g(u)=v^2\ne0$, and its monic leading term gives two rational points at infinity. Therefore $$\#H_T(k)=q+2+\sum_{x\in k}\chi_q((x-u)g(x)).
\tag{9.5}$$ Equation (9.4) implies $(f*f)(T)=-a_{H_T}$. Finally $f(-P)=\varepsilon f(P)$ gives $(f*f)(T)=\varepsilon C_E(T)$, proving (9.2). The midpoint contribution and the two rational points at infinity cannot be dropped. $\square$

## 9.1 Cubic model, CM parameter and independent proof scope

An explicit Weierstrass model follows from $s=1/(x-u)$, $z=w/(x-u)^2$, and $c=g(u)=v^2$, $d=g'(u)=3u^2+a$: $$z^2=cs^3+ds^2+3us+1,
\qquad
 Y^2=X^3+dX^2+3ucX+c^2.
\tag{9.6}$$ Here $X=cs$ and $Y=cz$. The discriminant and invariant are $$\Delta(H_T)=16c^2(-4a^3-27b^2),\qquad
j(H_T)=\frac{256(a^2-3au^2-9bu)^3}
{g(u)^2(-4a^3-27b^2)}.
\tag{9.7}$$ For the CM model $a=0$, this simplifies to $j(H_T)=6912bu^3/(u^3+b)^2$. In particular it depends only on $u^3$, but this is not an ECDLP algorithm or an isogeny-orbit classification.

For example $E/\mathbf F_{31}:y^2=x^3+7$ has $N=21$; at $T=(1,15)$ the curve $H_T$ has $27$ points and $C_E(T)=32-27=5$, as checked by direct enumeration. The detailed independent presentation of the exact character-sum argument, finite Fourier identities and small-field reproducibility records appears in the companion research artifact *Exact elliptic Frobenius traces for ordinate-character autocorrelation*.

## 9.2 Relation to the genus-five quotient

The original genus-five double-cover construction still explains the geometric rank-two summand: its free diagonal two-torsion quotient is the genus-two curve of Section 7.1b, whose second elliptic quotient is precisely $H_T$. The new elementary identity should be taken as the primary arithmetic argument for (9.2), while the sheaf-theoretic comparison remains a proposed structural interpretation.

# 10. Extension fields and arithmetic phases

This section records an additional consequence of the full arithmetic-component calculation. It is not needed for the base-field theorems.

Fix a curve over an admissible $\mathbf F_q$. For extension degree $d\ge1$, put $Q=q^d$, use the quadratic character of $\mathbf F_Q$ extended by $\chi_Q(0)=0$, set the value at $O$ to zero, and define $S_{d,\psi}$ over $E(\mathbf F_Q)$. The natural normalization inherited from (7.2) is $$X_{d,\psi}=\frac{-i^d S_{d,\psi}}{2q^{d/2}}.
\qquad \text{(10.1)}$$ This is real: for odd $d$ the sum is imaginary; for even $d$ it is real.

In the finite factor, arithmetic Frobenius is $A^d$. The invariant trace is $$\frac18\sum_{u\in Q_8}\operatorname{tr}(A^d\rho(u))^{2r}
=\begin{cases}
1,&3\nmid d,\\
4^{r-1},&3\mid d.
\end{cases}
\qquad \text{(10.2)}$$ The first line uses the binary tetrahedral three-cycle coset. In the second, $A^d\in Q_8$, and the standard quaternion representation has traces $2,-2,0,0,0,0,0,0$.

The same convolution proof therefore gives limiting laws, as extension sizes tend to infinity along the indicated subsequences: $$\begin{cases}
\mu_{\mathrm{sc}},&3\nmid d,\\
\displaystyle\frac34\delta_0+\frac14\mu_{{\mathrm{sc}},2},&3\mid d,
\end{cases}
\qquad \text{(10.3)}$$ where $\mu_{{\mathrm{sc}},2}$ is the radius-two semicircle law. Without using the rank-two simplification, the rank of $\mathcal M^{*2r}$ gives the safe extension-field error bound $2r4^{r-1}/\sqrt Q$ for these raw even moments. When $3\nmid d$, the rank-two simplification applies again and improves this to $r/(2\sqrt Q)$.

There is an elementary check on the atom at zero. Over a degree divisible by three, the quaternion lifts and all two-torsion points are rational. Formula (2.4) then shows that the quadratic ordinate predicate is invariant under $E[2]$. Its Fourier transform is consequently supported only on characters trivial on $E[2]$: at least three quarters of all Fourier coefficients vanish **exactly**. For every character, the original four-branch Kummer system with its unramified character twist has first cohomology of dimension four. The ordinary Weil bound therefore gives $|S|\le4\sqrt Q$, without assuming that a character has a square root in the even-order character group.

One extra step is needed to deduce a signed limiting law over even extension degrees. When $d$ is even, $f$ is even under inversion, so its odd spectral moments are not forced to vanish by (1.4). Instead, for every odd integer $j\geq1$, $W^{\otimes j}$ has no $SL_2$-invariants. There is no punctual part in $\mathcal M^{*j}$, and its rank is $j4^{j-1}$. The same weight estimate gives

$$\left|\frac{1}{\#E(\mathbf F_Q)}\sum_\psi X_{d,\psi}^{\,j}\right|
\leq\frac{j\,2^{j-2}}{\sqrt Q}. \qquad (10.4)$$

Thus odd moments tend to zero even on those subsequences. For even moments, (10.2) and the invariant dimension $C_r$ give $C_r/4^r$ when $3\nmid d$ and $C_r/4$ when $3\mid d$. These are exactly the moments of the two measures in (10.3). The bound $|X_{d,\psi}|\leq2$, valid in every extension, gives a common compact support, so convergence of all moments proves the stated weak limits. When $3\nmid d$, the Frobenius three-cycle and the rank-two trace reduction remain available, giving the sharper support $[-1,1]$ and the sharper even-moment error already stated.

This illustrates why connected $SL_2$ alone is not the correct statement of the distribution theorem. Arithmetic components can produce different laws over different extension degrees.

# 11. Consequences for the original scalar-information question

These are consequences for one specific observable, not lower bounds for arbitrary private-key-recovery algorithms.

## 11.1 Fourier incompressibility

Assume the group is cyclic of prime order $n$. Its Fourier energy is $$\sum_k|S_k|^2=n(n-1).$$ By Theorem A, any set of $s$ frequencies carries energy at most $4qs$. Hence a Fourier-supported approximation capturing a fraction $\eta$ of the total energy needs $$\boxed{s\ge\eta\,\frac{n(n-1)}{4q}.}
\qquad \text{(11.1)}$$ For $n\sim q$, this is linear in $n$. This is an approximation statement in the Fourier basis, not an unrestricted circuit or query lower bound.

## 11.2 Canonical scalar parity and affine reparameterization

Let $f_d=f([d]G)$, $f_0=0$, and let $a(d)=(-1)^d$ on the canonical representatives $0\le d<n$. Its discrete Fourier transform satisfies $$|\widehat a(k)|=\frac1{|\cos(\pi k/n)|}.
\qquad \text{(11.2)}$$ An elementary harmonic-sum estimate gives $$\sum_{k=1}^{n-1}|\widehat a(k)|\le n(2+\log n).
\qquad \text{(11.3)}$$ For completeness, pair $k$ with $n-k$, write the distance from $n/2$ as $j-1/2$, and use $\sin x\ge2x/\pi$ on $[0,\pi/2]$. The remaining sum is bounded by $2+\log n$.

For any known $u\ne0,v\pmod n$, the Fourier magnitudes of $d\mapsto f_{ud+v}$ are a permutation of those of $f$. Fourier inversion, (3.1), and (11.3) imply $$\boxed{
\left|\frac1{n-1}\sum_{d=1}^{n-1}(-1)^d f([ud+v]G)\right|
\le\frac{2\sqrt q(2+\log n)+1}{n-1}.
}
\qquad \text{(11.4)}$$ The $+1$ accommodates removing the $d=0$ term; it is unnecessary when $v=0$. The zero Fourier mode vanishes because $f$ is odd.

Thus every fixed affine-query version of this particular Legendre predicate has only square-root-times-logarithmic direct parity correlation. The theorem does **not** rule out arbitrary adaptive combinations of many queries, other predicates, high-degree functions, or quantum algorithms.

# 12. Numerical motivation and mathematical scope

The exploratory investigation used numerical evaluations to test and refine the initial intuition about the quadratic ordinate character. They motivated the comparison between a uniform square-root Fourier envelope and semicircle moments. No software-specific calculation, unarchived numerical array, or fitted distribution is intended as an input to the proposed proofs.

The second moment is fixed by Parseval, so it cannot by itself distinguish the semicircle law from another variance-matched model. Likewise, selecting arbitrary signs from sixfold frequency orbits changes a signed empirical distribution. Theorems C and Corollary 8.1 use the full character set and make neither of these substitutions. They do not treat the coefficients as independent random observations.

The principal mathematical ingredients are an explicit cover, its quaternionic translation symmetry, the arithmetic three-cycle, and the elliptic-convolution framework of \[CDRS\] and \[FFK\]. The finite factor is essential both to the constant two in the pointwise envelope and to the extension-field phases. The absolute bound and the new exact autocorrelation identity have complementary cover and elementary character-sum arguments, whereas the limiting law also uses the convolution duality and the descended rank-two trace model.

The framework itself is established literature. The candidate contribution proposed in this investigation is the explicit ordinate-character example and its deductions. A claim of priority for this collection would require a separate comprehensive literature investigation. The application bounds concern one observable and are not lower bounds for arbitrary ECDLP algorithms.

# Research provenance, contributions, and verification status

## Origin and development of the investigation

This mathematical investigation was initiated and directed by Louis Desbiens and developed through extensive interaction with OpenAI's ChatGPT. Louis Desbiens identified the original research questions, set the objectives, guided the investigation, assessed its progress at a conceptual level, and selected the material for public dissemination.

ChatGPT contributed substantially to mathematical exploration, including alternative formulations, derivation of algebraic identities, formulation and examination of conjectures and proposed proofs, identification of potential counterexamples and exceptional cases, design and execution of symbolic and numerical checks, organization of relevant literature, and drafting and revision of the text. These contributions went well beyond linguistic or editorial assistance.

## Attribution and scientific authorship

Louis Desbiens is identified as the **human initiator and curator**, not as an independent mathematical authority certifying the results. OpenAI's ChatGPT is identified as the **AI mathematical research contributor**, not as an accountable conventional scholarly coauthor. These designations describe the provenance without implying that the human curator personally derived or independently verified all the arguments.

## Mathematical verification status

The candidate mathematical contributions have not undergone independent specialist validation, formal proof verification, or an exhaustive originality and priority review. In particular, independent examination is needed of the compatible-cover and quaternionic actions; convolution duality and its arithmetic sign; convolution Tannaka group identification; the extended Frobenius pairing, geometric projector and purity estimate; the moment and extension-degree calculations. Locally displayed proofs are proposed arguments. Established results cited from public literature should be assessed separately from new deductions; neither an AI-generated proof nor a successful computational check is by itself an independently certified theorem. Individual statements may be correct, partly correct, incomplete, or incorrect.

## Responsibility and purpose of public release

Louis Desbiens assumes responsibility for the decision to release this collection and for a good-faith account of its origin, contributors and verification status. He does **not** claim to have personally established or independently certified the correctness, completeness or originality of the proposed mathematical results. The material is made available for independent examination, criticism, reproducibility and possible further development; publication does not constitute scientific endorsement. This disclosure does not eliminate ordinary responsibilities associated with distributing public material.

## Institutional independence, funding, and competing interests

No institutional affiliation or endorsement is claimed. The investigation was undertaken independently, without institutional funding or resources. No external research funding was received. The human curator reports no competing interests.

## Computational evidence and source availability

Numerical evaluations helped develop the initial intuition. The public repository contains the original scripts and the additional exact rank-two, extension-field and autocorrelation checkers, with archived results and a claim-by-claim verification coverage guide. These are scoped finite arithmetic, symbolic, and numerical checks, not independent verification of the general mathematical results. Historical exploratory calculations for which independent source data are unavailable are not treated as reproducible evidence.

# References and dependency map

\[CDRS\] B. Collas, M. Dettweiler, S. Reiter, and W. Sawin, "Monodromy of elliptic curve convolution, seven-point sheaves of $G_2$-type and motives of Beauville type," *Journal fuer die reine und angewandte Mathematik* 784 (2022), 1--26. DOI: 10.1515/crelle-2021-0070. Public version: <https://arxiv.org/abs/1803.05883v2>. Numbering used here is from that version: Proposition 1.2.2 (the semisimple property-P convolution category), Lemma 1.2.4 (generic-rank formula), Lemma 1.2.5 (finite objects), and the argument of Lemma 1.2.6 (translation self-twists and the connected component). Only these algebraic statements, not the subsequent complex-analytic discussion, are used over finite fields.

\[Deligne\] P. Deligne, "La conjecture de Weil. II," *Publications Mathematiques de l'IHES* 52 (1980), 137--252. DOI: 10.1007/BF02684780. Public text: <https://www.numdam.org/item/PMIHES>\_1980\_\_52\_\_137_0/. The purity and weight estimates used in Sections 4--10 are standard inputs; no new general purity theorem is asserted.

\[FFK\] A. Forey, J. Fresan, and E. Kowalski, *Arithmetic Fourier transforms over finite fields: generic vanishing, convolution, and equidistribution*, arXiv:2109.11961v6, 8 September 2025. Public version: <https://arxiv.org/abs/2109.11961v6>. Chapters 3--4 supply the general Tannakian and equidistribution context. The explicit moment proof in Section 7 treats the arithmetic component directly rather than invoking equidistribution from a connected-group identification alone.

\[Milne\] J. S. Milne, *Elliptic Curves*, second edition, World Scientific, 2021. Public author version: <https://www.jmilne.org/math/Books/EC2.pdf>. Used for finite-field elliptic curves, divisors, coverings, and the classical curve Weil bound in the explicit-cover arguments.

\[SEC2\] Certicom Research, *SEC 2: Recommended Elliptic Curve Domain Parameters*, version 2.0, 27 January 2010, Section 2.4.1. <https://www.secg.org/sec2-v2.pdf>. The secp256k1 parameters provide a motivating example, not an additional hypothesis of the general theorem.

\[Sutherland\] A. V. Sutherland, *18.783 Elliptic Curves, Lecture 7: Point Counting*, MIT (2022), Theorem 7.3; Hasse's theorem and the quadratic-character point-count formula. <https://math.mit.edu/classes/18.783/2022/LectureNotes7.pdf>.

\[Companion 06\] *Technical evidence for the quaternionic elliptic Fourier model*, public AI-developed mathematical research artifact, 2 November 2026. Detailed proposed projector, Frobenius bookkeeping, checks, and limitations; independent proof certification not claimed.

\[Companion 07\] *Exact elliptic Frobenius traces for ordinate-character autocorrelation*, public AI-developed mathematical research artifact, 2 November 2026. The standalone proposed proof of (9.2), its cubic models, and its finite Fourier consequences.
