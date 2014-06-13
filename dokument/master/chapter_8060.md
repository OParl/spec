oparl:Person (Person)  {#oparl_person}
--------------------

Jede natürliche Person, die in der parlamentarischen Arbeit tätig
und insbesondere Mitglied in einer Gruppierung ([oparl:Organization](#oparl_organization)) ist,
wird mit einem Objekt vom Typ `oparl:Person` abgebildet.

Es existieren bereits eine ganze Reihe von Vokabularen für Personenobjekte
außerhalb von OParl. Dazu gehören FOAF (_Friend of a Friend_) und vCard. Darüber
hinaus hält der XÖV-Standard ein XML-Schema für natürliche Personen bereit.
Für `oparl:Person` wurde daraus, und basierend auf dem Input der OParl-Stakeholder,
eine Auswahl von Eigenschaften zusammengestellt.

TODO: für Personennamen wird keine Mehrsprachigkeit benötigt. Dies im
Kontext berücksichtigen. Dies spricht auch für je einen Kontext pro Klasse.

Ein Beispiel in expandierter Form:

~~~~~  {#person_ex1 .json}
{
    "@type": "http://oparl.org/schema/1.0/Person",
    "@id": "https://oparl.example.org/person/29",
    "name": "Prof. Dr. Max Mustermann",
    "familyName": { 
        "@value": "Mustermann",
        "@language": "de"
    },
    "givenName": {
        "@value": "Max",
        "@language": "de"
    },
    "title": [
        "https://oparl.example.org/vocab/prof",
        "https://oparl.example.org/vocab/dr"
    ],
    "formOfAddress": "https://oparl.example.org/formofaddress/ratsmitglied",
    "gender": "http://www.w3.org/2006/vcard/ns#Male",
    "email": "mailto:max@mustermann.de",
    "phone": "tel:+493012345678",
    "streetAddress": "Musterstraße 5",
    "postalCode": "11111",
    "locality": {
        "de": "Musterort",
        "en": "Sample Town"
    },
    "status": "https://oparl.example.org/status/buergermeister",
    "hasMembership": [
        "https://oparl.example.org/membership/11",
        "https://oparl.example.org/membership/34"
    ],
    "created": "2011-11-11T11:11:00+01:00",
    "modified": "2012-08-16T14:05:27+02:00"
}
~~~~~

Das selbe Beispiel in kompakter Form. Zunächst der verwendete Kontext:

~~~~~  {#person_ex_context .json}
{
    "@language": "de",
    "gender": "vcard:hasGender",
    "givenName": "foaf:firstName",
    "familyName": "foaf:familyName",
    "title": {
        "TODO": "Hier context für title einfügen."
    },
    "email": {
        "@id": "foaf:mbox",
        "@type": "@id"
    },
    "phone": "foaf:phone",
    "streetAddress": "vcard:street-address",
    "locality": {
        "@id": "vcard:locality",
        "@container": "@language"
    },
    "created": {
        "@id": "dc:created",
        "@type": "xsd:dateTime"
    },
    "modified": {
        "@id": "dc:modified",
        "@type": "xsd:dateTime"
    }
}
~~~~~

~~~~~  {#person_ex2 .json}
{
    "@context": "https://oparl.example.org/Pfad/zum/Kontext/person.jsonld",
    "@type": "oparl:Person",
    "@id": "https://oparl.example.org/person/29",
    "name": "Prof. Dr. Max Mustermann",
    "familyName": "Mustermann",
    "givenName": "Max",
    "title": [
        "besipielris:vocab/prof",
        "besipielris:vocab/dr"
    ],
    "formOfAddress": "beispielris:formofaddress/ratsmitglied",
    "gender": "vcard:Male",
    "email": "mailto:max@mustermann.de",
    "phone": "tel:+493012345678",
    "streetAddress": "Musterstraße 5",
    "postalCode": "11111",
    "locality": {
        "de": "Musterort",
        "en": "Sample Town"
    },
    "status": "beispielris:status/buergermeister",
    "hasMembership": [
        "https://oparl.example.org/membership/11",
        "https://oparl.example.org/membership/34"
    ],
    "created": "2011-11-11T11:11:00+01:00",
    "modified": "2012-08-16T14:05:27+02:00"
}
~~~~~

Und das selbe Beispiel ohne Mehrsprachigkeit für den Ort. Der Kontext bleibt wie zuvor.

~~~~~  {#person_ex3 .json}
{
    ...
    "locality": "Musterort",
    ...
}
~~~~~

### Eigenschaften ###

`name`
:   Der vollständige Name der Person mit akademischem Grad und dem gebräuchlichen Vornamen.
    Typ: Zeichenkette.
    Kardinalität: 1.
    Die Eigenschaft ist ZWINGEND.

`familyName`
:   Familienname bzw. Nachname.
    Typ: Zeichenkette.
    OPTIONAL.

`givenName`
:   Vorname bzw. Taufname.
    Typ: Zeichenkette.
    OPTIONAL.

`formOfAddress`
:   Anrede
    Begriff mit `skos:prefLabel`. Ähnlich wie `status`. Beispiele für die `skos:prefLabel` sind
    "Ratsherr | Ratsfrau" und "Herr | Frau".
    Vgl. [Vokabulare zur Klassifizierung](#vokabulare_klassifizierung).
    Typ: `skos:Concept`.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`title`
:   Akademische(r) Titel. Vgl. [Vokabulare zur Klassifizierung](#vokabulare_klassifizierung).
    Typ: `skos:Concept`.
    Kardinalität: 0 bis *.
    OPTIONAL.

`gender`
:   Geschlecht. Zulässige Werte sind `vcard:Female`, `vcard:Male`, `vcard:None`, `vcard:Other` und `vcard:Unknown`.
    Typ: Zeichenkette (TODO: Entsprechende `vcard:`-Eigenschaft angeben).
    Kardinalität: 0 bis 1.
    OPTIONAL.

`phone`
:   Telefonnummer mit `tel:` Schema.
    Typ: Zeichenkette mit "tel:" am Anfang, keine Leerzeichen.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`email`
:   E-Mail-Adresse mit `mailto:` Schema.
    Typ: `foaf:mbox`.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`streetAddress`
:   Straße und Hausnummer der Kontakt-Anschrift der Person.
    Typ: Zeichenkette.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`postalCode`
:   Postleitzahl der Kontakt-Anschrift der Person.
    Typ: Zeichenkette.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`locality`
:   Ortsangabe der Kontakt-Anschrift der Person.
    Typ: `vcard:locality`
    Kardinalität: 0 bis 1.
    OPTIONAL.

`status`
:   Status. Begriff mit `skos:prefLabel`.
    Die Zeichenketten SOLLEN sowohl die männliche als auch die weibliche Form enthalten, und zwar in dem Muster
    "männliche Form | weibliche Form" (genau in der Reihenfolge mit einem Leerzeichen vor und nach dem "|").
    Wenn sich beide Formen nicht unterscheiden, dann DARF die Form nur einmal verwendet werden:
    "Ratsmitglied" und nicht "Ratsmitglied | Ratsmitglied".
    Dadurch kann auch solche Software einen sinnvollen Text anzeigen, die keine Fall-Unterscheidung nach Geschlecht
    der Personen vornimmt.
    Weitere Beispiele: "Bürgermeister | Bürgermeisterin",
    "Bezirksbürgermeister | Bezirksbürgermeisterin",
    "Stadtverordneter | Stadtverordnete",
    "Bezirksverordneter | Bezirksverordnete",
    "Sachkundiger Bürger | Sachkundige Bürgerin",
    "Einzelstadtverordneter | Einzelstadtverordnete" (Mitglieder des Rates die keiner Fraktion/Organisation
    angehören).
    Vgl. [Vokabulare zur Klassifizierung](#vokabulare_klassifizierung).
    Typ: `skos:Concept`.
    Kardinalität: 0 bis *.
    OPTIONAL.

`hasMembership`
:   Mitgliedschaft(en) der Person in Gruppierungen (oparl:Organization), z. B. Gremien und
    Fraktionen.
    Typ: `org:Membership`.
    Kardinalität: 0 bis *.
    OPTIONAL.

`keyword`
:   Typ: `skos:Concept`.
    Kardinalität: 0 bis *.
    OPTIONAL.

`created`
:   Datum/Uhrzeit der Erzeugung des Objekts.
    Typ: `xsd:dateTime`
    Kardinalität: 0 bis 1.
    EMPFOHLEN.

`modified`
:   Datum/Uhrzeit der letzten Bearbeitung des Objekts.
    Typ: `xsd:dateTime`.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.
