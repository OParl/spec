oparl:Person (Person)  {#oparl_person}
--------------------

Jede natürliche Person, die in der parlamentarischen Arbeit tätig ist
und insbesondere Mitglied in einer Gruppierung ([oparl:Organization](#oparl_organization)),
wird mit einem Objekt vom Typ `oparl:Person` abgebildet.

Ein Beispiel in expandierter Form:

~~~~~  {#person_ex1 .json}
{
    "@type": "http://oparl.org/schema/1.0/Person",
    "@id": "http://oparl.beispielris.de/people/29",
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
    "organizations": [
        "http://oparl.beispielris.de/organizations/11",
        "http://oparl.beispielris.de/organizations/34"
    ],
    "created": "2011-11-11T11:11:00+01:00",
    "last_modified": "2012-08-16T14:05:27+02:00",
}
~~~~~

Das selbe Beispiel in kompakter Form. Ein geeigneter Inhalt des angegebenen Kontext wird hierbei vorausgesetzt:

~~~~~  {#person_ex2 .json}
{
    "@context": "https://oparl.beispielris.de/Pfad/zum/Kontext/oparl.jsonld",
    "@type": "oparl:Person",
    "@id": "beispielris:people/29", // kann möglicherweise weiter gekürzt werden
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
    "organizations": ["11", "34"],
    "created": "2011-11-11T11:11:00+01:00",
    "last_modified": "2012-08-16T14:05:27+02:00",
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

`organizations`
:   Liste der URLs der Gruppierungen (Objekte vom Typ `oparl:Organization`), in der die
    Person aktuell Mitglied ist, oder alternativ die URL zum Abruf der Liste.
    Diese Eigenschaft ist ZWINGEND. Sollte die Person Mitglied in keiner Gruppierung sein,
    enthält die Liste keine Einträge.

`created`
:   Datum/Uhrzeit der Erzeugung des Objekts. EMPFOHLEN.

`lastModified`
:   Datum/Uhrzeit der letzten Bearbeitung des Objekts. EMPFOHLEN.
