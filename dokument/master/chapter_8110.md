OParlDocument (Dokument)
------------------------

Ein Dokument hält die Metadaten einer Datei vor, beispielsweise einer 
PDF-Datei, eines RTF- oder Word-Dokuments.

Wird von einem Word-Dokument eine PDF-Ableitung hinterlegt, ist diese 
Ableitung ebenfalls ein Dokument. Um zu zeigen, dass es sich um eine Ableitung
handelt, verweist dieses auf das Original als "Master".

Im Unterschied zur Drucksache benötigt das Dokument keine nutzerfreundliche 
Kennung.

![Objekttyp Dokument](images/datenmodell_dokument.png)

### Eigenschaften ###
Schlüssel (`id`)
:   Unveränderliche Kennung
Name (`name`)
:   Dateiname, z.B. "12345.pdf"
Dateityp (`mime_type`)
:   Mime-Typ des Inhalts, z.B. "application/pdf"
Veröffentlichungsdatum (`date`)
:   Datum des Tages, an dem das Dokument ins System eingestellt wurde
Änderungsdatum und -uhrzeit (`last_modified`)
:   Datum und Uhrzeit der letzten Änderung des Dokuments
Prüfsumme (`sha1_checksum`)
:   SHA1-Prüfsumme des Dokumenteninhalts
URL (`url`)
:   URL zum Abruf der Daten dieses Dokuments mittels HTTP GET-Aufruf
Nur-Text-Version (`text`)
:   Reine Text-Wiedergabe des Dokumenteninhalts, sofern es sich nicht 
    um eine reine Abbildung handelt.


### Beziehungen ###

* Dokumente gehören zwingend zu einer **Drucksache**, optional auch zu 
mehreren. Ein Dokument kann entweder als Hauptdokument einer Drucksache oder 
als Anlage eingestuft sein.
* Ein Dokument kann auf ein anderes Dokument referenzieren, wenn es von dem 
anderen Dokument abstammt. So ist es möglich, von einem abgeleiteten Dokument 
zu seinem Dokumenten-Master zu gelangen (Beispiel: von einem PDF-Dokument zum 
OpenOffice-Original).

~~~~~  {#document_ex1 .json}
{
    "id": "3000",
    "name": "3000.pdf",
    "mime_type": "application/pdf",
    "date": "2013-01-04T07:54:13+01:00",
    "last_modified": "2013-01-04T07:54:13+01:00",
    "sha1_checksum": "da39a3ee5e6b4b0d3255bfef95601890afd80709",
    "url": "http://ris.beispielstadt.de/api/documents/3000.pdf",
    "text": "Der Übersichtsplan zeigt alle Ebenen des ...",
    "master": "2099"
}
~~~~~


