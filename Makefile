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

# Seks matematikbind. Kildekapitlerne deles med den samlede PDF.
BIND_NUMRE := 1 2 3 4 5 6
.PHONY: bind-1 bind-2 bind-3 bind-4 bind-5 bind-6 alle-bind
alle-bind: $(addprefix bind-,$(BIND_NUMRE))
$(addprefix bind-,$(BIND_NUMRE)): bind-%:
	mkdir -p build/00-matematik/bind-$*
	latexmk -lualatex -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build/00-matematik/bind-$* 00-matematik/volumes/bind-$*.tex
	python3 scripts/check_pdf.py build/00-matematik/bind-$*/bind-$*.pdf build/00-matematik/bind-$*/bind-$*.log
