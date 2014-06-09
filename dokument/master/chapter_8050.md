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
    "shortName": {
        "@language" :"de",
        "@value": "Finanzausschuss"
    },
    "name": {
        "@language": "de",
        "@value": "Ausschuss für Haushalt und Finanzen"
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

Das entsprechende Beispiel in kompakter Form:


~~~~~  {#organization_ex2 .json}
{
    "@context": "https://oparl.beispielris.de/Pfad/zum/Kontext/organization.jsonld",
    "@type": "oparl:Organization",
    "@id": "beispielris:organization/34",
    "body": "0",
    "shortName": "Finanzausschuss",
    "name": "Ausschuss für Haushalt und Finanzen",
    "post": [
        "beispielris:post/chairperson",
        "beispielris:post/deputyChairperson"
    ],
    "member": [
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
:   Körperschaft, zu der diese Gruppierung gehört.
    Typ: `oparl:Body`.
    Kardinalität: 1.
    ZWINGEND.

`meeting`
:   Sitzung dieser Gruppierung.
    Typ: `oparl:Meeting`.
    Kardinalität: 0 bis *.
    Constraint: Diese Eigenschaft ist invers zur Eigenschaft `organization` der Klasse `oparl:Meeting`
    (In OWL: `oparl:organization owl:inverseOf oparl:meeting .`)
    EMPFOHLEN.

`name`
:   Offizielle (lange) Form des Namens der Gruppierung.
    Typ: Datentyp `xsd:string`.
    Kardinalität: 1.
    Diese Eigenschaft ist ZWINGEND.

`shortName`
:   Der Name der Gruppierung als Kurzform.
    Typ: Datentyp `xsd:string`.
    Kardinalität: 0 bis 1.
    Die Eigenschaft ist OPTIONAL.

`post`
:   Position oder Positionen, die für diese Gruppierung vorgesehen sind. Die Objekte gehören zu der Klasse `org:Post` oder einer ihrer Unterklassen.
    Die `skos:prefLabel`-Eigenschaften der Objekte SOLLEN sowohl die männliche als auch die weibliche Form enthalten, und zwar in dem Muster
    "männliche Form | weibliche Form" (genau in der Reihenfolge mit einem Leerzeichen vor und nach dem "|").
    Wenn sich beide Formen nicht unterscheiden, dann DARF die Form nur einmal verwendet werden:
    "Mitglied" und nicht "Mitglied | Mitglied".
    Dadurch kann auch solche Software einen sinnvollen Text anzeigen, die keine Fall-Unterscheidung nach Geschlecht
    der Personen vornimmt.
    z. B. "Vorsitzender | Vorsitzende",
    "1. Stellvertreter | 1. Stellvertreterin",
    "2. Stellvertreter | 2. Stellvertreterin",
    "Schriftführer | Schriftführerin",
    "Stellvertretender Schriftführer | Stellvertretende Schriftführerin",
    "Ordentliches Mitglied",
    "Stellvertretendes Mitglied"
Siehe https://github.com/OParl/specs/issues/45
    TODO: "Ordentliches Mitglied", "Stellvertretendes Mitglied" müssen anders behandelt werden!
    Typ: `oparl:Post`.
    Kardinalität: 0 bis *.
    Die Eigenschaft ist OPTIONAL.

`member`
:   Mitglieder dieser Organisation. Auch alle Personen mit
    Positionen in der Organisation sind hier anzugeben.
    Typ: `oparl:Person`.
    Kardinalität: 0 bis *.
    Diese Eigenschaft ist ZWINGEND.
    
`subOrganizationOf`
:   Ggf. URL der übergeordneten Organisation.
    Typ: `oparl:Organization`.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`organizationType`
:   Objekt mit `skos:prefLabel`, z. B. für "Rat", "Hauptausschuss", "Ausschuss",
    "Beirat", "Projektbeirat", "Kommission", "AG", "Verwaltungsrat".
    Vgl. [Vokabulare zur Klassifizierung](#vokabulare_klassifizierung).
    Typ: `skos:Concept`.
    Kardinalität: 0 bis 1.
    OPTIONAL.
    
`keyword`
:   Schlagworte. Vgl. [Vokabulare zur Klassifizierung](#vokabulare_klassifizierung).
    Typ: `skos:Concept`.
    Kardinalität: 0 bis *.
    OPTIONAL.

`startDate`
:   Datum des ersten Tages der Existenz der Organisation.
    FRAGE: Muss zwischen Konstituierung und Beschluss zur Gründung unterschieden werden? 
    Typ:`xsd:date`.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.
    
`endDate`
:   Datum des letzten Tages der Existenz der Organisation.
    Typ: `xsd:date`.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`created`
:   Datum/Uhrzeit der Erzeugung des Objekts.
    Typ: `xsd:dateTime`.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.

`modified`
:   Datum/Uhrzeit der letzten Bearbeitung des Objekts.
    Typ: `xsd:dateTime`.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.
