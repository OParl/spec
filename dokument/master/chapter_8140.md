oparl:Membership {#oparl_membership}
----------------

Über Objekte diesen Typs wird die Mitgliedschaft von Personen in
Gruppierungen dargestellt. Diese Mitgliedschaften können zeitlich
begrenzt sein. Zudem kann abgebildet werden, dass eine Person
eine bestimmte Rolle bzw. Position innerhalb der Gruppierung
inne hat, beispielsweise den Vorsitz einer Fraktion.

### Beispiel ###

Ein Kontext:

~~~~~  {#membership_ex1 .json}
{
    "person": {
        "@id": "oparl:person",
        "@type": "@id"
    },
    "organization": {
        "@id": "oparl:organization",
        "@type": "@id"
    },
    "role": {
        "@id": "oparl:role",
        "@type": "@id"
    },
    "post": {
        "@id": "oparl:post",
        "@type": "@id"
    },  
    "onBehalfOf": {
        "@id": "oparl:onBehalfOf",
        "@type": "@id"
    },
    "startDate": {
        "@id": "schorg:startDate",
        "@type": "xsd:dateTime"
    },
    "endDate": {
        "@id": "schorg:endDate",
        "@type": "xsd:dateTime"
    }
}
~~~~~


~~~~~  {#membership_ex2 .json}
{
...
    "person": "beispielris:people/862",
    "organization": "beispielris:organizations/5",
    "role": "beispielris:vocab/chair",
    "votingRight": true,
    "startDate": "2013-12-03T16:30:00+01:00"
...
}
~~~~~

### Eigenschaften

`person`
:   Die betreffende Person, die Mitglied einer Gruppierung ist oder war.
    Typ: `oparl:Person`.
    Kardinalität: 1.
    ZWINGEND.
    
`organization`
:   Die Gruppierung, in der die Person Mitglied ist oder war.
    Typ: `oparl:Organization`.
    Kardinalität: 1.
    ZWINGEND.

`role`
:   Rolle der Person für die Gruppierung. Das Objekt hat eine `skos:prefLabel`-Eigenschaft,
    deren Wert eine Funktionsbezeichnung ist, z. B.
    "1. pers. Vertreter | 1. pers. Vertreterin" oder "2. pers. Vertreter | 2. pers. Vertreterin".
    Gewöhnliche Mitglieder haben in der Regel keine besondere Rolle,
    aber auch eine Unterscheidung zwischen z. B. "Sachkundige Bürger | Sachkundige Bürgerin"
    und "Ratsherr | Ratsfrau" bei einfachen Mitgliedern ist hiermit möglich.
    FRAGE: Wie soll bei einem sachkundigen Bürger verfahren werden, der gleichzeitig Vorsitzender ist?
    Typ: `org:Role`.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`post`
:   The post held by the person in the organization.
    Typ: `org:Post`.
    OPTIONAL.

`onBehalfOf`
:   Entsendende Gruppierung, Fraktion, fraktionsloses oder externes Gremium.
    Dies entspricht `opengov:onBehalfOf` in Popolo.
    Es kann auch Mitglieder geben, die von keiner anderen Gruppierung entsendet wurden (z. B. fraktionslose Abgeordnete).
    Da eine solche Person sich selbst "entsendet" hat, SOLL in dem Fall hier der
    selbe Wert angegeben werden wie bei der Eigenschaft `person`.
    Typ: `oparl:Organization` | `oparl:Person`.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`votingRight`
:   Gibt an, ob die Person in der Gruppierung stimmberechtites Mitglied ist.
    Typ: `boolean`.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`startDate`
:   Der Anfangszeitpunkt der Mitgliedschaft.
    Abgeleitet von: `schema:validFrom` wie bei Popolo^[<http://popoloproject.com/specs/membership.html>].
    Typ: `xsd:dateTime`.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`endDate`
:   Der Endzeitpunkt der Mitgliedschaft.
    Abgeleitet von: `schema:validThrough` wie bei Popolo^[<http://popoloproject.com/specs/membership.html>].
    Typ: `xsd:dateTime`.
    Kardinalität: 0 bis 1.
    OPTIONAL.

TODO: Folgende Verweise einbauen oder entfernen:

* https://github.com/OParl/specs/issues/122
* http://www.w3.org/TR/vocab-org/#membership-roles-posts-and-reporting
