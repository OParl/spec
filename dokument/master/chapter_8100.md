oparl:Paper (Drucksache)  {#oparl_paper}
------------------------

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
    "@context": "https://oparl.beispielris.de/Pfad/zum/Kontext/oparl.jsonld",
    "@type": "oparl:Paper",
    "@id": "https://oparl.beispielris.de/paper/749",
    "body": "beispielris:bodies/1",
    "name": "Antwort auf Anfrage 1200/2014",
    "reference": "1234/2014",
    "publishedDate": "2014-04-04T16:42:02+02:00",
    "paperType": "beispielris:vocab/answer",
    "relatedPaper": "beispielris:paper/699",
    "mainDocument": "beispielris:document/925",
    "auxiliaryDocument": "beispielris:document/926",
    "location": [
        {
            "description": "Theodor-Heuss-Ring 1",
            "geometry": "POINT(7.148  50.023)"
        }
    ],
    "originator": [
        "beispielris:organization/2000",
        "beispielris:people/1000"
    ],
    "consultation": [
        "beispielris:consultation/5676",
        "beispielris:consultation/5689"
    ],
    "modified": "2013-01-08T12:05:27+01:00"
}
~~~~~

### Eigenschaften

`body`
:   Körperschaft, zu der die Drucksache gehört.
    Typ: `oparl:Body`.
    Kardinalität: 1.
    Diese Eigenschaft ist ZWINGEND.

`name`
:   Titel der Drucksache.
    Typ: Zeichenkette.
    Kardinalität: 1.
    Diese Eigenschaft ist ZWINGEND.

`reference`
:   Kennung bzw. Aktenzeichen der Drucksache, mit der sie in der parlamentarischen
    Arbeit eindeutig referenziert werden kann.
    Typ: Zeichenkette.
    Kardinalität: 0 bis 1.
    Die Eigenschaft ist OPTIONAL.

`publishedDate`
:   Veröffentlichungsdatum der Drucksache.
    Typ: Datum mit oder ohne Zeit.
    Kardinalität: 0 bis 1.
    Diese Eigenschaft ist EMPFOHLEN.

`paperType`
:   Begriff mit einem `skos:prefLabel`-Attribut, dessen Wert eine Zeichenkette
    ist und die Art der Drucksache beschreibt, z. B. "Beantwortung einer Anfrage".
    Für die URLs kommen als letztes Pfadelement z. B. "draft", "petition", "request",
    "note" und "answer" in Frage. Denkbar ist auch eine Kategorisierung z. B. in
    drei Arten von Drucksachen: initiierend, beratend und protokollierend.^[Eine
    Liste mit exemplarischen Drucksachentypen:
    <https://wiki.piratenpartei.de/BE:BVVupdates/Glossar>]
    Kardinalität: 0 bis 1.
    Typ: `skos:Concept`.
    Diese Eigenschaft ist EMPFOHLEN.

`relatedPaper`
:   Inhaltlich verwandte Drucksache(n).
    Typ: `oparl:Paper`.
    Kardinalität: 0 bis *.
    Die Eigenschaft ist OPTIONAL.

`mainDocument`
:   Das Hauptdokument zu dieser Drucksache. Beispiel: Die Drucksache repräsentiert
    eine Beschlussvorlage und das Hauptdokument enthält den Text der Beschlussvorlage.
    Typ: `oparl:Document`.
    Kardinalität: 1.
    Diese Eigenschaft ist ZWINGEND.
    
`auxiliaryDocument`
:   Anhänge zur Drucksache. Diese sind, in Abgrenzung zum Hauptdokument
    (`mainDocument`), untergeordnet und es kann beliebig viele davon geben.
    Typ: `oparl:Document`.
    Kardinalität: 0 bis *.
    Die Eigenschaft ist OPTIONAL.
    
`location`
:   Sofern die Drucksache einen inhaltlichen Ortsbezug hat, beschreibt diese
    Eigenschaft den Ort in Textform und/oder in Form von Geodaten.
    Typ: `oparl:Location`.
    Kardinalität: 0 bis *.
    Die Eigenschaft ist OPTIONAL.

`originator`
:   Urheber der Drucksache, kann eine oder mehrere Person(en) bzw. Gruppierung(en)
    sein.
    Typ: `oparl:Person` | `oparl:Organization`.
    Kardinalität: 0 bis *.
    Die Eigenschaft ist EMPFOHLEN.

`consultation`
:   Beratungen der Drucksache.
    Typ: `oparl:Consultation`.
    Kardinalität: 0 bis *.
    Die Eigenschaft ist OPTIONAL.

`modified`
:   Letzter Änderungszeitpunkt des Objekts.
    Typ: Zeitstempel.
    Kardinalität: 1.

`keyword`
:   Begriff mit `skos:prefLabel`. Allgemeiner als `paperType`.
    Typ: `skos:Concept`.
    Kardinalität: 0 bis *.
    Die Eigenschaft ist OPTIONAL.
