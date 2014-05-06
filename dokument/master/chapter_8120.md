oparl:Consultation (Beratung)  {#oparl_consultation}
----------------------------

Der Objekttyp `oparl:Consultation` dient dazu, die Beratung einer Drucksache
([`oparl:Paper`](#oparl_paper)) in einer Sitzung abzubilden. Dabei ist es nicht entscheidend,
ob diese Beratung in der Vergangenheit stattgefunden hat oder diese für die
Zukunft geplant ist.

Die Gesamtheit aller Objekte des Typs `oparl:Consultation` zu einer bestimmten
Drucksache bildet das ab, was in der Praxis als "Beratungsfolge" der Drucksache
bezeichnet wird.

Ein Beispiel:

~~~~~  {#consultation_ex1 .json}
{
    "@type": "oparl:Consultation",
    "@id": "http://beispielris.de/consultation/47594",
    "paper": "http://beispielris.de/paper/2396",
    "agendaitem": "http://beispielris.de/agendaitem/15569",
    "committee": "http://beispielris.de/organization/96",
    "authoritative": false,
    "role": "http://beispielris.de/role/decision"
}
~~~~~

Das selbe Beispiel in kompakter Form (ein passender Kontext wird vorausgesetzt):

~~~~~  {#consultation_ex2 .json}
{
    "@context": "https://oparl.beispielris.de/Pfad/zum/Kontext/oparl.jsonld",
    "@type": "oparl:Consultation",
    "@id": "beispielris:consultation/47594",
    "paper": "beispielris:paper/2396",
    "agendaitem": "beispielris:agendaitem/15569",
    "committee": "beispielris:organization/96",
    "authoritative": false,
    "role": "beispielris:role/decision"
}
~~~~~

Das Objekt "beispielris:roles/decision" kann so aussehen:

~~~~~  {#role_ex1 .json}
{
    "@context": "https://oparl.beispielris.de/Pfad/zum/Kontext/oparl.jsonld"
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
    Typ: `oparl:Paper`
    ZWINGEND.

`agendaitem`
:   Tagesordnungspunkt, unter dem die Drucksache beraten wird.
    Typ: `oparl:AgendaItem`
    ZWINGEND.

`committee`
:   Gremium, dem die Sitzung zugewiesen ist, zu welcher der zuvor genannte Tagesordnungspunkt gehört.
    Hier kann auch eine mit Liste von Gremien angegeben werden (die verschiedenen `oparl:Body` und `oparl:System`
    angehören können).
    Die Liste ist dann geordnet.
    Das erste Gremium der Liste ist federführend.
    Typ: `oparl:Organization`
    ZWINGEND.

`authoritative`
:   Drückt aus, ob bei dieser Beratung ein Beschluss zu der Drucksache gefasst 
    wird (`true`) wird oder nicht (`false`).
    Typ: boolean.
    Diese Eigenschaft ist OPTIONAL.

`role`
:   Rolle oder Funktion der Beratung. z.B. Anhörung (hearing), Entscheidung (decision), 
    Kenntnisnahme (notice), Vorberatung (counseling) usw. Es wird empfohlen in den URLs entsprechende englische
    Bestandteile zu verwenden. Die Rollenobjekte haben nur eine festgelegte Eigenschaft: `skos:prefLabel` für den Namen.
    In einer zukünftigen Version von OParl können gegebenenfalls die am stärksten benötigten Rollen
    standardisiert werden.
    Typ: `skos:Concept`
    OPTIONAL

`classification`
:   Schlagwort, Begriff mit `skos:prefLabel`. Allgemeiner verwendbar als `role`.
    Typ: `skos:Concept`
    OPTIONAL
