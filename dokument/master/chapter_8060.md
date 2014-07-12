oparl:Person (Person)  {#oparl_person}
--------------------

Jede natürliche Person, die in der parlamentarischen Arbeit tätig
und insbesondere Mitglied in einer Gruppierung ([oparl:Organization](#oparl_organization)) ist,
wird mit einem Objekt vom Typ `oparl:Person` abgebildet.

**Beispiel**

~~~~~  {#person_ex2 .json}
{
    "id": "https://oparl.example.org/person/29",
    "type": "http://oparl.org/schema/1.0/Person",
    "name": "Prof. Dr. Max Mustermann",
    "familyName": "Mustermann",
    "givenName": "Max",
    "title": [
        "https://oparl.example.org/vocab/person/title/prof",
        "https://oparl.example.org/vocab/person/title/dr"
    ],
    "formOfAddress": "https://oparl.example.org/vocab/foa/ratsmitglied",
    "gender": "https://oparl.example.org/vocab/person/gender/male",
    "email": "mailto:max@mustermann.de",
    "phone": "tel:+493012345678",
    "streetAddress": "Musterstraße 5",
    "postalCode": "11111",
    "locality": "Musterort",
    "status": "https://oparl.example.org/status/buergermeister",
    "membership": [
        "https://oparl.example.org/membership/11",
        "https://oparl.example.org/membership/34"
    ],
    "created": "2011-11-11T11:11:00+01:00",
    "modified": "2012-08-16T14:05:27+02:00"
}
~~~~~

### Eigenschaften ###

`name`
:   Der vollständige Name der Person mit akademischem Grad und dem gebräuchlichen Vornamen,
    wie er zur Anzeige durch den Client genutzt werden kann.
    Typ: String.
    Kardinalität: 1.
    ZWINGEND.

`familyName`
:   Familienname bzw. Nachname.
    Typ: String.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`givenName`
:   Vorname bzw. Taufname.
    Typ: String.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`formOfAddress`
:   Anrede. Diese Eigenschaft funktioniert wie in 
    [Vokabulare zur Klassifizierung](#vokabulare_klassifizierung) beschrieben 
    entweder als URL zu einem `skos:Concept` oder als String.
    Der String bzw. `prefLabel` SOLL sowohl die männliche als auch die weibliche Bezeichnung
    enthalten. Beispiele: "Herr | Frau", "Ratsherr | Ratsfrau".
    Typ: URL eines `skos:Concept` Objekts oder String.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`title`
:   Akademische(r) Titel. Vgl. [Vokabulare zur Klassifizierung](#vokabulare_klassifizierung).
    Typ: URL eines `skos:Concept` Objekts oder String.
    Kardinalität: 0 bis *.
    OPTIONAL.

`gender`
:   Geschlecht. Empfohlene Werte sind `Female`, `Male`, `None` und `Other`.
    Für den Fall, dass das Geschlecht der Person unbekannt ist, SOLL die Eigenschaft nicht
    ausgegeben werden. Vgl. [Vokabulare zur Klassifizierung](#vokabulare_klassifizierung).
    Typ: String oder URL eines `skos:Concept` Objekts.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`phone`
:   Telefonnummer der Person mit `tel:` Schema, ohne Leerzeichen.
    Typ: String
    Kardinalität: 0 bis 1.
    OPTIONAL.

`email`
:   E-Mail-Adresse mit `mailto:` Schema.
    Typ: String im Format `foaf:mbox`.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`streetAddress`
:   Straße und Hausnummer der Kontakt-Anschrift der Person.
    Typ: String.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`postalCode`
:   Postleitzahl der Kontakt-Anschrift der Person.
    Typ: String.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`locality`
:   Ortsangabe der Kontakt-Anschrift der Person.
    Typ: `vcard:locality`
    Kardinalität: 0 bis 1.
    OPTIONAL.

`status`
:   Status. Diese Eigenschaft funktioniert wie in 
    [Vokabulare zur Klassifizierung](#vokabulare_klassifizierung) beschrieben entweder
    als URL zu einem `skos:Concept` oder als String.
    Die Strings bzw. `prefLabel` SOLLEN sowohl die männliche als auch die weibliche
    Form enthalten, und zwar in dem Muster
    "männliche Form | weibliche Form" (genau in der Reihenfolge mit einem Leerzeichen
    vor und nach dem "|").
    Wenn sich beide Formen nicht unterscheiden, dann DARF die Form nur einmal verwendet werden:
    "Ratsmitglied" und nicht "Ratsmitglied | Ratsmitglied".
    Dadurch kann auch solche Software einen sinnvollen Text anzeigen, die keine
    Fall-Unterscheidung nach Geschlecht
    der Personen vornimmt.
    Weitere Beispiele: "Bürgermeister | Bürgermeisterin",
    "Bezirksbürgermeister | Bezirksbürgermeisterin",
    "Stadtverordneter | Stadtverordnete",
    "Bezirksverordneter | Bezirksverordnete",
    "Sachkundiger Bürger | Sachkundige Bürgerin",
    "Einzelstadtverordneter | Einzelstadtverordnete" (Mitglieder des Rates die keiner Fraktion/Organisation
    angehören).
    Vgl. [Vokabulare zur Klassifizierung](#vokabulare_klassifizierung).
    Typ: URL eines `skos:Concept` Objekts oder String.
    Kardinalität: 0 bis *.
    OPTIONAL.

`membership`
:   Mitgliedschaften der Person in Gruppierungen, z. B. Gremien und
    Fraktionen.
    Typ: Liste von `org:Membership` Objekten.
    Kardinalität: 0 bis *.
    OPTIONAL.

`keyword`
:   Schlagworte.
    Typ: Array von Strings oder URLs zu `skos:Concept` Objekten
    (vgl. [Vokabulare zur Klassifizierung](#vokabulare_klassifizierung)).
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
