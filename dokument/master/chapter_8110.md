oparl:Document (Datei)  {#oparl_document}
----------------------

Ein Objekt vom Typ `oparl:Document` repräsentiert eine Datei,
beispielsweise eine PDF-Datei, ein RTF- oder ODF-Dokument,
und hält Metadaten zu der Datei sowie URLs zum Zugriff auf 
die Datei bereit.

Ein Beispiel:

~~~~~  {#document_ex1 .json}
{
    "@type": "oparl:Document",
    "@id": "https://oparl.beispielris.de/document/57739",
    "name": "Anlage 1 zur Anfrage",
    "paper": "https://oparl.beispielris.de/paper/2396",
    "mimeType": "application/pdf",
    "date": "2013-01-04T07:54:13+01:00",
    "lastModified": "2013-01-04T07:54:13+01:00",
    "sha1Checksum": "da39a3ee5e6b4b0d3255bfef95601890afd80709",
    "size": 82930,
    "accessUrl": "https://oparl.beispielris.de/document/57739.pdf",
    "downloadUrl": "https://oparl.beispielris.de/document/download/57739.pdf",
    "text": "Der Übersichtsplan zeigt alle Ebenen des ...",
    "masterDocument": "https://oparl.beispielris.de/document/57738",
    "license": "http://www.opendefinition.org/licenses/cc-by",
    "documentRole": "https://oparl.beispielris.de/document-role/evidence",
}
~~~~~

Objekt vom Typ `oparl:Document` können mit Drucksachen (`oparl:Paper`)
oder Sitzungen (`oparl:Meeting`) in Beziehung stehen. Dies wird durch 
die Eigenschaft `paper` bzw. `meeting` angezeigt.

Mehrere Objekte vom Typ `oparl:Document` können mit einander in direkter
Beziehung stehen, wenn sie den selben Inhalt in unterschiedlichen
technischen Formaten wiedergeben. Hierfür werden die Eigenschaften
`masterDocument` bzw. `derivativeDocuments` eingesetzt. Das oben angezeigte
Beispiel-Objekt repräsentiert eine PDF-Datei (zu erkennen an der
Eigenschaft `mimeType`) und zeigt außerdem über die Eigenschaft 
`masterDocument` an, von welcher anderen Datei es abgeleitet wurde.
Umgekehrt KANN über die Eigenschaft `derivativeDocuments` angezeigt
werden, welche Ableitungen einer Datei existieren.

### Eigenschaften ###

`name`
:   Name des Objekts, der Nutzern angezeigt werden kann.
    Typ: Zeichenkette.
    ZWINGEND

`mimeType`
:   Mime-Typ des Inhalts (vgl. RFC2046^[<http://tools.ietf.org/html/rfc2046>]).
    Sollte das System einer Datei keinen
    spezifischen Typ zuweisen können, wird EMPFOHLEN, hier 
    "application/octet-stream" zu verwenden.
    Typ: TODO
    ZWINGEND
    
`date`
:   Erstellungs- oder Veröffentlichungsdatum und -uhrzeit.
    Typ: Datum.
    ZWINGEND

`lastModified`
:   Datum und Uhrzeit der letzten Änderung der Datei bzw. der Metadaten.
    Typ: Datum.
    ZWINGEND

`size`
:   Größe der Datei in Bytes.
    Typ: ganze Zahl.
    ZWINGEND

`sha1Checksum`
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
:   Drucksache, sofern diese Datei zu einer Drucksache gehört. Wenn diese Datei zu einer Drucksache gehört,
    MUSS diese Eigenschaft vorhanden sein, andernfalls DARF sie NICHT vorhanden sein.
    TODO: ist das eine Tautologie?
    Typ: `oparl:Paper`

`meeting`
:   Sitzung, sofern diese Datei zu einer Sitzung gehört. Wenn diese Datei zu einer Sitzung gehört,
    MUSS diese Eigenschaft vorhanden sein, andernfalls DARF sie NICHT
    vorhanden sein.
    TODO: ist das eine Tautologie?
    Typ: `oparl:Meeting`.

`masterDocument`
:   Datei von der das aktuelle Objekt abgeleitet wurde.
    Typ: `oparl:Document`.
    OPTIONAL

`derivativeDocuments`
:   Abgeleitete Datei die von dem aktuellen Objekt abgeleitet wurde.
    Typ: `oparl:Document`.
    OPTIONAL

`license`
:   Lizenz unter der die Datei angeboten wird. Wenn diese Eigenschaft verwendet
    wird, dann ist sie anstelle einer globalen Angabe im übergeordneten
    `oparl:Body` bzw. `oparl:System` Objekt maßgeblich.
    Typ: URL.
    OPTIONAL

`documentRole`
:   Rolle, Funktion, Sorte des Dokuments. Das Objekt enthält ein `skos:prefLabel`. Dessen Werte können z.B. sein:
    "Einladung", "Protokoll", "Wortprotokoll" oder "Beschlussprotokoll". In einer zukünftigen OParl-Version
    wird möglicherweise eine Menge der wichtigsten Kategorien vorgegeben.
    TODO: Besser in `oparl:Paper` oder `oparl:Meeting` ?
    Siehe Diskussion unter https://github.com/OParl/specs/issues/65
    Typ: `skos:Concept`
    OPTIONAL

`classification`
:   Begriff mit `skos:prefLabel`. Hat allgemeinere Bedeutung als `documentRole`.
    Typ: `skos:Concept`
    OPTIONAL

### Siehe auch

* [Dateizugriff](#dateizugriff)
