# Variables
VERSION=1.0-draft
BASENAME=OParl-$(VERSION)

# Directories
SRC_DIR=src
IMG_DIR=src/images
SHM_DIR=schema
EXP_DIR=examples
OUT_DIR=out
ARC_DIR=archives

# Command config and macros
PANDOC_FLAGS=--from markdown --standalone --table-of-contents --number-sections
PANDOC=cd $(SRC_DIR) && pandoc $(PANDOC_FLAGS)

LATEX=pdflatex
LATEX_TEMPLATE=resources/template.tex

HTML5_CSS=resources/html5.css
SCHEMA_MD=$(SRC_DIR)/3-99-generiertes-schema.md

GS_FLAGS=-dQUIET -dSAFER -dBATCH -dNOPAUSE -sDisplayHandle=0 -sDEVICE=png16m -r600 -dTextAlphaBits=4
GS=gs $(GS_FLAGS)

PDF_IMAGES=$(wildcard $(IMG_DIR)/*.pdf)
PNG_IMAGES=$(PDF_IMAGES:.pdf=.png)

.PHONY: all clean live html pdf odt txt epub

all: html pdf odt docx txt epub

# preliminary targets

$(IMG_DIR)/%.png: $(IMG_DIR)/%.pdf
	$(GS) -sOutputFile=$@ -f $<

$(OUT_DIR):
	mkdir -p $(OUT_DIR)

$(SCHEMA_MD): $(SHM_DIR)/*.json $(EXP_DIR)/*.json
	python scripts/json_schema2markdown.py $(SHM_DIR) $(EXP_DIR) > $(SCHEMA_MD)

# main targets

common: $(OUT_DIR) $(SCHEMA_MD)

html: common $(PNG_IMAGES)
	$(PANDOC) --to html5 --css ../$(HTML5_CSS) --section-divs --self-contained \
	    -o ../$(OUT_DIR)/$(BASENAME).html *.md

live: common $(PNG_IMAGES)
	$(PANDOC) --to html5 --section-divs --toc-depth=2 --no-highlight \
			-o ../$(OUT_DIR)/live.html *.md 

pdf: common
	$(PANDOC) --latex-engine=$(LATEX) --template ../$(LATEX_TEMPLATE) \
			-o ../$(OUT_DIR)/$(BASENAME).pdf *.md

odt: common $(PNG_IMAGES)
	$(PANDOC) -o ../$(OUT_DIR)/$(BASENAME).odt *.md

docx: common $(PNG_IMAGES)
	$(PANDOC) --metadata toc-title:"Inhaltsverzeichnis" \
			-o ../$(OUT_DIR)/$(BASENAME).docx *.md

txt: common
	$(PANDOC) -o ../$(OUT_DIR)/$(BASENAME).txt *.md

epub: common $(PNG_IMAGES)
	$(PANDOC) -o ../$(OUT_DIR)/$(BASENAME).epub *.md

clean:
	rm -rf $(OUT_DIR)
	rm -f $(SCHEMA_MD)
	rm -f $(PNG_IMAGES) 
	rm -rf $(ARC_DIR)

# archives

archives: zip gz bz

zip: all
	mkdir -p $(ARC_DIR) && zip -qr $(ARC_DIR)/$(BASENAME).zip $(OUT_DIR)/

gz: all
	mkdir -p $(ARC_DIR) && tar -czf $(ARC_DIR)/$(BASENAME).tar.gz $(OUT_DIR)/

bz: all
	mkdir -p $(ARC_DIR) && tar -cjf $(ARC_DIR)/$(BASENAME).tar.bz2 $(OUT_DIR)/

