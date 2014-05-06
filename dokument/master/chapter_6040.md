Serialisierung mittels JSON-LD und JSONP
----------------------------------------

Eine OParl-konforme API gibt Objekte in Form von JSON aus. Die Objekte werden dabei 
entsprechend der JSON-LD Spezifikation um Kontexte erweitert, welche die
Selbstbschreibungsfähigkeit der ausgegebenen Daten verbessert. Auf Anforderung des
Clients wird darüber hinaus JSONP unterstützt.

In jedem Fall MUSS ein Server die Anfrage eines Clients unter Verwendung des HTTP
`Content-type`-Headers `application/ld+json` beantworten. Die Spezifikation von JSON-LD
liefert dazu genauere Informationen^[JSON-LD 1.0: IANA COnsiderations: 
<http://www.w3.org/TR/json-ld/#iana-considerations>], auch zu dem optionalen Parameter `profile`
für die explizite Anforderung von JSON-LD in einer dieser drei Unterformen: kompakt,
expandiert oder flach.

Wenn der Server auch Anfragen nach `application/json` akzeptiert, dann SOLL er
expandierte JSON-LD Dokumente liefern (also solche ohne `@context`).

TODO: MUSS der Server solche Legacy-Anfragen akzeptieren? Warum?

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


### JSON-LD {#jsonld}

Das Kürzel LD im Namen "JSON-LD" steht für "Linked Data"^[siehe dazu [Linked Data](#linked_data)].
Entsprechend erweitert die JSON-LD-Spezifikation^[<http://www.w3.org/TR/json-ld/>] das JSON-Format um die Möglichkeit,

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

Am obigen Beispiel fällt auf, dass der `@context`-Teil des Objekts schon mehr Daten
umfasst, als die eigentlichen Objekteigenschaften. Sinnvollerweise kann jedoch der 
gesamte Inhalt des `@context`-Teils in eine externe Ressource ausgelagert werden. Das
folgende Beispiel verdeutlicht dies:

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
aller möglichen Attribute des Objekts aus. Die Kontext-Beschreibung des JSON-LD-Objekts
wurde somit in eine externe Ressource ausgelagert. Clients SOLLEN davon ausgehen, dass
sich diese externen Kontextbeschreibungen nur selten ändern. Somit genügt es, bei Abruf 
vieler gleichartiger JSON-LD-Objekte vom Server die Kontext-Ressource nur einmal zu laden.

Im Sinne der JSON-LD-Spezifikation sind Objekte mit eingebettetem und externem Kontext
identisch. Den Implementierern eines OParl-konformen Servers wird EMPFOHLEN, grundsätzlich
die Kontextinformation mittels externer Ressourcen zu übermitteln. Die OParl Autoren werden
hierzu die zu dieser Spezifikation passenden Ressourcen auf oparl.org für jegliche Verwendung
zur Verfügung stellen (mehr dazu im [Anhang](#jsonld_ressourcen_oparlorg)). Sollten Server-Implementierer zusätzliche Objekttypen benötigen, die nicht von dieser Spezifikation abgedeckt sind, SOLL entsprechend zusätzlich auf eigene Kontextressourcen unter geeigneten URLs verwiesen werden. Hierbei können herstellereigene und OParl-spezifische URls gemischt werden, wie in
einem Beispiel weiter unten verfeutlicht wird.

JSON-LD ermöglicht es auch, für ein Objekt einen **Objekttyp** zu kommunizieren. So könnte
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
URLs als sogenannte Vokabulare referenziert. Das eine Vokabular wird durch das 
Namensraum-Präfix `oparl` repräsentiert, das zweite (herstellereigene) durch das 
Namensraum-Präfix `vendor`.

Durch das Schlüsselwort `@type` wird nun dem Objekt ein oder mehrere Objekttypen zugewiesen.
Dabei werden die zuvor beschriebenen Namensraum-Präfixe genutzt. Ein JSON-LD-Client 
verarbeitet Namensraum-Präfixe und Typenbezeichnung so, dass diese letztlich für jeden
Objekttypen eine eindeutige URL ergeben.

* Aus `oparl:Paper` wird `http://oparl.org/schema/1.0/Paper`
* Aus `vendor:Drucksache` wird `http://www.vendor.de/oparl/schema/Drucksache`

TODO: Eventuell hier die Anforderung festhalten, dass jedes Objekt, das über eine OParl
API ausgegeben wird, das `@type`-Schlüsselwort haben MUSS. Das ist noch nicht geklärt, da
Listen hier eine Ausnahme bilden können.

Eine JSON-LD-konforme Ausgabe stellt noch weitere Anforderungen, von denen nachfolgend die 
wichtigsten zusammen gefasst werden.

* **Schlüssel MÜSSEN einzigartig sein**: Es ist nicht zulässig, in einem JSON-LD-Objekt
mehrmals den selben Schlüssel für ein Attribut zu verwenden.

* **Groß- und Kleinschreibung werden unterschieden**: Groß- und Kleinschreibung MÜSSEN
bei allen Bestandteilen eines JSON-LD-Dokuments unterschieden werden, also auch bei den
Attributnamen.

* **Listen gelten grundsätzlich als nicht sortiert**: Die JSON-Spezifikation
geht bei Listen grundsätzlich davon aus, dass diese eine Sortierung besitzen. Im Unterschied
dazu gilt für JSON-LD, dass die Reihenfolge der Werte zwischen zwei eckigen Klammern 
`[` und `]` als zufällig gilt, sofern nicht anders spezifiziert. Wer einen 
JSON-LD-Objekttyp spezifiziert, kann jedoch mittels des Schlüsselwortes `@list` kennzeichnen,
dass es sich hierbei um eine sortierte Liste handelt.

    Wo immer die OParl-Spezifikation eine stabile, nicht zufällige Sortierung von Listen 
erwartet, wird dies eigens erwähnt werden. Das OParl-JSON-LD-Vokabular wird an der 
entsprechenden Stelle das Schlüsselwort `@list` verwenden.

* **Verschachtelte Listen sind nicht möglich**: JSON-LD erlaubt keine Listen, die
wiederum Listen als Werte enthalten. TODO: [Issue 115](https://github.com/OParl/specs/issues/115).


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
