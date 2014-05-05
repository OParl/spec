org:Membership oder oparl:Membership {#oparl_membership}
------------------------------------

TODO. Siehe:
https://github.com/OParl/specs/issues/122
https://github.com/OParl/specs/issues/109

### Eigenschaften

`person`
:   `oparl:Person` Eine Person.
    OPTIONAL
    
`organization`
:   `oparl:Organization` Eine Organization.
    OPTIONAL

`role`
:   zeigt auf ein Objekt der Klasse `org:Role` oder einer Unterklasse. Das Objekt hat eine `skos:prefLabel`-Eigenschaft,
    deren Wert eine Funktionsbezeichnung ist, z.B.
    "1. pers. Vertreter | 1. pers. Vertreterin" oder "2. pers. Vertreter | 2. pers. Vertreterin".
    Popolo: "The role that the person fulfills in the organization".
    normale Mitglieder haben in der Regel keine eigene Funktion, aber auch eine Unterscheidung zwischen z.B.
    "Sachkundige Bürger | Sachkundige Bürgerin" und "Ratsherr | Ratsfrau" bei einfachen Mitgliedern ist hiermit möglich.
    TODO: was ist mit einem sachkundigen Bürger, der gleichzeitig Vorsitzender ist?
    OPTIONAL

`post`
:   The post held by the person in the organization
    OPTIONAL

`onBehalfOf`
:   Entsendende Organization - Fraktion, fraktionslos oder externes Gremium
    Dies entspricht `opengov:onBehalfOf` in Popolo.
    TODO: wie wird fraktionslos kodiert?
    OPTIONAL

`startDate`
:   `schema:validFrom` wie in Popolo. The date on which the relationship began
    OPTIONAL

`endDate`
:   `schema:validThrough` wie in Popolo. The date on which the relationship ended
    OPTIONAL

### Hinweise

http://www.w3.org/TR/vocab-org/#membership-roles-posts-and-reporting

http://popoloproject.com/specs/membership.html
