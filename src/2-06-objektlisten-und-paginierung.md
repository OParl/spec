## Objektlisten und Paginierung {#objektlisten-und-paginierung}

Oft wird für ein Attribut kein Wert ausgegeben, sondern ein anderes Objekt oder
eine Liste von Objekten. Dabei kann eine Referenz auf das Objekt bzw. die
Objektliste angegeben werden, oder das Objekt bzw. die Objektlist wird intern
ausgegeben. Beide Verfahren sollen im Folgenden erklärt werden.


### Referenzierung von Objekten via URL

Bei der Referenzierung einzelner Objekte wird eine URL angegeben, welche auf
das entsprechende Objekt verweist. Der Typ ist hierbei ein string (url: Object-id).
Ein Beispiel hierfür ist `subOrganizationOf` in `Organization`:

~~~~~  {#objektlisten_ex1 .json}
{
  "id": "https://oparl.example.org/organization/1",
  "type": "http://oparl.org/schema/1.0/Organization",
  "subOrganizationOf": "https://oparl.example.org/organization/2"
  ...
}
~~~~~

Es kann auch eine Liste von Referenzen ausgegeben werden. Der Typ ist in diese
Fall array of string (url: Object-id).

Ein Beispiel hierfür ist `meeting` in `Organization`:

~~~~~  {#objektlisten_ex2 .json}
{
  "id": "https://oparl.example.org/organization/1",
  "type": "http://oparl.org/schema/1.0/Organization",
  "meeting": [
    "https://oparl.example.org/meeting/1",
    "https://oparl.example.org/meeting/2",
    "https://oparl.example.org/meeting/3",
  ]
  ...
}
~~~~~

### Interne Ausgabe von Objekten

Objekte können auch intern ausgegeben werden. Dabei wird das gesamte Objekt als
Wert eines Attributs angegeben. Ein Beispiel für ein internes  Objekt ist
`location` in `Body`:

~~~~~  {#objektlisten_ex3 .json}
{
  "id": "https://oparl.example.org/body/1",
  "type": "http://oparl.org/schema/1.0/Body",
  "location": {
    "id": https://oparl.example.org/location/1,
    "type": "http://oparl.org/schema/1.0/Location",
    "description": "Ratshausvorplatz 1, 12345 Beispielstadt"
  },
  ...
}
~~~~~

Ebenso kann eine Liste von Objekten intern ausgegeben werden. Hier das Beispiel
Attributes `membership` in `Person`.

~~~~~  {#objektlisten_ex4 .json}
{
  "id": "https://oparl.example.org/person/1",
  "type": "http://oparl.org/schema/1.0/Person",
  "membership": [
    {
      "id": "https://oparl.example.org/memberships/385", 
      "organization": "https://oparl.example.org/organizations/5", 
      "role": "Vorsitzende", 
      "votingRight": true, 
      "startDate": "2013-12-03T16:30:00+01:00"
    }, 
    {
      "id": "https://oparl.example.org/memberships/693", 
      "organization": "https://oparl.example.org/organizations/9", 
      "role": "Sachkundige Bürgerin", 
      "votingRight": false, 
      "startDate": "2013-12-03T16:30:00+01:00", 
      "endDate": "2014-07-28T00:00:00+02:00"
    }
  ],
  ...
}
~~~~~

### Externe Objektlisten

Es können auch referenzen zu sogenannten externen Liste angegeben werden.
Diese enthält eine Liste der betreffenden Objekte mit interner Listenausgabe.
Ein Beispiel dafür ist `organization` in `Body`:

~~~~~  {#objektlisten_ex5 .json}
{
  "id": "https://oparl.example.org/body/1",
  "type": "http://oparl.org/schema/1.0/Body",
  "organization": "https://oparl.example.org/body/1/organization"
  ...
}
~~~~~

~~~~~  {#objektlisten_ex5 .json}
[
  {
    "id": "https://oparl.example.org/organization/1",
    "type": "http://oparl.org/schema/1.0/Organization",
    "name": "Organisation Nummer 1",
    ...
  },
  {
    "id": "https://oparl.example.org/organization/2",
    "type": "http://oparl.org/schema/1.0/Organization",
    "name": "Organisation Nummer 2",
    ...
  },
  {
    "id": "https://oparl.example.org/organization/3",
    "type": "http://oparl.org/schema/1.0/Organization",
    "name": "Organisation Nummer 3",
    ...
  },
]
~~~~~


### Paginierung  {#paginierung}

Für externe Objektlisten ist eine Blätterfunktion
(Paginierung) vorgesehen. Damit ist die Aufteilung einer Liste
in kleinere Teilstücke gemeint, die wir als *Listenseiten* bezeichnen.
Jede Listenseite wird vom Client jeweils mit einer eigenen API-Anfrage
abgerufen. Das dient dazu, die bei der jeweiligen Anfrage übertragenen
Datenmengen und Antwortzeiten zu begrenzen und Systemressourcen
sowohl beim Server als auch beim Client zu schonen.

Die Entscheidung, ob eine Seite teilweise und daher mit Paginierung
ausgegeben wird, liegt allein beim Server. Bei Listen mit mehr als 100
Einträgen wird dies EMPFOHLEN.

Der Server gibt für eine Liste, bei der die Paginierung aktiv ist, d. h.
nicht alle Listenelemente ausgegeben wurden, zusätzliche Eigenschaften aus.
Das nachfolgende Beispiel zeigt dies für den Anfang einer paginierten Liste:

~~~~~  {#objektlisten_ex4 .json}
{
    "items": [
        "https://oparl.example.org/bodies/0/papers/2",
        "https://oparl.example.org/bodies/0/papers/5",
        "https://oparl.example.org/bodies/0/papers/7",
        ...
    ],
    "nextPage": "https://oparl.example.org/bodies/0/papers/?skip_id=495"
}
~~~~~

Sobald es mehrere Seiten gibt, MUSS das Attribut `nextPage` bei
allen Seiten außer der letzten angegeben werden. Dieses Attribut
enthält eine URL, über die die nächste Listenseite abgerufen werden
kann. Die Beschaffenheit der URL bestimmt der Server frei, das
obige Beispiel ist in keiner Form bindend.

Es ergibt sich eine typische Abfolge, wie Clients bei Bedarf
mit mehreren Anfragen ganze Objektlisten vom Server abrufen:

1. Der Server stellt eine URL für eine Liste zur Verfügung.

2. Der Client ruft diese URL der Liste auf.

3. Der Server antwortet mit einer verkürzten Listenausgabe und
   gibt mittels `nextPage`-Eigenschaft die URL für den
   Abruf der nächsten Listenseite an.

4. Der Client ruft die URL für die nächste Listenseite auf.

Die Punkte 3 und 4 können sich nun so oft wiederholen, bis
die letzte Listenseite erreicht ist.

5. Der Server liefert die letzte Listenseite ohne
   `nextPage`-Eigenschaft aus.

Zusätzlich zur für die Paginierung ZWINGENDEN Eigenschaft
`nextPage`, die lediglich auf der letzten Listenseite entfällt,
können Server OPTIONAL weitere URLs zum Abruf bestimmter
Listenseiten anbieten:

Erste Listenseite (Eigenschaft `firstPage`):
:   Sofern die aktuell abgerufene Listenseite nicht den Anfang der
    Liste wiedergibt, KANN der Server diese Eigenschaft ausgeben,
    deren Wert die URL zum Abruf der *ersten* Listenseite ist.

Letzte Listenseite (Eigenschaft `lastPage`):
:   Sofern die aktuell abgerufene Listenseite nicht das Ende der
    Liste wiedergibt, KANN der Server diese Eigenschaft ausgeben,
    deren Wert die URL zum Abruf der *letzten* Listenseite ist.

Vorherige Listenseite (Eigenschaft `prevPage`):
:   Sofern die aktuell abgerufene Listenseite nicht den Anfang der
    Liste wiedergibt, KANN der Server diese Eigenschaft ausgeben,
    deren Wert die URL zum Abruf der *vorigen* Listenseite ist.

Anzahl der Seiten (Eigenschaft `itemsPerPage`):
:   Mit dem Attribut `itemsPerPage` kann die Anzahl der Objekte pro
    Seite ausgegeben werden. Wenn `itemsPerPage` ausgegeben wird,
    MUSS die Anzahl der Objekte auf allen Seiten bis auf der letzten
    identisch sein.
    
Anzahl der Seiten (Eigenschaft `numberOfPages`):
:   Mit `numberOfPages` kann die Anzahl der Seiten ausgegeben werden.
    Dies ist hilfreich, um prognostizieren zu können, wie lange ein
    Abruf dauern wird.


Zusammen mit allen Zusatzattributen sähe eine Liste also wie folgt aus:

~~~~~  {#objektlisten_ex7 .json}
{
  "items": [
    "https://oparl.example.org/bodies/0/papers/2",
    "https://oparl.example.org/bodies/0/papers/5",
    "https://oparl.example.org/bodies/0/papers/7",
    ...
  ],
  "numberOfPages": 123,
  "currentPage": 10,
  "itemsPerPage": 100,
  "firstPage": "https://oparl.example.org/bodies/0/papers/"
  "prevPage": "https://oparl.example.org/bodies/0/papers/?skip_id=239"
  "nextPage": "https://oparl.example.org/bodies/0/papers/?skip_id=495"
}
~~~~~

Damit eröffnet der Server dem Client zusätzliche Möglichkeiten,
die einzelnen Listenseiten abzurufen.

![Paginierung: Schematische Darstellung](images/pagination01.png)

Server-Implementierer entscheiden selbst, wie die URLs zum Abruf einzelner
Listenseiten aufgebaut sind und tragen damit selbst Verantwortung für die
Funktionsweise der Paginierung. Die im obigen Beispiel verwendete URL
einschließlich des fiktiven URL-Parameters dienen lediglich der
Veranschaulichung und sind in keiner Weise bindend. Bei der Entscheidung
für eine Form der Implementierung sollten die folgenden Anforderungen von
Clients berücksichtigt werden:

* Es ist davon auszugehen, dass Clients für den gesamten Abruf aller
Seiten einer Liste längere Zeit benötigen. In der Zwischenzeit kann sich
der Inhalt der Liste bereits ändern, etwa durch das Hinzukommen neuer
Einträge. Die Paginierung ist idealerweise so zu implementieren, dass sich
das Hinzukommen oder Entfernen von Einträgen möglichst nicht auf einen Client
auswirkt, der aktuell die Liste paginiert, um alle Einträge abzurufen. Wir
bezeichnen dies als **stabile Paginierung**.

* Eine wesentliche Anforderung an Listen mit Paginierung ist, dass alle
Einträge der Liste in einer konsistenten Reihenfolge sortiert ausgegeben
werden MÜSSEN. Das bedeutet, dass die Sortierung beim Server im Idealfall
anhand einer eindeutigen und unveränderlichen Objekteigenschaft vorgenommen
wird. Hierfür eignen sich die Objekt-URLs, da sie genau diese beiden
Anforderungen erfüllen sollten.

Über die Sortierung hinaus können bei der Implementierung einer stabilen
Paginierung auf Server-Seite weitere Überlegungen einbezogen werden.
Zur Verdeutlichung soll hier eine ungünstige (unstabile) Form der
Implementierung mit Hilfe einer SQL-Abfrage illustriert werden. Gegeben sei
eine Tabelle `example`, die einen
numerischen Primärschlüssel `id` enthält. Nehmen wir an, die erste Seite der
Liste wird mit der Abfrage

~~~~~  {#objektlisten_ex8 .sql}
SELECT * FROM example ORDER BY id LIMIT 10 OFFSET 0
~~~~~

abgerufen und würde 10 Datensätze mit den `id`s 1 bis 10 zurückliefern. Dann wird
die zweite Seite mit der Abfrage

~~~~~  {#objektlisten_ex9 .sql}
SELECT * FROM example ORDER BY id LIMIT 10 OFFSET 10
~~~~~

abgerufen. Sollte nach der ersten, aber vor der zweiten Abfrage beispielsweise
der Datensatz mit der `id=1` gelöscht worden sein, liefert die zweite Abfrage
Datensätze mit `id` > 9. In diesem Fall würde dies nur dazu führen, dass ein
Datensatz (`id=10`) zweimal ausgegeben wird. Bei ungünstigeren Konstellationen
wäre auch denkbar, dass eine unstabile Paginierung bewirkt, dass einzelne
Datensätze beim Paginieren übergangen werden. Je nach Bedeutung der fehlenden
Datensätze können solche Inkonsistenzen erhebliche Auswirkungen haben.

Besser wäre es, bei der Paginierung die Eintragsgrenze, bei der eine Listenseite
beginnen soll, explizit zu benennen. Wurden auf der ersten
Listenseite die Datensätze mit den IDs 1 bis 10 ausgegeben, so könnte der
Folgeaufruf, um beim SQL-Beispiel zu bleiben, so aussehen:

~~~~~  {#objektlisten_ex10 .sql}
SELECT * FROM example WHERE id > 10 ORDER BY id LIMIT 10
~~~~~

Die zuvor beschriebenen Anforderungen für die Paginierung von Listen
gelten auch unverändert, wenn der Umfang der Liste durch Abfrageparameter
vom Client eingeschränkt wurde.


### Sortierung

OParl definiert keine Möglichkeit für Clients, auf die Reihenfolge von Listeneinträgen
Einfluss zu nehmen. Von Servern wird die Einhaltung einiger grundlegender Anforderungen
erwartet, die teilweise bereits erwähnt wurden.

Server MUSS generell für eine **stabile Sortierung** von Listeneinträgen sorgen. Das
heißt, die Sortierung von Einträgen folgt einem konstanten Prinzip und ändert sich nicht von
Abfrage zu Abfrage. Eine Einfache Möglichkeit, dies Umzusetzen, wäre in vielen Fällen
die Sortierung von Objekten nach ihrer eindeutigen und unveränderlichen ID.


### Filter  {#filter}

Bei der *externen Listenausgabe* (siehe weiter oben) werden in Abhängigkeit vom ausgegebenen
Objekttyp bestimmte Möglichkeiten geboten, die Ausgabe von Listen auf eine
Teilmenge einzuschränken.

Hierfür sind die URL-Parameter `created` und `modified` vorgesehen, welche entsprechend des
[ElasticSearch Query String Syntax](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-query-string-query.html#_ranges_2)
verwendet werden. Beide Parameter beziehen sich auf die gleichnamigen Attribute der jeweiligen Objekte.

Der Server MUSS die Filter `created` und `modified` bei allen Listen unterstützen, welche Attribute des Objektes Body sind.

Die Filter werden vom Client aktiviert, indem der oder die gewünschte(n) URL-Parameter
der vom Server angegebenen URL für die Listenausgabe hinzugefügt werden. Lautet diese
URL für eine Liste von Drucksachen so,

    https://oparl.example.org/papers/

dann kann der Client die folgende URL bilden, um die Ausgabe der Liste auf Drucksachen
einzuschränken, die nach dem 1.1.2014 veröffentlicht wurden:

    https://oparl.example.org/papers/?created:>=2014-01-01T00%3A00%3A00%2B01%3A00

Es sind auch Einschränkungen mit Minimal- und Maximal-Wert möglich, hierfür MUSS
der logische Operator AND implementiert werden sein. Um eine Einschränkung vom 1.1.2014
bis zum 31.1.2014 vorzunehmen, wird domit der folgende Syntax verwendet:

    https://oparl.example.org/papers/?created:(>=2014-01-01T00%3A00%3A00%2B01%3A00%20AND%20<=2014-01-31T23%3A59%3A59%2B01%3A00)

Clients MÜSSEN die Werte von `created` und `modified` mit Uhrzeit und Zeitzone
angeben. Dabei MUSS das im Kapitel [Datums- und Zeitangaben](#datum_zeit)
definierte Format genutzt werden und Clients müssen für eine entsprechende
URL-Kodierung sorgen.
