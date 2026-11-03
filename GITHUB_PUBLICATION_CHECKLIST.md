# GitHub publication checklist

The files in this folder are intended as **public AI-developed research artifacts, not established mathematical preprints**.

Before making the repository public (manuscript edition date: **31 October 2026**):

- [x] Include all five LaTeX sources as the canonical editable mathematical editions alongside the PDFs.
- [x] Set the manuscript edition date to 31 October 2026, consistently in LaTeX, Word and Markdown.
- [ ] Upload the **extracted directories and files**, not merely the ZIP archive. Preserve the relative paths so README links work.
- [ ] Create a GitHub release or tag after upload, if desired. Do not confuse the 31 October manuscript edition date with the actual date the repository becomes public.


- [ ] Confirm that the public use of the curator's real name is intentional; it appears in the PDF and Word metadata, first-page attribution and repository documentation.
- [x] Apply CC BY 4.0 to the five manuscript editions and documentation, and MIT to the verification code; see `LICENSE`, `computational-checks/LICENSE` and `LICENSING.md`.
- [ ] Review the stated absence of institutional affiliations, institutional resources, external funding and competing interests for continued accuracy.
- [ ] Review `README.md`, `PROVENANCE.md` and `VERIFICATION.md` for a good-faith account of the human-AI process and pending mathematical proof audit.
- [ ] Inspect the PDF and LaTeX sources, including bibliographies and formula rendering; these were machine-typeset and may require reader-side final edits.
- [ ] Check whether a publicly visible Git commit name/email or GitHub profile reveals information you do not wish to disclose.
- [ ] If an independent mathematician later evaluates any result, add a dated review entry to `VERIFICATION.md` with the claim's scope and remaining assumptions.

There is no requirement to wait for a specialist before sharing *accurately labeled unverified artifacts* on a general-purpose public code hosting repository, but a disclaimer does not remove the responsibilities associated with distributing research materials. The existing code checks are not a substitute for independent proof review.

Do **not** upload chat histories, unreleased handoff notes, editor backups,
TeX `.aux`/`.log` intermediates or private files. Check `git status`, the
staged changes and Git commit author email before pushing. The source
package contains no personal correspondence email in the manuscript title
blocks, but the curator's name is intentionally public.

## Updating from the 31 October collection to the 2 November edition

Extract the small update overlay and copy its files into the **same paths** in the GitHub repository. In particular, replace `LaTeX/04_Quaternionic_Elliptic_Fourier.tex`, `PDF/04_Quaternionic_Elliptic_Fourier.pdf`, `Word/04_Quaternionic_Elliptic_Fourier.docx`, and `Markdown/04_Quaternionic_Elliptic_Fourier.md`. Add the matching 06/07 files, three additional `computational-checks/` programs, their archived results, and the updated root documentation. Do not upload intermediate TeX compilation files or private chat transcripts. Alternatively, use the complete seven-manuscript ZIP to initialize a fresh repository. No GitHub repository was modified by preparing this ZIP.
