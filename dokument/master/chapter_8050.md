oparl:Organization (Gruppierung)  {#oparl_organization}
--------------------------------

Dieser Objekttyp dient dazu, Gruppierungen von Personen abzubilden,
die in der parlamentarischen Arbeit eine Rolle spielen. Dazu zählen
in der Praxis insbesondere Fraktionen und Gremien.^[Ein Teil der 
Eigenschaften ist der "Organization" Ontologie (kurz: `org:Organization`)
des W3C entnommen. Quelle: The Organization Ontology, W3C Recommendation
16 January 2014, <http://www.w3.org/TR/vocab-org/>. Deren Bezeichnungen
wurden deshalb beibehalten. Das betrifft z.B. die Verwendung von
`classification`.]

**Beispiel 1**

~~~~~  {#organization_ex1 .json}
{
    "id": "https://oparl.example.org/organization/34",
    "type": "http://oparl.org/schema/1.0/Organization",
    "body": "https://oparl.example.org/bodies/1",
    "name": "Ausschuss für Haushalt und Finanzen",
    "shortName": "Finanzausschuss",
    "post": [
        "https://oparl.example.org/post/chairperson",
        "https://oparl.example.org/post/deputychairperson"
    ],
    "meeting": "https://oparl.example.org/meetings_for_org/34",
    "membership": [
        "https://oparl.example.org/memberships/27",
        "https://oparl.example.org/memberships/48",
        "https://oparl.example.org/memberships/57"
    ],
    "classification": "https://oparl.example.org/vocab/finance",
    "keyword": [
        "finanzen",
        "haushalt"
    ]
    "created": "2012-07-16T16:01:44+02:00",
    "startDate": "2012-07-17T00:00:00+02:00",
    "modified": "2012-08-16T14:05:27+02:00"
}
~~~~~

**Beispiel 2**

~~~~~  {#organization_ex1 .json}
{
    "id": "https://oparl.example.org/organization/34",
    "type": "http://oparl.org/schema/1.0/Organization",
    "body": "https://oparl.example.org/bodies/1",
    "name": "Ausschuss für Haushalt und Finanzen",
    "meeting": "https://oparl.example.org/meetings_for_org/34",
    "membership": "https://oparl.example.org/meetings_for_org/34",
    "modified": "2012-08-16T14:05:27+02:00"
}
~~~~~

### Eigenschaften ###

`body`
:   Körperschaft, zu der diese Gruppierung gehört.
    Typ: URL eines `oparl:Body` Objekts.
    Kardinalität: 1.
    ZWINGEND.

`name`
:   Offizielle (lange) Form des Namens der Gruppierung.
    Typ: Datentyp `xsd:string`.
    Kardinalität: 1.
    ZWINGEND.

`membership`
:   Mitgliedschaften dieser Gruppierung.
    Typ: Liste der URLs von `oparl:Membership` Objekten.
    Kardinalität: 0 bis *.
    ZWINGEND.

`meeting`
:   Sitzungen dieser Gruppierung. Invers zur
    Eigenschaft `organization` der Klasse `oparl:Meeting`. Da die Anzahl der
    Sitzungen stetig wachsen kann, wird EMPFOHLEN, die Liste über
    eine eigene URL verfügbar zu machen und damit Paginierung sowie die Filterung
    mittels startDate und endDate Parametern zu ermöglichen. Siehe dazu auch [Objektlisten](#objektlisten).
    Typ: Liste mit URLs von Objekten des Typs `oparl:Meeting`.
    Kardinalität: 0 bis *.
    ZWINGEND.

`shortName`
:   Der Name der Gruppierung als Kurzform.
    Typ: Datentyp `xsd:string`.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`post`
:   Position oder Positionen, die für diese Gruppierung vorgesehen sind.
    Diese Eigenschaft funktioniert wie in 
    [Vokabulare zur Klassifizierung](#vokabulare_klassifizierung) beschrieben entweder
    als URL zu einem `skos:Concept` oder als String.
    Die Strings bzw. `prefLabel`-Eigenschaften der Objekte SOLLEN sowohl die männliche
    als auch die weibliche Form enthalten, und zwar in dem Muster
    "männliche Form | weibliche Form" (genau in der Reihenfolge mit einem 
    Leerzeichen vor und nach dem "|"). Wenn sich beide Formen nicht unterscheiden,
    dann DARF die Form nur einmal verwendet werden: "Mitglied" und nicht "Mitglied | Mitglied".
    Weitere Beispiele: "Vorsitzender | Vorsitzende", "1. Stellvertreter | 1. Stellvertreterin",
    "2. Stellvertreter | 2. Stellvertreterin", "Schriftführer | Schriftführerin",
    "Stellvertretender Schriftführer | Stellvertretende Schriftführerin",
    "Ordentliches Mitglied", "Stellvertretendes Mitglied".
    TODO: "Ordentliches Mitglied", "Stellvertretendes Mitglied" müssen anders behandelt werden!
    Typ: String oder URL zu `skos:Concept` Objekt.
    Kardinalität: 0 bis *.
    OPTIONAL.

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
    "Hauptausschuss" kodiert sein ("https://oparl.example.org/hautausschuss skos:broader
    https://oparl.example.org/ausschuss"). Vgl. [Vokabulare zur Klassifizierung](#vokabulare_klassifizierung).
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
    Typ: `xsd:date` oder `xsd:dateTime`.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.
    
`endDate`
:   Datum des letzten Tages der Existenz der Gruppierung.
    Typ: `xsd:date` oder `xsd:dateTime`.
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
