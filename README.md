

[![OParl Wortmarke](https://raw.githubusercontent.com/OParl/brand/master/wortmarke/oparl-wortmarke-rgb-m.png)](https://oparl.org)

[![Build Status](https://travis-ci.org/OParl/spec.svg)](https://travis-ci.org/OParl/spec)

In diesem Repository wird die Spezifikation zum [OParl](https://oparl.org/)-Standard erarbeitet.

Der OParl-Standard dient der Definition einer einheitlichen Schnittstelle zum Abruf von
maschienlesbaren Informationen aus Ratsinformationssystemen. Mehr über OParl:

  [https://oparl.org](https://oparl.org)


## Änderungen an OParl vornehmen

OParl wird hauptsächlich auf GitHub entwickelt. Hilfe im Umgang mit GitHub findest du [hier](https://help.github.com/). Änderungsvorschläge können über Pull Requests eingebracht werden.

Durch den Befehl `make` kann aus den Quelldateien die Spezifikation erstellt werden. Dazu müssen pandoc und latex installiert sein.

Die Dateien, aus denen die Spezifikation erstellt wird, sind auf mehrere Ordner aufgeteilt:
 - `src/`:  Enthält den gesamten Fließtext als [Markdown](https://help.github.com/articles/markdown-basics/)-Dateien.
 - `schema/`: Enthält das Datenmodell, d.h. den Aufbau der von OParl genutzten json-Objekte, als json-Dateien in einem eigenen Format.
 - `examples/`: Die im Text eingebundenen Beispiele
 - `scripts/`: Enthält Skripte, die u.a. die json-Dateien in Markdown umwandeln und die Beispiele validieren
 - `out/`:  Die von `make` erstellten Dokumente 

## Die Spezifikation in verschiedenen Formaten

Es stehen Versionen des Dokuments in verschiedenen Formaten zur Verfügung:

* [PDF](https://spec.oparl.org/1.0.pdf)
* [html](https://spec.oparl.org/1.0.html)
* [OpenOffice/LibreOffice](https://spec.oparl.org/1.0.odt)
* [Microsoft Word](https://spec.oparl.org/1.0.docx)
* [EPub](https://spec.oparl.org/1.0.epub)
* [Nur Text](https://spec.oparl.org/1.0.txt)
