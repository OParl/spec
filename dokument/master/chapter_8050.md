oparl:Organization (Gruppierung)  {#oparl_organization}
--------------------------------

Dieser Objekttyp dient dazu, Gruppierungen von Personen abzubilden,
die in der parlamentarischen Arbeit eine Rolle spielen. Dazu zählen
in der Praxis insbesondere Fraktionen und Gremien.

Ein Teil der Eigenschaften ist der "Organization" Ontologie des W3C entnommen
(kurz: `org:Organization`)^[The Organization Ontology, W3C Recommendation 16 January 2014,
http://www.w3.org/TR/vocab-org/]. Deren Bezeichnungen wurden deshalb beibehalten.
Das betrifft z.B. die Verwendung von `classification`.

### Beispiel ###

Der Kontext:

~~~~~
    "body": {
        "@id": "oparl:body",
        "@type": "@id"
    },
    "shortName": {
        "@id": "oparl:shortName",
        "@type": "xsd:string"
    },
    "name": {
        "@id": "oparl:name",
        "@type": "xsd:string"
    },
    "post": {
        "@id": "oparl:post",
        "@container": "@list",
        "@type": "@id"
    },
    "member": {
        "@id": "oparl:member",
        "@type": "@id"
    },
    "classification": {
        "@id": "oparl:classification",
        "@type": "@id"
    },
    "modified": {
        "@id": "dc:modified",
        "@type": "xsd:dateTime"
    }   
~~~~~

~~~~~  {#organization_ex2 .json}
{
    "@context": "https://oparl.example.org/Pfad/zum/Kontext/organization.jsonld",
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
        "beispielris:person/27",
        "beispielris:person/48",
        "beispielris:person/57"
    ],
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
:   Sitzungen dieser Gruppierung. Invers zur
    Eigenschaft `organization` der Klasse `oparl:Meeting`. Da die Anzahl der
    Sitzungen stetig wachsen kann, wird EMPFOHLEN, die Liste unter
    einer eigenen URL auszugeben und damit Paginierung zu ermöglichen.
    Typ: `oparl:Meeting`.
    Kardinalität: 0 bis *.
    EMPFOHLEN.

`name`
:   Offizielle (lange) Form des Namens der Gruppierung.
    Typ: Datentyp `xsd:string`.
    Kardinalität: 1.
    ZWINGEND.

`shortName`
:   Der Name der Gruppierung als Kurzform.
    Typ: Datentyp `xsd:string`.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`post`
:   Position oder Positionen, die für diese Gruppierung vorgesehen sind.
    Die Objekte gehören zu der Klasse `org:Post` oder einer ihrer Unterklassen.
    Die `skos:prefLabel`-Eigenschaften der Objekte SOLLEN sowohl die männliche
    als auch die weibliche Form enthalten, und zwar in dem Muster
    "männliche Form | weibliche Form" (genau in der Reihenfolge mit einem 
    Leerzeichen vor und nach dem "|"). Wenn sich beide Formen nicht unterscheiden,
    dann DARF die Form nur einmal verwendet werden: "Mitglied" und nicht "Mitglied | Mitglied".
    Dadurch kann auch solche Software einen sinnvollen Text anzeigen, die keine
    Fall-Unterscheidung nach Geschlecht
    der Personen vornimmt.
    z. B. "Vorsitzender | Vorsitzende",
    "1. Stellvertreter | 1. Stellvertreterin",
    "2. Stellvertreter | 2. Stellvertreterin",
    "Schriftführer | Schriftführerin",
    "Stellvertretender Schriftführer | Stellvertretende Schriftführerin",
    "Ordentliches Mitglied",
    "Stellvertretendes Mitglied".
    Siehe https://github.com/OParl/specs/issues/45
    TODO: "Ordentliches Mitglied", "Stellvertretendes Mitglied" müssen anders behandelt werden!
    Typ: `oparl:Post`.
    Kardinalität: 0 bis *.
    OPTIONAL.

`member`
:   Mitglieder dieser Gruppierung. Auch alle Personen mit
    Positionen in der Gruppierung sind hier anzugeben.
    In der Eigenschaft member werden nur die Personen aufgezählt, ohne weitere
    Daten, in den `oparl:Membership`-Objekten sind zusätzliche Eigenschaften
    wie Start- und Endedatum oder Rolle vorhanden.
    Typ: `oparl:Person`.
    Kardinalität: 0 bis *.
    DEPRECATED.

`subOrganizationOf`
:   Ggf. URL der übergeordneten Gruppierung.
    Typ: `oparl:Organization`.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`classification`
:   Die Art der Gruppierung. In Frage kommen z.B. "Rat", "Hauptausschuss", "Ausschuss",
    "Beirat", "Projektbeirat", "Kommission", "AG", "Verwaltungsrat". Die Angabe soll
    möglichst präzise erfolgen. So ist die Angabe "Hauptausschuss" präziser als
    "Ausschuss". Im Vokabular SOLL dann dieses Verhältnis zwischen "Ausschuss" und
    "Hauptausschuss" kodiert sein ("beispielris:hautausschuss skos:broader
    beispielris:ausschuss"). Vgl. [Vokabulare zur Klassifizierung](#vokabulare_klassifizierung).
    Typ: `skos:Concept`.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.
    
`keyword`
:   Schlagworte. Vgl. [Vokabulare zur Klassifizierung](#vokabulare_klassifizierung).
    Typ: `skos:Concept`.
    Kardinalität: 0 bis *.
    OPTIONAL.

`startDate`
:   Gründungsdatum der Gruppierung. Kann z. B. das Datum der konstituierenden
    Sitzung sein.
    Typ:`xsd:date`.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.
    
`endDate`
:   Datum des letzten Tages der Existenz der Gruppierung.
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
