## Objektlisten und Paginierung {#objektlisten-und-paginierung}

Oft wird für ein Attribut kein Wert ausgegeben, sondern ein anderes Objekt oder
eine Liste von Objekten. Dabei kann eine Referenz auf das Objekt bzw. die
Objektliste angegeben werden, oder das Objekt bzw. die Objektlist wird intern
ausgegeben. Beide Verfahren sollen im Folgenden erklärt werden.
Zu beachten ist, dass für jedes Listenattribut festgelegt ist, welches dieser
Verfahren jeweils zu verwenden ist. Diese Information ist den
[Schemadefinitionen](#schema) zu entnehmen.

### Referenzierung von Objekten via URL

Bei der Referenzierung einzelner Objekte wird eine URL angegeben, welche auf
das entsprechende Objekt verweist. Der Typ ist hierbei ein
`string (url: Objekt-ID)`.
Ein Beispiel hierfür ist `subOrganizationOf` in `Organization`:

~~~~~  {#objektlisten_ex1 .json}
{
  "id": "https://oparl.example.org/organization/1",
  "type": "https://schema.oparl.org/1.1/Organization",
  "subOrganizationOf": "https://oparl.example.org/organization/2"
  ...
}
~~~~~

Es kann auch eine Liste von Referenzen ausgegeben werden. Der Typ ist in diese
Fall `array of string (url: Objekt-ID)`.

Ein Beispiel hierfür ist `meeting` in `Organization`:

~~~~~  {#objektlisten_ex2 .json}
{
  "id": "https://oparl.example.org/organization/1",
  "type": "https://schema.oparl.org/1.1/Organization",
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
Wert eines Attributs angegeben. Ein Beispiel für ein internes Objekt ist
`location` in `oparl:Body`:

~~~~~  {#objektlisten_ex3 .json}
{
  "id": "https://oparl.example.org/body/1",
  "type": "https://schema.oparl.org/1.1/Body",
  "location": {
    "id": "https://oparl.example.org/location/1",
    "type": "https://schema.oparl.org/1.1/Location",
    "description": "Ratshausvorplatz 1, 12345 Beispielstadt"
  },
  ...
}
~~~~~

Ebenso kann eine Liste von Objekten intern ausgegeben werden. Hier das
Beispiel des Attributes `membership` in `oparl:Person`.

~~~~~  {#objektlisten_ex4 .json}
{
  "id": "https://oparl.example.org/person/1",
  "type": "https://schema.oparl.org/1.1/Person",
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

Bei der internen Ausgabe von Objekten **darf** der Server keine gelöschten
Objekte ausgeben.

### Externe Objektlisten

Es können auch Referenzen zu sogenannten externen Objektlisten angegeben werden.
Die externe Liste enthält dann die betreffenden Objekte in Form einer
Listenausgabe. Ein Beispiel dafür ist `organization` in `oparl:Body`.

`oparl:Body`:

~~~~~  {#objektlisten_ex5a .json}
{
  "id": "https://oparl.example.org/body/1",
  "type": "https://schema.oparl.org/1.1/Body",
  "organization": "https://oparl.example.org/body/1/organization"
  ...
}
~~~~~

Die externe Objektliste:

~~~~~  {#objektlisten_ex5b .json}
{
    "data": [
      {
        "id": "https://oparl.example.org/organization/1",
        "type": "https://schema.oparl.org/1.1/Organization",
        "name": "Organisation Nummer 1",
        ...
      },
      {
        "id": "https://oparl.example.org/organization/2",
        "type": "https://schema.oparl.org/1.1/Organization",
        "name": "Organisation Nummer 2",
        ...
      },
      {
        "id": "https://oparl.example.org/organization/3",
        "type": "https://schema.oparl.org/1.1/Organization",
        "name": "Organisation Nummer 3",
        ...
      },
    ],
    ...
}
~~~~~


### Paginierung  {#paginierung}

Für externe Objektlisten ist eine Aufteilung sogenannte *Listenseiten*
vorgesehen, wobei jede Listenseite eine eigene URL erhält. Das dient dazu,
die bei der jeweiligen Anfrage übertragenen Datenmengen und Antwortzeiten zu
begrenzen.

Die Entscheidung, ob eine externe Objektliste mit Paginierung
ausgegeben wird, liegt allein beim Server. Bei Listen mit mehr als 100
Einträgen wird dies **empfohlen**.

Ein Server **muss** für eine stabile Sortierung von Listeneinträgen sorgen. Das
heißt, dass die Sortierung der Einträge einem konstanten Prinzip folgt und sich
nicht von Abfrage zu Abfrage ändert. Das kann z.B. durch die Sortierung von
Objekten nach einer eindeutigen und unveränderlichen ID erreicht werden.

Jede Listenseite **muss** die Attribute folgenden Attribute enthalten:

- **data** (Array der intern ausgegebenen Objekte)

- **pagination** (Object)

- **links** (Object)

Für `pagination` sind die folgenden Attribute festgelegt, die alle **optional**
sind:

- `totalElements`: Gibt die Gesamtanzahl der Objekte in der Liste an. Diese Zahl
kann sich unter Umständen bis zum Aufruf der nächsten Listenseiten ändern.

- `elementsPerPage`: Gibt die Anzahl der Objekte pro Listenseite an. Dieser Wert
muss auf allen Listenseiten bis auf die letzte gleich sein.

- `currentPage`: Gibt die aktuelle Seitenzahl in der Liste an.

- `totalPages`: Gibt die Gesamtanzahl der Seiten in der Liste an.

Für `links`  sind folgende Attribute festgelegt, die bis auf `next` alle
**optional** sind:

- `first`: URL der ersten Listenseite

- `prev`: URL der vorherigen Listenseite

- `self`: Die kanonische URL dieser Listenseite

- `next`: URL der nächsten Listen. Für alle Seiten bis auf die letzte ist die
Angabe dieser URL **zwingend**.

- `last`: URL der letzten Listenseite

- `web`: s. [web](#web). Neu in OParl 1.1

~~~~~  {#paginierung_ex1 .json}
{
    "data": [
        {...},
        {...},
        ...
    ],
    "pagination": {
        "totalElements": 50000,
        "elementsPerPage": 100,
        "currentPage": 3,
        "totalPages":500
    },
    "links": {
        "first": "https://oparl.example.org/organization/",
        "prev": "https://oparl.example.org/organization/?page=2",
        "self": "https://oparl.example.org/organization/?page=3",
        "next": "https://oparl.example.org/organization/?page=4",
        "last": "https://oparl.example.org/organization/?page=500",
        "web": "https://web.example.org/organization/?page=500"
    }
}
~~~~~

### Filter  {#filter}

Externe Objektlisten können mit den URL-Parametern `created_since`, `created_until`,
`modified_since` und `modified_until` eingeschränkt werden. Diese Parameter
beziehen sich auf die entsprechenden Attribute der jeweiligen Objekte, wobei
reservierte Zeichen URL-Kodiert werden müssen. Ein Server muss diese Parameter
bei allen externen Objektlisten unterstützen.

Neu in OParl 1.1: Wenn ein Client den Parameter `omit_internal` mit dem Wert
`true` angibt, dann **soll** der Server auf die Ausgabe von internen Listen
verzichten, sofern deren Objekte Teil einer der in OParl 1.1 neu eingeführten
Listen sind. Konkret bedeutet das, dass die folgenden Attribute nicht ausgegeben
werden müssen:

 - `auxiliaryFile` in `AgendaItem`
 - `auxiliaryFile` in `Meeting`
 - `auxiliaryFile` in `Paper`
 - `location` in `Paper`
 - `membership` in `Person`

Weiterhin ausgeben werden dagegen:

 - `legislativeTerm` in `Body` (Hier gibt es keine externe Liste)
 - `agendaItem` in `Meeting` (Hier ist die Reihenfolge der Objekte relevant)

Die Filter werden vom Client benutzt, indem die gewünschten URL-Parameter an
die URL der ersten Listenseite angehängt werden. Bei allen weiteren Seiten,
genauer gesagt bei den Werten von `links`, **muss** der Server sicherzustellen,
dass die verwendeten Filter erhalten bleiben.

Neu in OParl 1.1: Ein Server **muss** für den im nächsten Abschnitt beschrieben
Aktualisierungsmechanismus auch die den Filtern entsprechenden gelöschten
Objekte ausgeben, wenn der Parameter `modified_since` gesetzt ist
(s. [OParl 1.1](#oparl-1-1)). Wenn `modified_since` nicht gesetzt ist,
dann **dürfen** die gelöschten Objekte **nicht** ausgegeben werden.
Dadurch kann sich ein Client effizient darüber informieren, welche der Objekte
in seinem lokalen Bestand gelöscht wurden.

Lautet die URL für eine Liste von Drucksachen wie folgt:

    https://oparl.example.org/papers/

kann der Client die folgende URL bilden, um die Ausgabe der Liste auf
Drucksachen einzuschränken, die seit dem 1. Januar 2014 veröffentlicht wurden:

    https://oparl.example.org/papers/?created_since=2014-01-01T00%3A00%3A00%2B01%3A00

Mehrere Parameter können auch gemeinsam verwendet werden. So kann man z.B. eine
Einschränkung vom 1.1.2014 bis zum 31.1.2014 vornehmen:

    https://oparl.example.org/papers/?created_since=2014-01-01T00%3A00%3A00%2B01%3A00&created_until=2014-01-31T23%3A59%3A59%2B01%3A00

Die genannten URL-Parameter erwarten grundsätzlich eine vollständige [`date-time`-Angabe](#datum_zeit).

Des Weiteren kann ein Client die Anzahl der Objekte pro Listenseite durch
den URL-Parameter `limit` begrenzen, der sich auf das gleichnamige
Attribut bezieht. Ein Client **darf nicht** erwarten, dass sich ein Server an
seine `limit`-Anfrage hält.

### Der Aktualisierungsmechanismus {#aktualisierungsmechanismus}

Dieser Abschnitt ist neu in OParl 1.1.

Der Hauptnutzen der Filter ist die Möglichkeit, einen lokalen Datenbestand
inkrementell zu aktualisieren.

Ein Client könnte z.B. am 1.1.2014 um 2:00 Uhr deutscher Zeit die Liste aller
Drucksachen herunterladen und in einer Datenbank speichern.

    https://oparl.example.org/papers/

Um den Datenbestand am nächsten Tag zu aktualisieren, ruft der Client die selbe
URL auf, diesmal jedoch mit dem Parameter `modified_since` mit dem Wert
`2014-01-01T02:00:00+01:00`.

    https://oparl.example.org/papers/?modified_since=2014-01-01T02%3A00%3A00%2B01%3A00

Diese Liste ist in der Regel deutlich kürzer als die Liste aller Objekte,
sodass die Aktualisierung bedeutend schneller ist als der erste Abruf. Der
Client muss außerdem nur noch eine deutlich kleiner Menge an Objekten in die
Datenbank einfügen, aktualisieren oder löschen, um den gleichen Datenstand wie
der Server zu haben.
