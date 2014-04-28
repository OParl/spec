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
    "committee": "http://beispielris.de/organizations/96",
    "authoritative": false,
    "role": "http://beispielris.de/roles/decision"
}
~~~~~

Das selbe Beispiel in kompakter Form (ein passender Kontext wird vorausgesetzt):

~~~~~  {#consultation_ex2 .json}
{
    "@context": "https://oparl.beispielris.de/Pfad/zum/Kontext/oparl.jsonld"
    "@type": "oparl:Consultation",
    "@id": "beispielris:consultations/47594",
    "paper": "beispielris:papers/2396",
    "agendaitem": "beispielris:agendaitem/15569",
    "committee": "beispielris:organization/96",
    "authoritative": false,
    "role": "beispielris:roles/decision"
}
~~~~~

Das Objekt "beispielris:roles/decision" kann so aussehen:

~~~~~  {#role_ex1 .json}
{
    "@context": "https://oparl.beispielris.de/Pfad/zum/Kontext/oparl.jsonld"
    "@id": "beispielris:roles/decision",
    "prefLabel": "Entscheidung"
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
:   URL des Gremiums (oparl:Organization), dem die Sitzung zugewiesen ist, zu
    welcher der zuvor genannte Tagesordnungspunkt gehört.
    Hier kann auch eine mit Liste von Gremien angegeben werden. Die Liste ist dann geordnet.
    Das erste Gremium ist federführend.
    Diese Eigenschaft ist ZWINGEND.

`authoritative`
:   Drückt aus, ob bei dieser Beratung ein Beschluss zu der Drucksache gefasst 
    wird (*true*) wird oder nicht (*false*).
    Typ: Wahrheitswert.
    Diese Eigenschaft ist OPTIONAL.

`role`
:   URL der Rolle oder Funktion der Beratung. z.B. Anhörung (hearing), Entscheidung (decision), 
    Kenntnisnahme (notice), Vorberatung (counseling) usw. Es wird empfohlen in den URLs entsprechende englische
    Bestandteile zu verwenden. Die Rollenobjekte haben nur eine festgelegte Eigenschaft: "skos:prefLabel" für den Namen.
    In einer zukünftigen Version von OParl können gegebenenfalls die am stärksten benötigten Rollen
    standardisiert werden.
    OPTIONAL
