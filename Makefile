.PHONY: watch website clean

BUILD_ENV=templates/exercice.tex \
		  templates/website.html \
		  filters/exercice_split.py \
		  filters/knowledge.py \
		  filters/remove_exercices.lua \
		  static/css/styles.css \
		  static/css/styles-index.css 

site/%.html: %.md metadata.yaml $(BUILD_ENV)
	mkdir -p site
	pandoc \
		   --lua-filter filters/remove_exercices.lua \
		   -F filters/exercice_split.py \
		   -F filters/knowledge.py \
		   --mathjax \
		   --standalone \
		   -t html5 \
		   --number-sections \
		   --section-divs \
		   --template=templates/website.html \
		   --metadata-file=metadata.yaml \
		   -o $@ $<

website: $(patsubst %.md,site/%.html,$(wildcard *.md))
	mkdir -p site/static
	cp -r static/* site/static/



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


watch:
	ls *.md | entr -s "make *.html && echo reload" | websocat -s 8080

clean:
	latexmk -C *.pdf
