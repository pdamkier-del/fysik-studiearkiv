SHELL := /bin/bash
export TEXMFVAR := $(CURDIR)/build/.cache/texmf-var
export TEXMFCONFIG := $(CURDIR)/build/.cache/texmf-config
export XDG_CACHE_HOME := $(CURDIR)/build/.cache
.PHONY: pdf check clean templates statistik publication-check repository-check
pdf:
	mkdir -p build/00-matematik
	latexmk -lualatex -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build/00-matematik 00-matematik/main.tex
check: pdf
	python3 scripts/check_pdf.py build/00-matematik/main.pdf build/00-matematik/main.log
templates:
	python3 scripts/build_templates.py
statistik:
	mkdir -p build/02-fysikbibliotek/statistik
	latexmk -lualatex -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build/02-fysikbibliotek/statistik 02-fysikbibliotek/statistik/main.tex
publication-check: check statistik
	python3 scripts/check_repository.py
	python3 scripts/validate_publication.py
	python3 -m unittest discover -s tests -v
	python3 scripts/check_publication_plan.py
repository-check:
	python3 scripts/check_repository.py
clean:
	rm -rf build
