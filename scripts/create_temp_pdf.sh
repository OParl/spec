#!/bin/bash

# Erzeugt Derivate vom Master-Dokument (Markdown-Format in /dokument/master/)
# in verschiedenen Ausgabeformaten




PDFLATEX="/usr/local/texlive/2013/bin/x86_64-darwin/pdflatex"

echo "Generiere temporäres PDF-Dokument"
cd dokument/master
pandoc --latex-engine=$PDFLATEX --table-of-contents --template ../latex/template.tex -N \
	-o ../../temp_specs.pdf -f markdown+header_attributes+pipe_tables \
	*.md

