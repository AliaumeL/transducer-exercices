.PHONY: watch website

BUILD_ENV=templates/exercice.tex \
		  filters/exercice_split.py \
		  filters/knowledge.py \
		  filters/pandoc.css \
		  filters/remove_exercices.lua

site/index.html: index.md
	mkdir -p site
	pandoc --standalone \
		   --mathjax \
		   --number-sections \
		   --section-divs \
		   -t html5 \
		   -o $@ $<

website: site/index.html
	mkdir -p site



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
	pandoc \
		   --lua-filter filters/remove_exercices.lua \
		   -F filters/exercice_split.py \
		   -F filters/knowledge.py \
		   --mathjax \
		   --standalone \
		   -t html5 \
		   --number-sections \
		   -c templates/pandoc.css \
		   -o $@ $<

watch:
	ls *.md | entr -s "make *.html && echo reload" | websocat -s 8080

clean:
	latexmk -C *.pdf
