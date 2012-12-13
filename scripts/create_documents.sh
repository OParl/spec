#!/bin/bash

# Erzeugt Derivate vom Master-Dokument (Markdown-Format in /dokument/master/)
# in verschiedenen Ausgabeformaten

SOURCE="*.md"
DOC_FOLDER=".."
PWD=`pwd`
PDFLATEX="/usr/local/texlive/2012basic/bin/universal-darwin/pdflatex"

cd dokument/master


# HTML
pandoc -t html -s -N -o $DOC_FOLDER/html/document.html $SOURCE
cp -r images $DOC_FOLDER/html/images

# HTML5
pandoc -t html5 -s -N -o $DOC_FOLDER/html5/document.html $SOURCE
cp -r images $DOC_FOLDER/html5/images

# TeX
pandoc -t latex -o $DOC_FOLDER/latex/document.tex $SOURCE

# OpenOffice odt
pandoc -t odt -o $DOC_FOLDER/odt/document.odt $SOURCE

# docbook
pandoc -t docbook -o $DOC_FOLDER/docbook/document.xml $SOURCE

# epub
pandoc -t epub -o $DOC_FOLDER/epub/document.epub $SOURCE

# Word .docx
pandoc -t docx -o $DOC_FOLDER/docx/document.docx $SOURCE

# plain text
pandoc -t plain -o $DOC_FOLDER/plain/document.txt $SOURCE

# PDF
pandoc --latex-engine=$PDFLATEX -N -o $DOC_FOLDER/pdf/document.pdf $SOURCE


cd $PWD
