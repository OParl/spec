Feeds
-----

Feeds sind spezielle Arten von [Objektlisten](#objektlisten), für die
besondere Anforderungen gelten. Es werden drei verschiedene Feeds
spezifiziert.

Die Feeds sollen es Clients ermöglichen, schnelle und ressourcenschonende
abzufragen, welche Objekte auf dem Server neu hinzugefügt, geändert oder
entfernt wurden. Ziel ist, zu verhindern, dass Clients zur Aktualisierung
ihres Caches den gesamten Datenbestand eines Servers abrufen müssen.

Ein OParl-Server SOLL jeden der nachfolgend beschriebenen Feeds anbieten,
sofern möglich.

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

TODO: JSON-Beispiel einfügen

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

TODO: JSON-Beispiel einfügen

### Der Feed "Entfernte Objekte"

Der Feed für entferne Objekte listet die URLs entfernter Objekte in
der Reihenfolge des Datums ihrer Entfernung auf, wobei die zuletzt entfernten 
Objekte zuerst ausgegeben werden.

Mit "Entfernung" ist im Sinne dieses Feeds die Löschung eines Objekts, aber
auch die Depublikation oder das Beenden der öffentlichen Verfügbarkeit gemeint.

Client-Implementierer sind angehalten, diesen Feed zu nutzen, um beispielsweise
depublizierte Dokumente aus ihren lokalen Caches zu entfernen.

TODO: JSON-Beispiel einfügen
