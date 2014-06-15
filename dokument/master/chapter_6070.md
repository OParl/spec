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
abgedeckt wird. (FRAGE: Wie werden Clients darüber informiert, wie weit
ein Feed zurück reicht?)

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
        "@context": {
                "beispielris": "https://oparl.example.org/",
                "hydra": "http://www.w3.org/ns/hydra/core#",
                "prov": "http://www.w3.org/ns/prov#",
                "xsd": "http://www.w3.org/2001/XMLSchema#",

                "created": {
                        "@id": "prov:generatedAtTime",
                        "@type": "xsd:dateTime"
                },
		"generatedAt": {
                        "@id": "prov:generatedAtTime",
                        "@type": "xsd:dateTime"
                },
                "member": { "@id": "hydra:member", "@type": "@id" }
        },
        "@id": "beispielris:collection2349",
// TODO: @id ZWINGEND, OPTIONAL, EMPFOHLEN ?
        "@type": "hydra:Collection",
        "generatedAt": "2014-06-11T12:59:01.038+0100",
        "member": [
		{
			"@id": "https://oparl.example.org/bodies/0/papers/21/documents/3",
			"created": "2014-01-07T12:59:01.038+0100"
		},
    		{
        		"@id": "https://oparl.example.org/bodies/0/papers/21",
        		"created": "2014-01-05T18:29:37.123+0100"
    		},
    		{
        		"@id": "https://oparl.example.org/bodies/0/papers/20/documents/5",
        		"created": "2014-01-04T11:26:48.638+0100"
    		},
...
	]
}
~~~~~

Wie im Beispiel zu sehen ist, handelt es sich um eine JSON-Liste, deren Elemente
benannte Objekte sind. Jedes der Objekte in der Liste MUSS seinerseits wiederum
zwei Eigenschaften besitzen:

* `@id`: Die URL des neuen Objekts
* `created`: Der Zeitpunkt der Erzeugung des Objekts

Der jeweils in der Eigenschaft `created` ausgegebene Zeitpunkt SOLL vom Server
als Sortierkriterium der Liste genutzt werden. So können Clients den jeweils
am Anfang der Liste vorgefundenen Zeitpunkt als Begrenzung für die zukünftige
Abfrage des Feeds nutzen. Ein Beispiel zur Erläuterung:

Am 1. April 2014 ruft ein Client den Feed ab und findet im ersten Listeneintrag
den `created`-Zeitpunkt `2014-03-31T18:02:34.058+0200` vor, den er sich als
Grenzwert merkt. Beim nächsten Abruf des Feeds einige Tage später muss der 
Client die Liste nur so weit abarbeiten, so lange der `created`-Zeitpunkt der
Einträge größer oder gleich dem Grenzwert ist.

### Der Feed "Geänderte Objekte"  {#feed_geaenderte_objekte}

Der Feed für geänderte Objekte listet die URLs geänderter Objekte in
der Reihenfolge des Datums ihrer Änderung, wobei das zuletzt geänderte Objekt
zuerst ausgegeben wird.

Die Definition einer "Änderung" kann sich zwischen den Objekttypen
unterscheiden. Tendenziell soll die Definition eher weiter ausgelegt werden,
als enger. Als Änderung einer Organisation könnte es beispielsweise
verstanden werden, wenn ein neues Mitglied zur Organisation hinzukommt.
Das Erstellen eines Objekts (im Sinne des Feeds "Neue Objekte") sollte
hingegen nicht als Änderung gewertet werden, um das redundante Erscheinen
eines neuen Objekts sowohl im Feed "Neue Objekte" als auch im Feed "Geänderte
Objekte" zu vermeiden.

Auch hier SOLL der Feed sämtliche Objekttypen umfassen, die in einem System 
geführt werden.

~~~~~  {#feed_ex2 .json}
...
    {
        "@id": "https://oparl.example.org/bodies/0/papers/0/documents/2",
        "modified": "2014-01-08T14:28:31.568+0100"
    },
    {
        "@id": "https://oparl.example.org/bodies/0/papers/0",
        "modified": "2014-01-08T12:14:27.958+0100"
    },
    {
        "@id": "https://oparl.example.org/bodies/0/papers/0/documents/1",
        "modified": "2014-01-06T17:01:00.402+0100"
    },
...
~~~~~

Das Ausgabeformat entspricht weitgehend dem des Feeds "Neue Objekte", jedoch
heißt hier die Eigenschaft für den Zeitpunkt der letzten Änderung `modified`. 
Auch hier gilt, dass der als `modified` ausgegebene Zeitpunkt auch als
Sortierkriterium der Liste gelten SOLL.

### Der Feed "Entfernte Objekte" ### {#feed_entfernte_objekte}

Der Feed für entferne Objekte listet die URLs entfernter Objekte in
der Reihenfolge des Datums ihrer Entfernung auf, wobei die zuletzt entfernten 
Objekte zuerst ausgegeben werden.

Mit "Entfernung" ist im Sinne dieses Feeds die Löschung eines Objekts, aber
auch die Depublikation oder das Beenden der öffentlichen Verfügbarkeit gemeint.

Client-Implementierer sind angehalten, diesen Feed zu nutzen, um beispielsweise
depublizierte Dokumente aus ihren lokalen Caches zu entfernen.

~~~~~  {#feed_ex3 .json}
...
    {
        "@id": "https://oparl.example.org/bodies/0/people/22",
        "removed": "2013-11-11T11:11:00.000+0100"
    },
...
]
~~~~~

Die Eigenschaft zur Angabe des Entfernungszeitpunkts heißt hier `removed` und
SOLL, analog zu den beiden anderen Feeds, als Sortierkriterium der Liste
verwendet werden.
