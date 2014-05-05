org:Membership oder oparl:Membership {#oparl_membership}
------------------------------------

TODO. Siehe:
https://github.com/OParl/specs/issues/122
https://github.com/OParl/specs/issues/109


### Eigenschaften

`onBehalfOf`
:   Entsendende Organization - Fraktion, fraktionslos oder externes Gremium
    TODO: Hinweis auf `opengov:onBehalfOf`
    TODO: wie wird fraktionslos kodiert?
    OPTIONAL

`startDate`
:   `schema:validFrom` wie in Popolo. The date on which the relationship began
    OPTIONAL

`endDate`
:   `schema:validThrough` wie in Popolo. The date on which the relationship ended
    OPTIONAL

`role`
:   zeigt auf ein Objekt der Klasse `org:Role` oder einer Unterklasse. Das Objekt hat eine `skos:prefLabel`-Eigenschaft,
    deren Wert eine Funktionsbezeichnung ist, z.B.
    "1. pers. Vertreter | 1. pers. Vertreterin" oder "2. pers. Vertreter | 2. pers. Vertreterin".
    normale Mitglieder haben keine eigene Funktion.
    Popolo: "The role that the person fulfills in the organization"
    OPTIONAL

`
### Hinweise

http://www.w3.org/TR/vocab-org/#membership-roles-posts-and-reporting
http://popoloproject.com/specs/membership.html
