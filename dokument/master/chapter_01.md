Einleitung
==========

Ziel dieses Dokuments
---------------------

Ziel dieses Dokuments ist es, einen Diskurs über einen offenen Standard zum Datenabruf aus Ratsinformationssystemen in Gang zu bringen.

Ratsinformationssysteme (RIS) werden von vielen Körperschaften wie Kommunen, Landkreisen und Regierungsbezirken eingesetzt, um die anfallende Gremienarbeit (Ratssitzungen, Ausschüsse, Vertretungen) zu organisieren. Da ein großer Teil der schriftlichen Arbeit der Lokalpolitik über derartige Systeme verwaltet wird, sind die RIS – dort wo vorhanden – ein wichtiger Zugriffspunkt für alle, die sich für politischen Geschehnisse interessieren.

Eine wichtige Maßnahme von Körperschaften, die im Zuge von Open-Data- und Open-Government-Initiativen ihre Politik transparenter machen wollen, wird auch sein, die Daten in den RIS im Sinne des Open-Data-Begriffs zugänglich zu machen. Hierdurch können die Kommunen selbst, aber auch dritte, Anwendungen entwickeln, die Inhalte auf verschiedene Art und Weise auswerten, abrufbar und nutzbar machen, sei es für die Allgemeinheit oder für bestimmte Nutzerkreise.

In Deutschland gibt es über 10.000 Kommunen, außerdem hunderte weitere Körperschaften, die über RIS-ähnliche Systeme verfügen. Sollten diese beginnen, ihre RIS  zu öffnen, werden sie sämtlich vor der Frage stehen, wie Daten zu modellieren und Schnittstellen (APIs) zu spezifizieren sind.

Sowohl die Anbieter der Daten, als auch die Abnehmer (die Anwendungsentwickler) werden von einer Standardisierung der Schnittstellen und Datenmodelle profitieren. So wird die Kompatibilität von Software und die breite Einsetzbarkeit ermöglicht.

Dieses Dokument soll die Erarbeitung eines solchen Standards ermöglichen und als Diskussionsgrundlage dienen.

Status
------

Dieser Entwurf gibt aktuell einen Vorschlag des Autors wieder. Bisher ist noch kein Feedback eingeflossen.


Überblick
---------

Der Entwurf umfasst im ersten Schritt die abstrakte Beschreibung eines Datenmodells.

### Noch nicht abgedeckt: ###

* Angaben von Personen zu Tätigkeiten (z.B. Auskunft nach § 17 Korruptionsbekämpfungsgesetz). Diese werden von mehreren Systemen geführt und ausgegeben.
* Änderungsdatum (bei allen Objekttypen relevant)
* Unterscheidung von Rollen bzw. Zuständigkeiten zwischen Drucksachen und Tagesordnungspunkten (z.B. federführende Beratung, konsultierende Beratung etc.)


Nächste Schritte
----------------

1. Bis Ende Januar 2012: Einsammeln von Feedback zum Entwurf des Datenmodells
2. Anpassen des Entwurfs anhand von Feedback
3. Erarbeitung eines Entwurfs für eine REST-Schnittstelle. Darin soll beschrieben werden, wie über HTTP die zuvor beschriebenen Daten abgerufen werden sollen.


Feedback
--------

Feedback wird dringend benötigt und ist daher herzlichst willkommen. Feedback kann auf den folgenden Wegen eingereicht werden:

* Als Pull Requests über Github, direkt am Quelltext
* Über Issues auf Github
* Per E-Mail

### Pull Requests über Github ###

Dieses Dokument wird in folgendem Github-Repository gepflegt:

[https://github.com/marians/open-ris-specs](https://github.com/marians/open-ris-specs)


Der bevorzugte Feedback-Kanal für erfahrene Git- bzw. Github-Nutzer ist entsprechend die Mitwirkung direkt am Quelltext in Form von Pull-Requests. So können **Ergänzungen und Korrekturen** direkt in den Quelltext eingespielt werden.

Ausführliche Anleitungen zur Arbeit mit Git/Github finden sich auf der Plattform selbst sowie an vielen Orten im Netz. Der allgemeine Ablauf ist wie folgt:

1. Erzeugen Sie sich, sofern noch nicht geschehen, ein Benutzerkonto auf Github.
2. Duplizieren (_forken_) Sie das oben genannte Repository
3. Nehmen Sie die gewünschten Änderungen an Ihrem Repository vor. Committen Sie diese Änderungen möglichst kleinteilig.
4. Senden Sie die gewünschten Commits als Pull Requests.

Als Autor werde ich entscheiden, welche Pull Requests ich übernehme. Sie werden als Mitwirkender in diesem Dokument genannt. Wenn Sie mit einen Klarnamen unggf. Unternehmenszugehörigkeit genannt werden wollen, teilen Sie mir dies bitte per Mail an marian@sendung.de mit.


### Issues auf Github ###

Wer nicht über Github am Quelltext mitwirken möchte, aber einen Github-Account sein eigen nennt (oder zu diesem Zweck anlegen möchte) und **öffentlich kommentieren** möchte, der sollte das öffentliche Issue-Tracking-System unter

[https://github.com/marians/open-ris-specs/issues](https://github.com/marians/open-ris-specs/issues)

verwenden. Vorteil daran ist, dass auch andere die Einträge lesen und wiederum durch Kommentare ergänzen können. Zudem lässt sich der Bearbeitungsstatus eines Issue-Eintrags (offen, geschlossen) nachhalten.

Bitte achten Sie auf diesem Weg darauf, Ihre Kommentare in möglichst kleine thematische Einheiten herunter zu brechen.

### Feedback per E-Mail ###

Sollten Sie keinen der oben beschriebenen Wege beschreiten wollen, können Sie Anmerkungen zum Dokument per E-Mail an marian@sendung.de einsenden. Bitte verwenden Sie dabei den Begriff "open-ris-specs" im Betreff.

Sollten Sie auf diesem Wege Anmerkungen direkt am/im Dokumententext übersenden wollen, nutzen Sie bitte falls möglich die Word- oder OpenOffice-Version dieses Dokuments und ändern Sie das Dokument so, dass Änderungen aufgezeichnet werden (OpenOffice: Bearbeiten > Änderungen > Aufzeichnen; Word: Ribbon "Überprüfen" > Nachverfolgung > Änderungen nachverfolgen).


Mitwirkende
-----------

Felix Ebert