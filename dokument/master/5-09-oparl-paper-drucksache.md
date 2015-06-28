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

**Beispiel**

~~~~~  {#paper_ex1 .json}
{
    "id": "https://oparl.example.org/paper/749",
    "type": "http://oparl.org/schema/1.0/Paper",
    "body": "https://oparl.example.org/bodies/1",
    "name": "Antwort auf Anfrage 1200/2014",
    "reference": "1234/2014",
    "publishedDate": "2014-04-04T16:42:02+02:00",
    "paperType": "Beantwortung einer Anfrage",
    "relatedPaper": [
        "https://oparl.example.org/paper/699"
    ],
    "mainFile": "https://oparl.example.org/files/925",
    "auxiliaryFile": [
        "https://oparl.example.org/files/926"
    ],
    "location": [
        "https://oparl.example.org/locations/4472"
    ],
    "originator": [
        "https://oparl.example.org/organization/2000",
        "https://oparl.example.org/people/1000"
    ],
    "consultation": [
        "https://oparl.example.org/consultation/5676",
        "https://oparl.example.org/consultation/5689"
    ],
    "underDirectionOf": [
        "https://oparl.example.org/organization/2000"
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
    Typ: `xsd:dateTime` oder `xsd:date`.
    Kardinalität: 0 bis 1.
    ZWINGEND.

`paperType`
:   Art der Drucksache, z. B. "Beantwortung einer Anfrage".
    Diese Eigenschaft funktioniert wie in 
    [Vokabulare zur Klassifizierung](#vokabulare_klassifizierung) beschrieben 
    entweder als URL zu einem `skos:Concept` oder als String.
    Kardinalität: 0 bis 1.
    Typ: String oder URL eines `skos:Concept` Objekts.
    EMPFOHLEN.

`relatedPaper`
:   Inhaltlich verwandte Drucksachen.
    Typ: Liste von Objekten des Typs `oparl:Paper`. Vgl. [Objektlisten](#objektlisten).
    Kardinalität: 0 bis *.
    OPTIONAL.

`mainFile`
:   Die Haupt-Datei zu dieser Drucksache. Beispiel: Die Drucksache repräsentiert
    eine Beschlussvorlage und die Haupt-Datei enthält den Text der Beschlussvorlage.
    Typ: URL eines Objekts vom Typ `oparl:File`.
    Kardinalität: 1.
    ZWINGEND.
    
`auxiliaryFile`
:   Anhänge zur Drucksache. Diese sind, in Abgrenzung zur Haupt-Datei
    (`mainFile`), untergeordnet und es kann beliebig viele davon geben.
    Typ: Liste von Objekten des Typs `oparl:File`. Vgl. [Objektlisten](#objektlisten).
    Kardinalität: 0 bis *.
    OPTIONAL.
    
`location`
:   Sofern die Drucksache einen inhaltlichen Ortsbezug hat, beschreibt diese
    Eigenschaft den Ort in Textform und/oder in Form von Geodaten.
    Typ: Liste von Objekten des Typs `oparl:Location`. Vgl. [Objektlisten](#objektlisten).
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
:   Schlagworte.
    Typ: Array von Strings oder URLs zu `skos:Concept` Objekten
    (vgl. [Vokabulare zur Klassifizierung](#vokabulare_klassifizierung)).
    Kardinalität: 0 bis *.
    OPTIONAL.

`underDirectionOf`
:   Federführung. Amt oder Abteilung, für die Inhalte oder Beantwortung der Drucksache verantwortlich.
    Typ: Liste von Objekten des Typs `oparl:Organization`.
    Kardinalität: 0 bis *.
    OPTIONAL.
    
