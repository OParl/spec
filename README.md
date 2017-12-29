[![OParl Wortmarke](https://raw.githubusercontent.com/OParl/brand/master/wortmarke/oparl-wortmarke-rgb-m.png)][oparl]

[![Build Status](https://travis-ci.org/OParl/spec.svg)][travis]

In diesem Repository wird die Spezifikation zum [OParl][oparl]-Standard erarbeitet.

Der OParl-Standard dient der Definition einer einheitlichen Schnittstelle zum Abruf von
maschinenlesbaren Informationen aus Ratsinformationssystemen. Mehr über OParl:

- Mehr über OParl:  [https://oparl.org][oparl]
- Weitere Informationen für Entwickler: [https://dev.oparl.org][oparl-dev]

## Die Spezifikation in verschiedenen Formaten

Es stehen Versionen des Dokuments in verschiedenen Formaten zur Verfügung:

### Version 1.0

* [PDF][spec-1-0-pdf]
* [HTML][spec-1-0-html]
* [OpenOffice/LibreOffice][spec-1-0-odt]
* [Microsoft Word][spec-1-0-docx]
* [EPub][spec-1-0-epub]
* [Nur Text][spec-1-0-txt]

### Aktuelle Entwicklungsversion

* [PDF][spec-master-pdf]
* [HTML][spec-master-html]
* [OpenOffice/LibreOffice][spec-master-odt]
* [Microsoft Word][spec-master-docx]
* [EPub][spec-master-epub]
* [Nur Text][spec-master-txt]


## Änderungen an OParl vornehmen

OParl wird hauptsächlich auf GitHub entwickelt. Hilfe im Umgang mit GitHub findest du [hier][github-help]. Änderungsvorschläge können über Pull Requests eingebracht werden.

Die OParl-Spezifikation besteht aus verschiedenen Textdateien, die mit Hilfe verschiedener
Software automatisiert zu fertigen Dokumenten in verschiedenen Formaten bearbeitet werden.

## Genereller Aufbau des Repositories

Die Dateien, aus denen die Spezifikation erstellt wird, sind auf mehrere Ordner aufgeteilt:

 - `src/`:  Enthält den gesamten Fließtext als [Markdown][markdown-help]-Dateien.
 - `schema/`: Enthält das Datenmodell, d.h. den Aufbau der von OParl genutzten json-Objekte, als json-Dateien in einem
 auf [JSON Schema][json-schema] aufbauenden Format.
 - `examples/`: Die im Text eingebundenen Beispiele
 - `scripts/`: Enthält Skripte, die u.a. die json-Dateien in Markdown umwandeln und die Beispiele validieren

## Erstellen der Dokumente

Es gibt zwei Möglichkeiten, die Dokumente zu erstellen: Direkt mit `build.py` oder über eine Docker-Container.

### Mit `build.py`

Im Allgemeinen sollte die OParl-Spezifikation mit jedem Betriebssystem erstellbar
sein, auf dem folgende Software installiert ist:

- [Pandoc][pandoc]
- [Graphviz][graphviz]
- [Python >= 3.5][python]
- [Ghostscript][ghostscript]
- [ImageMagick][imagemagick]

Zur Erstellung der Archive außerdem:

- [GNU Tar][tar]
- [Zip][zip]

Unter Ubuntu können alle benötigten Pakete mit einem Befehl installiert werden:

```bash
sudo apt install etoolbox ghostscript lmodern graphviz make pandoc pandoc-citeproc texlive-fonts-recommended \
texlive-generic-recommended texlive-humanities texlive-lang-german texlive-latex-recommended texlive-luatex \
texlive-xetex librsvg2-bin python3 python3-yaml
```

Das eigentliche Bauen der Dokumente ist dann nur noch ein einziger Befehl:

```bash
python3 build.py
```

Ein einzelnes Ausgabeformat kann mit `python3 build.py <format>` erstellt werden, mit `python3 build.py archives` können
Archive der verschiedenen Ausgabeformate gepackt werden. Dazu müssen allerdings
die enstprechenden Archivierungsprogramme vorhanden sein.

Die fertigen Dokumente finden sich dann sich in `build/`.

### Docker

Für den geneigten Containerfreund findet sich in `resources/specbuilder` ein
Dockerfile, welches auch mit `docker pull oparl/specbuilder` installiert werden kann.

Gebaut wird die Spezifikation dann mit folgenden Befehl, wobei auch hier ein Ausgabeformat
an den Aufruf angehangen werden kann:

```
docker run -u $UID:$GID --rm -v $(pwd):$(pwd) -w $(pwd) oparl/specbuilder:latest <format>
```

[oparl]: https://oparl.org/
[oparl-dev]: https://dev.oparl.org/

[ghostscript]: https://www.ghostscript.com/
[github-help]: https://help.github.com/
[graphviz]: http://www.graphviz.org/
[imagemagick]: https://www.imagemagick.org/script/index.php
[json-schema]: https://json-schema.org/
[markdown-help]: https://help.github.com/articles/markdown-basics/
[pandoc]: http://pandoc.org/
[python]: https://www.python.org/
[tar]: https://www.gnu.org/software/tar/
[travis]: https://travis-ci.org/OParl/spec/
[zip]: http://www.info-zip.org/

[spec-1-0-pdf]: https://dev.oparl.org/downloads/spezifikation-1.0.pdf
[spec-1-0-html]: https://dev.oparl.org/downloads/spezifikation-1.0.html
[spec-1-0-odt]: https://dev.oparl.org/downloads/spezifikation-1.0.odt
[spec-1-0-docx]: https://dev.oparl.org/downloads/spezifikation-1.0.docx
[spec-1-0-epub]: https://dev.oparl.org/downloads/spezifikation-1.0.epub
[spec-1-0-txt]: https://dev.oparl.org/downloads/spezifikation-1.0.txt

[spec-master-pdf]: https://dev.oparl.org/downloads/spezifikation-master.pdf
[spec-master-html]: https://dev.oparl.org/downloads/spezifikation-master.html
[spec-master-odt]: https://dev.oparl.org/downloads/spezifikation-master.odt
[spec-master-docx]: https://dev.oparl.org/downloads/spezifikation-master.docx
[spec-master-epub]: https://dev.oparl.org/downloads/spezifikation-master.epub
[spec-master-txt]: https://dev.oparl.org/downloads/spezifikation-master.txt
