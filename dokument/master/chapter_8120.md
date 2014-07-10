oparl:Consultation (Beratung)  {#oparl_consultation}
-----------------------------

Der Objekttyp `oparl:Consultation` dient dazu, die Beratung einer Drucksache
([`oparl:Paper`](#oparl_paper)) in einer Sitzung abzubilden. Dabei ist es nicht entscheidend,
ob diese Beratung in der Vergangenheit stattgefunden hat oder diese für die
Zukunft geplant ist.

Die Gesamtheit aller Objekte des Typs `oparl:Consultation` zu einer bestimmten
Drucksache bildet das ab, was in der Praxis als "Beratungsfolge" der Drucksache
bezeichnet wird.

**Beispiel**

~~~~~  {#consultation_ex2 .json}
{
    "id": "https://oparl.example.org/consultation/47594",
    "type": "http://oparl.org/schema/1.0/Consultation",
    "paper": "https://oparl.example.org/paper/2396",
    "agendaItem": "https://oparl.example.org/agendaitem/15569",
    "organization": "https://oparl.example.org/organization/96",
    "authoritative": false,
    "role": "https://oparl.example.org/role/decision"
}
~~~~~


### Eigenschaften ###

`paper`
:   Drucksache, die beraten wird.
    Typ: URL eines Objekts vom Typ `oparl:Paper`.
    Kardinalität: 1.
    ZWINGEND.

`agendaItem`
:   Tagesordnungspunkt, unter dem die Drucksache beraten wird.
    Typ: URL eines Objekts vom Typ `oparl:AgendaItem`.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.

`organization`
:   Gremium, dem die Sitzung zugewiesen ist, zu welcher der zuvor genannte
    Tagesordnungspunkt gehört.
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
    Kardinalität: 0 bis 1.
    OPTIONAL.

`role`
:   Rolle oder Funktion der Beratung. Zum Beispiel Anhörung, Entscheidung, 
    Kenntnisnahme, Vorberatung usw. Diese Eigenschaft funktioniert wie in 
    [Vokabulare zur Klassifizierung](#vokabulare_klassifizierung) beschrieben 
    entweder als URL zu einem `skos:Concept` oder als String.
    Typ: String oder URL eines `skos:Concept` Objekts.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`keyword`
:   Schlagworte.
    Typ: Array von Strings oder URLs zu `skos:Concept` Objekten
    (vgl. [Vokabulare zur Klassifizierung](#vokabulare_klassifizierung)).
    Kardinalität: 0 bis *.
    OPTIONAL.
