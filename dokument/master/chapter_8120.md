oparl:Consultation (Beratung)  {#oparl_consultation}
-----------------------------

Der Objekttyp `oparl:Consultation` dient dazu, die Beratung einer Drucksache
([`oparl:Paper`](#oparl_paper)) in einer Sitzung abzubilden. Dabei ist es nicht entscheidend,
ob diese Beratung in der Vergangenheit stattgefunden hat oder diese für die
Zukunft geplant ist.

Die Gesamtheit aller Objekte des Typs `oparl:Consultation` zu einer bestimmten
Drucksache bildet das ab, was in der Praxis als "Beratungsfolge" der Drucksache
bezeichnet wird.

### Beispiel ###

Ein passender Kontext:

~~~~~
{   
    "paper": {
        "@id": "oparl:paper",
        "@type": "@id"
    },
    "agendaItem": {
        "@id": "oparl:agendaItem",
        "@type": "@id"
    },
    "organization": {
        "@id": "oparl:organization",
        "@type": "@id"
    },
    "authoritative": {
        "@id": "oparl:authoritative",
        "@type": "xsd:boolean"
    },
    "role": {
        "@id": "oparl:role",
        "@type": "@id"
    }
}
~~~~~


~~~~~  {#consultation_ex2 .json}
{
    "@context": "https://oparl.example.org/Pfad/zum/Kontext/oparl.jsonld",
    "@type": "oparl:Consultation",
    "@id": "beispielris:consultation/47594",
    "paper": "beispielris:paper/2396",
    "agendaItem": "beispielris:agendaitem/15569",
    "organization": "beispielris:organization/96",
    "authoritative": false,
    "role": "beispielris:role/decision"
}
~~~~~

Das Objekt "beispielris:roles/decision" kann so aussehen:

~~~~~  {#role_ex1 .json}
{
    "@context": "https://oparl.example.org/Pfad/zum/Kontext/oparl.jsonld",
    "@id": "beispielris:role/decision",
    "prefLabel": {
        "de": "Entscheidung",
        "en": "decision"
    }
}
~~~~~


### Eigenschaften ###

`paper`
:   Drucksache, die beraten wird.
    Typ: `oparl:Paper`.
    Kardinalität: 1.
    ZWINGEND.

`agendaItem`
:   Tagesordnungspunkt, unter dem die Drucksache beraten wird.
    Typ: `oparl:AgendaItem`.
    Kardinalität: 0 bis *.
    EMPFOHLEN.

`organization`
:   Gremium, dem die Sitzung zugewiesen ist, zu welcher der zuvor genannte Tagesordnungspunkt gehört.
    Hier kann auch eine mit Liste von Gremien angegeben werden (die verschiedenen `oparl:Body` und `oparl:System`
    angehören können).
    Die Liste ist dann geordnet.
    Das erste Gremium der Liste ist federführend.
    Typ: `oparl:Organization`.
    Kardinalität: 1 bis *.
    ZWINGEND.

`authoritative`
:   Drückt aus, ob bei dieser Beratung ein Beschluss zu der Drucksache gefasst 
    wird (`true`) wird oder nicht (`false`).
    Typ: Boolean.
    Kardinalität: 1.
    OPTIONAL.

`role`
:   Rolle oder Funktion der Beratung. Zum Beispiel Anhörung (hearing), Entscheidung (decision), 
    Kenntnisnahme (notice), Vorberatung (counseling) usw. Es wird empfohlen in den URLs entsprechende englische
    Bestandteile zu verwenden. Die Rollenobjekte haben nur eine festgelegte Eigenschaft: `skos:prefLabel` für den Namen.
    In einer zukünftigen Version von OParl können gegebenenfalls die am stärksten benötigten Rollen
    standardisiert werden.
    Typ: `skos:Concept`.
    Kardinalität: 1.
    OPTIONAL.

`keyword`
:   Schlagwort, Begriff mit `skos:prefLabel`. Allgemeiner verwendbar als `role`.
    Typ: `skos:Concept`.
    Kardinalität: 0 bis *.
    OPTIONAL.
