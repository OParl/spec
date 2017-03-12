# Hinweise für OParl-Mitschreiber

Die OParl-Spezifikation ist zwar im Endeffekt ein Textdokument, allerdings
wird dies mit Hilfe verschiedenster Software erstellt und bearbeitet.

## Genereller Aufbau des Repositories

Die Dateien, aus denen die Spezifikation erstellt wird, sind auf mehrere Ordner aufgeteilt:

 - `src/`:  Enthält den gesamten Fließtext als [Markdown](https://help.github.com/articles/markdown-basics/)-Dateien.
 - `schema/`: Enthält das Datenmodell, d.h. den Aufbau der von OParl genutzten json-Objekte, als json-Dateien in einem auf [JSON Schema](https://json-schema.org) aufbauenden Format.
 - `examples/`: Die im Text eingebundenen Beispiele
 - `scripts/`: Enthält Skripte, die u.a. die json-Dateien in Markdown umwandeln und die Beispiele validieren

## Softwareabhängigkeiten

Im Allgemeinen sollte die OParl-Spezifikation mit jedem Betriebssystem erstellbar
sein, auf dem folgende Software installiert ist:

- [Pandoc](http://pandoc.org/)
- [Graphviz](http://www.graphviz.org/)
- [Python 3](https://www.python.org/)
- [Ghostscript](https://www.ghostscript.com/)
- [ImageMagick](https://www.imagemagick.org/script/index.php)
- [GNU Make](https://www.gnu.org/software/make/)

Zur Erstellung der Archive außerdem:

- [GNU Tar](https://www.gnu.org/software/tar/)

## Erstellen der Derivate

Das `Makefile` stellt verschiedene Ausgabeformate zur Verfügung. Gebaut werden
können diese alle mit der selben Syntax `make <format>`. Ein einfacher Aufruf
von `make` führt zur Erstellung aller Formate, mit `make archives` können
Archive der verschiedenen Ausgabeformate gepackt werden. Dazu müssen allerdings
die enstprechenden Archivierungsprogramme vorhanden sein.

### Docker

Für den geneigten Containerfreund findet sich in `resources/specbuilder` ein
Dockerfile, welches auch mit `docker pull oparl/specbuilder` installiert werden kann.

Der `make`-Aufruf verändert sich dann zu:

`docker run --rm -v $(pwd):$(pwd) -w $(pwd) oparl/specbuilder:latest make [...]`
