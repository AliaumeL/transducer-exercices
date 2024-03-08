.PHONY: watch website clean pdfs

LOGOS= static/logo/apple-touch-icon.png \
	   static/logo/favicon-16x16.png \
	   static/logo/favicon-32x32.png \
	   static/logo/logo.png

BUILD_ENV=templates/exercice.tex \
		  templates/website.html \
		  templates/rss-template.xml \
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
				  --metadata=git-revision:$(shell git rev-parse HEAD) \
				  --metadata=git-repository:$(shell git remote get-url origin) \
				  --section-divs \
				  --template=templates/website.html \
				  --metadata-file=metadata.yaml 

PANDOC_TEX_OPTS= --lua-filter filters/remove_exercices.lua \
		         -F filters/exercice_split.py \
		         -F filters/knowledge.py \
				 --bibliography=static/bibtex/papers.bib \
				 --biblatex \
		         --number-sections \
				  --metadata=git-revision:$(shell git rev-parse HEAD) \
				  --metadata=git-repository:$(shell git remote get-url origin) \
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

site/rss/%.xml: content/%.md metadata.yaml $(BUILD_ENV)
	mkdir -p site/rss
	pandoc --template=templates/rss-item-template.xml \
		   --metadata=git-revision:$(shell git rev-parse HEAD) \
		   --metadata=git-repository:$(shell git remote get-url origin) \
		   --metadata-file=metadata.yaml \
		   -t html \
		   -f markdown \
		   -o $@ $<

site/rss.xml: $(pathsubst content/%.md,site/rss/%.xml,$(wildcard content/*.md)) metadata.yaml rss.md $(BUILD_ENV)
	mkdir -p site
	pandoc --template=templates/rss-template.xml \
		   --metadata=git-revision:$(shell git rev-parse HEAD) \
		   --metadata=git-repository:$(shell git remote get-url origin) \
		   --metadata=lastBuildDate:"$(shell date -R)" \
		   --metadata-file=metadata.yaml \
		   -F filters/rss_feed.py \
		   -t html \
		   -o $@ rss.md

site/%.html: content/%.md metadata.yaml $(BUILD_ENV)
	mkdir -p site
	pandoc $(PANDOC_HTML_OPTS) \
		   --number-sections \
		   -o $@ $<

site/index.html: index.md metadata.yaml $(BUILD_ENV)
	mkdir -p site
	pandoc $(PANDOC_HTML_OPTS) \
		   --metadata=main-page:true \
		   -o $@ $<

website: $(LOGOS) $(patsubst content/%.md,site/%.html,$(wildcard content/*.md)) site/index.html site/rss.xml
	mkdir -p site/static
	cp -r static/* site/static/

pdfs: $(patsubst content/%.md,latex/%.pdf,$(wildcard content/*.md))
	cp *.pdf latex/

latex/%.tex: content/%.md $(BUILD_ENV)
	mkdir -p latex
	pandoc $(PANDOC_TEX_OPTS) -s -o $@ $<

latex/%.pdf: latex/%.tex
	latexmk -pdf -xelatex $<

pdfs.tar.gz: pdfs
	cd latex && tar -czf $@ *.pdf
	mv latex/$@ .

pdfs.zip: pdfs
	cd latex && zip -r $@ *.pdf
	mv latex/$@ .

watch: export PANDOC_LIVE_RELOAD=1
watch:
	find . -name "*.md" | entr -s "make website && echo reload" | websocat -s 8080

clean:
	latexmk -C *.pdf
