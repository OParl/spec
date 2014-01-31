Architektur
===========

In diesem Abschnitt werden grundlegenden Konzepte, die von OParl abgedeckt
werden, erläutert. Die Erläuterungen sind nicht im engeren Sinne Teil der
Spezifikation, sondern dienen dazu, die Anwendungsbereiche von OParl und die
Funktionen einer OParl-konformen API verständlicher und konkreter beschreiben
zu können.

Überblick
---------

TODO: Architekturdiagramm einbinden


Parlamentarisches Informationssystem
------------------------------------

Parlamentarische Informationssysteme sind Software-Systeme, die von
verschiedensten Körperschaften eingesetzt werden, um die Zusammenarbeit
von Parlamenten zu organisieren, zu dokumentieren und öffentlich nachvollziehbar
zu machen.

Im kommunalen Umfeld in Deutschland, wo das Parlament je nach Art der Kommune
häufig als Stadtrat oder Gemeinderat bezeichnet wird, hat sich für diese Art
von Informationssystem auch der Begriff "Ratsinformationssystem" (kurz "RIS")
etabliert.

Parlamentarische Informationssysteme sind jedoch nicht auf die kommunale Ebene
begrenzt. Ähnliche Systeme werden auch auf Ebene z.B. von Landkreisen,
Regierungsbezirken und diversen Zweckverbänden eingesetzt.

Diese Systeme unterstützen in der Regel mehrere der folgenden Funktionen:

* Das Erzeugen, Bearbeiten und Darstellen von Sitzungen und deren Tagesordnung
* Das Erzeugen und Abrufen von Sitzungsprotokollen
* Das Erzeugen, Bearbeiten und Anzeigen von Drucksachen
* Das Erzeugen, Bearbeiten und Anzeigen von Gremien und deren Mitgliedern

Funktionen, die die Eingabe und Bearbeitung von Daten betreffen, sind in der
Regel einem geschlossenen Nutzerkreis vorbehalten. Die Darstellung und der Abruf
von Informationen und Dokumenten hingegen ist in vielen Fällen für die
Öffentlichkeit freigegeben.

Die OParl Spezifikation beschreibt eine Schnittstelle, die den maschinellen,
lesenden Zugriff auf derartige Informationen ermöglicht.

Server
------

Der Server im Sinne dieser Spezifikation ist ein Software-Dienst, der auf einem
mit dem Internet verbundenen Rechnersystem läuft. Dieser Dienst ist eine spezielle
Form eines WWW- bzw. HTTP(S)-Servers. Entsprechend beantwortet der Server
HTTP-Anfragen, die an ihn auf einem bestimmten TCP-Port gestellt werden.

API
---

Der Begriff API steht in diesem Dokument für die Webservice-Schnittstelle, die der
Server anbietet. Die Schnittstelle basiert auf dem HTTP-Protokoll. Mittels HTTPS
ist wahlweise auch die verschlüsselte Nutzung der API möglich, sofern Server dies
unterstützt.

Client
------

Cache
-----

Nutzer
------

