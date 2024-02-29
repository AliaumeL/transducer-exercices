.PHONY: watch website clean

LOGOS= static/logo/apple-touch-icon.png \
	   static/logo/favicon-16x16.png \
	   static/logo/favicon-32x32.png \
	   static/logo/logo.png

BUILD_ENV=templates/exercice.tex \
		  templates/website.html \
		  filters/exercice_split.py \
		  filters/knowledge.py \
		  filters/remove_exercices.lua \
		  static/css/styles.css \
		  static/css/styles-index.css 

PANDOC_HTML_OPTS= --lua-filter filters/remove_exercices.lua \
				  -F filters/exercice_split.py \
				  -F filters/knowledge.py \
				  --mathjax \
				  --standalone \
				  --bibliography=static/bibtex/papers.bib \
				  --citeproc \
				  -t html5 \
				  --metadata=live-reload:$(PANDOC_LIVE_RELOAD) \
				  --section-divs \
				  --template=templates/website.html \
				  --metadata-file=metadata.yaml 

PANDOC_TEX_OPTS= --lua-filter filters/remove_exercices.lua \
		         -F filters/exercice_split.py \
		         -F filters/knowledge.py \
				 --bibliography=static/bibtex/papers.bib \
				 --biblatex \
		         --number-sections \
		         --template=templates/exercice.tex \
				 --metadata-file=metadata.yaml \
		         -t latex

static/logo/apple-touch-icon.png: static/logo/logo.svg
	inkscape --export-background-opacity=0 \
             --export-width=180 \
             --export-type=png \
    		 --export-filename=$@ \
			 $<

static/logo/favicon-16x16.png: static/logo/logo.svg
	inkscape --export-background-opacity=0 \
             --export-width=16 \
             --export-type=png \
    		 --export-filename=$@ \
			 $<

static/logo/favicon-32x32.png: static/logo/logo.svg
	inkscape --export-background-opacity=0 \
             --export-width=32 \
             --export-type=png \
    		 --export-filename=$@ \
			 $<

static/logo/logo.png: static/logo/logo.svg
	inkscape --export-background-opacity=0 \
             --export-width=512 \
             --export-type=png \
    		 --export-filename=$@ \
			 $<


site/%.html: content/%.md metadata.yaml $(BUILD_ENV)
	mkdir -p site
	pandoc $(PANDOC_HTML_OPTS) \
		   --number-sections \
		   --shift-heading-level-by=1 \
		   -o $@ $<

site/index.html: index.md metadata.yaml $(BUILD_ENV)
	mkdir -p site
	pandoc $(PANDOC_HTML_OPTS) \
		   --metadata=main-page:true \
		   -o $@ $<

website: $(LOGOS) $(patsubst content/%.md,site/%.html,$(wildcard content/*.md)) site/index.html
	mkdir -p site/static
	cp -r static/* site/static/

pdfs: $(patsubst content/%.md,latex/%.pdf,$(wildcard content/*.md))
	mv *.pdf latex/

latex/%.tex: content/%.md $(BUILD_ENV)
	mkdir -p latex
	pandoc $(PANDOC_TEX_OPTS) -s -o $@ $<

latex/%.pdf: latex/%.tex
	latexmk -pdf -xelatex $<

watch: export PANDOC_LIVE_RELOAD=1
watch:
	find . -name "*.md" | entr -s "make website && echo reload" | websocat -s 8080

clean:
	latexmk -C *.pdf
