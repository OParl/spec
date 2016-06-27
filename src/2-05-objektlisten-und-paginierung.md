## Objektlisten und Paginierung {#objektlisten-und-paginierung}

Oft wird für ein Attribut kein Wert ausgegeben, sondern ein anderes Objekt oder
eine Liste von Objekten. Dabei kann eine Referenz auf das Objekt bzw. die
Objektliste angegeben werden, oder das Objekt bzw. die Objektlist wird intern
ausgegeben. Beide Verfahren sollen im Folgenden erklärt werden.

### Objekt- und Objektlistenausgabe im Allgemeinen

In einem JSON-Objekt muss jedem Wert ein Schlüssel zugeordnet sein, daher wird sowohl für OParl-Objektlisten, als auch für Einzelobjekte die folgende Ausgabestruktur erwartet:

~~~~~  {#objektformat_ex1 .json}
{
    "data": [
        <array von Objekten>
    ],
    "meta": {
        zusätzliche Angaben
    }
}
~~~~~

Diese Struktur ermöglicht es Server-Implementierern innerhalb des **meta**-Bereiches zusätzliche Informationen wie z.B. zur Bandbreitenlimitierung
anzugeben. Des weiteren wird dieser Bereich auch zur Paginierungsinformation genutzt.

### Referenzierung von Objekten via URL

Bei der Referenzierung einzelner Objekte wird eine URL angegeben, welche auf
das entsprechende Objekt verweist. Der Typ ist hierbei ein
`string (url: Objekt-ID)`.
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
Fall `array of string (url: Objekt-ID)`.

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

Ebenso kann eine Liste von Objekten intern ausgegeben werden. Hier das
Beispiel des Attributes `membership` in `Person`.

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

Es können auch Referenzen zu sogenannten externen Listen angegeben werden.
Die externe Liste enthält dann die betreffenden Objekte in Form einer
Listenausgabe. Ein Beispiel dafür ist `organization` in `Body`:

~~~~~  {#objektlisten_ex5a .json}
{
  "id": "https://oparl.example.org/body/1",
  "type": "https://oparl.org/schema/1.0/Body",
  "organization": "https://oparl.example.org/body/1/organization"
  ...
}
~~~~~

~~~~~  {#objektlisten_ex5b .json}
{
    data: [
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

Die Paginierung **muss** innerhalb eines `meta`-Blockes als `pagination`-Objekt wie folgt angegeben werden:

```.json
{
    "data": {
        [...],
        [...],
        ...
    },
    "meta": {
        "pagination": {
            "totalElements": 150,
            "elementsOnPage": 100,
            "elementsPerPage": 100,
            "currentPage": 1,
            "totalPages": 2,
            "links": [
                "first": "https://oparl.example.org/organization/",
                "self": "https://oparl.example.org/organization/?page=1",
                "next": "https://oparl.example.org/organization/?page=2",
                "last": "https://oparl.example.org/organization/?page=2"
            ]
        }
    }
}
```


Dem entsprechend gibt es die folgenden Eigenschaften zur Paginierung:

- **totalElements**: Gibt die Gesamtanzahl der Objekte in der Liste an.

- **elementsOnPage**: Gibt die Anzahl der Objekte auf der aktuellen Listenseite an, diese Angabe **kann** - insbesondere auf der letzten Listenseite - von **elementsPerPage** unterschieden, **muss** aber auf allen anderen Seiten mit **elementsPerPage** identisch sein.

- **elementsPerPage**: Gibt die Anzahl der Objekte pro Listenseite an.

- **currentPage**: Gibt die aktuelle Seitenzahl in der Liste an.

- **totalPages**: Gibt die Gesamtanzahl der Seiten in der Liste an.

- **links**: Stellt einige Links zur Navigation in der Liste zur Verfügung. Die Angabe dieser Links ist **zwingend**, da ein Client das URL-Schema eines spezifischen Servers nicht kennen können soll, um in ihm zu navigieren.

### Filter  {#filter}

Externe Objektlisten können mit den URL-Parametern `created_since`, `created_until`,
`modified_since` und `modified_until` eingeschränkt werden. Diese Parameter
beziehen sich auf die entsprechenden Attribute der jeweiligen Objekte, wobei
reservierte Zeichen URL-Kodiert werden müssen.

Die Filter werden vom Client benutzt, indem die gewünschten URL-Parameter an
die URL der ersten Listensiete angehängt werden. Bei allen weiteren Seiten hat
der Server sicherzustellen, dass die verwendeten Filter erhalten bleiben.
Lautet die URL für eine Liste von Drucksachen wie folgt:

    https://oparl.example.org/papers/

kann der Client die folgende URL bilden, um die Ausgabe der Liste auf
Drucksachen einzuschränken, die seit dem 1. Januar 2014 veröffentlicht wurden:

    https://oparl.example.org/papers/?created_since=2014-01-01

Mehrere Parameter können auch gemeinsam verwendet werden. So kann man z.B. eine
Einschränkung vom 1.1.2014 bis zum 31.1.2014 vornehmen:

    https://oparl.example.org/papers/?created_since=2014-01-01T00%3A00%3A00%2B01%3A00&created_until=2014-01-31T23%3A59%3A59%2B01%3A00

Die genannten URL-Parameter erwarten grundsätzlich eine [`date` oder `date-time`-Angabe](#datum_zeit). Bei der Angabe eines `date` **sollte** der
Server die Zeit 00:00 annehmen.
