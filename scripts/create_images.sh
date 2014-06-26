#!/bin/bash

GS="/usr/local/bin/gs"

cd dokument/master

echo "Generiere PNG aus PDF-Abbildungen"
for f in images/*.pdf
do
	$GS -dQUIET -dSAFER -dBATCH \
		-dNOPAUSE -sDisplayHandle=0 -dDOINTERPOLATE \
		-sDEVICE=png16m -r600 -dTextAlphaBits=4 \
		-sOutputFile=${f%.*}.png -f $f
done