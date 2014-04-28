Schema
======

Dieses Kapitel beschreibt das Schema von OParl. Das Schema bildet das
Datzenmodell der OParl-Architektur ab. Es definiert, welche Objekttypen
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

### Datums- und Zeitangaben

Für Datum und Zeit werden die in XML Schema festgelegten Typen verwendet (was nicht bedeutet, dass in OParl XML verwendet wird).

Für ein Datum wird http://www.w3.org/TR/xmlschema-2/#date verwendet und für eine Zeit http://www.w3.org/TR/xmlschema-2/#dateTime. Dabei wird ein Datum (ein Tag ohne Uhrzeit) ohne Zeitzone und ein Datum mit Zeit mit Zeitzone angegeben, denn nur damit ist die Uhrzeit weltweit eindeutig ohne zusätzlich auf den Ort einer Sitzung o.ä. Bezug nehmen zu müssen.

Diese Spezifikationen stützen sich auf RFC 3339 (http://www.ietf.org/rfc/rfc3339.txt) und RFC 3339 wiederum auf ISO 8601.

Im JSON-LD Kontext von OParl ist der Präfix 'xsd' so spezifiziert, dass Datums- und Zeittyp durch 'xsd:date' bzw. 'xsd:dateTime' abgekürzt werden können.

### Präfixe in Kontexten

Die Beispiel-Kontexte verwenden eine Reihe von Präfixen. Diese sind hier zusammengestellt und werden in den einzelnen Beispiel-Kontexten nicht jeweils wiederholt:

~~~~~  {#pcontext_praefixe .json}
    "beispielris": "http://beispielris.de/",
    "oparl": "http://oparl.org/xyz/",
    "dc": "http://purl.org/dc/terms/",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "vcard": "http://www.w3.org/2006/vcard/ns#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
~~~~~
