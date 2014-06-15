oparl:Meeting (Sitzung)  {#oparl_meeting}
-----------------------

Eine Sitzung ist die Versammlung einer oder mehrerer Gruppierungen
(oparl:Organization) zu einem bestimmten Zeitpunkt an einem bestimmten Ort.

Die geladenen Teilnehmer der Sitzung sind jeweils als Objekte vom Typ
oparl:Person in 
entsprechender Form referenziert. Verschiedene Dokumente (Einladung, 
Ergebnis- und Wortprotokoll, sonstige Anlagen) können referenziert werden.

Die Inhalte einer Sitzung werden durch Tagesordnungspunkte (oparl:AgendaItem)
abgebildet.

Ein Beispiel in expandierter Form:

~~~~~  {#meeting_ex1 .json}
{
    "@type": "http://oparl.org/schema/1.0/Meeting",
    "@id": "https://oparl.example.org/meeting/281",
    "name": "4. Sitzung des Finanzausschusses",
    "start": "2013-01-04T08:00:00+01:00",
    "end": "2013-01-04T12:00:00+01:00",
    "location": {
        "description": {
            "@value": "Rathaus, Raum 136",
            "@language": "de"
        },
        "description": {
            "@value": "Town Hall, room 136",
            "@language": "en"
        }
    },
    "organization": "https://oparl.example.org/organization/34",
    "participant": [
        "https://oparl.example.org/person/29",
        "https://oparl.example.org/person/75",
        "https://oparl.example.org/person/94"
    ],
    "invitation": "https://oparl.example.org/document/586",
    "resultsProtocol": "https://oparl.example.org/document/628",
    "verbatimProtocol": "https://oparl.example.org/document/691",
    "auxiliaryDocument": [
        "https://oparl.example.org/document/588",
        "https://oparl.example.org/document/589"
    ],
    "agendaItem": {
        "@list": [
            "https://oparl.example.org/agendaitem/1045",
            "https://oparl.example.org/agendaitem/1046",
            "https://oparl.example.org/agendaitem/1047",
            "https://oparl.example.org/agendaitem/1048"
        ]
    },
    "created": "2012-01-06T12:01:00+01:00",
    "modified": "2012-01-08T14:05:27+01:00"
}
~~~~~

Das selbe Beispiel in kompakter Form:

~~~~~  {#meeting_ex2 .json}
{
    "@context": "https://oparl.example.org/Pfad/zum/Kontext/oparl.jsonld",
    "@type": "oparl:Meeting",
    "@id": "https://oparl.example.org/meeting/281",
    "name": "4. Sitzung des Finanzausschusses",
    "start": "2013-01-04T08:00:00+01:00",
    "end": "2013-01-04T12:00:00+01:00",
    "location": {
        "description": "Rathaus, Raum 136",
            // default-Sprache ist im Kontext als "de" angegeben
            // TODO: doppelter Schlüssel
        "description": {
            "@value": "Town Hall, room 136",
            "@language": "en"
        }
    },
    "organization": "beispielris:organization/34",
    "participant": [
        "beispielris:person/29",
        "beispielris:person/75",
        "beispielris:person/94"
    ],
    "invitation": "beispielris:document/586",
    "resultsProtocol": "beispielris:document/628",
    "verbatimProtocol": "beispielris:document/691",
    "auxiliaryDocument": [
        "beispielris:document/588",
        "beispielris:document/589"
    ],
    "agendaItem": [
    // Reihenfolge ist wichtig, deshalb @list im Kontext angeben
        "beispielris:agendaitem/1045",
        "beispielris:agendaitem/1046",
        "beispielris:agendaitem/1047",
        "beispielris:agendaitem/1048"
    ],
    "created": "2012-01-06T12:01:00+01:00",
    "modified": "2012-01-08T14:05:27+01:00"
}
~~~~~

### Eigenschaften ###

`start`
:   Datum und Uhrzeit des Anfangszeitpunkts der Sitzung. Bei einer zukünftigen 
    Sitzung ist dies der geplante Zeitpunkt, bei einer stattgefundenen
    KANN es der tatsächliche Startzeitpunkt sein.
    TODO: besser zwei Eigenschaften?
    Typ: Datentyp `xsd:dateTime`.
    Kardinalität: 1.
    ZWINGEND.

`end`
:   Endzeitpunkt der Sitzung als Datum/Uhrzeit. Bei einer zukünftigen 
    Sitzung ist dies der geplante Zeitpunkt, bei einer stattgefundenen
    KANN es der tatsächliche Endzeitpunkt sein.
    TODO: besser zwei Eigenschaften?
    Typ: Datentyp `xsd:dateTime`.
    Kardinalität: 0 bis 1.
    FRAGE: Kommen in Sitzungen Unterbrechungen vor, die in RIS festgehalten werden (sollen)?
    EMPFOHLEN.

`location`
:   Sitzungsort.
    Typ: `oparl:Location`.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.

`organization`
:   Gruppierung der die Sitzung zugeordnet ist. Wenn eine Liste angegeben wird, dann ist diese geordnet. Das erste
    Element ist dann das federführende Gremium.
    TODO: Eigenschaft für federführendes Gremium ergänzen und dann Ordnung entfernen
    Diese Eigenschaft ist invers zur Eigenschaft `meeting` der Klasse `oparl:Organization` (In OWL: `oparl:organization owl:inverseOf oparl:meeting .`).
    Typ: `oparl:Organization`.
    Kardinalität: 1 bis *.
    ZWINGEND.

`participant`
:   Teilnehmer der Sitzung.
    Bei einer Sitzung in der Zukunft sind dies die geladenen Teilnehmer, bei einer stattgefundenen Sitzung SOLL die
    Liste nur diejenigen Teilnehmer umfassen, die tatsächlich an der Sitzung teilgenommen haben.
    TODO: besser `attendant` und `ìnvited` ?
    Typ: `oparl:Person`.
    Kardinalität: 0 bis *.
    OPTIONAL.

`invitation`
:   Einladungsdokument zur Sitzung.
    FRAGE: Kann es mehr als ein solches Dokument geben?
    Typ: `oparl:Document`.
    Kardinalität: 0 bis *.
    EMPFOHLEN.

`resultsProtocol`
:   Ergebnisprotokoll zur Sitzung. Diese Eigenschaft kann selbstverständlich erst nach
    dem Stattfinden der Sitzung vorkommen.
    Typ: `oparl:Document`.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.

`verbatimProtocol`
:   Wortprotokoll zur Sitzung. Diese Eigenschaft kann selbstverständlich erst nach
    dem Stattfinden der Sitzung vorkommen.
    Typ: `oparl:Document`.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.
    
`auxiliaryDocument`
:   Dokumentenanhang zur Sitzung.
    Hiermit sind Dokumente gemeint, die üblicherweise mit der Einladung
    zu einer Sitzung verteilt werden, und die nicht bereits über einzelne
    Tagesordnungspunkte referenziert sind.
    Typ: `oparl:Document`.
    Kardinalität: 0 bis *.
    OPTIONAL.

`agendaItem`
:   Tagesordnungspunkte der Sitzung.
    Die Reihenfolge ist relevant.
    Es kann Sitzungen ohne TOPs geben.
    Typ: `oparl:AgendaItem`.
    Kardinalität: 0 bis *.
    OPTIONAL.

`keyword`
:   Schlagwort.
    Typ: `skos:Concept`.
    Kardinalität: 0 bis *.
    OPTIONAL.
    
`created`
:   Datum und Uhrzeit der Erzeugung des Objekts.
    Typ: Datentyp `xsd:dateTime`.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.

`modified`
:   Datum und Uhrzeit der letzten Änderung des Objekts.
    Typ: Datentyp `xsd:dateTime`.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.
