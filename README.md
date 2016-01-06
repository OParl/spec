[![Build Status](https://travis-ci.org/OParl/spec.svg)](https://travis-ci.org/OParl/spec)

![OParl Wortmarke](https://raw.githubusercontent.com/OParl/brand/master/wortmarke/oparl-wortmarke-rgb-m.png)

In diesem Repository wird die Spezifikation zum [OParl](https://oparl.org/)-Standard erarbeitet.

Der OParl-Standard dient der Definition einer einheitlichen Schnittstelle zum Abruf von
maschienlesbaren Informationen aus Ratsinformationssystemen. Mehr über OParl:

  [oparl.org/](https://oparl.org/)


## Änderungen an OParl vornehmen

OParl wird hauptsächlich auf GitHub entwickelt. Hilfe im Umgang mit GitHub findest du [hier](https://help.github.com/). Änderungsvorschläge können über Pull Requests eingebracht werden.

Die Dateien, aus denen die Spezifikation erstellt wird, sind auf mehrere Ordner aufgeteilt:
 - `src/`:  Enthält den gesammten Fließtext als [Markdown](https://help.github.com/articles/markdown-basics/)-Dateien. 
 - `schema/`: Enthält das Datenmodell, d.h. den Aufbau der von OParl genutzten json-Objekte, als json-Dateien in einem eigenen Format.
 - `examples/`: Die im Text eingebundenen Beispiele
 - `scripts/`: Enthält hauptsächlich die python-skripte, die die json-Dateien in Markdown umwandeln

Durch den Befehl `make` kann aus den Quelldateien die Spezifikation erstellt werden. Dazu müssen pandoc und latex installiert sein. Die fertigen Dokumente finden sich dann im Ornder `out`.

## Die Spezifikation in verschiedenen Formaten

Es stehen Versionen des Dokuments in verschiedenen Formaten zur Verfügung:

* [PDF](http://spec.oparl.org/downloads/latest.pdf)
* [OpenOffice/LibreOffice](http://spec.oparl.org/downloads/latest.odt)
* [Microsoft Word](http://spec.oparl.org/downloads/latest.docx)
* [LaTeX](http://spec.oparl.org/downloads/latest.tex)
* [EPub](http://spec.oparl.org/downloads/latest.epub)
* [Nur Text](http://spec.oparl.org/downloads/latest.txt)

