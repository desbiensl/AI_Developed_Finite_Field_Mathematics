# Explorations in finite-field mathematics

### Public AI-developed research manuscripts awaiting independent verification

**Publication classification:** public mathematical research artifacts, **not** independently validated scholarly preprints.  
**Human initiator and curator:** Louis Desbiens.  
**AI mathematical research contributor:** OpenAI's ChatGPT.  
**Affiliation:** none claimed; no institutional endorsement.  
**Manuscript edition date:** 31 October 2026 (prepared for public release).  
**Reuse licenses:** CC BY 4.0 for manuscripts and documentation; MIT for the Python verification scripts.

> **Verification notice.** The documents contain candidate mathematical contributions and proposed proofs generated in a human-directed, substantially AI-developed investigation. No independent specialist audit, complete proof-assistant verification, or exhaustive novelty review has been performed. Finite computational checks cover selected identities and models only. The results could be correct, partly correct, incomplete, or incorrect. Public availability is an invitation to examine, correct and develop the material, **not** a certification of the mathematics.

The human curator organized and released the investigation but does not claim the expertise to independently certify the advanced proofs. The AI is identified as a mathematical contributor, not an accountable scholarly coauthor. See [PROVENANCE.md](PROVENANCE.md) for the development process, [VERIFICATION.md](VERIFICATION.md) for a claim-level coverage map, and [CITATION.md](CITATION.md) for attribution guidance. No private notes, chat transcripts or unpublished handoffs are needed as references for the manuscripts.

## The five manuscripts

| No. | Mathematical topic | Read | Sources | Word | Editable Markdown |
| --- | --- | --- | --- | --- | --- |
| 01 | Polynomial and rational osculation | [PDF](PDF/01_Osculation_and_Divisor_Reduction.pdf) | [LaTeX](LaTeX/01_Osculation_and_Divisor_Reduction.tex) | [Word](Word/01_Osculation_and_Divisor_Reduction.docx) | [Markdown](Markdown/01_Osculation_and_Divisor_Reduction.md) |
| 02 | Primitive norm-three CM dynamics | [PDF](PDF/02_Primitive_CM_Dynamics_and_Rigidity.pdf) | [LaTeX](LaTeX/02_Primitive_CM_Dynamics_and_Rigidity.tex) | [Word](Word/02_Primitive_CM_Dynamics_and_Rigidity.docx) | [Markdown](Markdown/02_Primitive_CM_Dynamics_and_Rigidity.md) |
| 03 | Division-polynomial covariance and Kummer sequences | [PDF](PDF/03_EDS_Kummer_and_Cyclic_Sequences.pdf) | [LaTeX](LaTeX/03_EDS_Kummer_and_Cyclic_Sequences.tex) | [Word](Word/03_EDS_Kummer_and_Cyclic_Sequences.docx) | [Markdown](Markdown/03_EDS_Kummer_and_Cyclic_Sequences.md) |
| 04 | Quaternionic Fourier transforms and semicircle laws | [PDF](PDF/04_Quaternionic_Elliptic_Fourier.pdf) | [LaTeX](LaTeX/04_Quaternionic_Elliptic_Fourier.tex) | [Word](Word/04_Quaternionic_Elliptic_Fourier.docx) | [Markdown](Markdown/04_Quaternionic_Elliptic_Fourier.md) |
| 05 | Symmetry constraints on scalar observables | [PDF](PDF/05_Symmetry_Constraints_on_Scalar_Observables.pdf) | [LaTeX](LaTeX/05_Symmetry_Constraints_on_Scalar_Observables.tex) | [Word](Word/05_Symmetry_Constraints_on_Scalar_Observables.docx) | [Markdown](Markdown/05_Symmetry_Constraints_on_Scalar_Observables.md) |

The text and equation detail have been retained while the publication framing, attribution and claim labels have been revised. The print editions use black-and-white A4 LaTeX with Latin Modern Roman and Latin Modern Math. Word copies are supplementary editable formats; the LaTeX source is the canonical typesetting source for each public PDF.

## Scope, status and limitations

* **Classical mathematical results** cited from published sources are distinguished from newly proposed deductions. Citation alone does not certify that a new application of an existing theorem is sound.
* **Proposed mathematical contributions** are statements and arguments available for expert evaluation; labels like *Proposed Theorem* do not imply peer review.
* **Computational checks** are reproducible finite or symbolic tests on specified inputs. They are not proofs of general statements or independent mathematical audits.
* **Cryptography:** this collection contains **no verified improvement** on elliptic-curve discrete-logarithm algorithms and no general hardness or security theorem.

The most demanding outstanding dependencies are the Kummer/geometric independence arguments in Manuscript III and the convolution, arithmetic monodromy, purity and moment steps in Manuscript IV. See [VERIFICATION.md](VERIFICATION.md).

## Reproducing the PDFs

Install a TeX distribution with LuaLaTeX, latexmk, Latin Modern, unicode-math and the standard packages referenced by the sources. Run:

```sh
make all
```

Generated PDFs appear in `build/` and may be compared with the `PDF/` snapshots. The
`build/` directory contains temporary compilation outputs and is ignored by Git.
**Publish the `LaTeX/` sources with the PDFs:** they are the canonical editable
versions for reproducibility, correction and pull requests. The supplied
`Word/` and `Markdown/` companions are optional for GitHub but included in
this small release archive. The `PDF/` files are versioned reading copies. To change one manuscript, edit the corresponding `LaTeX/*.tex` file and rebuild. Markdown and Word are convenience editions and are not automatically synchronized by the Makefile.

## Reproducing finite checks

See [computational-checks/README.md](computational-checks/README.md). Use Python with NumPy and SymPy dependencies in `computational-checks/requirements.txt`; assertions must remain enabled. The suite contains seven original scripts. For example:

```sh
cd computational-checks
python -m pip install -r requirements.txt
python verify_prime_certificate.py
python verify_cm_eds.py
python verify_osculation.py --output validation_results.json
python verify_mumford.py
python check_finite_algebra.py
python verify_small_fourier.py
python verify_revision_identities.py
```

Running the tests overwrites some archived JSON results; work on a copy if preservation matters. Success means specified assertions passed, not that the manuscript proofs were certified. Recorded output and provenance appear in `reproducibility/`.

## Independent mathematical review

Specific verification questions, underlying hypotheses and unverified steps are documented in [VERIFICATION.md](VERIFICATION.md). Researchers may cite the public artifact as an unverified proposal and are invited to submit documented corrections or independent proof assessments. [CONTRIBUTING.md](CONTRIBUTING.md) describes the suggested reporting format; no curator commitment to ongoing technical correspondence is implied.

## Reuse permissions and release responsibility

The five manuscripts (`LaTeX/`, `PDF/`, `Markdown/`, `Word/`) and repository
prose documentation are made available under **CC BY 4.0**, to the extent that
relevant rights are held. The Python verification programs and root Makefile
are distributed under the **MIT License**. The full CC BY legal code is in
[`LICENSE`](LICENSE); the MIT text is in
[`computational-checks/LICENSE`](computational-checks/LICENSE). See
[LICENSING.md](LICENSING.md) for precise scope, required attribution and
third-party caveats. Granting reuse permissions neither certifies the proposed
mathematics nor removes ordinary responsibility for an accurate release.
