oparl:Membership (Mitgliedschaft) {#oparl_membership}
---------------------------------

Über Objekte diesen Typs wird die Mitgliedschaft von Personen in
Gruppierungen dargestellt. Diese Mitgliedschaften können zeitlich
begrenzt sein. Zudem kann abgebildet werden, dass eine Person
eine bestimmte Rolle bzw. Position innerhalb der Gruppierung
inne hat, beispielsweise den Vorsitz einer Fraktion.

**Beispiel 1**

~~~~~  {#membership_ex1 .json}
{
    "id": "https://oparl.example.org/memberships/385",
    "type": "http://oparl.org/schema/1.0/Membership",
    "person": "https://oparl.example.org/people/862",
    "organization": "https://oparl.example.org/organizations/5",
    "role": "Vorsitzender | Vorsitzende",
    "votingRight": true,
    "startDate": "2013-12-03T16:30:00+01:00"
}
~~~~~

**Beispiel 2**

~~~~~  {#membership_ex2 .json}
{
    "id": "https://oparl.example.org/memberships/693",
    "person": "https://oparl.example.org/people/284",
    "organization": "https://oparl.example.org/organizations/9",
    "role": "Sachkundiger Bürger | Sachkundige Bürgerin",
    "votingRight": false,
    "startDate": "2013-12-03T16:30:00+01:00",
    "endDate": "2014-07-28T00:00:00+02:00"
}
~~~~~

### Eigenschaften

`person`
:   Die betreffende Person, die Mitglied einer Gruppierung ist oder war.
    Typ: URL eines `oparl:Person` Objekts.
    Kardinalität: 1.
    ZWINGEND.
    
`organization`
:   Die Gruppierung, in der die Person Mitglied ist oder war.
    Typ: URL eines `oparl:Organization` Objekts.
    Kardinalität: 1.
    ZWINGEND.

`role`
:   Rolle der Person für die Gruppierung. Kann genutzt werden, um verschiedene
    Arten von Mitgliedschaften zum Beispiel in Gremien zu unterscheiden. Diese
    Eigenschaft funktioniert wie in
    [Vokabulare zur Klassifizierung](#vokabulare_klassifizierung) beschrieben
    entweder als URL zu einem skos:Concept oder als String. Der
    String (oder entsprechend das prefLabel des verlinkten Objekts) SOLL in 
    dieser Form sowohl die männliche als auch die weibliche Rollenbezeichnung 
    enthalten: `"Vorsitzender | Vorsitzende"`.
    Typ: String oder URL eines `skos:Concept` Objekts.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`post`
:   The post held by the person in the organization.
    Typ: `org:Post`.
    TODO: Prüfen, ob das ohne JSON-LD Sinn macht, oder ob hier zusätzliche
    Erläuterungen notwendig sind.
    OPTIONAL.

`onBehalfOf`
:   Entsendende Gruppierung, Fraktion, fraktionsloses oder externes Gremium.
    Es kann auch Mitglieder geben, die von keiner anderen Gruppierung 
    entsendet wurden (z. B. fraktionslose Abgeordnete). Da eine solche Person
    sich gewissermaßen selbst "entsendet" hat, SOLL in dem Fall hier der
    selbe Wert angegeben werden wie bei der Eigenschaft `person`.^[
    Dies entspricht `opengov:onBehalfOf` in Popolo.
    <http://popoloproject.com/specs/membership.html>]
    Typ: URL eines `oparl:Organization` oder `oparl:Person` Objekts.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`votingRight`
:   Gibt an, ob die Person in der Gruppierung stimmberechtigtes Mitglied ist.
    Typ: `boolean`.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`startDate`
:   Anfangszeitpunkt der Mitgliedschaft.^[Abgeleitet von: `schema:validFrom`
    in Popolo. <http://popoloproject.com/specs/membership.html>]
    Typ: `xsd:dateTime`.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`endDate`
:   Der Endzeitpunkt der Mitgliedschaft.^[Abgeleitet von: `schema:validThrough`
    in Popolo. <http://popoloproject.com/specs/membership.html>]
    Typ: `xsd:dateTime`.
    Kardinalität: 0 bis 1.
    OPTIONAL.
