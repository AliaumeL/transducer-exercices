.PHONY: watch

BUILD_ENV=templates/exercice.tex filters/exercice_split.py

%.tex: %.md $(BUILD_ENV)
	pandoc \
		   --lua-filter filters/remove_exercices.lua \
		   -F filters/exercice_split.py \
		   -F filters/knowledge.py \
		   --number-sections \
		   --template=templates/exercice.tex \
		   -t latex \
		   -s -o $@ $<

%.pdf: %.tex
	latexmk -pdf -xelatex $<

%.html: %.md
	pandoc --number-sections \
		   -F filters/knowledge.py \
		   --mathjax \
		-s -o $@ $<

watch:
	ls exercices.md | entr -s "make exercices.html && echo reload" | websocat -s 8080

clean:
	latexmk -C exercices.pdf
