JSON-Ausgabe
------------

Eine OParl-Server MUSS Objekte in Form von JSON ausgeben. Die Abkürzung JSON steht
für "JavaScript Object Notation". Das JSON-Format ist in
RFC4627^[RFC4627: <https://tools.ietf.org/html/rfc4627>] beschrieben. Nachfolgend werden nur die
wichtigsten Definitionen übernommen, um eine Terminologie zur weiteren
Verwendung in diesem Dokument zu etablieren.

JSON unterstützt die folgenden primitiven Datentypen:

* Zeichenketten bzw. Strings (Unicode)
* Zahlen bzw. Number (sowohl Ganzzahlen als auch Fließkommazahlen)
* Wahrheitswert bzw. Boolean (`true` oder `false`)
* `null`

Darüber hinaus werden zwei komplexe Datentypen unterstützt:

* Objekt: Eine Sammlung von Schlüssel-Wert-Paaren ohne Reihenfolge, wobei der Schlüssel eine Zeichenkette sein muss und der Wert ein beliebiger Datentyp ist.
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
