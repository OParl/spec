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
    "access_url": "http://beispielris.de/documents/57739.pdf",
    "access_url": "http://beispielris.de/documents/download/57739.pdf",
    "text": "Der Übersichtsplan zeigt alle Ebenen des ...",
    "master_document": "http://beispielris.de/documents/57738",
    "license": "http://www.opendefinition.org/licenses/cc-by"
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
:   Name des Objekts, der Nutzern angezeigt werden kann. Diese Eigenschaft 
    ist ZWINGEND. Typ: Zeichenkette.

`mime_type`
:   Mime-Typ des Inhalts (vgl. RFC2046^[<http://tools.ietf.org/html/rfc2046>]).
    Diese Eigenschaft ist ZWINGEND. Sollte das System einer Datei keinen
    spezifischen Typ zuweisen können, wird EMPFOHLEN, hier 
    "application/octet-stream" zu verwenden.

`date`
:   Erstellungs- oder Veröffentlichungsdatum und -uhrzeit. Diese Eigenschaft
    ist ZWINGEND. Typ: Datum.

`last_modified`
:   Datum und Uhrzeit der letzten Änderung der Datei bzw. der Metadaten. Diese
    Eigenschaft ist ZWINGEND. Typ: Datum.

`size`
:   Größe der Datei in Bytes. Diese Eigenschaft ist ZWINGEND. Typ: Zahl.

`sha1_checksum`
:   SHA1-Prüfsumme des Dokumenteninhalts in Hexadezimal-Schreibweise.
    Typ: Zeichenkette.

`text`
:   Reine Text-Wiedergabe des Dateiinhalts, sofern dieser in Textform
    wiedergegeben werden kann. Diese Eigenschaft ist EMPFOHLEN.
    Typ: Zeichenkette.

`access_url`
:   URL zum gewöhnlichen Abruf der Datei mittels
    HTTP GET-Aufruf. Diese Eigenschaft ist ZWINGEND. Typ: URL.

`download_url`
:   URL zum Download der Datei. Diese Eigenschaft ist EMPFOHLEN. Typ: URL.

`paper`
:   URL des zugehörigen Objekts vom Typ `oparl:Paper`, sofern diese Datei
    zu einer Drucksache gehört. Wenn diese Datei zu einer Drucksache gehört,
    MUSS diese Eigenschaft vorhanden sein, andernfalls DARF sie NICHT
    vorhanden sein. Typ: URL.

`meeting`
:   URL des zugehörigen Objekts vom Typ `oparl:Meeting`, sofern diese Datei
    zu einer Sitzung gehört. Wenn diese Datei zu einer Sitzung gehört,
    MUSS diese Eigenschaft vorhanden sein, andernfalls DARF sie NICHT
    vorhanden sein. Typ: URL.

`master_document`
:   URL des Objekts vom Typ `oparl:Document`, von dem das aktuelle
    Objekt abgeleitet wurde. Diese Eigenschaft ist OPTIONAL. Typ: URL.

`derivative_documents`
:   URLs aller Objekte vom Typ `oparl:Document`, die von dem aktuellen
    Objekt abgeleitet wurden. Diese Eigenschaft ist OPTIONAL. Typ: Liste
    von URLs.

`license`
:   URL der Lizenz unter der die Datei angeboten wird. Wenn diese Eigenschaft verwendet
    wird, dann ist sie massgeblich und nicht die globalere Angabe in dem `oparl:Body` Objekt der Körperschaft.
    Lesenswert zum Thema Lizensierung von Linked Data ist http://linkeddatabook.com/editions/1.0/#htoc48
    OPTIONAL

### Siehe auch

* [Dokumentenabruf](#dokumentenabruf)
