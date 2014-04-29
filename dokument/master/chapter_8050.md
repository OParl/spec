oparl:Organization (Gruppierung)  {#oparl_organization}
--------------------------------

Dieser Objekttyp dient dazu, Gruppierungen von Personen abzubilden,
die in der parlamentarischen Arbeit eine Rolle spielen. Dazu zählen
in der Praxis insbesondere Fraktionen und Gremien.

Ein Beispiel in expandierter Form:

~~~~~  {#organization_ex1 .json}
{
    "@type": "http://oparl.org/schema/1.0/Organization",
    "@id": "http://oparl.beispielris.de/organizations/34",
    "body": "http://oparl.beispielris.de/bodies/0",
    "name": "Finanzausschuss",
    "nameLong": "Finanzausschuss des Rates der Stadt Köln",
    "role": {
        "@list": [
        // ohne @list wird in JSON-LD die Reihenfolge nicht festgelegt
        "http://oparl.beispielris.de/roles/vorsitze",
        "http://oparl.beispielris.de/people/stellvertretender_vorsitz"
        ]
    },
    "members": [
        "http://oparl.beispielris.de/people/27",
        "http://oparl.beispielris.de/people/48",
        "http://oparl.beispielris.de/people/57"
    ],
    "category": "http://oparl.beispielris.de/org-categories/finance",
    "last_modified": "2012-08-16T14:05:27+02:00"
}
~~~~~

Das selbe Beispiel in kompakter Form. Ein geeigneter Kontext wird vorausgesetzt:

~~~~~  {#organization_ex2 .json}
{
    "@context": "https://oparl.beispielris.de/Pfad/zum/Kontext/oparl.jsonld",
    "@type": "oparl:Organization",
    "@id": "beispielris:organizations/34",
      // kann eventuell weiter verkürzt werden
    "body": "0",
    "name": "Finanzausschuss",
    "nameLong": "Finanzausschuss des Rates der Stadt Köln",
    "role:" [
        "beispielris:roles/vorsitz",
        "beispielris:roles/stellvertretender_vorsitz"
    ],
    "members": [
        "27",
        "48",
        "57"
    ],
    "category": "beispielris:org-categories/finance",
    "last_modified": "2012-08-16T14:05:27+02:00"
}
~~~~~
### Eigenschaften ###

`body`
:   URL der Körperschaft, zu der diese Gruppierung gehört. 
    ZWINGEND

`name`
:   Der Name der Gruppierung.
    ZWINGEND

`nameLong`
:   Langform des Namens der Gruppierung.
    OPTIONAL

`role`
:   Rolle oder Rollen, die für diese Gruppierung vorgesehen sind. Die Rollen-Objekte gehören zu der Klasse org:Role oder einer ihrer Unterklassen.
    OPTIONAL

`members`
:   Entweder die vollständige Liste der URLs aller Mitglieder
    dieser Organisation (Objekte vom Typ `[oparl:Person](#oparl_person)`)
    oder URL zum Abruf dieser Liste.
    Sollte die Gruppierung keine
    Mitglieder haben, enthält die Liste keine Einträge.
    ZWINGEND
    
`subOrganizationOf`
:   Ggf. URL der übergeordneten Organisation.
    OPTIONAL.

`created`
:   Datum/Uhrzeit der Erzeugung des Objekts.
    EMPFOHLEN

`category`
    Schlagworte. Dies sind Objekte mit einem `skos:prefLabel`-Attribut (für jede unterstützte Sprache) mit einer
    Zeichenkette. In einer zukünftigen OParl-Version wird möglicherweise eine Menge solcher Schlagwort-Objekte
    definiert. Anregungen gibt es u.a. in der Tabelle "Kategorien" im unteren Drittel der Seite http://htmlpreview.github.io/?https://github.com/fraunhoferfokus/ogd-metadata/blob/master/OGPD_JSON_Schema.html 
    OPTIONAL
    
`lastModified`
:   Datum/Uhrzeit der letzten Bearbeitung des Objekts.
    EMPFOHLEN
