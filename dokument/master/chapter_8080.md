oparl:Meeting (Sitzung)  {#oparl_meeting}
----------------------

Eine Sitzung ist die Versammlung der Mitglieder eines Gremiums oder mehrerer
Gremien zu einem bestimmten Zeitpunkt an einem bestimmten Ort.

Die geladenen Teilnehmer der Sitzung sind jeweils als „Person“ in 
entsprechender Form referenziert. Verschiedene Dokumente (Einladung, 
Ergebnis- und Wortprotokoll, sonstige Anlagen) können referenziert werden.

### Eigenschaften ###

Schlüssel (`id`)
:   Zur eindeutigen Identifizierung der Sitzung innerhalb des Systems. In der 
    Praxis wird ein solcher Schlüssel entweder durch eine numerische ID gebildet 
    oder durch Kombination mehrerer Merkmale wie dem Kürzel des Gremiums, der 
    laufenden Nummer der Sitzung in einem Jahr und der Jahreszahl
    (z.B. "BV1/0034/2012").
Nummer (`sequence_number`)
:   _Optional_. Laufende Nummer der Sitzung, üblicherweise innerhalb der 
    Wahlperiode mit 1 beginnend. In der Praxis wird dadurch z.B. die "2. 
    Sitzung des Rats" gekennzeichnet. Ist dieses Feld gesetzt, MUSS ein
    numerischer Wert enthalten sein.
Anfang (`start`)
:   Datum und ggf. Uhrzeit des Anfangszeitpunkts der Sitzung
Ende (`end`)
:   _Optional_. Datum und Uhrzeit vom Ende der Sitzung
Ort (`address`)
:   _Optional_. Textliche Information zum Ort der Sitzung, z.B. "Rathaus, Raum 136".
Zuletzt geändert (`last_modified`)
:   Datum und Uhrzeit der letzten Änderung


### Beziehungen ###

* Sitzungen sind mindestens einem Gremium zugeordnet
* Einer Sitzung sind Personen zugeordnet, um die Teilnahme an der Sitzung 
auszudrücken.
* Dokumente können vom Typ `oparl:Meeting` _optional_ zu mehreren Zwecken 
referenziert werden:
    * Zum Verweis auf die Einladung zur Sitzung
    * Zum Verweis auf das Ergebnisprotokoll zur Sitzung
    * Zum Verweis auf das Wortprotokoll zur Sitzung
* Weiterhin können Sitzungen beliebige weitere Dokumente, die keine 
eigenständigen Drucksachen sind, referenzieren. Dabei handelt es sich dann 
um nicht weiter spezifizierte Anlagen.

### Beispiel ###

~~~~~  {#meeting_ex1 .json}
{
    "id": "3271",
    "identifier": "STA/0034/2012",
    "start": "2013-01-04T08:00:00+01:00",
    "end": "2013-01-04T12:00:00+01:00",
    "address": "Rathaus, Raum 136",
    "sequence_number": 1,
    "committees": ["STA"],
    "people": ["1000", "1001"],
    "invitation": "0001/2013",
    "result_minutes": "0002/2013",
    "verbatim_minutes": "0003/2013",
    "attachments": [
        "0004/2013",
        "0005/2013"
    ],
    "last_modified": "2012-01-08T14:05:27+01:00"
}
~~~~~


