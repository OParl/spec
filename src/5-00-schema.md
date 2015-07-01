Schema  {#schema}
======

Dieses Kapitel beschreibt das Schema von OParl. Das Schema bildet das
Datenmodell der OParl-Architektur ab. Es definiert, welche Objekttypen
über eine OParl-API abgerufen werden können und welche Eigenschaften
diese Objekttypen haben dürfen und müssen. Darüber hinaus ist im Schema
auch festgelegt, in welcher Beziehung verschiedene Objekttypen zu
einander stehen.

![OParl Objekttypen: Ein Überblick](images/objekttypen_graph.png)


Übergreifende Aspekte
---------------------

### Unicode-Zeichenketten als Standard  {#unicode_zeichenketten}

Die Schema-Beschreibung gibt zu jeder Eigenschaft eines Objekttypen an,
welchen Typ der Wert dieser Eigenschaft haben muss.

Sofern keine Typ-Angabe zu einer Eigenschaft vorhanden ist, oder die
Typ-Angabe `String` oder `xsd:string` lautet, werden Unicode-Zeichenketten
als Datentyp erwartet.

### `null`-Werte und leere Listen

JSON erlaubt es grundsätzlich, Eigenschaften mit dem Wert `null` zu versehen.
Im Rahmen von OParl SOLLEN Server nach Möglichkeit davon absehen, Eigenschaften
mit dem Wert `null` auszugeben. Obligatorische Eigenschaften (in diesem Kapitel mit "ZWINGEND" markiert) DÜRFEN NICHT den Wert `null` haben.

Im Fall von Arrays erlaubt JSON grundsätzlich die Ausgabe von `[]` für leere Arrays.
Wie bei `null` wird auch hier EMPFOHLEN, auf die Ausgabe einer Eigenschaft mit dem Wert `[]` zu verzichten, sofern es sich nicht um eine obligatorische Eigenschaft handelt.

Obligatorische Eigenschaften, die als Wert eine Liste von Objekten haben können,
stellen einen Sonderfall dar. Diese können, wie im Abschnitt
[Objektlisten](#objektlisten) beschrieben, entweder ein JSON-Array oder eine
URL zum externen Abruf einer Objektliste als Wert haben. In der Praxis kann es
vorkommen, dass solche Listen leer sind. Beispielsweise könnte eine Gruppierung
neu erstellt worden sein und noch keine Sitzungstermine aufweisen. In diesem
Fall ist ein leeres Array die richtige Möglichkeit, dies auszudrücken. Da es sich
dabei um eine obligatorische Eigenschaft handelt, MUSS sie jedoch ausgegeben werden.

Beispiel:

~~~~~  {#schema_ex1 .json}
{
    "id": "https://oparl.example.org/",
    "type": "http://oparl.org/schema/1.0/Organization",
    "meeting": [],
    ...
}
~~~~~

Clients können so unmittelbar feststellen, dass zu dieser Gruppierung (noch) keine
Sitzungen vorliegen.

Ist eine Liste leer, wird EMPFOHLEN, diese NICHT über eine eigene URL anzubieten,
da so Clients eine zusätzliche Anfrage für den Abruf einer leeren Liste stellen
müssen.


### Kardinalität

Zur expliziten Unterscheidung, ob eine Eigenschaft einen einzelnen Wert
(z. B. eine Zeichenkette, eine URL, eine Zahl) oder alternativ eine Liste mit
mehreren Elementen als Wert haben darf, ist in der Schema-Beschreibung 
zu jeder Eigenschaft die *Kardinalität* angegeben. Dabei sind verschiedene
Angaben zur Eigenschaft möglich:

* 0 bis 1: OPTIONAL und MUSS NICHT gesetzt sein. Wenn sie gesetzt ist,
  DARF sie genau einen Wert haben.

* 1: MUSS gesetzt sein und genau einen Wert haben.

* 0 bis *: OPTIONAL und MUSS NICHT gesetzt sein. Wenn sie gesetzt ist,
  DARF sie beliebig viele Werte haben.

* 1 bis *: MUSS vorhanden sein, es MUSS mindestens ein Wert gesetzt sein.
  Es DÜRFEN auch mehrere Werte vorhanden sein.

Zur Ausgabe von Listen innerhalb eines Objekts sowie über eigene URLs finden sich
ausführlichere Erläuterungen im Abschnitt [Objektlisten](#objektlisten).

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

In der vorliegenden Spezifikation verwenden wir den Präfix `xsd`, um
Eigenschaften aus der XMLSchema-Spezifikation zu referenzieren.^[Der Präfix
"xsd" steht somit für die URL <http://www.w3.org/2001/XMLSchema#>]. Datums-
und Zeittyp werden entsprechend in diesem Dokument als `xsd:date` bzw.
`xsd:dateTime` bezeichnet.

### Vokabulare zur Klassifizierung  {#vokabulare_klassifizierung}

Einige Objekttypen besitzen Eigenschaften zum Zweck der Klassifizierung von Objekten.
Im Einzelnen sind dies:

* `classification` des Objekttyps [`oparl:Body`](#oparl_body)
* `classification` des Objekttyps [`oparl:Organization`](#oparl_organization)
* `fileRole` des Objekttyps [`oparl:File`](#oparl_file)
* `formOfAddress` des Objekttyps [`oparl:Person`](#oparl_person)
* `gender` des Objekttyps [`oparl:Person`](#oparl_person)
* `keyword` in mehreren Objekttypen
* `paperType` des Objekttyps [`oparl:Paper`](#oparl_paper)
* `post` des Objekttyps [`oparl:Organization`](#oparl_organization)
* `result` des Objekttyps [`oparl:AgendaItem`](#oparl_agendaitem)
* `role` des Objekttyps [`oparl:Consultation`](#oparl_consultation)
* `role` des Objekttyps [`oparl:Membership`](#oparl_membership)
* `role` des Objekttyps [`oparl:Person`](#oparl_person)
* `status` des Objekttyps [`oparl:Person`](#oparl_person)
* `title` des Objekttyps [`oparl:Person`](#oparl_person)

Beispielsweise dient die Eigenschaft `paperType` des Objekttyps `oparl:Paper`
dazu, eine Drucksache als Mitteilung, Antrag, Anfrage, Beschlussvorlage etc. zu
kennzeichnen. Hierbei kann jeweils wahlweise ein einfacher Strings (Zeichenkette)
als Wert der Eigenschaft ausgegeben werden oder eine URL.

Die folgenden Beispiele verdeutlichen die Alternativen. Zunächst die
Klassifizierung mittels String:

~~~~~  {#vokabular_ex1 .json}
{
    ...
    "paperType": "Beantwortung einer Anfrage",
    ...
}
~~~~~

Die Alternative mittels einer (fiktiven) URL:

~~~~~  {#vokabular_ex1 .json}
{
    ...
    "paperType": "http://example.com/InquiryResponse",
    ...
}
~~~~~

Grundsätzlich liegt die Wahl der genutzten Variante beim Betreiber des Systems,
wobei innerhalb eines Systems beide Varianten vermischt werden KÖNNEN.

Wird als Wert eine URL verwendet, MUSS diese auf ein JSON-LD-Objekt^[JSON-LD 1.0:
<http://www.w3.org/TR/json-ld/>] vom Typ `skos:Concept` zeigen. Dieses Objekt MUSS
eine Eigenschaft `prefLabel` besitzen, in dem die benutzerfreundliche Benennung
des Konzepts wiedergegeben wird.^[Diese Konstrukte entstammen dem _Simple Knowledge
Organization System_ (SKOS): <http://www.w3.org/2009/08/skos-reference/skos.html>]

Die vorliegende Spezifikation macht in der Regel keine Vorgaben dazu, welche
Begrifflichkeiten bei der Nutzung von Strings zu verwenden sind. Ebenso ist der
Betreiber des System frei bei der Entscheidung, welche URLs dieses nutzt.

Ein Beispiel für ein `skos:Concept` Objekt, wie es für die Eigenschaft
`status` eines Objekts vom Typ `oparl:Person` genutzt werden kann:

~~~~~  {#skosconcept_ex1 .json}
{
	"@context": {
		"prefLabel": {
			"@id": "http://www.w3.org/2004/02/skos/core#prefLabel"
		}
	},
	"@type": "http://www.w3.org/2004/02/skos/core#Concept",
	"prefLabel": "Beantwortung einer Anfrage"
}
~~~~~

Das Objekt DARF unter einer beliebigen URL abgelegt werden. Diese kann, muss
aber nicht Teil des jeweiligen OParl-Systems sein.

Sinnvoll wird die Verwendung von URLs anstelle von Strings zur Klassifizierung,
wenn mehrere Systeme auf die selben
URLs verweisen, damit also ein gemeinsames Vokabular zur Klassifizierung nutzen.
Die Verwendung eines übergreifenden Vokabulars soll dazu beitragen, dass
die automatisierte Auswertung von parlamentarischen Informationen über die
Grenzen einzelner Systeme hinweg deutlich erleichtert wird. So könnte
beispielsweise eine bestimmte Art von Drucksache über Systemgrenzen hinweg als
solche erkannt werden, wenn die Systeme auf dasselbe `skos:Concept` Objekt
verweisen.

Für die Zukunft ist geplant, dass OParl hierzu Vokabulare mit entsprechenden
SKOS-Objekten zur Verfügung stellt, die dann von Datenanbietern per URL
referenziert werden können.

Da die `skos:Concept` Objekte, die über eine URL verlinkt werden, praktisch
keinen Änderungen unterliegen, SOLLEN Clients diese Ressourcen nur selten
abrufen und das Ergebnis der Anfragen in ihrem eigenen Cache speichern. Server
SOLLEN das Caching unterstützen, indem Sie die üblichen Mechanismen von
HTTP-Headern wie `Expires` und `Max-age` nutzen.

### Herstellerspezifische Erweiterungen

Diese sind – falls tatsächlich erforderlich – mit den JSON-LD-Mitteln einfach möglich. Z. B.

~~~~~
"herstellera:newWonderProperty": "Dies ist ein Feature,
    welches noch kein anderer Hersteller bietet!",
"herstellerb:faxNumber": "012345678"
~~~~~

Das Zeichen '@' DARF NICHT als Bestandteil des Herstellerprefix verwendet werden,
um eine ggf. später aufkommende JSON-LD-Erweiterung nicht zu stören.

### URL-Pfade in den Beispielen

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
nicht in OParl festgelegt.
