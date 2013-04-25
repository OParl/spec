Einleitung
==========

Dieses Dokument wird bei seiner Fertigstellung die Spezifikation des OParl 
Schnittstellen-Standards für parlamentarische Informationssysteme 
(Ratsinformationssysteme, RIS) darstellen. Es dient damit als Grundlage für 
die Implementierung von OParl-konformen Server- und Clientanwendungen.


Parlamentarische Informationssysteme
------------------------------------

Parlamentarische Informationssysteme (oft Ratsinformationssystem, RIS oder 
Bürgerinformationssystem genannt) werden von vielen Körperschaften wie 
Kommunen, Landkreisen und Regierungsbezirken eingesetzt, um die anfallende 
Gremienarbeit (Ratssitzungen, Ausschüsse, Vertretungen) zu organisieren. Da 
ein großer Teil der schriftlichen Arbeit in der Lokalpolitik über derartige 
Systeme verwaltet wird, sind diese Systeme – dort wo vorhanden – ein 
wichtiger Zugriffspunkt für alle, die sich für politischen Geschehnisse 
interessieren.


Gründe für den standardisierten Datenzugriff
--------------------------------------------

Eine wichtige Maßnahme von Körperschaften, die im Zuge von Open-Data- und 
Open-Government-Initiativen ihre Politik transparenter machen wollen, wird 
auch sein, die Daten in den parlamentarischen Informationssystemen im Sinne 
des Open-Data-Begriffs zugänglich zu machen. Hierdurch können die Kommunen 
selbst, aber auch dritte, Anwendungen entwickeln, die Inhalte auf 
verschiedene Art und Weise auswerten, abrufbar und nutzbar machen, sei es 
für die Allgemeinheit oder für bestimmte Nutzerkreise.

Darüber hinaus sollen parlamentarische Informationssysteme in verschiedenste 
Prozesse und Systemlandschaften integriert werden. Durch eine einheitliche 
Schnittstelle bieten sich effiziente Möglichkeiten zur Integration der Daten 
in anderen Systemen, wie beispielsweise Web-Portalen.


Funktionsumfang der OParl-Schnittstelle
---------------------------------------

Die vorliegende Spezifikation soll eine Webservice-Schnittstelle definieren, 
die den anonymen und lesenden Zugriff auf öffentliche Inhalte aus 
Parlamentarischen Informationssystemen ermöglicht. Die Zugriffe erfolgen 
über das Hypertext Transfer Protocol (HTTP). Daten werden als JSON, JSONP 
oder optional als XML ausgeliefert.

Die Spezifikation wird obligatorische Bestandteile (MUSS) und optionale 
Bestandteile (KANN) haben. Der tatsächliche Funktionsumfang kann daher 
zwischen den Implementierungen variieren.


Status
------

Die Spezifikation befindet sich in Arbeit. Das Dokument enthält entsprechend 
viele Ungenauigkeiten und Hinweise auf offene Fragestellungen.


Überblick
---------

Der Entwurf umfasst aktuell die Beschreibung eines Datenmodells. 


Nächste Schritte
----------------

Bis Ende Juni 2013: Fertigstellung von Version 1.0. Bis dahin ist zu 
erledigen:

* Fertigstellung Datenmodell
* Beschreibung von Methoden und URL-Parametern
* HTTP Status-Codes und besondere Anforderungen an Verwendung bestimmter 
HTTP-Header
* Klärung einer gemeinsamen Nomenklatur für Inhalte, beispielsweise für Arten 
von Drucksachen


Feedback und Mitwirkung
-----------------------

Feedback wird dringend benötigt und ist daher herzlichst willkommen. 
Feedback kann auf den folgenden Wegen eingereicht werden:

* Als Pull Requests über Github, direkt am Quelltext
* Über Issues auf Github
* Per E-Mail

### Pull Requests über Github ###

Dieses Dokument wird in folgendem Github-Repository gepflegt:

[https://github.com/OParl/specs](https://github.com/OParl/specs)


Der bevorzugte Feedback-Kanal für erfahrene Git- bzw. Github-Nutzer ist 
entsprechend die Mitwirkung direkt am Quelltext in Form von Pull-Requests. 
So können **Ergänzungen und Korrekturen** direkt in den Quelltext 
eingespielt werden.

Ausführliche Anleitungen zur Arbeit mit Git/Github finden sich auf der 
Plattform selbst sowie an vielen Orten im Netz. Der allgemeine Ablauf ist 
wie folgt:

1. Erzeugen Sie sich, sofern noch nicht geschehen, ein Benutzerkonto auf 
Github.
2. Duplizieren (_forken_) Sie das oben genannte Repository
3. Nehmen Sie die gewünschten Änderungen an Ihrem Repository vor. Committen 
Sie diese Änderungen möglichst kleinteilig.
4. Senden Sie die gewünschten Commits als Pull Requests.

Als Autor werde ich entscheiden, welche Pull Requests ich übernehme. Sie 
werden als Mitwirkender in diesem Dokument genannt. Wenn Sie mit einen 
Klarnamen unggf. Unternehmenszugehörigkeit genannt werden wollen, teilen 
Sie mir dies bitte per Mail an marian@sendung.de mit.


### Issues auf Github ###

Wer nicht über Github am Quelltext mitwirken möchte, aber einen 
Github-Account sein eigen nennt (oder zu diesem Zweck anlegen möchte) und 
**öffentlich kommentieren** möchte, der sollte das öffentliche 
Issue-Tracking-System unter

[https://github.com/OParl/specs/issues](https://github.com/OParl/specs/issues)

verwenden. Vorteil daran ist, dass auch andere die Einträge lesen und 
wiederum durch Kommentare ergänzen können. Zudem lässt sich der 
Bearbeitungsstatus eines Issue-Eintrags (offen, geschlossen) nachhalten.

Bitte achten Sie auf diesem Weg darauf, Ihre Kommentare in möglichst kleine 
thematische Einheiten herunter zu brechen.

### Feedback per E-Mail ###

Sollten Sie keinen der oben beschriebenen Wege beschreiten wollen, können 
Sie Anmerkungen zum Dokument per E-Mail an marian@sendung.de einsenden. 
Bitte verwenden Sie dabei den Begriff "oparl-specs" im Betreff.

Sollten Sie auf diesem Wege Anmerkungen direkt am/im Dokumententext 
übersenden wollen, nutzen Sie bitte falls möglich die Word- oder 
OpenOffice-Version dieses Dokuments und ändern Sie das Dokument so, dass 
Änderungen aufgezeichnet werden (OpenOffice: Bearbeiten > Änderungen > 
Aufzeichnen; Word: Ribbon "Überprüfen" > Nachverfolgung > Änderungen 
nachverfolgen).


Mitwirkende
-----------

Felix Ebert, Jan Erhardt, Andreas Kuckartz, Babett Schalitz
