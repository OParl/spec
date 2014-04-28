oparl:Meeting (Sitzung)  {#oparl_meeting}
----------------------

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
    "@id": "http://oparl.beispielris.de/meetings/281",
    "name": "4. Sitzung des Finanzausschusses",
    "start": "2013-01-04T08:00:00+01:00",
    "end": "2013-01-04T12:00:00+01:00",
    "location": {
        "description": "Rathaus, Raum 136"
    },
    "organizations": [
        "http://oparl.beispielris.de/organizations/34"
    ],
    "participants": [
        "http://oparl.beispielris.de/people/29",
        "http://oparl.beispielris.de/people/75"
        "http://oparl.beispielris.de/people/94"
    ],
    "invitation": "http://oparl.beispielris.de/documents/586",
    "resultsProtocol": "http://oparl.beispielris.de/documents/628",
    "verbatimProtocol": "http://oparl.beispielris.de/documents/691",
    "attachments": [
        "http://oparl.beispielris.de/documents/588",
        "http://oparl.beispielris.de/documents/589"
    ],
    "agendaItems": [
        "http://oparl.beispielris.de/agendaitems/1045",
        "http://oparl.beispielris.de/agendaitems/1046",
        "http://oparl.beispielris.de/agendaitems/1047",
        "http://oparl.beispielris.de/agendaitems/1048"
    ],
    "created": "2012-01-06T12:01:00+01:00",
    "lastModified": "2012-01-08T14:05:27+01:00"
}
~~~~~

Das selbe Beispiel in kompakter Form:

~~~~~  {#meeting_ex2 .json}
{
    "@context": "https://oparl.beispielris.de/Pfad/zum/Kontext/oparl.jsonld"
    "@type": "oparl:Meeting",
    "@id": "http://oparl.beispielris.de/meetings/281",
    "name": "4. Sitzung des Finanzausschusses",
    "start": "2013-01-04T08:00:00+01:00",
    "end": "2013-01-04T12:00:00+01:00",
    "location": {
        "description": "Rathaus, Raum 136"
    },
    "organizations": [
        "beispielris:organizations/34"
    ],
    "participants": [
        "beispielris:people/29",
        "beispielris:people/75",
        "beispielris:people/94"
    ],
    "invitation": "beispielris:documents/586",
    "resultsProtocol": "beispielris:documents/628",
    "verbatimProtocol": "beispielris:documents/691",
    "attachments": [
        "beispielris:documents/588",
        "beispielris:documents/589"
    ],
    "agendaItems": [
        "beispielris:agendaitems/1045",
        "beispielris:agendaitems/1046",
        "beispielris:agendaitems/1047",
        "beispielris:agendaitems/1048"
    ],
    "created": "2012-01-06T12:01:00+01:00",
    "lastModified": "2012-01-08T14:05:27+01:00"
}
~~~~~

### Eigenschaften ###

`start`
:   Datum und Uhrzeit des Anfangszeitpunkts der Sitzung. Bei einer zukünftigen 
    Sitzung ist dies der geplante Zeitpunkt, bei einer stattgefundenen
    KANN es der tatsächliche Startzeitpunkt sein.
    Diese Eigenschaft ist ZWINGEND.

`end`
:   Endzeitpunkt der Sitzung als Datum/Uhrzeit. Bei einer zukünftigen 
    Sitzung ist dies der geplante Zeitpunkt, bei einer stattgefundenen
    KANN es der tatsächliche Endzeitpunkt sein.
    Diese Eigenschaft ist EMPFOHLEN.

`location`
:   Sitzungsort in Form eines `oparl:Location` Objekts.
    Diese Eigenschaft ist EMPFOHLEN.

`organizations`
:   IRI der Gruppierung oder Liste der IRIs der Gruppierungen (oparl:Organization), denen die
    Sitzung zugeordnet ist.
    Diese Eigenschaft ist ZWINGEND. Die Liste MUSS mindestens eine
    Gruppierung umfassen.

`participants`
:   IRI der Gruppierung oder Liste der IRLs der geladenen Teilnehmer (oparl:Person) der Sitzung.
    Bei einer stattgefundenen Sitzung SOLL die Liste nur diejenigen Teilnehmer umfassen, die tatsächlich
    an der Sitzung teilgenommen haben. Die Eigenschaft ist ZWINGEND.

`invitation`
:   URL des Einladungsdokuments (oparl:Document) zur Sitzung. Diese
    Eigenschaft ist EMPFOHLEN.

`resultsProtocol`
:   URL des Ergebnisprotokolls (oparl:Document) zur Sitzung. Diese
    Eigenschaft ist EMPFOHLEN. Sie kann selbstverständlich erst nach
    dem Stattfinden der Sitzung vorkommen.

`verbatimProtocol`
:   URL des Wortprotokolls (oparl:Document) zur Sitzung. Diese
    Eigenschaft ist EMPFOHLEN. Sie kann selbstverständlich erst nach
    dem Stattfinden der Sitzung vorkommen.

`attachments`
:   Liste von URLs zu Dokumentenanhängen (oparl:Document) zur Sitzung,
    oder alternativ die URL zum Abruf einer solchen Liste.
    Die Eigenschaft ist OPTIONAL.
    Hiermit sind Dokumente gemeint, die üblicherweise mit der Einladung
    zu einer Sitzung verteilt werden und die nicht bereits über einzelne
    Tagesordnungspunkte referenziert sind.

`agendaItems`
:   Liste der URLs aller Tagesordnungspunkte (oparl:AgendaItem) der Sitzung,
    oder alternativ die URL zum Abfruf dieser Liste.

`created`
:   Datum und Uhrzeit der Erzeugung des Objekts.
    Diese Eigenschaft ist EMPFOHLEN.

`lastModified`
:   Datum und Uhrzeit der letzten Änderung des Objekts.
    Diese Eigenschaft ist EMPFOHLEN.
