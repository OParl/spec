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
    "fileName": "57739.pdf",
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

`fileName`
:   Dateiname, unter dem die Datei in einem Dateisystem gespeichert werden
    kann.
    Typ: ASCII-Zeichenkette.
    ZWINGEND.

`name`
:   Ein zur Anzeige für Endnutzer bestimmter Name für dieses Objekt.
    Der Wert SOLL NICHT mit dem Wert der Eigenschaft `fileName` identisch
    sein.
    Typ: Zeichenkette.
    EMPFOHLEN.

`mimeType`
:   Mime-Typ des Inhalts^[vgl. RFC2046: <http://tools.ietf.org/html/rfc2046>].
    Sollte das System einer Datei keinen
    spezifischen Typ zuweisen können, wird EMPFOHLEN, hier 
    `application/octet-stream` zu verwenden.
    Typ: Zeichenkette
    ZWINGEND.
    
`date`
:   Datum und Zeit der Erstellung der Datei. Wahlweise, falls dies nicht
    vom System kommuniziert werden kann oder soll, KANN alternativ
    der Zeitpunkt der Veröffentlichung ausgegeben werden.
    Typ: Datum.
    ZWINGEND.

`lastModified`
:   Datum und Zeit der letzten Änderung der Datei bzw. der Metadaten. Als
    Änderung der Datei gilt alles, was den Inhalt der Datei verändert und
    beispielsweise zu einer Veränderung der Prüfsumme führen würde, nicht
    aber die Änderung des Dateinamens (siehe Eigenschaft `name`). Als 
    Änderung der Metadaten hingegen würde beispielsweise die Änderung des 
    Dateinamens gelten. Hier soll immer das größere der beiden Daten
    ausgegeben werden, also der am wenigsten lang zurückliegende
    Änderungszeitpunkt.
    Typ: Datum.
    ZWINGEND.

`size`
:   Größe der Datei in Bytes.
    Typ: ganze Zahl.
    ZWINGEND.

`sha1Checksum`
:   SHA1-Prüfsumme des Dokumenteninhalts in Hexadezimal-Schreibweise.
    Typ: Zeichenkette.
    OPTIONAL.
    
`text`
:   Reine Text-Wiedergabe des Dateiinhalts, sofern dieser in Textform
    wiedergegeben werden kann.
    Typ: Zeichenkette.
    EMPFOHLEN.

`accessUrl`
:   URL zum allgemeinen Zugriff auf die Datei. Näheres unter [Dateizugriff](#dateizugriff).
    Typ: URL.
    ZWINGEND.

`downloadUrl`
:   URL zum Download der Datei. Näheres unter [Dateizugriff](#dateizugriff).
    Typ: URL.
    EMPFOHLEN.

`paper`
:   Falls die Datei zu einer Drucksache (oparl:Paper) gehört, MUSS über diese Eigenschaft die
    URL des Drucksache-Objekts ausgegeben werden. Andernsfalls DARF diese Eigenschaft NICHT
    vorhanden sein.
    Typ: `oparl:Paper`.

`meeting`
:   Falls die Datei zu einer Sitzung (oparl:Meeting) gehört, MUSS über diese Eigenschaft
    die URL des Sitzung-Objekts ausgegeben werden. Andernfalls DARF diese Eigenschaft NICHT
    vorhanden sein.
    Typ: `oparl:Meeting`.

`masterDocument`
:   Datei von der das aktuelle Objekt abgeleitet wurde.
    Typ: `oparl:Document`.
    OPTIONAL.

`derivativeDocuments`
:   Abgeleitete Datei die von dem aktuellen Objekt abgeleitet wurde.
    Typ: `oparl:Document`.
    OPTIONAL.

`license`
:   Lizenz unter der die Datei angeboten wird. Wenn diese Eigenschaft verwendet
    wird, dann ist sie anstelle einer globalen Angabe im übergeordneten
    `oparl:Body` bzw. `oparl:System` Objekt maßgeblich.
    Typ: URL.
    OPTIONAL

`documentRole`
:   Rolle, Funktion, Sorte des Dokuments. Das Objekt enthält ein `skos:prefLabel`.
    Dessen Werte können z.B. sein:
    "Einladung", "Protokoll", "Wortprotokoll" oder "Beschlussprotokoll". In einer
    zukünftigen OParl-Version wird möglicherweise eine Menge der wichtigsten
    Kategorien vorgegeben.
    Typ: `skos:Concept`.
    OPTIONAL.
    TODO: Link auf Erkärungs-Kapitel, damit klar ist, dass hier auf externes
    Vokabular verlinkt wird.

`classification`
:   Begriff mit `skos:prefLabel`. Hat allgemeinere Bedeutung als `documentRole`.
    Typ: `skos:Concept`.
    OPTIONAL.
    TODO: 
    TODO: Link auf Erkärungs-Kapitel, damit klar ist, dass hier auf externes
    Vokabular verlinkt wird.
