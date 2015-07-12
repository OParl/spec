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

* [PDF](https://github.com/OParl/specs/blob/master/dokument/pdf/document.pdf?raw=true)
* [OpenOffice/LibreOffice](https://github.com/OParl/specs/blob/master/dokument/odt/document.odt?raw=true)
* [Microsoft Word](https://github.com/OParl/specs/blob/master/dokument/docx/document.docx?raw=true)
* [LaTeX](https://github.com/OParl/specs/blob/master/dokument/latex/document.tex?raw=true)
* [EPub](https://github.com/OParl/specs/blob/master/dokument/epub/document.epub?raw=true)
* [Nur Text](https://github.com/OParl/specs/blob/master/dokument/plain/document.txt?raw=true)

Die Derivate werden mit [Pandoc](http://johnmacfarlane.net/pandoc/) erzeugt. Das Script unter 'scripts/create_documents.sh' automatisiert diesen Vorgang.
