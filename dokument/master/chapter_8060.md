oparl:Person (Person)  {#oparl_person}
--------------------

Jede natürliche Person, die in der parlamentarischen Arbeit tätig ist
und insbesondere Mitglied in einer Gruppierung ([oparl:Organization](#oparl_organization)),
wird mit einem Objekt vom Typ `oparl:Person` abgebildet.

Es gibt existieren bereits eine ganze Reihe von Vokabularen für Personen. Dazu gehören FOAF (Friend of a Friend) und vCard. Es gibt aber auch der XÖV-Standard für natürliche Personen, ein XML Schema. Für `oparl:Person` wurde daraus
und basierend auf dem Input der OParl-Stakeholder eine Auswahl von Eigenschaften zusammengestellt.

Ein Beispiel in expandierter Form:

~~~~~  {#person_ex1 .json}
{
    "@type": "http://oparl.org/schema/1.0/Person",
    "@id": "http://oparl.beispielris.de/person/29",
    "name": "Prof. Dr. Max Mustermann",
    "familyName": "Mustermann",
    "givenName": "Max",
    "title": "Prof. Dr.",
    "gender": "male",
    "email": "mailto:max@mustermann.de",
    "phone": "tel:+493012345678",
    "streetAddress": "Musterstraße 5",
    "postalCode": "11111",
    "locality": "Musterort",
    "organization": [
        "http://oparl.beispielris.de/organization/11",
        "http://oparl.beispielris.de/organization/34"
    ],
    "status": "http://oparl.beispielris.de/status/buergermeister",
    "hasMembership": "http://oparl.beispielris.de/membership/34",
    "created": "2011-11-11T11:11:00+01:00",
    "last_modified": "2012-08-16T14:05:27+02:00"
}
~~~~~

Das selbe Beispiel in kompakter Form. Zunächst der verwendete Kontext:

~~~~~  {#person_ex_context .json}
{
    // Präfixe siehe Abschnitt 8000

    "gender": "vcard:hasGender",
    "givenName": "foaf:firstName",
    "familyName": "foaf:lastName",
    "academic_degree": "foaf:title",
    "email": {
        "@id": "foaf:mbox",
        "@type": "@id"
    },
    "phone": "foaf:phone",
    "address": "vcard:street-address",
    "created": {
        "@id": "dc:created",
        "@type": "xsd:dateTime"
    },
    "last_modified": {
        "@id": "dc:modified",
        "@type": "xsd:dateTime"
    }
}
~~~~~

~~~~~  {#person_ex2 .json}
{
    "@context": "https://oparl.beispielris.de/Pfad/zum/Kontext/oparl.jsonld",
    "@type": "oparl:Person",
    "@id": "http://oparl.beispielris.de/person/29",
    "name": "Prof. Dr. Max Mustermann",
    "familyName": "Mustermann",
    "givenName": "Max",
    "title": "Prof. Dr.",
    "gender": "male",
    "email": "mailto:max@mustermann.de",
    "phone": "tel:+493012345678",
    "streetAddress": "Musterstraße 5",
    "postalCode": "11111",
    "locality": "Musterort",
    "organization": ["11", "34"],
    "status": "beispielris:status/buergermeister",
    "hasMembership": "beispielris:membership/34",
    "created": "2011-11-11T11:11:00+01:00",
    "last_modified": "2012-08-16T14:05:27+02:00"
}
~~~~~
### Eigenschaften ###

`name`
:   Der Vollständige Name der Person, üblicherweise mit Titel und Vorname.
    Diese Eigenschaft ist ZWINGEND.

`familyName`
:   Familienname bzw. Nachname. Diese Eigenschaft ist OPTIONAL.

`givenName`
:   Vorname bzw. Taufname. Diese Eigenschaft ist OPTIONAL.

`title`
:   Akademische(r) Titel. Diese Eigenschaft ist OPTIONAL.

`gender`
:   Geschlecht. Üblicherweise `male` oder `female`. Diese Eigenschaft ist OPTIONAL.

`phone`
:   Telefonnummer mit `tel:` Schema. Diese Eigenschaft ist OPTIONAL.

`email`
:   E-Mail-Adresse mit `mailto:` Schema. Diese Eigenschaft ist OPTIONAL.

`streetAddress`
:   Straße und Hausnummer der Kontakt-Anschrift der Person. Diese Eigenschaft ist OPTIONAL.

`postalCode`
:   Postleitzahl der Kontakt-Anschrift der Person. Diese Eigenschaft ist OPTIONAL.

`locality`
:   Ortsangabe der Kontakt-Anschrift der Person. Diese Eigenschaft ist OPTIONAL.

`organization`
:   URLs der Gruppierung oder Liste der URLs der Gruppierungen (Objekte vom Typ `oparl:Organization`), in der
    bzw. in denen die Person aktuell Mitglied ist.
    Diese Eigenschaft ist ZWINGEND. Sollte die Person Mitglied in keiner Gruppierung sein,
    enthält die Liste keine Einträge.

`status`
:   URLs von Objekten mit skos:prefLabel.
    z.B. "Bürgermeister", "Bezirksbürgermeister", "Stadtverordneter", "Bezirksverordneter",
    "Sachkundige Bürgerin/Bürger", "Einzelstadtverordnete" (Mitglieder des Rates die keiner Fraktion/Organisation
    angehören -> die Zuordbarkeit einer fiktiven Organisation ermöglichen TODO: warum will man das?).
    Denkbar ist aber auch z.B. "Pfarrer"
    TODO: kann ein Pfarrer gleichzeitig Bürgermeister sein?!
    Siehe https://github.com/OParl/specs/issues/45
    OPTIONAL

`hasMembership`
:   URLs der Mitgliedschaft oder Liste von URLs der Mitgliedschaften (Objekte vom Typ `org:Membership`). TODO: Eventuell     Unterklasse von org:Membership definieren.
    OPTIONAL.

`created`
:   Datum/Uhrzeit der Erzeugung des Objekts.
    EMPFOHLEN.

`lastModified`
:   Datum/Uhrzeit der letzten Bearbeitung des Objekts. EMPFOHLEN.
