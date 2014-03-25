Serialisierung mittels JSON-LD und JSONP
----------------------------------------

Eine OParl-konforme API gibt Objekte in Form von JSON aus. Die Objekte werden dabei 
entsprechend der JSON-LD Spezifikation um Kontexte erweitert, welche die
Selbstbschreibungsfähigkeit der ausgegebenen Daten verbessert. Auf Anforderung des
Clients wird darüber hinaus JSONP unterstützt.

### JSON

Die Abkürzung JSON steht für "JavaScript Object Notation". Das JSON-Format ist in
RFC4627^[<https://tools.ietf.org/html/rfc4627>] beschrieben. Nachfolgend werden nur die
wichtigsten Definitionen übernommen, um eine Terminologie zur weiteren
Verwendung in diesem Dokument zu etablieren.

Das JSON-Format unterstützt die Ausgabe von vier verschiedenen primitiven
Datentypen:

* Zeichenkette (Unicode)
* Zahl (sowohl Ganzzahlen als auch Fließkommazahlen)
* Wahrheitswert (*true* oder *false*)
* Null

Darüber hinaus werden zwei komplexe Datentypen unterstützt:

* Objekt: Eine Sammlung von Schlüssel-Wert-Paaren ohne Reihenfolge, wobei der Schlüssel eine Zeichenkette sein muss und der Wert ein beliebiger Datentyp sein kann.
* Array: Eine geordnete Liste mit beliebigen Datentypen.

Beispiel eines Objekts in JSON-Notation:

~~~~~  {#json_ex1 .json}
{
    "zeichenkette": "Das ist eine Zeichenkette",
    "zahl": 1.23456789,
    "wahrheitswert": true,
    "null": null,
    "objekt": {
    	"foo": "bar"
    },
    "array": ["foo", "bar"]
}
~~~~~


### JSON-LD

- JSON-LD: http://www.w3.org/TR/json-ld/
- Einschränkungen von OParl gegenüber JSON-LD
- Schlüssel in einem JSON-LD-Objekt müssen einzigartig sein.
- Unterscheidung von Groß- und Kleinschreibung
- Benannte Objekte (URL als Schlüssel)
- Anonyme Objekte (Blank Nodes)
- Mime Type application/ld+json
- Kompakte Form mit Verwendung externer @context-URL als SOLL-Anforderung
- Verweis auf http://www.bmi.bund.de/SharedDocs/Downloads/DE/Themen/OED_Verwaltung/ModerneVerwaltung/opengovernment.pdf?__blob=publicationFile
- Siehe https://github.com/OParl/specs/issues/77
- Siehe https://github.com/OParl/specs/issues/10

### JSONP

- TODO: Spezifikation finden/verlinken. (RFC gibt es nicht)
- https://github.com/OParl/specs/issues/67
- Zeichenvorrat für callback-Parameter beschränken auf [a-zA-Z0-9] aus Sicherheitsgründen
