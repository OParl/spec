oparl:Person (Person)  {#oparl_person}
--------------------

Jede natürliche Person, die Mitglied eines Gremiums ist, ist als `oparl:Person` im 
Datenmodell eindeutig identifizierbar.

### Eigenschaften ###

Schlüssel (`id`)
:   Zur eindeutigen Identifizierung sollte jede Person eine Kennung besitzen, 
    die keinen Änderungen unterworfen ist und aus diesem Grund nicht mit dem 
    Namen in Verbindung stehen sollte. Viele RIS nutzen rein numerische 
    Kennungen.
Vorname (`first_name`)
:   Der Vorname der Person.
Nachname (`last_name`)
:   Der Nachname der Person.
Titel (`academic_degree`)
:   _Optional_. Akademische Titel wie "Dr." und "Prof. Dr.". Aber auch akademische Grade wie "Dipl. Inform." (die rechtlich nicht Teil des Namens sind) sind hier zugelassen.
Geschlecht (`sex`)
:   _Optional_. Weiblich (Wert `F` für _female_), männlich (Wert `M`
    für _male_), anderes (Wert `O` für _others_)
Beruf (`profession`)
:   _Optional_. Z.B. "Rechtsanwalt"
E-Mail-Adresse (`email`)
:   _Optional_.
Telefon (`phone`)
:   _Optional_.
Fax (`fax`)
:   _Optional_.
Anschrift (`address`)
:   _Optional_. Straße und Hausnummer, Postleitzahl und Ort
Zuletzt geändert (`last_modified`)
:   Datum und Uhrzeit der letzten Änderung


#### Anmerkungen ####

* Das System von Euskirchen scheint Vor- und Nachname (evtl. einschl. Titel) 
in einem gemeinsamen Feld "Name" zu führen. Ob das System hier technisch 
differenziert, ist unklar. Falls einzelne Systeme den angezeigten Namen nur 
als ganzes speichern, sollte dies für den Standard übernommen werden, da es 
für die meisten Anwendungen ausreichen sollte.
* Das System PROVOX unterscheidet zwischen privaten und geschäftlichen 
Anschriften.


### Beziehungen ###

* Objekte vom Typ `oparl:Person` können einer Organisation, z.B. einer Fraktion, 
zugeornet werden. Diese Beziehung ist datiert.
* Objekte vom Typ `oparl:Person` können einem oder mehreren Gremien zugewiesen 
werden, um die Mitgliedschaft in diesem Gremium darzustellen. Diese 
Beziehungen sind ebenfalls datiert.

### Beispiel ###

~~~~~  {#person_ex1 .json}
{
    "id": "1000",
    "first_name": "Max",
    "last_name": "Mustermann",
    "academic_degree": "Dr. oec. troph",
    "sex": "M",
    "profession": "Rechtsanwalt",
    "email": "max@mustermann.de",
    "phone": "+4977777",
    "fax": "+4988888",
    "address": "Musterstraße 5, 11111 Musterort",
    "last_modified": "2012-08-16T14:05:27+02:00",
    "organisations": [
        {
            "id": "2000",
            "start": "2011-03-01",
            "end": "2013-02-28"
        },
        {
            "id": "2001",
            "start": "2013-03-01"
        }
    ],
    "committees": [
        {
            "id": "7",
            "start": "2013-01-01"
        }
    ]
}
~~~~~

