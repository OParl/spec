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


Motivationen für den standardisierten Datenzugriff
--------------------------------------------------

Die Gründe, warum Betreiber von parlamentarischen Informationssystemen den
Zugriff darauf über eine standardisierte Schnittstelle ermöglichen sollten,
können vielfältig sein.

Ein zentrales Argument ist die Verpflichtung der Parlamente gegenüber der
Bevölkerung, diese über die Fortschritte der parlamentarischen Arbeit zu
informieren und auf dem Laufenden zu halten. Ein erster Schritt, der
Bevölkerung Einblicke in die Arbeit und Zugriff auf Dokumente zu gewähren,
ist vielerorts in den letzten Jahren durch Einführung von Ratsinformationssystemen
mit anonymem, lesenden Zugriff über das World Wide Web gemacht worden.

Die damit eingeschlagene Richtung konsequent weiter zu gehen, bedeutet, die
Daten der parlamentarischen Informationssystemen gänzlich offen zu legen,
sofern die Inhalte es erlauben. Es bedeutet, die Daten und Inhalte so
universell weiterverwendbar und so barrierearm wie möglich anzubieten, dass
jegliche weitere Verwendung durch Dritte technisch möglich ist. Der seit
einiger Zeit etablierte Begriff für dieses Prinzip heißt "Open Data".

Das Interesse an parlamentarischen Informationen und an Anwendungen, die diese
nutzbar und auswertbar machen, ist offensichtlich vorhanden. Die Entwickler
der alternativen Ratsinformationssysteme wie Frankfurt Gestalten[14], Offenes 
Köln[15] oder der OpenRuhr:RIS-Instanzen[16] wissen zu berichten, wie viel
Interesse den Projekten gerade aus Orten entgegen gebracht wird, in denen
derartige Systeme noch nicht verfügbar sind.

Die Anwendungsmöglichkeiten für parlamentarische Informationen, wenn sie über
eine Schnittstelle schnell und einfach abgerufen werden können, sind vielfältig.
Beispiele könnten sein:

* Apps für den Abruf auf mobilen Endgeräten
* Möglichkeiten zur Wiedergabe für Nutzerinnen und Nutzer mit Beeinträchtigung des Sehvermögens
* Alternative und erweiterte Suchmöglichkeiten in Inhalten
* Auswertung und Analyse von Themen, Inhalten, Sprache etc.
* Benachrichtigungsfunktionen beim Erscheinen bestimmte Inhalte

Die Standardisierung dieses Zugriffs über die Grenzen einzelner Systeme hinweg
erlaubt zudem, diese Entwicklungen grenzüberschreitend zu denken. Damit steigt
nicht nur die potenzielle Nutzerschaft einzelner Entwicklungen. Auch das
Potenzial für Kooperationen zwischen Anwendungsentwicklern wächst.

Darüber hinaus sind auch Motivationen innerhalb von Organisationen und Körperschaften
erkennbar. So sollen parlamentarische Informationssysteme vielerorts in
verschiedenste Prozesse und heterogene Systemlandschaften integriert werden. Durch
eine einheitliche Schnittstelle bieten sich effiziente Möglichkeiten zur Integration
der Daten in anderen Systeme, wie beispielsweise Web-Portale.


Funktionsumfang der OParl-Schnittstelle
---------------------------------------

Die vorliegende Spezifikation soll eine Webservice-Schnittstelle definieren, 
die den anonymen und lesenden Zugriff auf öffentliche Inhalte aus 
Parlamentarischen Informationssystemen ermöglicht. Die Zugriffe erfolgen 
über das Hypertext Transfer Protocol (HTTP). Daten werden als JSON oder als
JSONP ausgeliefert.

Die Spezifikation wird obligatorische Bestandteile (MUSS) und optionale 
Bestandteile (KANN) haben. Der tatsächliche Funktionsumfang kann daher 
zwischen den Implementierungen variieren.


Status
------

Die Spezifikation befindet sich in Arbeit. Das Dokument enthält entsprechend 
viele Ungenauigkeiten und Hinweise auf offene Fragestellungen.



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
