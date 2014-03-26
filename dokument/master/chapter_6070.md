Feeds
-----

Feeds sind spezielle Arten von [Objektlisten](#objektlisten), für die
besondere Anforderungen gelten. Es werden drei verschiedene Feeds
spezifiziert.

Der Begriff "Feed" ist eine Anlehnung an die weit verbreiteten RSS- oder 
Atom-Feeds, deren Publikationslogik im Wesentlichen auf der chronologischen
Sortierung beruht. Im Unterschied zu Atom oder RSS ist hier jedoch keine
XML-Ausgabe beabsichtigt.

Die Feeds sollen es Clients ermöglichen, schnelle und ressourcenschonende
abzufragen, welche Objekte auf dem Server neu hinzugefügt, geändert oder
entfernt wurden. Ziel ist, zu verhindern, dass Clients zur Aktualisierung
ihres Caches den gesamten Datenbestand eines Servers abrufen müssen.

Ein OParl-Server SOLL jeden der nachfolgend beschriebenen Feeds anbieten,
sofern möglich.

Für alle Feeds drei gilt, dass mindestens ein Zeitraum von 365 Tagen, 
gerechnet vom Zeitpunkt der Abfrage, abgedeckt werden SOLL.

### Der Feed "Neue Objekte"

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
    		"@id": "http://refserv.oparl.org/bodies/0/papers/21/documents/3",
    		"created": "2014-01-07T12:59:01.038+0100"
    	},
    	{
    		"@id": "http://refserv.oparl.org/bodies/0/papers/21",
    		"created": "2014-01-05T18:29:37.123+0100"
    	},
    	{
    		"@id": "http://refserv.oparl.org/bodies/0/papers/20/documents/5",
    		"created": "2014-01-04T11:26:48.638+0100"
    	},
    	...
    ],
    "nextpage": "http://refserv.oparl.org/feeds/new/?t=20140106170100402"
}
~~~~~

Wie im Beispiel zu sehen ist, enthält die Eigenschaft `items` eine Liste
mit unbenannten Objekten. Dies ist ein Unterschied zu herkömmlichen Objektlisten,
bei denen an dieser Stelle lediglich URLs als Listeneinträge erwartet werden.

Jedes der Objekte in der `items`-Liste MUSS seinerseits wiederum zwei
Eigenschaften besitzen:

* `@id`: Die URL des neuen Objekts
* `created`: Der Zeitpunkt der Erzeugung des Objekts

Wie für Objektlisten üblich, SOLL auch für Feeds automatisch eine Aufteilung
auf mehrere Seiten vorgenommen und ein Paginierungs-Link angeboten werden, um
die übertragenen Datenmengen je Abruf einzugrenzen.

Der jeweils in der Eigenschaft `created` ausgegebene Zeitpunkt SOLL vom Server
als Sortierkriterium der Liste genutzt werden. So können Clients den jeweils
am Anfang der Liste vorgefundenen Zeitpunkt als Begrenzung für die zukünftige
Abfrage des Feeds nutzen. Ein Beispiel zur Erläuterung:

Am 1. April 2014 ruft ein Client den Feed ab und findet im ersten Listeneintrag
den `created`-Zeitpunkt `2014-03-31T18:02:34.058+0200` vor, den er sich als
Grenzwert merkt. Beim nächsten Abruf des Feeds einige Tage später muss der 
Client die Liste nur so weit abarbeiten, so lange der `created`-Zeitpunkt der
Einträge größer oder gleich dem Grenzwert ist.

### Der Feed "Geänderte Objekte"

Der Feed für geänderte Objekte listet die URLs geänderter Objekte in
der Reihenfolge des Datums ihrer Änderung, wobei das zuletzt Objekt
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
{
    "items": [
    	{
    		"@id": "http://refserv.oparl.org/bodies/0/papers/0/documents/2",
    		"last_modified": "2014-01-08T14:28:31.568+0100"
    	},
    	{
    		"@id": "http://refserv.oparl.org/bodies/0/papers/0",
    		"last_modified": "2014-01-08T12:14:27.958+0100"
    	},
    	{
    		"@id": "http://refserv.oparl.org/bodies/0/papers/0/documents/1",
    		"last_modified": "2014-01-06T17:01:00.402+0100"
    	},
    	...
    ],
    "nextpage": "http://refserv.oparl.org/feeds/updated/?t=20140106170100402"
}
~~~~~

Das Ausgabeformat entspricht weitgehend dem des Feeds "Neue Objekte", jedoch
heißt hier die Eigenschaft für den Zeitpunkt der letzten Änderung `last_modified`. 
Auch hier gilt, dass der als `last_modified` ausgegebene Zeitpunkt auch als
Sortierkriterium der Liste gelten SOLL.

### Der Feed "Entfernte Objekte"

Der Feed für entferne Objekte listet die URLs entfernter Objekte in
der Reihenfolge des Datums ihrer Entfernung auf, wobei die zuletzt entfernten 
Objekte zuerst ausgegeben werden.

Mit "Entfernung" ist im Sinne dieses Feeds die Löschung eines Objekts, aber
auch die Depublikation oder das Beenden der öffentlichen Verfügbarkeit gemeint.

Client-Implementierer sind angehalten, diesen Feed zu nutzen, um beispielsweise
depublizierte Dokumente aus ihren lokalen Caches zu entfernen.

~~~~~  {#feed_ex3 .json}
{
    "items": [
    	{
    		"@id": "http://refserv.oparl.org/bodies/0/people/22",
    		"removed": "2013-11-11T11:11:00.000+0100"
    	},
    	...
    ],
    "nextpage": "http://refserv.oparl.org/feeds/updated/?t=20131111111100"
}
~~~~~

Die Eigenschaft zur Angabe des Entfernugnszeitpunkts heißt hier `removed` und
SOLL, analog zu den beiden anderen Feeds, als Sortierkriterium der Liste
verwendet werden.
