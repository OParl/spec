Serialisierung mittels JSON und JSONP
-------------------------------------

Eine OParl-konforme API gibt Objekte in Form von JSON aus.
Auf Anforderung des Clients wird darüber hinaus JSONP unterstützt.

### JSON

Die Abkürzung JSON steht für "JavaScript Object Notation". Das JSON-Format ist in
RFC4627^[RFC4627: <https://tools.ietf.org/html/rfc4627>] beschrieben. Nachfolgend werden nur die
wichtigsten Definitionen übernommen, um eine Terminologie zur weiteren
Verwendung in diesem Dokument zu etablieren.

Das JSON-Format unterstützt die Ausgabe von vier verschiedenen primitiven
Datentypen:

* *Zeichenkette* (Unicode)
* *Zahl* (sowohl Ganzzahlen als auch Fließkommazahlen)
* *Wahrheitswert* (`true` oder `false`)
* *Null*

Darüber hinaus werden zwei komplexe Datentypen unterstützt:

* *Objekt*: Eine Sammlung von Schlüssel-Wert-Paaren ohne Reihenfolge, wobei der Schlüssel eine Zeichenkette sein muss und der Wert ein beliebiger Datentyp sein kann.
* *Array*: Eine geordnete Liste mit beliebigen Datentypen.

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


### JSONP

Eine Einschränkung bei der Nutzung von JSON ist das Sicherheitsmodell von
Web-Browsern. Die gängigen Browser erlauben es innerhalb von Webanwendungen nicht,
JSON-Ressourcen von Domains auszulesen, die nicht der Domain entsprechen, von der
die Webanwendung selbst geladen wurde. AnwendungsentwicklerInnen sind dadurch bei
der Implementierung von Client-Anwendungen eingeschränkt.

Diese Einschränkung gilt nicht für JSONP^[JSONP steht für "JSON with padding".
Eine formelle Spezifikation existiert nicht. Der Wikipedia-Artikel <http://en.wikipedia.org/wiki/JSONP> fasst viele Quellen zusammen.]. Durch 
JSONP wird die JSON-Notation so erweitert, dass der 
ausgegebene Code ausführbarer JavaScript-Code wird. Damit wird erreicht, dass 
der JSON-Code über die Grenzen von Domains hinweg direkt von Webanwendungen 
eingebunden werden kann.

Das folgende Beispiel verdeutlicht den Unterschied zwischen JSON und JSONP.
Zunächst ein einfaches JSON-Beispiel:

~~~~~  {#jsonp_ex1 .json}
{
    "foo": "bar"
}
~~~~~

Durch Einbettung in eine sogenannte Callback-Funktion wird daraus JSONP:

~~~~~  {#jsonp_ex2 .jsonp}
mycallback({
    "foo": "bar"
})
~~~~~

Der Name der Callback-Funktion (im Beispiel `mycallback`) wird grundsätzlich 
bei der Anfrage vom Client bestimmt, und zwar mittels URL-Parameter.

Für eine OParl-konforme Schnittstelle wird EMPFOHLEN, dass der Server die 
JSONP-Ausgabe unterstützt. Die JSONP-Ausgabe MUSS in diesem Fall für sämtliche
Abfragen möglich sein. Eine JSONP-Unterstützung nur für bestimmte Anfragen ist
nicht vorgesehen.

Der URL-Parameter, den Clients zur Aktivierung der JSONP-Ausgabe verwenden,
MUSS `callback` lauten. Der Wert des `callback`-URL-Parameters
MUSS vom Server unverändert als Callback-Funktionsname verwendet werden.

Aus Sicherheitsgründen MUSS der Client den Wert des `callback`-Parameters
aus einem eingeschränkten Zeichenvorrat bilden, erlaubt sind ausschließlich
die Klein- und Großbuchstaben von a bis z bzw. A bis Z sowie die Ziffern 
von 0 bis 9. (FRAGE: Sind Umlaute erlaubt?)

Hält sich der Client nicht an diese Einschränkung und wird ein `callback`-Parameter
mit nicht erlaubten Zeichen verwendet, SOLL der Server die Anfrage
mit einer HTTP 400 (_Bad Request_) Antwort bedienen.
