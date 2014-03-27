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
    "@id": "http://beispielris.de/consultations/47594",
    "paper": "http://beispielris.de/papers/2396",
    "agendaitem": "http://beispielris.de/agendaitems/15569",
    "committee": "http://beispielris.de/organisations/96",
    "authoritative": false
}
~~~~~

### Eigenschaften ###

`@id`
:   URL des Objekts. Diese Eigenschaft ist ZWINGEND.

`paper`
:   URL der Drucksache, die beraten wird. Diese Eigenschaft ist ZWINGEND.

`agendaitem`
:   URL des Tagesordnungspunktes (oparl:Agendaitem), unter dem die Drucksache 
    beraten wird. Diese Eigenschaft ist ZWINGEND.

`committee`
:   URL des Gremiums (oparl:Organization), dem die Sitzung zugewisen ist, zu
    welcher der zuvor genannte Tagesordnungspunkt gehört. Diese Eigenschaft
    ist ZWINGEND.

`authoritative`
:   Drückt aus, ob bei dieser Beratung ein Beschluss zu der Drucksache gefasst 
    wird (*true*) wird oder nicht (*false*). Diese Eigenschaft ist OPTIONAL.
    Typ: Wahrheitswert.
