![OParl Wortmarke](https://raw.githubusercontent.com/OParl/brand/master/wortmarke/oparl-wortmarke-rgb-m.png)

In diesem Repository wird die Spezifikation zum [OParl](http://oparl.org/)-Standard erarbeitet.

OParl ist eine Initiative für die Offenheit parlamentarischer Informationssysteme. Der
OParl-Standard dient der Definition einer einheitlichen Schnittstelle zum Abruf von
öffenltichen Informationen aus Ratsinformationssystemen. Mehr über OParl:

  [http://oparl.org/](http://oparl.org/)


Original: Editieren, Änderungen nachvollziehen
----------------------------------------------

Wenn Du Dich für die Quellen des Dokuments sowie für das Nachvollziehen von Änderungen an den Quellen interessierst, findest Du dies im Ordner:

    src

Die Quelldateien sind reine Textdateien (Zeichensatz: UTF-8) mit [Markdown](http://daringfireball.net/projects/markdown/)-Formatierung (Dateiendung: .md).

Änderungswünsche am Dokument können in Form von Pull Requests beigesteuert werden. Dazu erzeugst Du zunächst einen Fork dieses Repositories. Dann committest Du Änderungen an Deinem Fork. Danach kannst Du am einzelnen Commit die Funktion "Send Pull Request" auslösen. Mehr dazu in der [Github-Hilfe](https://help.github.com/articles/using-pull-requests).

**Übrigens:** [prose.io](http://prose.io/) ist ein fantastischer Web-basierter Editor, mit dem Du die Markdown-Dateien in Deinem eigenen Repository spielend im Browser bearbeiten kannst.

Änderungsinfos können übrigens in Form eines [Atom Feeds](https://github.com/OParl/specs/commits/master.atom) abonniert werden.

Derivate: Bequemes Lesen auf verschiedenen Geräten
--------------------------------------------------

Es stehen Versionen des Dokuments in vielen Formaten zur Verfügung:

* [PDF](http://spec.oparl.org/downloads/latest.pdf)
* [OpenOffice/LibreOffice](http://spec.oparl.org/downloads/latest.odt)
* [Microsoft Word](http://spec.oparl.org/downloads/latest.docx)
* [LaTeX](http://spec.oparl.org/downloads/latest.tex)
* [EPub](http://spec.oparl.org/downloads/latest.epub)
* [Nur Text](http://spec.oparl.org/downloads/latest.txt)

Die Derivate werden unter anderem mit der Hilfe von [Pandoc](http://johnmacfarlane.net/pandoc/)
erzeugt. Der gesamte Prozess wird durch das `Makefile` automatisiert.
