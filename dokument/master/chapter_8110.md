oparl:Document (Datei)  {#oparl_document}
----------------------

Ein Objekt vom Typ `oparl:Document` repräsentiert eine Datei,
beispielsweise eine PDF-Datei, ein RTF- oder ODF-Dokuments,
und hält Metadaten zu der Datei sowie URLs zum Zugriff auf 
die Datei bereit.

Ein Beispiel:

~~~~~  {#document_ex1 .json}
{
    "@type": "oparl:Document",
    "@id": "http://beispielris.de/documents/57739",
    "name": "Anlage 1 zur Anfrage",
    "paper": "http://beispielris.de/papers/2396",
    "mime_type": "application/pdf",
    "date": "2013-01-04T07:54:13+01:00",
    "last_modified": "2013-01-04T07:54:13+01:00",
    "sha1_checksum": "da39a3ee5e6b4b0d3255bfef95601890afd80709",
    "size": 82930,
    "accessUrl": "http://beispielris.de/documents/57739.pdf",
    "downloadUrl": "http://beispielris.de/documents/download/57739.pdf",
    "text": "Der Übersichtsplan zeigt alle Ebenen des ...",
    "master_document": "http://beispielris.de/documents/57738",
    "license": "http://www.opendefinition.org/licenses/cc-by",
    "documentRole": "http://beispielris.de/document-roles/evidence",
}
~~~~~

Objekt vom Typ `oparl:Document` können mit Drucksachen (`oparl:Paper`)
oder Sitzungen (`oparl:Meeting`) in Beziehung stehen. Dies wird durch 
die Eigenschaft `paper` bzw. `meeting` angezeigt.

Mehrere Objekte vom Typ `oparl:Document` können mit einander in direkter
Beziehung stehen, wenn sie den selben Inhalt in unterschiedlichen
technischen Formaten wiedergeben. Hierfür werden die Eigenschaften
`master_document` bzw. `derivative_documents` eingesetzt. Das oben angezeigte
Beispiel-Objekt repräsentiert eine PDF-Datei (zu erkennen an der
Eigenschaft `mime_type`) und zeigt außerdem über die Eigenschaft 
`master_document` an, von welcher anderen Datei es abgeleitet wurde.
Umgekehrt KANN über die Eigenschaft `derivative_documents` angezeigt
werden, welche Ableitungen einer Datei existieren.

### Eigenschaften ###

`@id`
:   Die URL des Objekts.

`name`
:   Name des Objekts, der Nutzern angezeigt werden kann.
    Typ: Zeichenkette.
    ZWINGEND

`mime_type`
:   Mime-Typ des Inhalts (vgl. RFC2046^[<http://tools.ietf.org/html/rfc2046>]).
    Sollte das System einer Datei keinen
    spezifischen Typ zuweisen können, wird EMPFOHLEN, hier 
    "application/octet-stream" zu verwenden.
    ZWINGEND
`date`
:   Erstellungs- oder Veröffentlichungsdatum und -uhrzeit.
    Typ: Datum.
    ZWINGEND

`last_modified`
:   Datum und Uhrzeit der letzten Änderung der Datei bzw. der Metadaten.
    Typ: Datum.
    ZWINGEND

`size`
:   Größe der Datei in Bytes.
    Typ: ganze Zahl.
    ZWINGEND

`sha1_checksum`
:   SHA1-Prüfsumme des Dokumenteninhalts in Hexadezimal-Schreibweise.
    Typ: Zeichenkette.
    OPTIONAL
    
`text`
:   Reine Text-Wiedergabe des Dateiinhalts, sofern dieser in Textform
    wiedergegeben werden kann.
    Typ: Zeichenkette.
    EMPFOHLEN

`accessUrl`
:   URL zum gewöhnlichen Abruf der Datei mittels HTTP GET-Aufruf.
    Typ: URL.
    ZWINGEND

`downloadUrl`
:   URL zum Download der Datei. Besser ist es, bereits unter `accessUrl` einen "schönen" Dateinamen anzugeben.
    TODO: Zweck erklären.
    Typ: URL.
    EMPFOHLEN

`paper`
:   Zugehöriges Objekts vom Typ `oparl:Paper`, sofern diese Datei
    zu einer Drucksache gehört. Wenn diese Datei zu einer Drucksache gehört,
    MUSS diese Eigenschaft vorhanden sein, andernfalls DARF sie NICHT
    vorhanden sein.
    Typ: URL.

`meeting`
:   Zugehöriges Objekt vom Typ `oparl:Meeting`, sofern diese Datei
    zu einer Sitzung gehört. Wenn diese Datei zu einer Sitzung gehört,
    MUSS diese Eigenschaft vorhanden sein, andernfalls DARF sie NICHT
    vorhanden sein.
    Typ: URL.

`master_document`
:   `oparl:Document`, von dem das aktuelle Objekt abgeleitet wurde.
    Typ: URL.
    OPTIONAL

`derivative_documents`
:   `oparl:Document`, die von dem aktuellen Objekt abgeleitet wurden.
    Typ: URL.
    OPTIONAL
    
`license`
:   Lizenz unter der die Datei angeboten wird. Wenn diese Eigenschaft verwendet
    wird, dann ist sie massgeblich und nicht die globalere Angabe in dem `oparl:Body` Objekt der Körperschaft.
    Lesenswert zum Thema Lizensierung von Linked Data ist http://linkeddatabook.com/editions/1.0/#htoc48
    Type: URL
    OPTIONAL

`documentRole`
:   Rolle, Funktion, Sorte des Dokuments. Das Objekt enthält ein `skos:prefLabel`. Dessen Werte können z.B. sein:
    "Einladung", "Protokoll", "Wortprotokoll" oder "Beschlussprotokoll". In einer zukünftigen OParl-Version
    wird möglicherweise eine Menge der wichtigsten Kategorien vorgegeben.
    TODO: Besser in `oparl:Paper` oder `oparl:Meeting` ?
    Siehe Diskussion unter https://github.com/OParl/specs/issues/65
    Typ: URL
    OPTIONAL

### Siehe auch

* [Dokumentenabruf](#dokumentenabruf)
