# Verification register: five AI-developed mathematical research artifacts

**Interpretation:** this is a status register, not a proof of correctness. No claimed new theorem has been independently certified by a qualified specialist. Formal verification in Lean or a comparable proof assistant has not been performed. Conventional published background results are cited in the manuscripts but their application to new deductions has not been independently reviewed.

| ID | Central candidate contribution | Available evidence in this repository | Independent status | Priority for mathematical review |
| --- | --- | --- | --- | --- |
| 01 | Residual-divisor/group-sum identities, explicit osculation, genus-one reduction, rational-contact norm | `verify_osculation.py`, `verify_mumford.py` on finite inputs | **Unreviewed candidate deductions**; classical divisor inputs cited | Multiplicities, non-split divisors, global Riemann--Roch hypotheses |
| 02 | secp256k1 primitive norm-three scalar, quotient dynamics, degree and rigidity deductions | Recursive prime certificate and `verify_cm_eds.py` on selected inputs | **Exact finite certificates available; general deductions unreviewed** | Rational-map degree model; classical rigidity hypotheses and scope |
| 03 | Kummer covariance, branch-layer independence, 78-position recurrence and 39-word bounds, quotient/isogeny geometry | Character and integer threshold calculations; `verify_revision_identities.py` | **Unreviewed candidate geometric proofs** | Kummer character-sum inputs; conductor and geometric independence; descent |
| 04 | Uniform elliptic Fourier envelope, full quaternionic convolution group, moment estimate, semicircle limit, autocorrelation | Finite quaternion matrices and small-field Fourier tests | **Unreviewed candidate geometric and asymptotic proofs** | Cover linearization, convolution duality, arithmetic Frobenius, purity and moment bounds |
| 05 | Negation-invariant parity obstruction, normalized division-polynomial identity, symmetry-aware surrogate covariance and limit | Finite normalization, covariance and Fourier tests | **Elementary arguments supplied; no independent expert verification** | Normalization conventions; probabilistic assumptions and interpretation |

## How evidence is classified

| Evidence level | Meaning | Present in this release? |
| --- | --- | --- |
| Public classical source | A theorem or definition in cited external mathematics literature | Yes; manuscript bibliographies |
| Human-independent specialist proof review | A qualified mathematician independently checks a new argument and its hypotheses | **No** |
| Machine-checked proof | Kernel-verified derivation without unproved candidate-claim axioms | **No** |
| Exact finite computation | Reproducible checks of specific integers and finite-field instances | Yes, within documented bounds |
| Symbolic algebra check | Symbolic identity on programmed expressions | Yes, within documented hypotheses |
| Floating-point Fourier evaluation | Numerically tests sampled transform values with tolerances | Yes, within sampled models only |
| Priority / novelty audit | Comprehensive search to establish originality | **No** |

## Detailed program-to-claim coverage

The comprehensive table below updates the earlier validation coverage, using each paper's section or claim number (the word *Proposed* was added to new theorem/corollary labels). A passing check does not validate the assumptions of a geometric proof.



This coverage map references the **numbered statements and headings in the manuscripts**, not PDF page numbers (which may change on re-typesetting). A check being listed next to a result does **not** mean that the result, in its full generality, has been proved by code.

- **Exact, parameter-specific arithmetic:** an executable assertion on named integers or a fixed finite-field instance; results are exact for those inputs. It is still necessary to audit the implementation and assumptions.
- **Symbolic consistency:** a finite algebraic identity checked by SymPy on an explicitly given representation. It does not establish the existence or geometric properties of the underlying abstract objects.
- **Finite sample or enumeration:** evaluations on the explicitly programmed point sets. Even if the enumeration is exhaustive on those small curves, it is not a universal proof.
- **Numerical Fourier check:** floating-point comparisons with the explicit program tolerance; not exact algebraic certification of complex-valued transforms.
- **Uncovered:** no specific program establishes this statement. A proof may be written in the manuscript or cited from public literature, but that proof has not been mechanically or independently audited by the seven scripts.

All the archived programs are **Python assertion-based validation**, not Lean or another proof assistant. The programs also share some implementation components; their successful execution does not make their error models independent. No script recovers an unknown discrete logarithm or establishes an ECDLP complexity improvement.

## Cross-reference: programs and where they apply

| Existing program (preserved unchanged) | Direct computational scope | Articles |
| --- | --- | --- |
| `verify_prime_certificate.py` | Recursive Lucas primality certification for **46 certificate records** from `prime_certificate.json` | II, III |
| `verify_cm_eds.py` | Exact secp256k1 CM and EDS-related calculations; primitive order, rational quotient on **35 known scalar inputs**, cubic identities, and integer threshold inequalities | II, III, V (selected sixfold identities) |
| `verify_osculation.py` | Local-coefficient and residual tests on **4,416 small-field points** and **67 known secp256k1 multiples** | I |
| `verify_mumford.py` | Genus-one reduction on **2,852 small-field cases** and **391 secp256k1 cases** | I |
| `check_finite_algebra.py` | Two-torsion translation identity; 2x2 quaternion matrices, coset traces, extension-phase traces and finite symmetric-power rank formulas | IV |
| `verify_small_fourier.py` | Fourier and autocorrelation evaluations over **152 selected prime-order curve models**, **3,262 coefficients**, **3,110 nonzero-shift autocorrelations** | IV, V (finite examples only) |
| `verify_revision_identities.py` | **27 exact normalization cases**, **nine Ward-recurrence cases**, three symbolic quotient identities, and covariance on five cyclic group orders | III, V |

The five machine-readable results in `computational-checks/` are the **archived outputs**, not extrapolations. New run logs and a separate reproducibility report are in `reproducibility/`. For precise model choices, field restrictions, and index ranges, consult the scripts.

## Article I — Polynomial and rational osculation on elliptic curves

| Manuscript claim | Executed check | Boundary of verification |
| --- | --- | --- |
| Lemma 2.1, formal coefficient recurrence | `verify_osculation.py` computes local coefficients by the stated recursion on its enumerated points | Not a universal formal-power-series proof over every eligible field |
| Proposed Theorem 3.1, contact polynomial, degree and coordinate-trace identities | `verify_osculation.py` checks contact orders, residual coefficients, and Vieta traces for nonzero leading coefficients on enumerated points | Divisor-theoretic proof and arbitrary non-split residual divisors are not verified; **group sums are checked directly only when residual polynomials split** over the tested base field |
| Proposed Theorem 3.1, elliptic group sum of residual divisor | `verify_osculation.py` checks 7,442 split-divisor sums in the small-field cases | Does not test general non-split divisors, multiplicity statements in arbitrary extensions, or a general Picard-group argument |
| Lemma 4.1, low-order torsion exceptions, and tripling/quadrupling formulas | `verify_osculation.py` checks the exceptional cases and group-law formulas at enumerated points | Exact finite-input consistency, not a proof for all elliptic curves |
| Section 4.3, finite-field counterexample to coordinate-trace substitution | The program records explicit small-field examples and directly checks the relevant identities | Independently inspect the cited printed counterexample against the program's examples; program output is not a manuscript parsing check |
| Proposition 5.1, genus-one Mumford reduction | `verify_mumford.py` checks 3,243 reductions and compares results with the elliptic group law | Does not formally verify the general semireduced divisor algorithm or all exceptional extensions |
| Proposed Theorem 6.1 and Proposed Corollary 6.2, Riemann--Roch rational contact | `verify_osculation.py` includes rational-contact systems and torsion/denominator cases on the selected inputs | General Riemann--Roch existence, uniqueness, norm pushforward, and all exceptional hypotheses remain mathematical arguments, not software-certified theorems |
| Section 7, impossibility of extracting an unknown scalar from these identities | No runtime or complexity theorem is checked by these scripts | The software deliberately evaluates multiples with known scalars |

## Article II — Primitive norm-three CM dynamics on secp256k1

| Manuscript claim | Executed check | Boundary of verification |
| --- | --- | --- |
| Proposition 2.1, norm-three endomorphism and CM scalar action | `verify_cm_eds.py` verifies CM identities and 35 pointwise actions | Does not independently formalize the general endomorphism-ring arguments |
| Proposition 2.2, primitive order of the chosen secp256k1 scalar | `verify_prime_certificate.py` validates 46 recursive prime records; `verify_cm_eds.py` checks the factorization of `n-1`, power tests for `h`, and modular field parameters | These are exact computational certificates for the **specific constants**; not a proof of any general primitive-order phenomenon |
| Proposition 3.1, sixfold quotient orbit invariant | `verify_cm_eds.py` checks cube-of-abscissa invariance across its known-scalar tests | Completeness and freeness for every rational subgroup point rely on the manuscript's group argument |
| Theorem 3.2, quotient formula and the relation to tripling | `verify_cm_eds.py` checks the quotient formula and functional-square identity at 35 selected points | The generic identity as a rational function and the whole quotient-cycle statement are not independently machine-proved here; the cycle also uses the exact order certificate |
| Corollary 4.1, orbit-index reformulation | Primitive-order arithmetic supports the group-theoretic setup | No method to solve the orbit-index problem faster is demonstrated |
| Proposed Theorem 6.1, finite-set degree obstruction | No dedicated formal-degree proof program | The theorem's polynomial root-count reasoning must be audited from the manuscript |
| Theorem 7.1 and Corollary 7.2, rigidity and hidden-scalar action | No algebraic-geometric verification program | Classical structural theorems are cited in the paper; no runtime lower bound follows |
| Proposition 10.1 and Proposition 10.2, commuting CM maps / conditional correspondences | Pointwise CM checks are consistent with a special commuting map | General families and the geometric correspondence result are not program-verified |
| Section 9, embedding-degree and field-of-definition arithmetic | `verify_cm_eds.py` checks exact modular exponent and order conditions | Does not prove a general pairing impossibility or ECDLP hardness |

## Article III — Division-polynomial covariance and Kummer sequences on secp256k1

| Manuscript claim | Executed check | Boundary of verification |
| --- | --- | --- |
| Propositions 2.1 and 3.1, covariance target and divisor restrictions | `verify_cm_eds.py` checks selected `psi_3` character-covariance identities on 35 known points | Does not verify the general divisor equalities or arbitrary candidate functions |
| Proposition 4.1, single division-polynomial obstruction | No general single-factor obstruction checker | The statement relies on the paper's character/divisor reasoning |
| Lemma 4.2, Kummer character-sum input; Theorem 5.1, support obstruction | No numerical checker proves the Weil/Kummer conductor estimate or its hypotheses | Both are mathematical arguments, not inferred from the threshold calculations |
| Proposition 6.1, cubic splitting calculation | `verify_cm_eds.py` checks cubic discriminant, root formula and finite-field irreducibility conditions | Does not prove every geometric or normalization statement |
| Proposition 6.2, positive-index geometric independence | No program certifies the general independent Kummer classes | Do not infer independence solely from successful small-field character evaluations |
| Proposed Theorem 8.1, recurrence exclusion through 78 positions | `verify_cm_eds.py` verifies the **exact integer inequality** at lengths 77, 78 and 79 | Does not verify branch supports, conductor formulas, Kummer independence, or the character-sum proof that supplies the inequality's hypotheses |
| Section 9, every ternary word of length at most 39 | `verify_cm_eds.py` verifies the **sufficient inequality** at 38, 39 and 40 | Does not enumerate all 3^39 words or independently prove the word-count formula |
| Section 10, Kummer towers | No general tower-independence checker | Needs mathematical specialist review |
| Proposition 11.1, four quotient genera / Jacobian decomposition | Some algebraic quotient expressions are symbolically consistent in `verify_revision_identities.py` | Genera, full quotient constructions, and the decomposition are not established by the symbolic identities |
| Proposition 11.2, reciprocal quotient model | `verify_revision_identities.py` validates the displayed rational-function quotient equations; `verify_cm_eds.py` checks selected cubic relations | Field-of-definition and geometric isomorphism statements still require proof review |
| Proposition 11.3, degree-three isogeny | No checker constructs and certifies the stated isogeny or Jacobian splitting | **Not independently checked** by this supplement |
| Appendix A, arithmetic certificate | `verify_prime_certificate.py` and `verify_cm_eds.py` provide exact parameter-specific arithmetic verification | This certificate does not cover the higher-genus geometry |

## Article IV — Quaternionic symmetry and semicircle laws for elliptic Fourier transforms

| Manuscript claim | Executed check | Boundary of verification |
| --- | --- | --- |
| Lemmas 2.1--2.2, two-torsion lifts and quaternionic/Frobenius algebra | `check_finite_algebra.py` checks translation identity, the standard 2x2 quaternion representation, and finite arithmetic-phase trace formulas | Matrix identities do not prove compatibility of sheaf actions, lifts on all covers, or arithmetic descent |
| Proposed Theorem A, uniform Fourier bound | `verify_small_fourier.py` tests the bound on 152 selected prime-order curves (3,262 Fourier coefficients) | Not a proof of the bound for all fields/curves satisfying (1.1); some test models do **not** establish the special CM assumptions of the general theorem |
| Proposed Theorem B, connected convolution group `SL_2` | `check_finite_algebra.py` checks relevant finite representation and rank identities | **No program verifies** the geometric convolution group, translation stabilizer, Tannakian category, or monodromy identification |
| Section 6, arithmetic sign and full group | Finite quaternion/coset calculations test the intended sign patterns | Does not verify Frobenius-stable projectors or arithmetic-component classification |
| Proposed Theorem C, Catalan moments and uniform error | `verify_small_fourier.py` compares even moments 2--12 with the claimed finite-field envelope (floating-point); `check_finite_algebra.py` checks related symmetric-power rank identities | No proof of uniform bounds for arbitrary moments or of the underlying purity/convolution inputs; finite second moments alone cannot establish a semicircle law |
| Proposed Corollary 8.1, semicircle law | No asymptotic theorem is mechanically verified | Sampled finite moments do not prove convergence in distribution |
| Proposed Theorem D, autocorrelation envelope | `verify_small_fourier.py` tests 3,110 nonzero shifts by **exact integer correlation** on selected small curves | Does not verify the full genus-five cover argument or the universal theorem |
| Section 10, extension-field phases | `check_finite_algebra.py` checks finite-factor traces for extension degrees 1--6 | Does not prove the complete extension-field distribution or geometric arguments |
| Sections 11--12, scalar-information consequences | Some simple consequences can be checked arithmetically given an envelope | No cryptanalytic speedup, security proof, or deterministic distribution law follows from these tests |

## Article V — Symmetry constraints on elliptic-curve scalar observables

| Manuscript claim | Executed check | Boundary of verification |
| --- | --- | --- |
| Propositions 2.1--2.2, scalar layers and exact parity-oracle reduction | No specific general-purpose verifier | The reduction is explained mathematically in the paper; no parity oracle is implemented |
| Proposed Theorem 3.1, parity obstruction for negation-invariant features | No dedicated formal enumeration or proof assistant certificate | Elementary pairing proof is in the manuscript; the program suite does not certify it |
| Theorem 5.1, intrinsic division-polynomial normalization | `verify_revision_identities.py` checks **27 exact identities** on selected secp256k1 inputs; nine normalized Ward recurrences are checked | Does not prove the identity for all scalars or points, or certify the intrinsic construction's hypotheses generally |
| Section 6, sixfold scalar symmetry and collision identities | `verify_cm_eds.py` checks sixfold quotient identities at 35 known scalar inputs | Does not provide or benchmark an ECDLP collision attack |
| Section 8, Fourier parity and character symmetry | `verify_small_fourier.py` checks the imaginary/nonzero spectrum on selected prime-order curve models | Does not assert a universal nontrivial Fourier-envelope for arbitrary observables |
| Proposition 9.1, random-sign covariance | `verify_revision_identities.py` computes covariance matrices at group orders 7, 13, 19, 31 and 43; maximum error and the 1e-10 tolerance are recorded | Covariance is a **floating-point** finite-dimensional test, not a proof of the stated general identity |
| Proposition 9.2, surrogate Gaussian marginal limit | No limit theorem is program-verified | The statement concerns an explicitly defined random-sign model, not measured deterministic elliptic-curve predicates |
| Proposition 10.1, consequences of an assumed Fourier envelope | No dedicated program independently proves these conditional inequalities | The envelope is a hypothesis; nothing in this supplement establishes it for arbitrary signals |

## Strong limitations and review priorities

1. **Article IV remains the largest mathematical review priority.** The connected `SL_2` convolution-group statement, arithmetic projector, purity/weight inputs, and extension-field phases need independent specialist examination. A successful numerical bound does not verify these.
2. **Article III's Kummer independence and isogeny claims are not software-verified.** Checking the final 78/39 integer thresholds is not checking their geometric prerequisites.
3. **Article II's rigidity results are not computational runtime lower bounds.** The certificate verifies named integers, not cryptanalytic hardness.
4. **Article I's non-split divisors and global Riemann--Roch statements are not covered by finite point enumeration.**
5. **Article V's general parity and probabilistic statements are not established by numerical curve tests.**
6. **No originality or priority assessment is supplied here.** A successful run does not certify that a claim is new.
7. **No external datasets were needed.** The fixed test points/parameters, models, witnesses and numerical tolerances are encoded in the scripts; recorded results are included in `computational-checks/`.

For reproducibility and archive provenance, see `computational-checks/README.md`, `reproducibility/CHECKS_PROVENANCE.json`, `reproducibility/RERUN_REPORT.json`, and `SHA256SUMS.txt`.
