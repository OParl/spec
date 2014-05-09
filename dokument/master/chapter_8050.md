oparl:Organization (Gruppierung)  {#oparl_organization}
--------------------------------

Dieser Objekttyp dient dazu, Gruppierungen von Personen abzubilden,
die in der parlamentarischen Arbeit eine Rolle spielen. Dazu zählen
in der Praxis insbesondere Fraktionen und Gremien.

Ein Beispiel in expandierter Form:

~~~~~  {#organization_ex1 .json}
{
    "@type": "http://oparl.org/schema/1.0/Organization",
    "@id": "https://oparl.beispielris.de/organization/34",
    "body": "https://oparl.beispielris.de/body/0",
    "name": {
        @language" :"de",
        @value": "Finanzausschuss"
    },
    "nameLong": {
        "@language": "de",
        "@value": "Finanzausschuss des Rates der Stadt Köln"
    },
    "post": {
        "@list": [
            "https://oparl.beispielris.de/post/chairperson",
            "https://oparl.beispielris.de/post/deputyChairperson"
        ]
    },
    "member": [
        "https://oparl.beispielris.de/person/27",
        "https://oparl.beispielris.de/person/48",
        "https://oparl.beispielris.de/person/57"
    ],
    "organizationType": "https://oparl.beispielris.de/vocab/committee",
    "classification": "https://oparl.beispielris.de/vocab/finance",
    "modified": "2012-08-16T14:05:27+02:00"
}
~~~~~

Das selbe Beispiel in kompakter Form.

Ein Kontext:
~~~~~~~~~~
{
    "@language": "de",
    // ...
}
~~~~~~~~~~


~~~~~  {#organization_ex2 .json}
{
    "@context": "https://oparl.beispielris.de/Pfad/zum/Kontext/organization.jsonld",
    "@type": "oparl:Organization",
    "@id": "beispielris:organization/34",
      // kann eventuell weiter verkürzt werden
    "body": "0",
    "name": "Finanzausschuss",
    "nameLong": "Finanzausschuss des Rates der Stadt Köln",
    "post:" [
        "beispielris:post/chairperson",
        "beispielris:post/deputyChairperson"
    ],
    "members: [
        "27",
        "48",
        "57"
    ],
    "organizationType": "beispielris:vocab/committee",
    "classification": "beispielris:vocab/finance",
    "modified": "2012-08-16T14:05:27+02:00"
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

`post`
:   Position oder Positionen, die für diese Gruppierung vorgesehen sind. Die Objekte gehören zu der Klasse `org:Post` oder einer ihrer Unterklassen.
    Die `skos:prefLabel`-Eigenschaften der Objekte SOLLEN sowohl die männliche als auch die weibliche Form enthalten, und zwar in dem Muster
    "männliche Form | weibliche Form" (genau in der Reihenfolge mit einem Leerzeichen vor und nach dem "|")
    Wenn sich beide Formen nicht unterscheiden, dann DARF die Form nur einmal verwendet werden:
    "Mitglied" und nicht "Mitglied | Mitglied".
    Dadurch kann auch solche Software einen sinnvollen Text anzeigen, die keine Fall-Unterscheidung nach Geschecht
    der Personen vornimmt.
    z.B. "Vorsitzender | Vorsitzende",
    "1. Stellvertreter | 1. Stellvertreterin",
    "2. Stellvertreter | 2. Stellvertreterin",
    "Schriftführer | Schriftführerin",
    "Stellvertretender Schriftführer | Stellvertretende Schriftführerin",
    "Ordentliches Mitglied",
    "Stellvertretendes Mitglied"
Siehe https://github.com/OParl/specs/issues/45
TODO: "Ordentliches Mitglied", "Stellvertretendes Mitglied" müssen anders behandelt werden!
    OPTIONAL

`member`
:   URLs aller Mitglieder dieser Organisation (Objekte vom Typ `[oparl:Person](#oparl_person)`). Auch alle Personen mit
    Positionen in der Organisation sind hier anzugeben.
    ZWINGEND (falls es Mitglieder gibt)
    
`subOrganizationOf`
:   Ggf. URL der übergeordneten Organisation.
    OPTIONAL.

`created`
:   Datum/Uhrzeit der Erzeugung des Objekts.
    EMPFOHLEN

`classification`
:   Schlagworte. Dies sind `skos:Concept`-Objekte mit einem `skos:prefLabel`-Attribut (für jede unterstützte Sprache) mit einer
    Zeichenkette. In einer zukünftigen OParl-Version wird möglicherweise eine Menge solcher Schlagwort-Objekte
    definiert. Anregungen gibt es u.a. in der Tabelle "Kategorien" im unteren Drittel der Seite http://htmlpreview.github.io/?https://github.com/fraunhoferfokus/ogd-metadata/blob/master/OGPD_JSON_Schema.html 
    OPTIONAL

`organizationType`
:   Objekt mit `skos:prefLabel`, z.B. "Rat", "Hauptausschuss", "Ausschuss"
    "Beirat", "Projektbeirat", "Kommission", "AG", "Verwaltungsrat"
    OPTIONAL
    
`modified`
:   Datum/Uhrzeit der letzten Bearbeitung des Objekts.
    EMPFOHLEN
