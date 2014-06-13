oparl:Membership {#oparl_membership}
----------------

Über Objekte diesen Typs wird die Mitgliedschaft von Personen in
Gruppierungen dargestellt. Diese Mitgliedschaften können zeitlich
begrenzt sein. Zudem kann abgebildet werden, dass eine Person
eine bestimmte Rolle bzw. Position innerhalb der Gruppierung
inne hat, beispielsweise den Vorsitz einer Fraktion.

~~~~~  {#location_ex1 .json}
{
    "person": "beispielris:people/862",
    "organization": "beispielris:organizations/5",
    "role": "beispielris:vocab/chair",
    "startDate": "2013-12-03T16:30:00+01:00"
}
~~~~~

### Eigenschaften

`person`
:   Die betreffende Person, die Mitglied einer Gruppierung ist oder war.
    Typ: `oparl:Person`.
    Kardinalität: 1.
    Die Eigenschaft ist ZWINGEND.
    
`organization`
:   Die Gruppierung, in der die Person Mitglied ist oder war.
    Typ: `oparl:Organization`.
    Kardinalität: 1.
    Die Eigenschaft ist ZWINGEND.

`role`
:   Rolle der Person für die Gruppierung. Das Objekt hat eine `skos:prefLabel`-Eigenschaft,
    deren Wert eine Funktionsbezeichnung ist, z. B.
    "1. pers. Vertreter | 1. pers. Vertreterin" oder "2. pers. Vertreter | 2. pers. Vertreterin".
    Gewöhnliche Mitglieder haben in der Regel keine besondere Rolle,
    aber auch eine Unterscheidung zwischen z. B. "Sachkundige Bürger | Sachkundige Bürgerin"
    und "Ratsherr | Ratsfrau" bei einfachen Mitgliedern ist hiermit möglich.
    FRAGE: Wie soll bei einem sachkundigen Bürger verfahren werden, der gleichzeitig Vorsitzender ist?
    Typ: `org:Role`.
    Kardinalität: 0 bis 1.
    Die Eigenschaft ist OPTIONAL.

`post`
:   The post held by the person in the organization.
    Typ: `org:Post`.
    OPTIONAL.

`onBehalfOf`
:   Entsendende Gruppierung, Fraktion, fraktionsloses oder externes Gremium.
    Dies entspricht `opengov:onBehalfOf` in Popolo.
    Es kann auch Mitglieder geben, die von keiner anderen Gruppierung entsendet wurden (z. B. fraktionslose Abgeordnete).
    FRAGE: Muss diese Situation vom Fehlen von Informationen über Entsendungen unterschieden werden?
    Typ: `oparl:Organization`.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`startDate`
:   `schema:validFrom` wie in Popolo. The date on which the relationship began.
    Typ: `xsd:dateTime`.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`endDate`
:   `schema:validThrough` wie in Popolo. The date on which the relationship ended.
    Typ: `xsd:dateTime`.
    Kardinalität: 0 bis 1.
    OPTIONAL.

TODO: Folgende Verweise einbauen oder entfernen:

* https://github.com/OParl/specs/issues/122
* http://www.w3.org/TR/vocab-org/#membership-roles-posts-and-reporting
* http://popoloproject.com/specs/membership.html
