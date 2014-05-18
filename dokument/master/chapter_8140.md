org:Membership oder oparl:Membership {#oparl_membership}
------------------------------------

TODO. Siehe:
https://github.com/OParl/specs/issues/122
https://github.com/OParl/specs/issues/109

### Eigenschaften

`person`
:   Person.
    Typ: `oparl:Person` 
    OPTIONAL
    
`organization`
:   Organization.
    Typ: `oparl:Organization`
    OPTIONAL

`role`
:   Rolle. Das Objekt hat eine `skos:prefLabel`-Eigenschaft,
    deren Wert eine Funktionsbezeichnung ist, z.B.
    "1. pers. Vertreter | 1. pers. Vertreterin" oder "2. pers. Vertreter | 2. pers. Vertreterin".
    Popolo: "The role that the person fulfills in the organization".
    normale Mitglieder haben in der Regel keine eigene Funktion, aber auch eine Unterscheidung zwischen z.B.
    "Sachkundige Bürger | Sachkundige Bürgerin" und "Ratsherr | Ratsfrau" bei einfachen Mitgliedern ist hiermit möglich.
    FRAGE: Wie soll bei einem sachkundigen Bürger verfahren werden, der gleichzeitig Vorsitzender ist?
    Typ: `org:Role`
    OPTIONAL

`post`
:   The post held by the person in the organization
    Typ: `org:Post`
    OPTIONAL

`onBehalfOf`
:   Entsendende Organization - Fraktion, fraktionslos oder externes Gremium
    Dies entspricht `opengov:onBehalfOf` in Popolo.
    Es kann auch Mitglieder geben, die von keiner anderen Organisation entsendet wurden (z.B. fraktionslose Abgeordnete).
    FRAGE: Muss diese Situation vom Fehlen von Informationen über Entsendungen unterschieden werden?
    Typ: `oparl:Organization`
    OPTIONAL

`startDate`
:   `schema:validFrom` wie in Popolo. The date on which the relationship began
    Typ: String im Format `xsd:dateTime` 
    OPTIONAL

`endDate`
:   `schema:validThrough` wie in Popolo. The date on which the relationship ended
    Typ: String im Format `xsd:dateTime`
    OPTIONAL

### Hinweise

http://www.w3.org/TR/vocab-org/#membership-roles-posts-and-reporting

http://popoloproject.com/specs/membership.html
