# Variables
VERSION=1.1-draft
HUMAN_VERSION="1.1 Entwurf"
BASENAME=OParl-$(VERSION)

# Directories
SRC_DIR=src
IMG_DIR=src/images
SHM_DIR=schema
EXP_DIR=examples
OUT_DIR=out
ARC_DIR=archives

# Command config and macros
PANDOC=pandoc --from markdown --standalone --table-of-contents --toc-depth=2 \
			--number-sections

GRAPHVIZ_DOT=dot

LATEX_ENGINE=xelatex
LATEX_TEMPLATE=resources/template.tex
SCHEMA_MD=$(SRC_DIR)/3-99-generiertes-schema.md
HTML5_CSS=resources/html5.css

GS=gs -dQUIET -dSAFER -dBATCH -dNOPAUSE -sDisplayHandle=0 -sDEVICE=png16m \
			-r600 -dTextAlphaBits=4

CONVERT=convert

PDF_IMAGES=$(wildcard $(IMG_DIR)/*.pdf)
GS_IMAGES=$(PDF_IMAGES:.pdf=.png)

SVG_IMAGES=$(wildcard $(IMG_DIR)/*.svg)
MAGICK_IMAGES=$(SVG_IMAGES:.svg=.png)

DOT_IMAGES=$(wildcard $(IMG_DIR)/*.dot)
GRAPHVIZ_IMAGES=$(DOT_IMAGES:.dot=.png)

SCHEMA_JSON=$(wildcard $(SHM_DIR)/*.json)

.PHONY: all clean test live html pdf odt txt epub

all: html pdf odt docx txt epub

# preliminary targets

# transform dot file using dot -Tpng graphviz.dot -o graphviz.png
$(IMG_DIR)/%.png: $(IMG_DIR)/%.dot
	$(GRAPHVIZ_DOT) -Tpng $< -o $@

$(IMG_DIR)/%.png: $(IMG_DIR)/%.pdf
	$(GS) -sOutputFile=$@ -f $<

$(IMG_DIR)/%.png: $(IMG_DIR)/%.svg
	$(CONVERT) $< $@

$(OUT_DIR):
	mkdir -p $(OUT_DIR)

$(SCHEMA_MD): $(SHM_DIR)/*.json $(EXP_DIR)/*.json scripts/json_schema2markdown.py
	python3 scripts/json_schema2markdown.py $(SHM_DIR) $(EXP_DIR) $(SCHEMA_MD)

# main targets

common: $(OUT_DIR) $(SCHEMA_MD) $(GS_IMAGES) $(MAGICK_IMAGES) $(GRAPHVIZ_IMAGES)

html: common
	$(PANDOC) --to html5 --css $(HTML5_CSS) --section-divs --self-contained \
	    -o $(OUT_DIR)/$(BASENAME).html resources/lizenz-als-bild.md $(SRC_DIR)/*.md

pdf: common
	$(PANDOC) --latex-engine=$(LATEX_ENGINE) --template $(LATEX_TEMPLATE) \
			-o $(OUT_DIR)/$(BASENAME).pdf $(SRC_DIR)/*.md

odt: common
	$(PANDOC) -o $(OUT_DIR)/$(BASENAME).odt resources/lizenz-als-text.md $(SRC_DIR)/*.md

docx: common # FIXME: License information in header is missing
	$(PANDOC) -o $(OUT_DIR)/$(BASENAME).docx resources/lizenz-als-text.md $(SRC_DIR)/*.md

txt: common
	$(PANDOC) -o $(OUT_DIR)/$(BASENAME).txt $(SRC_DIR)/*.md

epub: common
	$(PANDOC) -o $(OUT_DIR)/$(BASENAME).epub $(SRC_DIR)/*.md

# Used for the spec website
live: common
	$(PANDOC) --to html5 --section-divs --toc-depth=2 --no-highlight \
			-o $(OUT_DIR)/live.html $(SRC_DIR)/*.md

clean:
	rm -rf $(OUT_DIR)
	rm -f  $(CONTRIB_MD)
	rm -f  $(SCHEMA_MD)
	rm -f  $(GS_IMAGES)
	rm -f  $(MAGICK_IMAGES)
	rm -rf $(ARC_DIR)

# archives

archives: zip gz bz

zip: all
	mkdir -p $(ARC_DIR) && cd $(OUT_DIR) && zip -qr ../$(ARC_DIR)/$(BASENAME).zip .

gz: all
	mkdir -p $(ARC_DIR) && cd $(OUT_DIR) && tar -czf ../$(ARC_DIR)/$(BASENAME).tar.gz .

bz: all
	mkdir -p $(ARC_DIR) && cd $(OUT_DIR) && tar -cjf ../$(ARC_DIR)/$(BASENAME).tar.bz2 .

# test

test:
	scripts/test.sh
