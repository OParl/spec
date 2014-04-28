oparl:Paper (Drucksache)  {#oparl_paper}
-----------------------

Dieser Objekttyp dient der Abbildung von Drucksachen in der parlamentarischen
Arbeit, wie zum Beispiel Anfragen, Anträgen und Beschlussvorlagen.

Drucksachen werden in Form einer Beratung (oparl:Consultation) im Rahmen
eines Tagesordnungspunkts (oparl:AgendaItem) einer Sitzung (oparl:Meeting)
behandelt.

Drucksachen spielen in der schriftlichen wie mündlichen Kommunikation eine 
besondere Rolle, da in vielen Texten auf bestimmte Drucksachen Bezug genommen 
wird. Hierbei kommen in parlamentarischen Informationssystemen unveränderliche
Kennungen der Drucksachen zum Einsatz.

Ein Beispiel in kompakter Form:

~~~~~  {#paper_ex1 .json}
{
    "@context": "https://oparl.beispielris.de/Pfad/zum/Kontext/oparl.jsonld"
    "@type": "oparl:Paper",
    "@id": "http://oparl.beispielris.de/papers/749",
    "reference": "1234/2014",
    "publishedDate": "2014-04-04T16:42:02+02:00",
    "name": "Antwort auf Anfrage 1200/2014",
    "paperType": "Beantwortung einer Anfrage",
    "relatedPapers": [
        "http://oparl.beispielris.de/papers/699"
    ],
    "mainDocument": "http://oparl.beispielris.de/documents/925",
    "auxiliaryDocuments": [
        "http://oparl.beispielris.de/documents/926"
    ],
    "locations": [
        {
            "description": "Theodor-Heuss-Ring 1",
            "lat": 7.148,
            "lon": 50.023
        }
    ],
    "creators": [
        "beispielris:organizations/2000",
        "beispielris:people/1000"
    ],
    "consultations": [
        {
            "meeting": "beispielris:meeting/3271",
            "agendaitem": "beispielris:agendaitem/3.1.2",
            "role": "Federführende Beratung"
        }
    ],
    "lastModified": "2013-01-08T12:05:27+01:00"
}
~~~~~

TODO:
* Eigenschaften beschreiben
* Eigenschaft "locations" im Beispiel ändern
* Eigenschaft "creators" im Beispiel ändern
* Eigenschaft "consultations" im Beispiel ändern
