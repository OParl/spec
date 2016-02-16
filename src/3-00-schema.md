# Schema {#schema}

Dieses Kapitel beschreibt das Schema von OParl. Das Schema bildet das
Datenmodell der OParl-Architektur ab. Es definiert, welche Objekttypen
über eine OParl-API abgerufen werden können und welche Eigenschaften
diese Objekttypen haben dürfen und müssen. Darüber hinaus ist im Schema
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
Im Rahmen von OParl **sollten** Eigenschaften nicht mit dem Wert `null`
ausgegeben werden. Obligatorische Eigenschaften **dürfen nicht** den Wert
`null` haben.

Im Fall von Arrays erlaubt JSON grundsätzlich die Ausgabe von `[]` für leere
Arrays. Wie bei `null` wird auch hier **empfohlen**, auf die Ausgabe einer
Eigenschaft mit dem Wert `[]` zu verzichten, sofern es sich nicht um eine
obligatorische Eigenschaft handelt.

Obligatorische Eigenschaften, die als Wert eine Liste von Objekten haben können,
stellen einen Sonderfall dar. Diese können, wie im Abschnitt
[Objektlisten](#objektlisten) beschrieben, entweder ein JSON-Array oder eine
URL zum externen Abruf einer Objektliste als Wert haben. In der Praxis kann es
vorkommen, dass solche Listen leer sind. Beispielsweise könnte eine Gruppierung
neu erstellt worden sein und noch keine Sitzungstermine aufweisen. In diesem
Fall ist ein leeres Array die richtige Möglichkeit, dies auszudrücken. Da es sich
dabei um eine obligatorische Eigenschaft handelt, **muss** sie jedoch ausgegeben werden.

Beispiel:

~~~~~  {#schema_ex1 .json}
{
    "id": "https://oparl.example.org/",
    "type": "https://oparl.org/schema/1.0/Organization",
    "meeting": [],
    ...
}
~~~~~

Clients können so unmittelbar feststellen, dass zu dieser Gruppierung (noch) keine
Sitzungen vorliegen.

Ist eine Liste leer, wird **empfohlen**, diese **nicht** über eine eigene URL anzubieten,
da so Clients eine zusätzliche Anfrage für den Abruf einer leeren Liste stellen
müssen.


### Kardinalität {#kardinalitaet}

Ob eine Eigenschaft ein einzelner Wert oder eine Liste aus mehreren Werten ist,
kann im Schema an Spalte `Typ` erkannt werden:

* Der Typ array mit dem Zusatz **zwingend** beschreibt ein JSON-Array mit mindestens einem
  Wert, somit einer Kardinalität von 1 - n.

* Der Typ array ohne den Zusatz **zwingend** beschreibt ein JSON-Array ohne Mindestanzahl
  von Werten, somit einer Kardinalität von 0 - n.

* Alle anderen Typen (object, string, integer, boolean) mit dem Zusatz **zwingend** beschreiben
  den genannten Typus mit exakt einem Wert, d.h. einer Kardinalität von 1.
  
* Alle anderen Typen (object, string, integer, boolean) ohne den Zusatz **zwingend** beschreiben
  den genannten Typus mit keinem oder einem Wert, d.h. einer Kardinalität von 0 - 1
  
Liegen keine Information zu dem Attribut vor, so **muss** das Attribut entfernt werden.
Dies ist bei allen inhaltlichen Attributen möglich, die nicht mit `**zwingend**` markiert
sind.


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

Diese sind – falls tatsächlich erforderlich – mit einem Herstellerprefix einfach möglich. Z. B.

~~~~~
"herstellera:newWonderProperty": "Dies ist ein Feature,
    welches noch kein anderer Hersteller bietet!",
"herstellerb:faxNumber": "012345678"
~~~~~

Das Zeichen '@' **darf nicht** als Bestandteil des Herstellerprefix verwendet werden,
um eine ggf. später aufkommende JSON-LD-Erweiterung nicht zu stören.

### URL-Pfade in den Beispielen {#url-pfade-in-den-beispielen}

OParl-Clients wissen *nichts* vom Aufbau von Pfaden innerhalb von URLs,
müssen dies nicht wissen, und es gibt deshalb in der OParl-Spezifikation
*keine* Festlegungen dazu.

Wenn der Betreiber eines OParl-Systems beispielsweise meint, dass eine
Person eine eigene Domain verdient, dann ist dies aus Sicht der OParl-Spezifikation
völlig in Ordnung:

    https://ratsherr-mustermann.example.org/

Noch etwas extremer: selbst eine eigene Domain für jedes einzelne
OParl-Objekt würde der OParl-Spezifikation nicht widersprechen.

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
