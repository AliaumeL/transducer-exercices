.PHONY: watch

%.pdf: %.tex
	latexmk -pdf $<

%.tex: %.md
	pandoc -s -o $@ $<

%.html: %.md
	pandoc -s -o $@ $<

watch:
	ls -d *.md | entr make
