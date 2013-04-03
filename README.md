In diesem Repository werden die Inhalte eines Dokuments verwaltet.

Original: Editieren, Änderungen nachvollziehen
----------------------------------------------

Wenn Du Dich für die Quellen des Dokuments sowie für das Nachvollziehen von Änderungen an den Quellen interessierst, findest Du dies im Ordner:

    dokument/master

Die Quelldateien sind reine Textdateien (Zeichensatz: UTF-8) mit Markdown-Formatierung (Dateiendung: .md).

Änderungswünsche am Dokument können in Form von Pull Requests beigesteuert werden. Dazu erzeugst Du zunächst einen Fork dieses Repositories. Dann committest Du Änderungen an Deinem Fork. Danach kannst Du am einzelnen Commit die Funktion "Send Pull Request" auslösen.

**Übrigens:** [prose.io](http://prose.io/) ist ein fantastischer Web-basierter Editor, mit dem Du die Markdown-Dateien in Deinem eigenen Repository spielend im Browser bearbeiten kannst.

Änderungsinfos können übrigens in Form eines [Atom Feeds](https://github.com/marians/open-ris-specs/commits/master.atom) abonniert werden.

Derivate: Bequemes Lesen auf verschiedenen Geräten
--------------------------------------------------

Es stehen Exporte des Dokuments in verschiedensten Formaten zur Verfügung:

* [PDF](https://github.com/marians/open-ris-specs/blob/master/dokument/pdf/document.pdf?raw=true)
* [Word .docx](https://github.com/marians/open-ris-specs/blob/master/dokument/docx/document.docx?raw=true)
* [OpenOffice .odt](https://github.com/marians/open-ris-specs/blob/master/dokument/docx/document.docx?raw=true)

und andere. Du findest alle Formate im Ordner 'dokument/'.

Die Derivate werden mit [Pandoc](http://johnmacfarlane.net/pandoc/) erzeugt. Das Script unter 'scripts/create_documents.sh' automatisiert diesen Vorgang.

