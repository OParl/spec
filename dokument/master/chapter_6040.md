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


### JSON-LD

Das Kürzel LD im Namen "JSON-LD" steht für Linked Data. Entsprechend erweitert die JSON-LD-Spezifikation^[<http://www.w3.org/TR/json-ld/>] das JSON-Format um die Möglichkeit,

* Objekte mit anderen Objekten zu verknüpfen,
* Objekte und Eigenschaften bestimmten Typen zuzuordnen und damit
* Auskunft über die semantische Bedeutung von Objekten und Eigenschaften zu geben.

Ein Beispiel aus der JSON-LD-Spezifikation illustriert, wie JSON-LD ein Objekt um zusätzliche
semantische Informationen erweitert. Als Ausgangspunkt dient eine Personenbeschreibung in
gewöhnlichem JSON:

~~~~~  {#jsonld_ex1 .json}
{
  "name": "Manu Sporny",
  "homepage": "http://manu.sporny.org/",
  "image": "http://manu.sporny.org/images/manu.png"
}
~~~~~

Als menschlicher Betrachter kann man leicht erkennen, dass die Eigenschaft `name` den 
Namen der Person enthält, dass `homepage` die Website der Person sein könnte und dass 
`image` die URL einer Bilddatei der Person sein könnte. Ein automatisierter Client jedoch,
dem die Objekteigenschaften nicht bekannt sind, kann die Bedeutung dieser Eigenschaften
nicht entschlüsseln.

Entsprechend der JSON-LD-Spezifikation kann diese Erläuterung über die `@context`-Eigenschaft
direkt im selben Objekt, sozusagen als Unterobjekt, mitgeliefert werden:

~~~~~  {#jsonld_ex2 .json}
{
  "@context":
  {
    "name": "http://xmlns.com/foaf/0.1/name",
    "image": {
      "@id": "http://xmlns.com/foaf/0.1/img",
      "@type": "@id"
    },
    "homepage": {
      "@id": "http://xmlns.com/foaf/0.1/homepage",
      "@type": "@id"
    }
  },
  "name": "Manu Sporny",
  "homepage": "http://manu.sporny.org/",
  "image": "http://manu.sporny.org/images/manu.png"
}
~~~~~

Hier sind die Eigenschaften wie `image` einer URL wie http://schema.org/image zugewiesen.
Ein Client, der diese URL kennt, kann daraus folgern, dass über die Objekteigenschaft
`image` immer die URL eines Bildes zu finden ist. Das Schlüssel-Wert-Paar

    "@type": "@id"

sagt darüber hinaus aus, dass der Wert dieser Eigenschaft die URL eines anderen
Objekts ist^[URLs heißen in der JSON-LD-Spezifikation "IRI" (für "Internationalized
Resource Identifier"), wir verwenden hier jedoch weiterhin die Bezeichnung "URL".].
Mittels `@type`-Deklaration könnte aber auch beispielsweise eine Eigenschaft, die 
im JSON-Sinn eine Zeichenkette ist, als Datum deklariert werden.

Am obigen Beispiel fällt auf, dass der `@context`-Teil des Objects schon mehr Daten
umfasst, als die eigentlichen Objekteigenschaften. Sinnvollerweise kann jedoch der 
gesamte Inhalt des `@context`-Teils in eine externe Ressource ausgelagert werden. Clients,
die eine Vielzahl von gleichartigen Objekten laden und interpretieren wollen, müssen
diese Ressource dann nur einmal laden. Das Ergebnis könnte so aussehen:

~~~~~  {#jsonld_ex3 .json}
{
  "@context": "http://json-ld.org/contexts/person.jsonld",
  "name": "Manu Sporny",
  "homepage": "http://manu.sporny.org/",
  "image": "http://manu.sporny.org/images/manu.png"
}
~~~~~

Die `@context`-Eigenschaft hat nun als Wert eine URL. Die URL (hier: 
http://json-ld.org/contexts/person.jsonld) gibt wiederum in JSON kodiert die Beschreibung
aller möglichen Attribute des Objekts aus.

JSON-LD ermöglicht es auch, für ein Objekt einen Objekttyp zu kommunizieren. So könnte
passend zu unserem Beispiel ausgedrückt werden, um welche Art von Objekt es sich bei den
vorliegenden Daten handelt. Dazu wird die `@type`-Eigenschaft verwendet, deren Wert
eine URL ist:

~~~~~  {#jsonld_ex4 .json}
{
  "@context": "http://json-ld.org/contexts/person.jsonld",
  "@type": "http://schema.org/Person",
  "name": "Manu Sporny",
  "homepage": "http://manu.sporny.org/",
  "image": "http://manu.sporny.org/images/manu.png"
}
~~~~~

Objekte können mehreren Typen zugeordnet sein und damit die Eigenschafen mehrerer
Objekttypen nutzen. Im Fall von OParl kann diese Möglichkeit genutzt werden, um
über die API Eigenschaften auszugeben, die nicht Teil des OParl-Schemas sind.

~~~~~  {#jsonld_ex5 .json}
{
  "@context": {
  	"oparl": "http://oparl.org/schema/1.0/",
  	"vendor": "http://www.vendor.de/oparl/schema/"
  },
  "@type": ["oparl:Paper", "vendor:Drucksache"],
  "title": "Beschlussvorlage zum Haushalt",
  "created": "2013-05-29T14:17:39+02:00",
  "aktenzeichen": "ABC123"
}
~~~~~

Das Beispiel oben zeigt ein Objekt, das über die `@context`-Eigenschaft zwei verschiedene
URLs als sogenannte Vokabulare referenziert. Das eine Vokabular wird durch das Präfix `oparl`
repräsentiert, das zweite (herstellereigene) durch das Präfix `vendor`. Ein JSON-LD-Client 
setzt Präfix und Typenbezeichnung letztlich wieder zu einer URL zusammen.

* Aus `oparl:Paper` wird `http://oparl.org/schema/1.0/Paper`
* Aus `vendor:Drucksache` wird `http://www.vendor.de/oparl/schema/Drucksache`

TODO: Ab hier weiter ausformulieren

Darüber hinaus stellt JSON-LD zusätzliche Anforderungen an JSON-Daten, die in diesem Abschnitt
weiter ausgeführt werden sollen...

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

Eine Einschränkung bei der Nutzung von JSON ist das Sicherheitsmodell von
Web-Browsern. Die gängigen Browser erlauben es innerhalb von Webanwendungen nicht,
JSON-Ressourcen von Domains auszulesen, die nicht der Domain entsprechen, von der
die Webanwendung selbst geladen wurde. AnwendungsentwicklerInnen sind dadurch bei
der Implementierung von Client-Anwendungen eingeschränkt.

Diese Einschränkung gilt nicht fürt JSONP^[TODO: URL zur Spezifikation]. Durch 
JSONP (TODO: Abkürzung erläutern) wird die JSON-Notation so erweitert, dass der 
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

~~~~~  {#jsonp_ex2 .json}
mycallback({
    "foo": "bar"
})
~~~~~

Der Name der Callback-Funktion (im Beispiel "mycallback") wird grundsätzlich 
bei der Anfrage vom Client bestimmt, und zwar mittels URL-Parameter.

Für eine OParl-konforme Schnittstelle wird EMPFOHLEN, dass der Server die 
JSONP-Ausgabe unterstützt. Die JSONP-Ausgabe MUSS in diesem Fall für sämtliche
Abfragen möglich sein. Eine JSONP-Unterstzung nur für bestimmte Anfragen ist
nicht vorgesehen.

Der URL-Parameter, den Clients zur Aktivierung der JSONP-Ausgabe verwenden,
MUSS `callback` lauten. Der Wert des `callback`-URL-Parameters
MUSS vom Server unverändert als Callback-Funktionsname verwendet werden.

Aus Sicherheitsgründen MUSS der Client den Wert des `callback`-Parameters
aus einem eingeschränkten Zeichenvorrat bilden, erlaubt sind ausschließlich
die Klein- und Großbuchstaben von a bis z bzw. A bis Z sowie die Ziffern 
von 0 bis 9.

Hält sich der Client nicht an diese Einschränkung und wird ein `callback`-Parameter
mit nicht erlaubten Zeichen verwendet, SOLL der Server die Anfrage
mit einer HTTP XXX (Bad Request) Antwort bedienen. (TODO: Status Code einfügen
oder prüfen, welche HTTP-Antwort die geeignetste ist.)

- TODO: Spezifikation finden/verlinken. (RFC gibt es nicht)
- https://github.com/OParl/specs/issues/67
