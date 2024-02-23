.PHONY: watch

%.pdf: %.tex
	latexmk -pdf $<

%.tex: %.md
	pandoc -s -o $@ $<

%.html: %.md
	pandoc --number-sections -s -o $@ $<

watch:
	ls exercices.md | entr -s "make exercices.html && echo reload" | websocat -s 8080
