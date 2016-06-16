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
  "type": "https://oparl.org/schema/1.0/Organization",
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
  "type": "https://oparl.org/schema/1.0/Organization",
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
  "type": "https://oparl.org/schema/1.0/Body",
  "location": {
    "id": "https://oparl.example.org/location/1",
    "type": "https://oparl.org/schema/1.0/Location",
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
  "type": "https://oparl.org/schema/1.0/Person",
  "membership": [
    {
      "id": "https://oparl.example.org/memberships/385",
      "organization": "https://oparl.example.org/organizations/5",
      "role": "Vorsitzende",
      "votingRight": true,
      "startDate": "2013-12-03"
    },
    {
      "id": "https://oparl.example.org/memberships/693",
      "organization": "https://oparl.example.org/organizations/9",
      "role": "Sachkundige Bürgerin",
      "votingRight": false,
      "startDate": "2013-12-03",
      "endDate": "2014-07-28"
    }
  ],
  ...
}
~~~~~

### Externe Objektlisten

Es können auch Referenzen zu sogenannten externen Liste angegeben werden.
Die externe Liste enthält dann die betreffenden Objekte in Form der internen
Listenausgabe. Ein Beispiel dafür ist `organization` in `Body`:

~~~~~  {#objektlisten_ex5 .json}
{
  "id": "https://oparl.example.org/body/1",
  "type": "https://oparl.org/schema/1.0/Body",
  "organization": "https://oparl.example.org/body/1/organization"
  ...
}
~~~~~

~~~~~  {#objektlisten_ex5 .json}
[
  {
    "id": "https://oparl.example.org/organization/1",
    "type": "https://oparl.org/schema/1.0/Organization",
    "name": "Organisation Nummer 1",
    ...
  },
  {
    "id": "https://oparl.example.org/organization/2",
    "type": "https://oparl.org/schema/1.0/Organization",
    "name": "Organisation Nummer 2",
    ...
  },
  {
    "id": "https://oparl.example.org/organization/3",
    "type": "https://oparl.org/schema/1.0/Organization",
    "name": "Organisation Nummer 3",
    ...
  },
]
~~~~~


### Paginierung  {#paginierung}

Für externe Objektlisten ist eine Aufteilung sogenannte *Listenseiten*
vorgesehen, wobei jede Listenseite eine eigene URL erhält. Das dient dazu,
die bei der jeweiligen Anfrage übertragenen Datenmengen und Antwortzeiten zu
begrenzen.

Die Entscheidung, ob eine externe Objektliste mit Paginierung
ausgegeben wird, liegt allein beim Server. Bei Listen mit mehr als 100
Einträgen wird dies **empfohlen**.

Server **muss** für eine stabile Sortierung von Listeneinträgen sorgen. Das
heißt, dass die Sortierung der Einträge einem konstanten Prinzip folgt und sich
nicht von Abfrage zu Abfrage ändert. Das kann z.B. durch die Sortierung von
Objekten nach einer eindeutigen und unveränderlichen ID erreicht werden.

Jede Listenseite außer der Letzten muss dabei das Attribut `nextPage`
enthalten, welches auf die nächste Listenseite verweist. Ein Client kann damit
nacheinander alle Listenseiten abrufen.

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

Es gibt dazu einige **optionale** Attribute für Listenseiten:

 * `firstPage`: URL der ersten Listenseite
 * `lastPage`: URL der letzten Listenseite
 * `prevPage`: URL der vorherigen Listenseite
 * `itemsPerPage`: Die Anzahl der Objekte pro Seite. Wird dieses Attribut
 angegeben, dann muss die Anzahl der Objekte pro Seite auf allen Seiten ausser
 der letzten Seite konstant sein.
 * `numberOfPages`: Die Anzahl der Listenseiten
 * `currentPage`: Die wievielte Seite ausgegeben wird.

Zusammen mit allen Zusatzattributen sieht eine Listenseite wie folgt aus:

~~~~~  {#objektlisten_ex7 .json}
{
  "items": [
    "https://oparl.example.org/bodies/0/papers/2",
    "https://oparl.example.org/bodies/0/papers/5",
    "https://oparl.example.org/bodies/0/papers/7",
    ...
  ],
  "nextPage": "https://oparl.example.org/bodies/0/papers/?skip_id=495"
  "firstPage": "https://oparl.example.org/bodies/0/papers"
  "prevPage": "https://oparl.example.org/bodies/0/papers/?skip_id=239"
  "itemsPerPage": 100,
  "numberOfPages": 123,
  "currentPage": 10,
}
~~~~~

![Paginierung: Schematische Darstellung](images/pagination01.png)

Es ist davon auszugehen, dass Clients für den gesamten Abruf aller
Seiten einer Liste längere Zeit benötigen. In der Zwischenzeit kann sich
der Inhalt der Liste ändern, etwa durch das Hinzukommen neuer Einträge.
Die Paginierung **soll** so implementiert werden, dass sich
das Hinzufügen oder Entfernen von Einträgen möglichst nicht auf den Client
auswirkt, der aktuell die Liste paginiert, um alle Einträge abzurufen. Wir
bezeichnen dies als stabile Paginierung.

Die Funktionsweise der stabilen Paginierung soll im Folgenden an einem Beispiel
verdeutlicht werden. Nehmen wir an, die erste Seite der Liste wird mit der Abfrage

~~~~~  {#objektlisten_ex8 .sql}
SELECT * FROM example ORDER BY id LIMIT 10 OFFSET 0
~~~~~

abgerufen, die 10 Datensätze mit den `id`s 1 bis 10 zurückliefert. Dann wird
die zweite Seite mit der Abfrage

~~~~~  {#objektlisten_ex9 .sql}
SELECT * FROM example ORDER BY id LIMIT 10 OFFSET 10
~~~~~

abgerufen. Sollte nach der ersten, aber vor der zweiten Abfrage beispielsweise
ein Datensatz mit der `id=1` gelöscht worden sein, liefert die zweite Abfrage
Datensätze mit `id` > 11. Das führt dazu, dass der Datensatz mit der `id=11`
nie ausgegeben wird und der Client diesen Datensatz somit nie erhält.

Eine mögliche Lösung ist es, die `id`, bei der eine Listenseite
beginnen soll, explizit zu benennen. Wurden auf der ersten
Listenseite die Datensätze mit den `id`s 1 bis 10 ausgegeben, so könnte der
Folgeaufruf so aussehen:

~~~~~  {#objektlisten_ex10 .sql}
SELECT * FROM example WHERE id > 10 ORDER BY id LIMIT 10
~~~~~

Im diesem Fall würde dann der Datensatz mit der `id` 11 auch ausgegeben, wenn
`id` 1 gelöscht worden ist.


### Filter  {#filter}

Externe Objektlisten können mit den URL-Parametern `created_since`, `created_until`,
`modified_since` und `modified_until` eingeschränkt werden. Diese Parameter
beziehen auf die entsprechenden Attribute der jeweiligen Objekte, wobei
reservierte Zeichen URL-Kodiert werden müssen.

Die Filter werden vom Client benutzt, indem die gewünschten URL-Parameter an
die URL angehängt werden. Lautet die URL für eine Liste von Drucksachen wie
folgt,

    https://oparl.example.org/papers/

dann kann der Client die folgende URL bilden, um die Ausgabe der Liste auf
Drucksachen einzuschränken, die seit dem 1.1.2014 veröffentlicht wurden:

    https://oparl.example.org/papers/?created_since=2014-01-01T00%3A00%3A00%2B01%3A00

Mehrere Parameter können auch gemeinsam verwendet werden. So kann man z.B. eine
Einschränkung vom 1.1.2014 bis zum 31.1.2014 vornehmen:

    https://oparl.example.org/papers/?created_since=2014-01-01T00%3A00%3A00%2B01%3A00&created_until=2014-01-31T23%3A59%3A59%2B01%3A00
