# Schema {#schema}

Dieses Kapitel beschreibt das Schema von OParl. Das Schema definiert 
die Objekttypen und ihre Eigenschaften. Darüber hinaus ist im Schema
auch festgelegt, in welcher Beziehung verschiedene Objekttypen zu
einander stehen.

![OParl Objekttypen: Ein Überblick](images/objekttypen_graph.png)

## Übergreifende Aspekte {#uebergreifende-aspekte}

### Vollständigkeit {#schema-vollstaendigkeit}

Alle regulär öffentlich abrufbaren Informationen **sollten** auch in OParl
ausgegeben werden, solange dies nicht den Datenschutzbestimmungen widerspricht.
Daher sind sämtliche Felder im Schema als **empfohlen** zu behandeln, wenn
nicht explizit etwas anderes angegeben wurde.


### `null`-Werte und leere Listen {#null-werte-und-leere-listen}

JSON erlaubt es grundsätzlich, Eigenschaften mit dem Wert `null` zu versehen.
Eigenschaften **sollten** nicht mit dem Wert `null` ausgegeben werden.
Obligatorische Eigenschaften **dürfen nicht** den Wert `null` haben.

Im Fall von Arrays erlaubt JSON grundsätzlich die Ausgabe von `[]` für leere
Arrays. Wie bei `null` wird auch hier **empfohlen**, auf die Ausgabe einer
Eigenschaft mit dem Wert `[]` zu verzichten. Bei obligatorische Eigenschaften
**muss** jedoch eine leere Liste ausgegeben werden.

### Datums- und Zeitangaben  {#datum_zeit}

Für Datum und Zeit werden die in XML-Schema festgelegten Typen verwendet
(was nicht bedeutet, dass in OParl XML verwendet wird).

Für ein Datum wird http://www.w3.org/TR/xmlschema-2/#date verwendet und
für eine Zeit http://www.w3.org/TR/xmlschema-2/#dateTime. Dabei wird ein
Datum (ein Tag ohne Uhrzeit) ohne Zeitzone und ein Datum mit Zeit mit
Zeitzone angegeben, denn nur damit ist die Uhrzeit weltweit eindeutig
ohne zusätzlich auf den Ort einer Sitzung o. ä. Bezug nehmen zu müssen.

Diese Spezifikationen stützen sich auf RFC 3339^[RFC3339:
<http://www.ietf.org/rfc/rfc3339.txt>]) und RFC 3339 wiederum auf ISO 8601.

### Herstellerspezifische Erweiterungen {#herstellerspezifische-erweiterungen}

In OParl können zusätzliche, herstellerspezifische Eigenschaften hinzugefügt werden.
Dazu wird diesen Eigenschaften ein Herstellerprefix vorangestellt. So könnte man z.B.
`Person` um eine Faxnummer erweitern:

~~~~~
"BeispielHersteller:faxNumber": "012345678",
~~~~~

### URL-Pfade in den Beispielen {#url-pfade-in-den-beispielen}

OParl-Clients wissen nichts vom Aufbau von Pfaden innerhalb von URLs,
müssen dies nicht wissen, und es gibt deshalb in der OParl-Spezifikation
keine Festlegungen dazu.

Wenn also in einer Beispiel-URL ein Pfad wie

    bodies/0/peoples/

auftaucht, bedeutet das nicht, dass genau solche Pfade durch
die OParl-Spezifikation vorgeschrieben sind.

Auch dies wäre als URL z. B. für eine Person verwendbar:

    https://www.ratsinfo.net/personen/?__=LfyIfvCWq8SpBQj0MiyHaxDZwGJ

Gleichzeitig ist aber aus verschiedenen Gründen ein strukturierter Aufbau
der Pfade durchaus sinnvoll, der sich an der Hierarchie der Objekte
orientiert (nicht zuletzt, weil dies Softwareentwicklern während der
Entwicklung helfen kann). Dennoch wird eine solche Struktur bewusst
nicht in OParl 1.0 festgelegt.
