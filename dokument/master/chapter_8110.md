oparl:File (Datei)  {#oparl_document}
----------------------

Ein Objekt vom Typ `oparl:File` repräsentiert eine Datei,
beispielsweise eine PDF-Datei, ein RTF- oder ODF-Dokument,
und hält Metadaten zu der Datei sowie URLs zum Zugriff auf 
die Datei bereit.

### Beispiel ###

Ein Kontext:

~~~~~
{
    "name": "rdfs:label",
    "fileName": "oparl:fileName",
    "paper": {
        "@id": "oparl:paper",
        "@type": "@id"
    },
    "mimeType": "oparl:mimeType",
    "date": {
        "@id": "oparl:date",
        "@type": "xsd:dateTime"
    },
    "modified": {
        "@id": "dc:modified",
        "@type": "xsd:dateTime"
    },
    "sha1Checksum": "oparl:sha1Checksum",
    "size": {
        "@type": "xsd:integer" TODO ausreichend?
    }
    "accessUrl": {
        "@id": "oparl:accessUrl",
        "@type": "@id"
    },
    "downloadUrl": {
        "@id": "oparl:downloadUrl",
        "@type": "@id"
    },
    "text": "oparl:text",
    "masterDocument": {
        "@id": "prov:wasDerivedFrom",
        "@type": "@id"
    },
    "derivativeDocument": {
        "@id": "prov:hadDerivation",
            TODO: invers zu masterDocument, deshalb nicht verwenden
        "@type": "@id"
    },  
    "license": {
        "@id": "oparl:",
        "@type": "@id"
    },
    "documentRole": {
        "@id": "oparl:downloadRole",
        "@type": "@id"
    }
}
~~~~~


~~~~~  {#document_ex1 .json}
{
    "@type": "oparl:File",
    "@id": "beispielris:document/57739",
    "name": "Anlage 1 zur Anfrage",
    "fileName": "57739.pdf",
    "paper": "https://oparl.example.org/paper/2396",
    "mimeType": "application/pdf",
    "date": "2013-01-04T07:54:13+01:00",
    "modified": "2013-01-04T07:54:13+01:00",
    "sha1Checksum": "da39a3ee5e6b4b0d3255bfef95601890afd80709",
    "size": 82930,
    "accessUrl": "beispielris:document/57739.pdf",
    "downloadUrl": "beispielris:document/download/57739.pdf",
    "text": "Der Übersichtsplan zeigt alle Ebenen des ...",
    "masterDocument": "beispielris:document/57738",
    "license": "http://www.opendefinition.org/licenses/cc-by",
    "documentRole": "beispielris:document-role/evidence"
}
~~~~~

### Anmerkungen ###

Objekte vom Typ `oparl:File` können mit Drucksachen (`oparl:Paper`)
oder Sitzungen (`oparl:Meeting`) in Beziehung stehen. Dies wird durch 
die Eigenschaft `paper` bzw. `meeting` angezeigt.

Mehrere Objekte vom Typ `oparl:File` können mit einander in direkter
Beziehung stehen, wenn sie den selben Inhalt in unterschiedlichen
technischen Formaten wiedergeben. Hierfür werden die Eigenschaften
`masterDocument` bzw. `derivativeDocument` eingesetzt. Das oben angezeigte
Beispiel-Objekt repräsentiert eine PDF-Datei (zu erkennen an der
Eigenschaft `mimeType`) und zeigt außerdem über die Eigenschaft 
`masterDocument` an, von welcher anderen Datei es abgeleitet wurde.
Umgekehrt KANN über die Eigenschaft `derivativeDocument` angezeigt
werden, welche Ableitungen einer Datei existieren.

### Eigenschaften ###

`fileName`
:   Dateiname, unter dem die Datei in einem Dateisystem gespeichert werden
    kann. Beispiel: "einedatei.pdf"
    Typ: ASCII-Zeichenkette, aber als Unicode-String
    Kardinalität: 1.
    ZWINGEND.

`name`
:   Ein zur Anzeige für Endnutzer bestimmter Name für dieses Objekt.
    Leerzeichen DÜRFEN enthalten sein werden, Datei-Extension wie ".pdf" SOLLEN
    NICHT enthalten sein.
    Der Wert SOLL NICHT mit dem Wert der Eigenschaft `fileName` identisch
    sein.
    Typ: String.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.

`mimeType`
:   MIME-Type des Inhalts^[vgl. RFC2046: <http://tools.ietf.org/html/rfc2046>].
    Sollte das System einer Datei keinen
    spezifischen Typ zuweisen können, wird EMPFOHLEN, hier 
    `application/octet-stream` zu verwenden.
    Typ: String.
    Kardinalität: 1.
    EMPFOHLEN.

`date`
:   Datum und Zeit der Erstellung der Datei. Wahlweise, falls dies nicht
    vom System kommuniziert werden kann oder soll, KANN alternativ
    der Zeitpunkt der Veröffentlichung ausgegeben werden.
    Typ: xsd:dateTime.
    Kardinalität: 1.
    ZWINGEND.

`modified`
:   Datum und Zeit der letzten Änderung der Datei bzw. der Metadaten. Als
    Änderung der Datei gilt alles, was den Inhalt der Datei verändert und
    beispielsweise zu einer Veränderung der Prüfsumme führen würde, nicht
    aber die Änderung des Dateinamens (siehe Eigenschaft `name`). Als 
    Änderung der Metadaten hingegen würde beispielsweise die Änderung des 
    Dateinamens gelten. Hier soll immer das größere der beiden Daten
    ausgegeben werden, also der am wenigsten lang zurückliegende
    Änderungszeitpunkt.
    Typ: xsd:dateTime.
    Kardinalität: 1.
    ZWINGEND.

`size`
:   Größe der Datei in Bytes.
    Typ: ganze Zahl.
    Kardinalität: 1.
    ZWINGEND.

`sha1Checksum`
:   SHA1-Prüfsumme des Dokumenteninhalts in Hexadezimal-Schreibweise.
    Typ: String.
    Kardinalität: 0 bis 1.
    OPTIONAL.
    
`text`
:   Reine Text-Wiedergabe des Dateiinhalts, sofern dieser in Textform
    wiedergegeben werden kann.
    Typ: String.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.

`accessUrl`
:   URL zum allgemeinen Zugriff auf die Datei. Näheres unter [Dateizugriff](#dateizugriff).
    Typ: URL.
    Kardinalität: 1.
    ZWINGEND.

`downloadUrl`
:   URL zum Download der Datei. Näheres unter [Dateizugriff](#dateizugriff).
    Typ: URL.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.

`paper`
:   Falls die Datei zu einer Drucksache (`oparl:Paper`) gehört, MUSS über diese Eigenschaft die
    URL des Drucksache-Objekts ausgegeben werden.
    vorhanden sein.
    Typ: `oparl:Paper`.
    Kardinalität: 0 bis *.
    EMPFOHLEN.

`meeting`
:   Falls die Datei zu einer Sitzung (`oparl:Meeting`) gehört, MUSS über diese Eigenschaft
    die URL des Sitzung-Objekts ausgegeben werden.
    Typ: `oparl:Meeting`.
    Kardinalität: 0 bis *.
    EMPFOHLEN.

`masterDocument`
:   Datei, von der das aktuelle Objekt abgeleitet wurde. Details dazu in der
    allgemeinen Beschreibung weiter oben.
    Typ: `oparl:File`.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`derivativeDocument`
:   Datei, die von dem aktuellen Objekt abgeleitet wurde. Details dazu in der
    allgemeinen Beschreibung weiter oben.
    TODO: invers zu `masterDocument`. Von der Verwendung
    wird deshalb in der `prov`-Spezifikation abgeraten^[<http://www.w3.org/TR/prov-o/#inverse-names>].
    Typ: `oparl:File`.
    Kardinalität: 0 bis *.
    OPTIONAL.

`license`
:   Lizenz, unter der die Datei angeboten wird. Wenn diese Eigenschaft verwendet
    wird, dann ist sie anstelle einer globalen Angabe im übergeordneten
    `oparl:Body`- bzw. `oparl:System`-Objekt maßgeblich.^[vgl. [license](#eigenschaft_license)]
    Typ: URL.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`documentRole`
:   Rolle, Funktion, Sorte des Dokuments in Bezug auf eine Sitzung. Die Eigenschaft
    SOLL entsprechend nur in Verbindung mit der Eigenschaft `meeting` gesetzt sein.
    Siehe dazu [Vokabulare zur Klassifizierung](#vokabulare_klassifizierung).
    Typ: `skos:Concept`.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`keyword`
:   Schlagwort. Hat allgemeinere Bedeutung als `documentRole`.
    Siehe dazu [Vokabulare zur Klassifizierung](#vokabulare_klassifizierung).
    Typ: `skos:Concept`.
    Kardinalität: 0 bis *.
    OPTIONAL.
