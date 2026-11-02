.PHONY: pdf check clean
pdf:
	mkdir -p build
	latexmk -lualatex -interaction=nonstopmode -halt-on-error -outdir=build main.tex
check: pdf
	@! grep -Eq 'Overfull \\hbox|Overfull \\vbox|undefined references|Missing character' build/main.log
	@pdfinfo build/main.pdf | grep -E '^Pages:'
clean:
	latexmk -C -outdir=build main.tex
