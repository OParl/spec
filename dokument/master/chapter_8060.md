oparl:Person (Person)  {#oparl_person}
--------------------

Jede natürliche Person, die in der parlamentarischen Arbeit tätig ist
und insbesondere Mitglied in einer Gruppierung ([oparl:Organization](#oparl_organization)),
wird mit einem Objekt vom Typ `oparl:Person` abgebildet.

Es gibt existieren bereits eine ganze Reihe von Vokabularen für Personen. Dazu gehören FOAF (Friend of a Friend) und vCard. Es gibt aber auch der XÖV-Standard für natürliche Personen, ein XML Schema. Für `oparl:Person` wurde daraus
und basierend auf dem Input der OParl-Stakeholder eine Auswahl von Eigenschaften zusammengestellt.

TODO: für Personen-Namen und Titel wird keine Mehrsprachigkeit benötigt. Dies im Kontext berücksichtigen. Dies spricht auch für je einen Kontext pro Klasse.

Ein Beispiel in expandierter Form:

~~~~~  {#person_ex1 .json}
{
    "@type": "http://oparl.org/schema/1.0/Person",
    "@id": "http://oparl.beispielris.de/person/29",
    "name": "Prof. Dr. Max Mustermann",
    "familyName": { // könnte mehrsprachig sein, z.B. griechisch, russisch, tamilisch 
        "@value": "Mustermann",
        "@language": "de"
    }
    "givenName": { // könnte mehrsprachig sein
        "@value": "Max",
        "@language": "de"
    }
    "title": "Prof. Dr.", // TODO: nicht mehrsprachig?!
    "formOfAddress": "http://oparl.beispielris.de/formofaddress/ratsmitglied",
    "gender": "http://www.w3.org/2006/vcard/ns#Male",
    "email": "mailto:max@mustermann.de",
    "phone": "tel:+493012345678",
    "streetAddress": "Musterstraße 5", // nicht mehrsprachig
    "postalCode": "11111",
    "locality": {
        "de": "Musterort",
        "en": Sample Town"
    }
    "organization": [
        "http://oparl.beispielris.de/organization/11",
        "http://oparl.beispielris.de/organization/34"
    ],
    "status": "http://oparl.beispielris.de/status/buergermeister",
    "hasMembership": "http://oparl.beispielris.de/membership/34",
    "created": "2011-11-11T11:11:00+01:00",
    "lastModified": "2012-08-16T14:05:27+02:00"
}
~~~~~

Das selbe Beispiel in kompakter Form. Zunächst der verwendete Kontext:

~~~~~  {#person_ex_context .json}
{
    "@language": "de",
    
    // Präfixe siehe Abschnitt 8000

    "gender": "vcard:hasGender",
    "givenName": "foaf:firstName",
    "familyName": "foaf:lastName",
    "academic_degree": {
        "@language": null , // keine Vorgabesprache da nicht mehrsprachig
        "@id": "foaf:title"
    }
    "email": {
        "@id": "foaf:mbox",
        "@type": "@id"
    },
    "phone": "foaf:phone",
    "streetAddress": "vcard:street-address",
    "locality": {
        "@id": "vcard:locality",
        "@container": "@language" // für eine "language map"
    }
    "created": {
        "@id": "dc:created",
        "@type": "xsd:dateTime"
    },
    "lastModified": {
        "@id": "dc:modified",
        "@type": "xsd:dateTime"
    }
}
~~~~~

~~~~~  {#person_ex2 .json}
{
    "@context": "https://oparl.beispielris.de/Pfad/zum/Kontext/person.jsonld",
    "@type": "oparl:Person",
    "@id": "http://oparl.beispielris.de/person/29",
    "name": "Prof. Dr. Max Mustermann",
    "familyName": "Mustermann", // Kontext gibt deutsche Spache vor
    "givenName": "Max",
    "title": "Prof. Dr.",
    "formOfAddress": "beispielris:formofaddress/ratsmitglied",
    "gender": "vcard:Male",
    "email": "mailto:max@mustermann.de",
    "phone": "tel:+493012345678",
    "streetAddress": "Musterstraße 5",
    "postalCode": "11111",
    "locality": "Musterort",
    "locality": {
        "en": "Sample Town" // TODO prüfen, ob Eigenschaft doppelt erscheinen darf
    }
    "organization": ["11", "34"],
    "status": "beispielris:status/buergermeister",
    "hasMembership": "beispielris:membership/34",
    "created": "2011-11-11T11:11:00+01:00",
    "last_modified": "2012-08-16T14:05:27+02:00"
}
~~~~~
### Eigenschaften ###

`name`
:   Der vollständige Name der Person mit akademischem Grad und Vornamen.
    ZWINGEND

`familyName`
:   Familienname bzw. Nachname.
    OPTIONAL

`givenName`
:   Vorname bzw. Taufname.
    OPTIONAL

`formOfAddress`
:   Anrede
    URLs von Objekten mit skos:prefLabel. Ähnlich wie `status`. Beispiele für die `skos:prefLabel` sind
    "Ratsherr | Ratsfrau" und "Herr | Frau".
    OPTIONAL

`title`
:   Akademische(r) Titel.
    TODO: "Dr."? "Diplom"?
    OPTIONAL

`gender`
:   Geschlecht. Zulässige Werte sind `vcard:Female`, `vcard:Male`, `vcard:None`, `vcard:Other` und `vcard:Unknown`.
    OPTIONAL

`phone`
:   Telefonnummer mit `tel:` Schema.
    OPTIONAL

`email`
:   E-Mail-Adresse mit `mailto:` Schema.
    OPTIONAL

`streetAddress`
:   Straße und Hausnummer der Kontakt-Anschrift der Person.
    OPTIONAL

`postalCode`
:   Postleitzahl der Kontakt-Anschrift der Person.
    OPTIONAL

`locality`
:   Ortsangabe der Kontakt-Anschrift der Person.
    OPTIONAL

`organization`
:   URLs der Gruppierung oder Liste der URLs der Gruppierungen (Objekte vom Typ `oparl:Organization`), in der
    bzw. in denen die Person aktuell Mitglied ist.
    Sollte die Person Mitglied in keiner Gruppierung sein,
    enthält die Liste keine Einträge.
    ZWINGEND
    
`status`
:   URLs von Objekten mit skos:prefLabel.
    Die Zeichenketten SOLLEN sowohl die männliche als auch die weibliche Form enthalten, und zwar in dem Muster
    "männliche Form | weibliche Form" (genau in der Reihenfolge mit einem Leerzeichen vor und nach dem "|")
    Wenn sich beide Formen nicht unterscheiden, dann DARF die Form nur einmal verwendet werden:
    "Mitglied" und nicht "Mitglied | Mitglied".
    Dadurch kann auch solche Software einen sinnvollen Text anzeigen, die keine Fall-Unterscheidung nach Geschecht
    der Personen vornimmt.
    z.B. "Bürgermeister | Bürgermeisterin",
    "Bezirksbürgermeister | Bezirksbürgermeisterin",
    "Stadtverordneter | Stadtverordnete",
    "Bezirksverordneter | Bezirksverordnete",
    "Sachkundiger Bürger | Sachkundige Bürgerin",
    "Einzelstadtverordneter | Einzelstadtverordnete" (Mitglieder des Rates die keiner Fraktion/Organisation
    angehören -> die Zuordbarkeit einer fiktiven Organisation ermöglichen TODO: warum will man das?).
    Siehe https://github.com/OParl/specs/issues/45
    OPTIONAL

`hasMembership`
:   URLs der Mitgliedschaft oder Liste von URLs der Mitgliedschaften (Objekte vom Typ `org:Membership`). TODO: Eventuell     Unterklasse von org:Membership definieren.
    OPTIONAL.

`classification`
:   `skos:Concept`
    OPTIONAL

`created`
:   Datum/Uhrzeit der Erzeugung des Objekts.
    EMPFOHLEN.

`lastModified`
:   Datum/Uhrzeit der letzten Bearbeitung des Objekts.
    EMPFOHLEN.
