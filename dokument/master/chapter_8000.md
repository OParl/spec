Schema
======

Dieses Kapitel beschreibt das Schema von OParl. Das Schema bildet das
Datenmodell der OParl-Architektur ab. Es definiert, welche Objekttypen
über eine OParl-API abgerufen werden können und welche Eigenschaften
diese Objekttypen haben dürfen und müssen. Darüber hinaus ist im Schema
auch festgelegt, in welcher Beziehung verschiedene Objekttypen zu
einander stehen.


Übergreifende Aspekte
---------------------

### Unicode-Zeichenketten als Standard

Wenn in der nachfolgenden Schema-Beschreibung nicht anders angegeben, werden bei
den Werten grundsätzlich Unicode-Zeichenketten (Strings) erwartet.

### null-Werte

JSON erlaubt es grundsätzlich, dass Eigenschaften den Wert `null` haben können.
Im Rahmen dieser Spezifikation DARF das jedoch nur bei Eigenschaften der Fall sein,
die als OPTIONAL oder EMPFOHLEN gekennzeichnet sind. ZWINGENDE Eigenschaften müssen
einen Wert ungleich `null` besitzen.

### Kardinalität

Viele Eigenschaften erlauben es, entweder einen einzelnen Wert (z.B. eine Zeichenkette,
eine URL, eine Zahl) oder alternativ ein JSON-Array mit mehreren Elementen des
jeweils erlaubten Typs auszugeben. Die entsprechende Regel ist in der Schema-Beschreibung
am Stichwort _Kardinalität_ angegeben. Dabei sind verschiedene Angaben möglich:

* 0 bis 1: Die Eigenschaft ist optional und muss nicht gesetzt sein. Wenn sie gesetzt ist,
  darf sie genau einen Wert haben.

* 1: Die Eigenschaft muss gesetzt sein,
  sie muss genau einen Wert haben.

* 0 bis *: Die Eigenschaft ist optional und muss nicht gesetzt sein. Wenn sie gesetzt ist,
  darf sie beliebig viele Werte haben.

* 1 bis *: Die Eigenschaft muss vorhanden sein, es muss mindestens ein Wert gesetzt sein.
  Es dürfen auch mehrere Werte vorhanden sein.

### Datums- und Zeitangaben

Für Datum und Zeit werden die in XML Schema festgelegten Typen verwendet
(was nicht bedeutet, dass in OParl XML verwendet wird).

Für ein Datum wird http://www.w3.org/TR/xmlschema-2/#date verwendet und
für eine Zeit http://www.w3.org/TR/xmlschema-2/#dateTime. Dabei wird ein
Datum (ein Tag ohne Uhrzeit) ohne Zeitzone und ein Datum mit Zeit mit
Zeitzone angegeben, denn nur damit ist die Uhrzeit weltweit eindeutig
ohne zusätzlich auf den Ort einer Sitzung o.ä. Bezug nehmen zu müssen.

Diese Spezifikationen stützen sich auf RFC 3339^[RFC3339:
<http://www.ietf.org/rfc/rfc3339.txt>]) und RFC 3339 wiederum auf ISO 8601.

Im JSON-LD Kontext von OParl ist der Präfix `xsd` so spezifiziert, dass 
Datums- und Zeittyp durch `xsd:date` bzw. `xsd:dateTime` abgekürzt werden 
können.

### Mehrsprachigkeit

Für Texte in OParl-Objekten ist durchgehend vorgesehen, dass diese 
mehrsprachig sein können. JSON-LD sieht das Schlüsselwort
`@language` vor, um zu einem Attribut mehrere Werte in bestimmten
Sprachen zu definieren. Diesen Mechanismus SOLLEN Server-Implementierer
nutzen, um Mehrsprachigkeit von Inhalten zu realisieren.

In den von OParl bereitgestellten JSON-LD-Kontexten ist die Deutsche Sprache
(Kürzel `de`) für sämtliche Texteigenschaften voreingestellt. Das `@language`
Stichwort SOLL daher nur dann eingesetzt werden, wenn ein Inhalt nicht
deutschsprachig ist.

### Präfixe in Kontexten

Die Beispiel-Kontexte verwenden eine Reihe von Präfixen. Diese sind hier
zusammengestellt und werden in den einzelnen Beispiel-Kontexten nicht
jeweils wiederholt:

~~~~~  {#pcontext_praefixe .json}
    "beispielris": "https://oparl.beispielris.de",
    "oparl": "http://oparl.org/specs/1.0/",
    "dc": "http://purl.org/dc/terms/",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "vcard": "http://www.w3.org/2006/vcard/ns#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "ogc": "http://www.opengis.net/ont/geosparql#",
~~~~~

### Herstellerspezifische Erweiterungen

Diese sind - falls tatsächlich erforderlich - mit den JSON-LD Mitteln einfach möglich. z.B.

~~~~~
"herstellera:newWonderProperty": "Dies ist ein Feature
    welches noch kein anderer Hersteller bietet!"
~~~~~

### URL-Pfade in den Beispielen

OParl-Clients wissen *nichts* vom Aufbau von Pfaden innerhalb von URLs,
müssen dies nicht wissen und es gibt deshalb in der OParl-Spezifikation
*keine* Festlegungen dazu.

Wenn der Betreiber eines OParl-Systems beispielsweise meint, dass eine
Person eine eigene Domain verdient, dann ist dies aus Sicht der OParl-Spezifikation
völlig in Ordnung:

~~~~~~~~~~
https://ratsmitglied-max-mustermann.beispielris.de/mein-oparl-datensatz
~~~~~~~~~~

Noch etwas extremer: selbst eine eigene Domain für jedes einzelne 
OParl-Objekt würde der OParl-Spezifikation nicht widersprechen.

Wenn also in einer Beispiel-URL so etwas wie

~~~~~~~~~~
bodies/0/peoples/
~~~~~~~~~~

auftaucht, dann bedeutet das nicht, dass genau solche Pfade durch
die OParl-Spezifikation vorgeschrieben sind.

Auch dies wäre als absoluter Link z.B. für eine Person verwendbar:

~~~~~~~~~~
https://www.ratsinfomanagement.net/personen/?__=LfyIfvCWq8SpBQj0MiyHaxDZwGJ
~~~~~~~~~~

Dies käme dann als relativer Link für die Person in Frage:

~~~~~~~~~~
personen/?__=LfyIfvCWq8SpBQj0MiyHaxDZwGJ
~~~~~~~~~~

oder auch z.B. dies
~~~~~~~~~~
LfyIfvCWq8SpBQj0MiyHaxDZwGJ
~~~~~~~~~~

Gleichzeitig ist aber aus verschiedenen Gründen ein strukturierter Aufbau
der Pfade durchaus sinnvoll, der sich an der Hierarchie der Objekte
orientiert (nicht zuletzt, weil dies Softwareentwicklern während der
Entwicklung helfen kann). Dennoch wird eine solche Struktur bewusst
nicht in OParl festgelegt.
