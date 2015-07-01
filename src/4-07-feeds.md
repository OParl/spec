Feeds  {#feeds}
-----

Feeds sind spezielle Arten von [Objektlisten](#objektlisten), für die
besondere Anforderungen gelten. Es werden drei verschiedene Feeds
spezifiziert:

* Der Feed *Neue Objekte*
* Der Feed *Geänderte Objekte*
* Der Feed *Entfernte Objekte*

Der Begriff "Feed" ist eine Anlehnung an die weit verbreiteten RSS-^[RSS
2.0 Specification: <http://cyber.law.harvard.edu/rss/rss.html>] oder 
Atom-Feeds^[Atom ist in RFC4287 spezifiziert: <http://www.ietf.org/rfc/rfc4287.txt>],
deren Publikationslogik im Wesentlichen auf der chronologischen
Sortierung beruht. Im Unterschied zu Atom oder RSS ist hier jedoch keine
XML-Ausgabe beabsichtigt.

Die Feeds sollen es Clients ermöglichen, schnell und ressourcenschonend
abzufragen, welche Objekte auf dem Server neu hinzugefügt, geändert oder
entfernt wurden. Damit können Clients beispielsweise schnell und einfach
neue Dokumente auffinden und verarbeiten oder entfernte Objekte aus ihren
Caches entfernen und dabei nur ein Mindestmaß an Anfragen ausführen. Die
Feeds unterstützen oder ermöglichen also die Synchronisation.

Ein OParl-Server SOLL jeden der nachfolgend beschriebenen Feeds anbieten.

Für alle drei Feeds wird EMPFOHLEN, dass mindestens ein Zeitraum von 365 Tagen
abgedeckt wird.

Da Feeds üblicherweise eine große und stetig steigende Anzahl von Objekten
beinhalten können, ist hier die [Paginierung](#paginierung) anzuwenden, wie
sie im vorigen Abschnitt über [Objektlisten](#objektlisten) beschrieben wird.

### Der Feed "Neue Objekte"  {#feed_neue_objekte}

Der Feed für neue Objekte listet die URLs neu hinzugekommener Objekte in
der Reihenfolge des Datums ihrer Erstellung, wobei die jüngsten Objekte
zuerst ausgegeben werden.

Die Definition, was ein "neues" Objekt bzw. die "Erstellung" bedeutet, kann
zwischen Systemen und Objekttypen variieren. So werden bestimmte Objekte
in einigen Systemen zunächst erstellt und erst dann für die Öffentlichkeit
freigegeben. In diesem Fall ist im Sinne dieses Feeds die Freigabe als
Zeitpunkt der Erstellung zu verwenden.

Der Feed SOLL sämtliche Objekttypen umfassen, die in einem System geführt
werden.

Das nachstehende Beispiel zeigt die mögliche Ausgabe des Feeds:

~~~~~  {#feed_ex1 .json}
{
    "items": [
        {
            "id": "https://oparl.example.org/files/3",
            "type": "http://oparl.org/schema/1.0/File",
            "created": "2014-01-07T12:59:01+01:00"
        },
        {
            "id": "https://oparl.example.org/papers/21",
            "type": "http://oparl.org/schema/1.0/Paper",
            "created": "2014-01-05T18:29:37+01:00"
        },
        {
            "id": "https://oparl.example.org/files/5",
            "type": "http://oparl.org/schema/1.0/File",
            "created": "2014-01-04T11:26:48+01:00"
        },
        ...
    ],
    "itemsPerPage": ...,
    "nextPage": ...
}
~~~~~

Die Funktionsweise entspricht grundsätzlich der von gewöhnlichen Listen
mit Paginierung, wie im Kapitel [Objektlisten](#objektlisten) beschrieben.

Davon abweichend gibt der Feed zu jedem neuen Objekt in der Liste unter
`items` ein JSON-Objekt mit drei Eigenschaften aus:

* `id`: Die URL des neuen Objekts
* `type`: Die URL des Typs des neuen Objekts
* `created`: Der Zeitpunkt der Erzeugung des Objekts

Der jeweils in der Eigenschaft `created` ausgegebene Zeitpunkt SOLL vom Server
als Sortierkriterium des Feeds genutzt werden.

### Der Feed "Geänderte Objekte"  {#feed_geaenderte_objekte}

Der Feed für geänderte Objekte listet die URLs geänderter Objekte in
der Reihenfolge des Datums ihrer Änderung, wobei das zuletzt geänderte Objekt
zuerst ausgegeben wird.

Die Definition einer "Änderung" kann sich zwischen den Objekttypen
unterscheiden. Tendenziell soll die Definition eher weiter ausgelegt werden,
als enger. Als Änderung einer Gruppierung (oparl:Organization) könnte es beispielsweise
verstanden werden, wenn eine neue Mitgliedschaft zur Organisation hinzukommt.
Das Erstellen eines Objekts (im Sinne des Feeds "Neue Objekte") sollte
hingegen nicht als Änderung gewertet werden, um das redundante Erscheinen
eines neuen Objekts sowohl im Feed "Neue Objekte" als auch im Feed "Geänderte
Objekte" zu vermeiden.

Auch hier SOLL der Feed sämtliche Objekttypen umfassen, die in einem System 
geführt werden.

~~~~~  {#feed_ex2 .json}
{
    "items": [
        {
            "id": "https://oparl.example.org/files/2",
            "type": "http://oparl.org/schema/1.0/File",
            "modified": "2014-01-08T14:28:31+01:00"
        },
        {
            "id": "https://oparl.example.org/papers/0",
            "type": "http://oparl.org/schema/1.0/Paper",
            "modified": "2014-01-08T12:14:27+01:00"
        },
        {
            "id": "https://oparl.example.org/files/1",
            "type": "http://oparl.org/schema/1.0/File",
            "modified": "2014-01-06T17:01:00+01:00"
        },
    ],
    "itemsPerPage": ...,
    "nextPage": ...
}
~~~~~

Das Ausgabeformat entspricht weitgehend dem des Feeds "Neue Objekte", jedoch
heißt hier die Eigenschaft für den Zeitpunkt der letzten Änderung `modified`. 
Entsprechend gilt, dass der als `modified` ausgegebene Zeitpunkt als
Sortierkriterium der Liste gelten SOLL.

### Der Feed "Entfernte Objekte" ### {#feed_entfernte_objekte}

Der Feed für entferne Objekte listet die URLs entfernter Objekte in
der Reihenfolge des Datums ihrer Entfernung auf, wobei die zuletzt entfernten 
Objekte zuerst ausgegeben werden.

Mit "Entfernung" ist im Sinne dieses Feeds die Löschung eines Objekts, aber
auch die Depublikation oder das Beenden der öffentlichen Verfügbarkeit gemeint.

Client-Implementierer sind angehalten, diesen Feed zu nutzen, um beispielsweise
depublizierte Drucksachen aus ihren lokalen Caches zu entfernen.

~~~~~  {#feed_ex3 .json}
{
    "items": [
        {
            "id": "https://oparl.example.org/people/22",
            "removed": "2013-11-11T11:11:00+01:00"
        },
        ...
    ],
    "itemsPerPage": ...,
    "nextPage": ...
]
~~~~~

Die Eigenschaft zur Angabe des Entfernungszeitpunkts heißt hier `removed` und
SOLL, analog zu den beiden anderen Feeds, als Sortierkriterium der Liste
verwendet werden.

Im Unterschied zu den beiden zuvor beschriebenen Feeds wird im Feed "Gelöschte
Objekte" keine Eigenschaft `type` am jeweiligen Objekt ausgegeben.

Clients SOLLEN anhand dieser Informationen in der Lage sein, gecachte Objekte
aus ihrem Cache zu entfernen. Entsprechend sollten Caches so beschaffen sein,
dass ihre Informationen auf die URLs der jeweiligen Objekte zurück zu führen
sind. Insbesondere im Fall von Dateien (Objekte des Typs `oparl:File`) ist
darauf zu achten, dass gecachte Dateien mit der URL des `oparl:File`-Objekts
assoziiert sind.

Clients SOLLEN vermeiden, die URLs der jeweiligen Einträge im Feed
"Entfernte Objekte" erneut aufzurufen.
