LATEXMK = latexmk
TEXFLAGS = -lualatex -interaction=nonstopmode -halt-on-error -file-line-error -output-directory=build

.PHONY: all clean article-01 article-02 article-03 article-04 article-05 article-06 article-07

all: article-01 article-02 article-03 article-04 article-05 article-06 article-07

article-01:
	mkdir -p build
	$(LATEXMK) $(TEXFLAGS) LaTeX/01_Osculation_and_Divisor_Reduction.tex

article-02:
	mkdir -p build
	$(LATEXMK) $(TEXFLAGS) LaTeX/02_Primitive_CM_Dynamics_and_Rigidity.tex

article-03:
	mkdir -p build
	$(LATEXMK) $(TEXFLAGS) LaTeX/03_EDS_Kummer_and_Cyclic_Sequences.tex

article-04:
	mkdir -p build
	$(LATEXMK) $(TEXFLAGS) LaTeX/04_Quaternionic_Elliptic_Fourier.tex

article-05:
	mkdir -p build
	$(LATEXMK) $(TEXFLAGS) LaTeX/05_Symmetry_Constraints_on_Scalar_Observables.tex


article-06:
	mkdir -p build
	$(LATEXMK) $(TEXFLAGS) LaTeX/06_Quaternionic_Fourier_Technical_Evidence.tex

article-07:
	mkdir -p build
	$(LATEXMK) $(TEXFLAGS) LaTeX/07_Exact_Elliptic_Autocorrelation_Trace_Identity.tex

clean:
	rm -rf build
