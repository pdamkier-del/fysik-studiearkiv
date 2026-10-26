SHELL := /bin/bash
export TEXMFVAR := $(CURDIR)/build/.cache/texmf-var
export TEXMFCONFIG := $(CURDIR)/build/.cache/texmf-config
export XDG_CACHE_HOME := $(CURDIR)/build/.cache
.PHONY: pdf check clean templates statistik
pdf:
	mkdir -p build/matematik
	latexmk -lualatex -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build/matematik 00-matematik/main.tex
check: pdf
	python3 scripts/check_pdf.py build/matematik/main.pdf build/matematik/main.log
templates:
	@set -e; for subject in 0[1-5]-*; do for kind in formelsamling udledningsnoter opgavenoter opgavesamling; do mkdir -p "build/$$subject/$$kind"; latexmk -lualatex -interaction=nonstopmode -halt-on-error -file-line-error -outdir="build/$$subject/$$kind" "$$subject/$$kind/main.tex" > "build/$$subject/$$kind/console.log" 2>&1 || { cat "build/$$subject/$$kind/console.log"; exit 1; }; done; done
statistik:
	mkdir -p build/statistik
	latexmk -lualatex -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build/statistik 06-statistik/main.tex
clean:
	rm -rf build
