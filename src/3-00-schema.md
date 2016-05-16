# Schema {#schema}

Dieses Kapitel beschreibt das Schema von OParl. Das Schema definiert
die Objekttypen und ihre Eigenschaften. Darüber hinaus ist im Schema
auch festgelegt, in welcher Beziehung verschiedene Objekttypen zu
einander stehen.

![OParl Objekttypen: Ein Überblick](images/objekttypen_graph.png)

## Die Objekte {#objekttypen}

OParl ist aufgeteilt in Hauptobjekte, globale Subobjekte und Subobjekte.
Subobjekte werden in Form der internen Ausgabe (siehe Kapitel 2.05) ausgegeben.
Globale Subobjekte werden von mehreren Hauptobjekten verwendet und benötigen so
die Eigenschaft `created`, `modified` und ggf. `deleted`.

Es gibt die folgenden Hauptobjekte:

* System
* Body
* Organization
* Person
* Meeting
* Paper

Die Subobjekte lassen sich ihren jeweiligen Hauptobjekten zuordnen:

* LegislativeTerm als Subobjekt von Body
* Membership als Subobjekt von Person
* AgendaItem als Subobjekt von Meeting
* Consultation als Subobjekt von Paper
* File als globales Subobjekt von Meeting, AgendaItem und Paper
* Location als globales Subobjekt von Body, Organization, Meeting und Paper

Grundsätzlich muss jedes Objekt unter seiner ID abrufbar sein. Wenn ein Objekt
intern ausgegeben wird, dann kann die Rückreferenz auf das Eltern-Objekt
weggelassen werden.

Als Beispiel hier eine Ausgabe von `Meeting`, in welchem ein `File` enthalten
ist:

~~~~~  {#objekte_example1 .json}
{
    "id": "https://oparl.example.org/meeting/281",
    "type": "https://oparl.org/schema/1.0/Meeting",
    "name": "4. Sitzung des Finanzausschusses",
    "start": "2013-01-04T08:00:00+01:00",
    "end": "2013-01-04T12:00:00+01:00",
    "invitation": {
        "id": "https://oparl.example.org/files/57739",
        "name": "Einladung",
        "fileName": "einladung.pdf",
        "mimeType": "application/pdf",
        "date": "2012-01-08T14:05:27+01:00",
        "modified": "2012-01-08T14:05:27+01:00",
        "sha1Checksum": "da39a3ee5e6b4b0d3255bfef95601890afd80709",
        "size": 82930,
        "accessUrl": "https://oparl.example.org/files/57739.pdf",
        "downloadUrl": "https://oparl.example.org/files/download/57739.pdf"
    }
    [...]
}
~~~~~

Das enthaltene `File` muss auch einzeln abgerufen werden können. Dabei kommt
dann das Eltern-Objekt als zusätzliches Attribut hinzu.:

~~~~~  {#objekte_example2 .json}
{
    "id": "https://oparl.example.org/files/57739",
    "name": "Einladung",
    "fileName": "einladung.pdf",
    "mimeType": "application/pdf",
    "date": "2012-01-08T14:05:27+01:00",
    "modified": "2012-01-08T14:05:27+01:00",
    "sha1Checksum": "da39a3ee5e6b4b0d3255bfef95601890afd80709",
    "size": 82930,
    "accessUrl": "https://oparl.example.org/files/57739.pdf",
    "downloadUrl": "https://oparl.example.org/files/download/57739.pdf",
    "meeting": [
        "https://oparl.example.org/meeting/281"
    ]
}
~~~~~

Das zusätzliche Attribut ist ein Array, da es auch möglich ist, dass Dateien
von mehreren Hauptobjekten aus genutzt werden. Das kann z.B. bei `Location`
vorkommen:

~~~~~  {#objekte_example2 .json}
{
    "id": "https://oparl.example.org/locations/29856",
    "description": "Honschaftsstraße 312, Köln",
    "geojson": {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [
                7.03291,
                50.98249
            ]
        }
    },
    "meeting": [
      "https://oparl.example.org/meeting/281",
      "https://oparl.example.org/meeting/766",
      "https://oparl.example.org/meeting/1002"
    ],
    "paper": [
        "https://oparl.example.org/paper/749",
        "https://oparl.example.org/paper/861",
        "https://oparl.example.org/paper/1077"
    ]
}
~~~~~


## Übergreifende Aspekte {#uebergreifende-aspekte}

### Vollständigkeit {#schema-vollstaendigkeit}

Alle regulär öffentlich abrufbaren Informationen **sollten** auch in OParl
ausgegeben werden, solange dies nicht den Datenschutzbestimmungen widerspricht.
Daher sind sämtliche Felder im Schema als **empfohlen** zu behandeln, wenn
nicht explizit etwas anderes angegeben wurde.

### Herstellerspezifische Erweiterungen {#herstellerspezifische-erweiterungen}

In OParl können zusätzliche, herstellerspezifische Eigenschaften hinzugefügt werden.
Dazu wird diesen Eigenschaften ein Herstellerprefix vorangestellt. So könnte man z.B.
`Person` um eine Faxnummer erweitern:

~~~~~
"BeispielHersteller:faxNumber": "012345678",
~~~~~

### URL-Pfade in den Beispielen {#url-pfade-in-den-beispielen}

OParl-Clients wissen nichts vom Aufbau von Pfaden innerhalb von URLs,
müssen dies nicht wissen, und es gibt deshalb in der OParl-Spezifikation
keine Festlegungen dazu. Die in den Beispielen verwendeten URLs zeigen jedoch
einen guten Weg, wie die Empfehlungen zu URLs umgesetzt werden können.
