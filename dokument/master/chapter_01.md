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
in anderen Systeme, wie beispielsweise Web-Portale.

TODO: Hier könnten konkrete, beispielhafte Szenarien aus Sicht von 
Anwendern, Herstellern und Kommunen beschrieben werden.


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

* In Form von Pull Requests über Github, direkt am Quelltext
* Über Issues auf Github

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

Die Entscheidung, welche Pull Requests übernommen werden, erfolgt nach 
Abwägung durch die federführenden Autoren der Spezifikation.

Es ist beabsichtigt, alle Mitwirkenden im Dokument zu nennen. Wenn Sie mit 
einen Klarnamen und ggf. Unternehmenszugehörigkeit genannt werden wollen, 
teilen Sie dies bitte in einem Kommentar zum Pull Request mit.


### Issues auf Github ###

Wenn Sie nicht über Github am Quelltext mitwirken möchten, aber einen 
Github-Account Ihr eigen nennen oder zu diesem Zweck anlegen möchten, können
Sie Sich an der **öffentlichen** Diskussion im Issue-Tracking-System unter

[https://github.com/OParl/specs/issues](https://github.com/OParl/specs/issues)

beteiligen. Dies hat den Vorteil, dass auch andere beteiligte die Einträge 
wahrnehmen und durch Kommentare dazu Stellung nehmen können. Dieser Weg 
eignet sich daher besonders zum Diskutieren von kontroversen Themen und
dem Austausch von Argumenten.

Bitte achten Sie auf diesem Weg darauf, Ihre Kommentare in möglichst kleine 
thematische Einheiten herunter zu brechen. Dadurch ermöglichen Sie, dass der
jeweilige Eintrag dem richtigen Thema zugeordnet und der Status der 
Diskussion (offen, erledigt) richtig gesetzt werden kann.


Mitwirkende
-----------

Marian Steinbach (Offenes Köln),
Felix Ebert,
Jan Erhardt,
Jens Klessmann (Fraunhofer FOKUS),
Andreas Kuckartz,
Babett Schalitz (CC e-gov),
T. Tursics (TODO: Vorname eintragen), 
Jakob Voss
