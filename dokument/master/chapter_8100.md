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


Zunächst ein Kontext:

~~~~~  {#paper_context_ex .json}
// consultations als @list deklarieren!
~~~~~

Ein Beispiel in kompakter Form:

~~~~~  {#paper_ex1 .json}
{
    "@context": "https://oparl.beispielris.de/Pfad/zum/Kontext/oparl.jsonld"
    "@type": "oparl:Paper",
    "@id": "http://oparl.beispielris.de/paper/749",
    "reference": "1234/2014",
    "publishedDate": "2014-04-04T16:42:02+02:00",
    "name": "Antwort auf Anfrage 1200/2014",
    "paperType": "beispielris:vocab/answer",
    "relatedPaper": "beispielris:paper/699",
    "mainDocument": "beispielris:document/925",
    "auxiliaryDocument": "beispielris:document/926",
    "location": [
        {
            "description": "Theodor-Heuss-Ring 1",
            "lat": 7.148,
            "lon": 50.023
        }
    ],
    "creator": [
        "beispielris:organization/2000",
        "beispielris:people/1000"
    ],
    "consultation": [
        "beispielris:consultation/5676",
        "beispielris:consultation/5689"
    ]
    "lastModified": "2013-01-08T12:05:27+01:00"
}
~~~~~

`paperType`
:   Ein Objekt mit einem `skos:prefLabel`-Attribut, dessen Wert eine Zeichenkette ist und 
    die Art der Drucksache beschreibt, z.B. "Beantwortung einer Anfrage". Eine weitere Liste
    mit exemplarischen Drucksachentypen gibt es hier: https://wiki.piratenpartei.de/BE:BVVupdates/Glossar
    Eine zukünftige Version von OParl wird möglicherweise solche Werte spezifizieren.
    OPTIONAL

TODO:
* Eigenschaften beschreiben
* Eigenschaft "locations" im Beispiel ändern
