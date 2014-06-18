Serialisierung mittels JSON-LD und JSONP
----------------------------------------

Eine OParl-konforme API gibt Objekte in Form von JSON aus. Die Objekte werden dabei 
entsprechend der JSON-LD-Spezifikation um Kontexte erweitert, welche die
Selbstbeschreibungsfähigkeit der ausgegebenen Daten verbessert. Auf Anforderung des
Clients wird darüber hinaus JSONP unterstützt.

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

OParl nutzt JSON-LD als Ausgabeformat. In diesem Abschnitt werden einige
grundlegenden Prinzipien von JSON-LD erläutert. Im nächsten Abschnitt werden
dann spezifische Anforderungen an JSON-LD im Einsatz für OParl beschrieben.

Das Kürzel *LD* im Namen *JSON-LD* steht für *Linked Data*^[siehe dazu [Linked Data](#linked_data)].
Entsprechend erweitert die JSON-LD-Spezifikation^[JSON-LD 1.0: 
<http://www.w3.org/TR/json-ld/>] das JSON-Format um die Möglichkeit,

* Objekte mit anderen Objekten zu verknüpfen,
* Objekte und Eigenschaften bestimmten Typen zuzuordnen und damit
* Auskunft über die semantische Bedeutung von Objekten und Eigenschaften zu geben.

Ein Beispiel aus der JSON-LD-Spezifikation verdeutlicht, wie JSON-LD ein Objekt um zusätzliche
semantische Informationen erweitert. Als Ausgangspunkt dient ein gewöhnliches JSON-Objekt:

~~~~~  {#jsonld_ex1 .json}
{
  "name": "Manu Sporny",
  "homepage": "http://manu.sporny.org/",
  "image": "http://manu.sporny.org/images/manu.png"
}
~~~~~

Als menschlicher Betrachter kann man leicht erkennen, dass die Eigenschaft `name` den 
Namen der Person enthält, dass `homepage` die Website der Person sein könnte, und dass 
`image` die URL einer Bilddatei der Person sein könnte. Ein automatisierter Client jedoch,
dem die Objekteigenschaften nicht bekannt sind, kann die Bedeutung dieser Eigenschaften
nicht entschlüsseln.

Entsprechend der JSON-LD-Spezifikation kann ein solches Dokument um einen oder mehrere
sogenannte Kontexte erweitert werden. Diese lassen sich als Meta-Informationen zu den
Eigenschaften des JSON-Dokuments verstehen. Integriert werden diese Kontexte über
eine zusätzliche Eigenschaft mit dem Namen `@context`. Nachfolgend wird das zuvor
gezeigte JSON-Beispiel um einen solchen JSON-LD-Kontext erweitert:

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

Der Kontext weist jedem der Schlüssel des JSON-Dokuments weitere Informationen zu.
So wird beispielsweise die Eigenschaft `name` mit der URL `http://xmlns.com/foaf/0.1/name`
gleichgesetzt. Dies teilt dem Client mit, dass die Eigenschaft `name` dieses Objekts
dieselbe Bedeutung hat, wie die Eigenschaft `name` des FOAF
Schemas^[The Friend of a Friend (FOAF) project: <http://www.foaf-project.org/>]. 

Der Inhalt der `@context`-Eigenschaft darf laut JSON-LD-Spezifikation in eine externe
Ressource ausgelagert werden, die wiederum über eine URL eingebunden wird. Damit können
mehrere Objekte, die denselben JSON-LD-Kontext benötigen, auf eine gemeinsame
Kontext-URL verweise. Clients können diese im Cache vorhalten und nur bei Bedarf neu laden.
Das folgende Beispiel zeigt dies:

~~~~~  {#jsonld_ex3 .json}
{
    "@context": "http://json-ld.org/contexts/person.jsonld",
    "name": "Manu Sporny",
    "homepage": "http://manu.sporny.org/",
    "image": "http://manu.sporny.org/images/manu.png"
}
~~~~~

Im Sinne der JSON-LD-Spezifikation sind Objekte mit eingebettetem und externem Kontext
inhaltlich identisch.

JSON-LD ermöglicht es, für ein Objekt einen **Objekttyp** zu kommunizieren. Dazu wird
eine Eigenschaft mit dem Schlüssel `@type` gesetzt, deren Wert eine URL ist. Das
folgende Beispiel zeigt, wie mit dieser Methode das bereits gezeigte Objekt mit einem
Typ versehen wird:

~~~~~  {#jsonld_ex4 .json}
{
    "@context": "http://json-ld.org/contexts/person.jsonld",
    "@type": "http://schema.org/Person",
    "name": "Manu Sporny",
    "homepage": "http://manu.sporny.org/",
    "image": "http://manu.sporny.org/images/manu.png"
}
~~~~~

JSON-LD kennt für dieselbe Information verschiedene **syntaktische Formen**. Das obige
Beispiel zeigt die *komprimierte Form* (engl.: "Compacted Form"). Die Daten dieses
Dokuments lassen durch Anwenden des sich  Information im obigen Beispiel ließe sich mit
der in JSON-LD-Spezifikation als *Expanded Form* (hier: *expandierte Form*) bezeichneten
Form ausführlich so darstellen:

~~~~~  {#jsonld_ex5 .json}
[
    {
        "@type": [
            "http://schema.org/Person"
        ],
        "http://xmlns.com/foaf/0.1/homepage": [
            {
                "@id": "http://manu.sporny.org/"
            }
        ],
        "http://xmlns.com/foaf/0.1/img": [
            {
                "@id": "http://manu.sporny.org/images/manu.png"
            }
        ],
        "http://xmlns.com/foaf/0.1/name": [
            {
                "@value": "Manu Sporny"
            }
        ]
    }
]
~~~~~

Wie zu sehen ist, entfällt in der expandierten Form die `@context`-Eigenschaft.
Sämtliche für das Objekt relevanten Informationen aus dem Kontext sind stattdessen 
direkt in das Objekt selbst eingebunden. Beispielsweise trägt der Schlüssel, der in
der komprimierten Form `name` heißt, hier die ausführliche URL 
`http://xmlns.com/foaf/0.1/name` als Namen, wie es der Gleichsetzung im Kontext,
weiter oben beschrieben, entspricht.

Die obige Darstellung der expandierten Form zeigt auch, dass alle Eigenschaften
in JSON-LD als Arrays interpretiert werden, also mehrere Werte haben können.

Zuvor wurde gezeigt, wie die Namen von Eigenschaften in JSON-LD-Objekten tatsächlich
URLs sind, die in der komprimierten Form mit Hilfe der Kontext-Informationen gegen
kürzere Namen ausgetauscht werden. Auch auf der Seite der Werte von Eigenschaften
gibt es in JSON-LD die Möglichkeit, ausführliche URLs zu verkürzen und somit die
Ausgabe kompakter oder leserlicher zu gestalten. Hierzu dienen **Präfixe**.

Diese Präfixe werden im JSON-LD-Kontext definiert und können dann sowohl in den
Schlüsseln (Namen) als auch den Werten von Eigenschaften eingesetzt werden. Eine
Präfix-Definition kann beispielsweise so aussehen:

~~~~~
    "foaf": "http://xmlns.com/foaf/0.1/"
~~~~~

An anderer Stelle kann der so definierte Präfix `foaf` so eingesetzt werden, um
die URL `http://xmlns.com/foaf/0.1/name` zu repräsentieren:

~~~~~
    "foaf:name"
~~~~~

Die JSON-LD-Spezifikation stellt noch weitere Anforderungen, von denen nachfolgend
die wichtigsten zusammengefasst werden.

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

* **Listen DÜRFEN NICHT verschachtelt werden**: JSON-LD erlaubt keine Listen, die
wiederum Listen als Werte enthalten.


### JSON-LD in OParl {#jsonld_oparl}

Ein OParl-Server MUSS in der Regel als Antwort auf eine Anfrage ein valides
JSON-LD-Objekt ausgeben. Ausnahmen von dieser Regel sind:

* Zugriffe auf Dateien (vgl. [Dateizugriffe](#dateizugriff))
* Fehlerfälle, in denen der Server kein Objekt ausgeben kann
  (vgl. [Ausnahmebehandlung](#ausnahmebehandlung))

Jede Anfrage eines Clients, die mit einem JSON-LD-Objekt beantwortet wird,
MUSS unter Verwendung des HTTP `Content-Type`-Headers `application/ld+json`
beantwortet werden.

Im Abschnitt [Schema](#schema) der Spezifikation werden die von OParl
definierten Objekttypen beschrieben. Zur eindeutigen Kennzeichnung über
die `@type`-Eigenschaft wird jeder Objekttyp mit einer eigenen URL versehen.
Z. B. wird der Objekttyp für eine Körperschaft (Body) durch die URL

~~~~~
    http://oparl.org/schema/1.0/Body
~~~~~

gekennzeichnet^[Eine vollständige Liste ist im Anhang
[JSON-LD-Ressourcen auf oparl.org](#jsonld_ressourcen_oparlorg) zu finden.].
So erkennen Clients leicht, welche Informationen sie in einem Objekt erwarten
können und welche Eigenschaften verpflichtend gesetzt sein müssen. Ein Server
MUSS deshalb den Typ des Objekts durch Ausgabe der entsprechenden URL angeben.

Ferner werden unter `oparl.org` für jeden Objekttypen eigene
Kontext-Ressourcen vorgehalten, die Auskunft über die Bedeutung der Eigenschaften
des jeweiligen Objekttyps geben. Auch diese werden im Anhang aufgelistet. Ein
Server MUSS von diesen Ressourcen durch Einbindung ihrer URLs im `@context`-Teil
Gebrauch machen.

Diese auf `oparl.org` vorgehaltenen Kontext-Ressourcen enthalten auch grundsätzlich
die folgenden Definitionen von URL-Präfixen:

Präfix       |URL                                    |Bedeutung
-------------|-------------------------------------- |-------------
`oparl`      |`http://oparl.org/specs/1.0/`          |
`dc`         |`http://purl.org/dc/terms/`            |Dublin Core
`dcat`       |`http://www.w3.org/ns/dcat#`           |Data Catalog Vocabulary (DCAT)^[Data Catalog Vocabulary (DCAT), W3C Recommendation: <http://www.w3.org/TR/vocab-dcat/>, DCAT application profile for data portals in Europe: <https://joinup.ec.europa.eu/asset/dcat_application_profile/description>
]
`foaf`       |`http://xmlns.com/foaf/0.1/`           |Friend Of A Friend
`prov`       |`http://www.w3.org/ns/prov#`           |PROV Ontology^[PROV-O: The PROV Ontology, W3C Recommendation: <http://www.w3.org/TR/prov-o/>]
`schmorg`    |`http://schema.org/`                   |
`skos`       |`http://www.w3.org/2004/02/skos/core#` |
`vcard`      |`http://www.w3.org/2006/vcard/ns#`     |
`xsd`        |`http://www.w3.org/2001/XMLSchema#`    |
`ogc`        |`http://www.opengis.net/ont/geosparql#`|

Durch Verwendung dieser URL-Präfixe SOLLEN die entsprechenden URLs wo immer möglich
abgekürzt werden.

OParl-Server SOLLEN JSON-LD-Daten in der komprimierten Form
(engl. *compacted form*) ausgeben.

Das folgende Beispiel zeigt ein JSON-LD-Objekt zur Beschreibung eines
OParl-Systems (`oparl:System`), wie es von einem Server unter der URL
`https://oparl.example.org/` ausgegeben werden könnte:

~~~~~  {#jsonld_oparl_ex1 .json}
{
    "@id": "https://oparl.example.org/",
    "@context": [
        "http://oparl.org/schema/1.0/System",
        "https://oparl.example.org/oparl-context"
    ],
    "@type": "oparl:System",
    "oparlVersion": "http://oparl.org/specs/1.0/",
    "name": "Beispiel-System",
    "website": "http://www.example.org/",
    "contactEmail": "mailto:info@example.org",
    "contactName": "Allgemeiner OParl Kontakt",
    "vendor": "http://example-software.com/",
    "product": "http://example-software.com/oparl-server/",
    "body": "beispielris:bodies/",
    "newObjects": "beispielris:new_objects/",
    "updatedObjects": "beispielris:updated_objects/",
    "removedObjects": "beispielris:removed_objects"
}
~~~~~

Wie im Beispiel zu sehen, werden im `@context`-Teil zwei URLs eingebunden. Die eine
ist die zum jeweils ausgelieferten OParl-Objekttyp gehörige. Die zweite ist eine
vom Server bestimmte URL einer zusätzlichen Kontext-Ressource. Wie der Inhalt dieser
zusätzlichen Kontext-Ressource aussehen könnte, zeigt das folgende Beispiel:

~~~~~  {#jsonld_oparl_ex2 .json}
{
    "@context": {
        "beispielris": "https://oparl.example.org/"
    }
}
~~~~~

Hier wird ein URL-Präfix `beispielris:` definiert, das dazu dient, die ausgegebenen
URLs innerhalb dieses Systems zu verkürzen. Es wird grundsätzlich EMPFOHLEN, dass
jeder Server durch Einbindung einer eigenen Kontext-Ressource einen URL-Präfix für
die URL des eigenen Systems definiert.

Betreiber oder Implementierer von OParl-Servern haben die Möglichkeit, Objekte mit
Eigenschaften auszugeben, die nicht im Schema-Teil dieser Spezifikation beschrieben
sind. So können zusätzliche Anforderungen umgesetzt werden. Hierzu muss zum einen
ein zusätzlicher Objekttyp über die Eigenschaft `@type` angegeben werden und außerdem
die eingebundene(n) Kontext-Ressource(n) die zusätzlichen Eigenschaften beschreiben.

Für das folgende Beispiel nehmen wir an, dass der Betreiber das System-Objekt um eine
weitere Eigenschaft erweitern möchte, welche die aktuelle Uhrzeit auf dem Server
ausgibt. Das Objekt selbst könnte (verkürzt) so aussehen:

~~~~~  {#jsonld_oparl_ex3 .json}
{
    "@id": "https://oparl.example.org/",
    "@context": [
        "http://oparl.org/schema/1.0/System",
        "https://oparl.example.org/oparl-context"
    ],
    "@type": [
        "oparl:System",
        "beispielris:BeispielRisSystem"
    ],
    "oparlVersion": "http://oparl.org/specs/1.0/",
    ...
    "beispielris:currentTime": "2014-07-03T12:41:28.402+0200"
}
~~~~~

Der Inhalt der eigenen Kontext-Ressource (`https://oparl.example.org/oparl-context`)
könnte nun so aussehen:

~~~~~  {#jsonld_oparl_ex2 .json}
{
    "@context": {
        "beispielris": "https://oparl.example.org/",
        "beispielris:currentTime": {
            "@type": "xsd:dateTime"
        }
    }
}
~~~~~

Besonders zu beachten ist hier die Kombination aus zwei Angaben innerhalb der
Eigenschaft `@type`. Die Typangabe `beispielris:BeispielRisSystem` wird vom Server
frei definiert. Durch Auflösung des URL-Präfix `beispielris:` wird daraus die
URL `https://oparl.example.org/BeispielRisSystem`.

Clients DÜRFEN NICHT erwarten, dass unter einer solchen Typ-URL tatsächlich
verwertbare Informationen abrufbar sind. Die URL dient zunächst lediglich der
eindeutigen Festlegung von Objekttypen.

Bei der Definition eigener Eigenschaften über eine Kontext-Ressource DARF der
Server NICHT die bereits von OParl definierten Schlüsselwörter (URL-Präfixe,
Eigenschaften etc.) verwenden. Dies könnte, abhängig von der Reihenfolge, in der
die Kontext-Ressourcen eingebunden werden, zu einem Überschreiben der Definitionen
aus dem OParl-Kontext führen. Dies würde für Clients zu nicht vorhersagbaren
Ergebnissen führen und ist daher ausgeschlossen. Um dies zu vermeiden, wird
EMPFOHLEN, die Namen der selbst definierten Eigenschaften (die Schlüssel) mit
einem eigenen Präfix zu versehen, wie auch im obigen Beispiel gezeigt. Damit wird
auch dem Problem vorgebeugt, dass bestimmte Schlüssel von zukünftigen
OParl-Versionen vereinnamt werden und damit ein Namenskonflikt entsteht.

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
