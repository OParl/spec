Einleitung
==========

Dieses Dokument wird bei seiner Fertigstellung die Spezifikation des OParl 
Schnittstellen-Standards für parlamentarische Informationssysteme 
(Ratsinformationssysteme, RIS) darstellen. Es dient damit als Grundlage für 
die Implementierung von OParl-konformen Server- und Clientanwendungen.


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

