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

### Beispiel ###

Zunächst ein Kontext:

~~~~~
{
    "body": {
        "@id": "oparl:body",
        "@type": "@id"
    },
    "name": {
        "@id": "rdfs:label"
    }
    "reference":
        "@id": "oparl:reference"
    }
    "publishedDate": {
        "@id": "schorg:datePublished",
        "@type": "xsd:dateTime"
    },  
    "paperType": {
        "@id": "oparl:paperType",
        "@type": "@id"
    },  
    "relatedPaper": {
        "@id": "oparl:relatedPaper",
        "@type": "@id"
    },
    "mainDocument": {
        "@id": "oparl:mainDocument",
        "@type": "@id"
    },
    "auxiliaryDocument": {
        "@id": "oparl:auxiliaryDocument",
        "@type": "@id"
    },
    "location": {
        "@id": "oparl:location",
        "@type": "@id"
    },
    "originator": {
        "@id": "prov:wasAttributedTo",
        "@type": "@id"
    },
    "consultation": {
        "@id": "oparl:consultation",
        "@type": "@id"
    },
    "modified": {
        "@id": "dc:modified",
        "@type": "xsd:dateTime"
    }
}
~~~~~

~~~~~  {#paper_ex1 .json}
{
    "@context": "https://oparl.example.org/Pfad/zum/Kontext/oparl.jsonld",
    "@type": "oparl:Paper",
    "@id": "beispielris:paper/749",
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
    ZWINGEND.

`name`
:   Titel der Drucksache.
    Typ: String.
    Kardinalität: 1.
    ZWINGEND.

`reference`
:   Kennung bzw. Aktenzeichen der Drucksache, mit der sie in der parlamentarischen
    Arbeit eindeutig referenziert werden kann.
    Typ: String.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`publishedDate`
:   Veröffentlichungsdatum der Drucksache.
    Typ: Datentyp `xsd:dateTime` | Datentyp `xsd:date`.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.

`paperType`
:   Begriff mit einem `skos:prefLabel`-Attribut, dessen Wert eine Zeichenkette
    ist und die Art der Drucksache beschreibt, z. B. "Beantwortung einer Anfrage".
    Für die URLs kommen als letztes Pfadelement z. B. "draft", "petition", "request",
    "note" und "answer" in Frage. Denkbar ist auch eine Kategorisierung z. B. in
    drei Arten von Drucksachen: initiierend, beratend und protokollierend.^[Eine
    Liste mit exemplarischen Drucksachentypen:
    <https://wiki.piratenpartei.de/BE:BVVupdates/Glossar>]
    Kardinalität: 0 bis 1.
    Typ: `skos:Concept`.
    EMPFOHLEN.

`relatedPaper`
:   Inhaltlich verwandte Drucksache(n).
    Typ: `oparl:Paper`.
    Kardinalität: 0 bis *.
    OPTIONAL.

`mainDocument`
:   Das Hauptdokument zu dieser Drucksache. Beispiel: Die Drucksache repräsentiert
    eine Beschlussvorlage und das Hauptdokument enthält den Text der Beschlussvorlage.
    Typ: `oparl:File`.
    Kardinalität: 1.
    ZWINGEND.
    
`auxiliaryDocument`
:   Anhänge zur Drucksache. Diese sind, in Abgrenzung zum Hauptdokument
    (`mainDocument`), untergeordnet und es kann beliebig viele davon geben.
    Typ: `oparl:File`.
    Kardinalität: 0 bis *.
    OPTIONAL.
    
`location`
:   Sofern die Drucksache einen inhaltlichen Ortsbezug hat, beschreibt diese
    Eigenschaft den Ort in Textform und/oder in Form von Geodaten.
    Typ: `oparl:Location`.
    Kardinalität: 0 bis *.
    OPTIONAL.

`originator`
:   Urheber der Drucksache, kann eine oder mehrere Person(en) bzw. Gruppierung(en)
    sein.
    Typ: `oparl:Person` | `oparl:Organization`.
    Kardinalität: 0 bis *.
    EMPFOHLEN.

`consultation`
:   Beratungen der Drucksache.
    Typ: `oparl:Consultation`.
    Kardinalität: 0 bis *.
    OPTIONAL.

`modified`
:   Letzter Änderungszeitpunkt des Objekts.
    Typ: Datentyp `xsd:dateTime`.
    Kardinalität: 1.
    EMPFOHLEN.
    
`keyword`
:   Begriff mit `skos:prefLabel`. Allgemeiner als `paperType`.
    Typ: `skos:Concept`.
    Kardinalität: 0 bis *.
    OPTIONAL.

`underDirectionOf`
:   Federführung. Amt oder Abteilung, für die Inhalte oder Beantwortung der Drucksache verantwortlich.
    Typ: `oparl:Organization`.
    Kardinalität: 0 bis *.
    OPTIONAL.
    
