# Erstellen der Spezifikation aus den Quelldokumenten

Die OParl-Spezifikation besteht aus verschiedenen Textdateien, die mit Hilfe verschiedener
Software automatisiert zu fertigen Dokumenten in verschiedenen Formaten bearbeitet werden.

## Genereller Aufbau des Repositories

Die Dateien, aus denen die Spezifikation erstellt wird, sind auf mehrere Ordner aufgeteilt:

 - `src/`:  Enthält den gesamten Fließtext als [Markdown](https://help.github.com/articles/markdown-basics/)-Dateien.
 - `schema/`: Enthält das Datenmodell, d.h. den Aufbau der von OParl genutzten json-Objekte, als json-Dateien in einem
 auf [JSON Schema](https://json-schema.org) aufbauenden Format.
 - `examples/`: Die im Text eingebundenen Beispiele
 - `scripts/`: Enthält Skripte, die u.a. die json-Dateien in Markdown umwandeln und die Beispiele validieren

## Erstellen der Dokumente

Es gibt zwei Möglichkeiten, die Dokumente zu erstellen: Direkt mit `make` oder über eine Docker-Container.

### Mit `make`

Im Allgemeinen sollte die OParl-Spezifikation mit jedem Betriebssystem erstellbar
sein, auf dem folgende Software installiert ist:

- [Pandoc](http://pandoc.org/)
- [Graphviz](http://www.graphviz.org/)
- [Python >= 3.5](https://www.python.org/)
- [Ghostscript](https://www.ghostscript.com/)
- [ImageMagick](https://www.imagemagick.org/script/index.php)
- [GNU Make](https://www.gnu.org/software/make/)

Zur Erstellung der Archive außerdem:

- [GNU Tar](https://www.gnu.org/software/tar/)

Unter Ubuntu können alle benötigten Pakete mit einem Befehl installiert werden:

```bash
sudo apt install etoolbox ghostscript lmodern graphviz make pandoc pandoc-citeproc texlive-fonts-recommended \
texlive-generic-recommended texlive-humanities texlive-lang-german texlive-latex-recommended texlive-luatex texlive-xetex
```

Das eingentlich bauen der Dokumente ist dann nur noch ein einziger Befehl:

```bash
make
```

Ein einzelnes Ausgabeformat kann mit `make <format>` erstellt werden, mit `make archives` können
Archive der verschiedenen Ausgabeformate gepackt werden. Dazu müssen allerdings
die enstprechenden Archivierungsprogramme vorhanden sein.

Die fertigen Dokumente finden sich dann sich in `out/`

### Docker

Für den geneigten Containerfreund findet sich in `resources/specbuilder` ein
Dockerfile, welches auch mit `docker pull oparl/specbuilder` installiert werden kann.

Gebaut wird die Spezifikation dann mit folgenden Befehl, wobei auch hier ein Ausgabe an den Aufruf von `make` 
angehängt werden kann:

```
docker run -u $UID:$GID --rm -v $(pwd):$(pwd) -w $(pwd) oparl/specbuilder:latest make
```
