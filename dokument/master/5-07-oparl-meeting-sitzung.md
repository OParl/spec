oparl:Meeting (Sitzung)  {#oparl_meeting}
-----------------------

Eine Sitzung ist die Versammlung einer oder mehrerer Gruppierungen
(oparl:Organization) zu einem bestimmten Zeitpunkt an einem bestimmten Ort.

Die geladenen Teilnehmer der Sitzung sind jeweils als Objekte vom Typ
oparl:Person in entsprechender Form referenziert. Verschiedene Dateien (Einladung, 
Ergebnis- und Wortprotokoll, sonstige Anlagen) können referenziert werden.

Die Inhalte einer Sitzung werden durch Tagesordnungspunkte (oparl:AgendaItem)
abgebildet.

**Beispiel**

~~~~~  {#meeting_ex2 .json}
{
    "id": "https://oparl.example.org/meeting/281",
    "type": "http://oparl.org/schema/1.0/Meeting",
    "name": "4. Sitzung des Finanzausschusses",
    "start": "2013-01-04T08:00:00+01:00",
    "end": "2013-01-04T12:00:00+01:00",
    "streetAddress": "Musterstraße 5, Raum 136",
    "postalCode": "11111",
    "locality": "Musterort",
    "organization": [
        "https://oparl.example.org/organization/34"
    ],
    "invitation": [
        "https://oparl.example.org/files/586"
    ],
    "resultsProtocol": "https://oparl.example.org/files/628",
    "verbatimProtocol": "https://oparl.example.org/files/691",
    "auxiliaryFile": [
        "https://oparl.example.org/files/588",
        "https://oparl.example.org/files/589"
    ],
    "agendaItem": [
        "https://oparl.example.org/agendaitem/1045",
        "https://oparl.example.org/agendaitem/1046",
        "https://oparl.example.org/agendaitem/1047",
        "https://oparl.example.org/agendaitem/1048"
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
    Typ: Datentyp `xsd:dateTime`.
    Kardinalität: 1.
    ZWINGEND.

`end`
:   Endzeitpunkt der Sitzung als Datum/Uhrzeit. Bei einer zukünftigen 
    Sitzung ist dies der geplante Zeitpunkt, bei einer stattgefundenen
    KANN es der tatsächliche Endzeitpunkt sein.
    Typ: Datentyp `xsd:dateTime`.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.

`streetAddress`
:   Straße und Hausnummer des Sitzungsortes.
    Typ: String.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`postalCode`
:   Postleitzahl des Sitzungsortes.
    Typ: String.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`locality`
:   Ortsangabe des Sitzungsortes.
    Typ: `vcard:locality`
    Kardinalität: 0 bis 1.
    OPTIONAL.

`location`
 :   Sitzungsort in Form von Geodaten.
     Typ: URL eines `oparl:Location` Objekts.
     Kardinalität: 0 bis 1.
     OPTIONAL.
 
`organization`
:   Gruppierungen, denen die Sitzung zugeordnet ist. Im Regelfall wird hier eine
    Gruppierung verknüpft sein, es kann jedoch auch gemeinsame Sitzungen mehrerer
    Gruppierungen geben. Das erste Element ist dann das federführende Gremium.
    TODO: Eigenschaft für federführendes Gremium ergänzen und dann Ordnung entfernen.
    invers zur Eigenschaft `meeting` der Klasse `oparl:Organization`.
    Typ: `oparl:Organization`.
    Kardinalität: 1 bis *.
    ZWINGEND.

`chairPerson`
:   Vorsitz der Sitzung
    Typ: `oparl:Person`.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.

`scribe`
:   Schriftführer, Protokollant. 
    Typ: `oparl:Person`.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.

`participant`
:   Teilnehmer der Sitzung.
    Bei einer Sitzung in der Zukunft sind dies die geladenen Teilnehmer, bei 
    einer stattgefundenen Sitzung SOLL die Liste nur diejenigen Teilnehmer umfassen,
    die tatsächlich an der Sitzung teilgenommen haben.
    Typ: Liste von Objekten des Typs `oparl:Person`. Vgl. [Objektlisten](#objektlisten).
    Kardinalität: 0 bis *.
    DEPRECATED.

`invitation`
:   Einladungsdokument zur Sitzung.
    Typ: Liste von Objekten des Typs `oparl:File`. Vgl. [Objektlisten](#objektlisten).
    Kardinalität: 0 bis *.
    EMPFOHLEN.

`resultsProtocol`
:   Ergebnisprotokoll zur Sitzung. Diese Eigenschaft kann selbstverständlich erst nach
    dem Stattfinden der Sitzung vorkommen.
    Typ: URL eines Objekts vom Typ `oparl:File`.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.

`verbatimProtocol`
:   Wortprotokoll zur Sitzung. Diese Eigenschaft kann selbstverständlich erst nach
    dem Stattfinden der Sitzung vorkommen.
    Typ: URL eines Objekts vom Typ `oparl:File`.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.
    
`auxiliaryFile`
:   Dateianhang zur Sitzung.
    Hiermit sind Dateien gemeint, die üblicherweise mit der Einladung
    zu einer Sitzung verteilt werden, und die nicht bereits über einzelne
    Tagesordnungspunkte referenziert sind.
    Typ: Liste von Objekten des Typs `oparl:File`. Vgl. [Objektlisten](#objektlisten).
    Kardinalität: 0 bis *.
    OPTIONAL.

`agendaItem`
:   Tagesordnungspunkte der Sitzung.
    Die Reihenfolge ist relevant.
    Es kann Sitzungen ohne TOPs geben.
    Typ: Liste von Objekten des Typs `oparl:AgendaItem`. Vgl. [Objektlisten](#objektlisten).
    Kardinalität: 0 bis *.
    OPTIONAL.

`keyword`
:   Schlagworte.
    Typ: Array von Strings oder URLs zu `skos:Concept` Objekten
    (vgl. [Vokabulare zur Klassifizierung](#vokabulare_klassifizierung)).
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
