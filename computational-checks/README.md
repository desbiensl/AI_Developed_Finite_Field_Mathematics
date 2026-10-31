# Reproducible arithmetic, algebraic and small-field checks

This folder contains the **seven original assertion-based Python programs**, their input certificates, archived run outputs, and five machine-readable result reports. All required program dependencies beyond the declared Python packages and inputs are included here. The original scripts and associated result files are preserved without mathematical changes; separate rerun records are provided in `../reproducibility/RERUN_REPORT.json`. No unpublished handoff or internal archive is needed to run the checks.

## Interpreter and packages

The release rerun succeeded with **Python 3.13.5**, **SymPy 1.14.0**, and **NumPy 2.3.5**. Python 3.13 is recommended to reproduce these exact versions. A virtual environment is optional.

```sh
python --version
python -m pip install -r requirements.txt
```

All checks deliberately use `assert`. **Do not run Python with `-O`, `-OO`, or `PYTHONOPTIMIZE` enabled**; optimization can remove the assertions and produce misleading PASS output. No internet access is needed when the packages are already installed. The programs do not request private keys.

## Run the programs

Run these commands in the `checks/` directory:

```sh
python verify_prime_certificate.py
python verify_cm_eds.py
python verify_osculation.py --output validation_results.json
python verify_mumford.py
python check_finite_algebra.py
python verify_small_fourier.py
python verify_revision_identities.py
```

When rerunning, the programs overwrite the five result JSON files in the current directory. **Use a copy of `checks/` if you want to keep archived outputs byte-for-byte unchanged.** The paper texts are not edited by these programs.

## Input and output mapping

| Script | Input beyond Python script | Archived machine-readable output |
| --- | --- | --- |
| `verify_prime_certificate.py` | `prime_certificate.json` | Console PASS; `prime_certificate_run.txt` |
| `verify_cm_eds.py` | `prime_certificate.json` and imported certificate checker; SymPy | `cm_eds_results.json` |
| `verify_osculation.py` | Standard library | `validation_results.json` |
| `verify_mumford.py` | Imports helpers from `verify_osculation.py` | `mumford_results.json` |
| `check_finite_algebra.py` | SymPy | Console PASS; `finite_algebra_run.txt` |
| `verify_small_fourier.py` | NumPy and helper from `verify_osculation.py` | `small_fourier_results.json` |
| `verify_revision_identities.py` | NumPy and SymPy | `revision_identity_results.json` |

The archived `*_run.txt` files record the earlier console outputs. The independent rerun logs are stored at `../reproducibility/rerun_logs/`. The newer rerun compared all five generated JSON reports byte-for-byte against the archives and recorded the results in `../reproducibility/RERUN_REPORT.json`.

## Interpretation

A successful script run is **not** a mathematical proof assistant verification and does not test the entirety of the published arguments. It checks the precise hard-coded models, values, and symbolic expressions in the source. The Fourier transform and covariance assertions use floating-point numerical tolerances; the program records the tolerance in each case. Curve enumeration, modular arithmetic, polynomial congruences and correlation dot products operate on exact integers (with intermediate symbolic expressions handled by SymPy).

For the exact relationship to numbered propositions and theorems in the five papers, read `../VERIFICATION.md`. That document explicitly distinguishes arithmetic checks from unverified geometric hypotheses and asymptotic claims.

## License and archive status

These codes are presented as a research supplement. **No software license is inferred or granted in this packaging step.** The human curator should select explicit reuse terms before public distribution. The five documents are public AI-developed research artifacts awaiting independent specialist verification.

## Software license

The seven Python verification scripts are available under the **MIT License**; see [`LICENSE`](LICENSE). Their successful execution does not certify the mathematical theorems.
