oparl:Body (Körperschaft)   {#oparl_body}
------------------------

Der Objekttyp `oparl:Body` dient dazu, eine Körperschaft und damit ein
Parlament zu repräsentieren, zu dem der Server Informationen bereithält.
Eine Körperschaft kann beispielsweise eine Gemeinde, ein Landkreis oder 
ein kommunaler Zweckverband sein.

Hätte das System beispielsweise den Zweck, Informationen über das kommunale
Parlament der Stadt Köln, namentlich den Rat der Stadt Köln, abzubilden,
dann müsste dieses System dazu ein Objekt vom Typ `oparl:Body` führen, welches
die Stadt Köln repräsentiert.

Ein Kontext:

~~~~~  {#body_ex_context .json}
{
    "@language": "de",
    "license": {
        "@id": "dc:license",
        "@type": "@id"
    },
    "exactMatch": {
        "@id": "skos:exactMatch",
        "@type": "@id"
    },
    "licenseValidSinceDay": "2013-04-01T12:00:00+00:00"
}
~~~~~

Ein expandiertes Beispiel:

~~~~~  {#oparlbody_ex1 .json}
{
    "@type": "http://oparl.org/schema/1.0/Body",
    "@id": "https://oparl.beispielris.de/body/0",
    "system": "https://oparl.beispielris.de/",
    "contactEmail": "mailto:ris@beispielstadt.de",
    "contactName": "RIS-Betreuung",
    "rgs": "053150000000",
    "equivalentBody": [
        "http://d-nb.info/gnd/2015732-0",
        "http://dbpedia.org/resource/Cologne"
    ],
    "name": "Stadt Köln",
    "nameLong": {
        "de": "Stadt Köln, kreisfreie Stadt",
        "en": "City of Cologne"
    },
    "website": "http://www.beispielstadt.de/",
    "license": "http://creativecommons.org/licenses/by/4.0/",
    "licenseValidSinceDay": "2014-01-01",
    "organization": "https://oparl.beispielris.de/body/0/organisation/",
    "meeting": "https://oparl.beispielris.de/body/0/meeting/",
    "paper": "https://oparl.beispielris.de/body/0/paper/",
    "member": "https://oparl.beispielris.de/body/0/person/",
    "classification": "https://oparl.beispielris.de/vocab/landkreis",
    "created": "2014-01-08T14:28:31.568+0100",
    "modified": "2014-01-08T14:28:31.568+0100"
}
~~~~~

Vom OParl-Server wird erwartet, dass er mindestens
ein Objekt vom Typ `oparl:Body` bereit hält. Teilen sich mehrere Körperschaften
das selbe technische System, können auf demselben Server auch mehrere
Objekte vom Typ `oparl:Body` beherbergt werden.

Über die Zuordnung zu einem bestimmten `oparl:Body`-Objekt zeigen andere
Objekte, wie beispielsweise Gremien oder Drucksachen, ihre Zugehörigkeit
zu einer bestimmten Körperschaft und damit implizit zu einem bestimmten
Parlament an.

### Eigenschaften

`system`
:   System, zu dem dieses Objekt gehört.
    Typ: `oparl:System`.
    Kardinalität: 1.
    Die Eigenschaft ist ZWINGEND.

`name`
:   Gibt den gebräuchlichen Namen der Körperschaft an.
    Typ: Zeichenkette.
    Kardinalität: 1.
    Die Eigenschaft ist ZWINGEND.

`nameLong`
:   Kann bei Bedarf dazu verwendet werden, eine längere Form des 
    Namens der Körperschaft anzugeben.
    Typ: Zeichenkette.
    Kardinalität: 0 bis 1.
    Die Eigenschaft ist OPTIONAL.

`website`
:   Allgemeine Website der Körperschaft.
    Typ: URL.
    Kardinalität: 0 bis 1.
    Die Eigenschaft ist EMPFOHLEN.

`license`
:   Lizenz, die für die Daten, die über diese API abgerufen werden
    können, gilt, sofern nicht am einzelnen Objekt anders angegeben.
    Siehe dazu auch die übergreifende Beschreibung zur Eigenschaft
    [`license`](#eigenschaft_license).
    Typ: URL.
    Kardinalität: 0 bis 1.
    Die Eigenschaft ist EMPFOHLEN.

`licenseValidSinceDay`
:   Zeitpunkt, seit dem die unter `license` angegebene Lizenz gilt.
    Vorsicht bei Änderungen der Lizenz die zu restriktiveren Bedingungen führen.
    Typ: `xsd:DateTime`.
    Kardinalität: 0 bis 1.
    Die Eigenschaft ist EMPFOHLEN.

`rgs`
:   Regionalschlüssel der Körperschaft als zwölfstellige Zeichenkette^[Regionalschlüssel können im [Gemeindeverzeichnis (GV-ISys) des Statistischen Bundesamtes](https://www.destatis.de/DE/ZahlenFakten/LaenderRegionen/Regionales/Gemeindeverzeichnis/Gemeindeverzeichnis.html) eingesehen werden].
    Typ: Zeichenkette.
    Kardinalität: 0 bis 1.
    Die Eigenschaft ist EMPFOHLEN.

`equivalentBody`
:   Dient der Angabe beliebig vieler zusätzlicher URLs, die die selbe Körperschaft
    repräsentieren. Hier können beispielsweise,
    sofern vorhanden, der entsprechende Eintrag der Gemeinsamen Normdatei der Deutschen Nationalbibliothek^[Gemeinsame Normdatei <http://www.dnb.de/gnd>],
    der DBPedia^[DBPedia <http://www.dbpedia.org/>] oder der Wikipedia^[Wikipedia <http://de.wikipedia.org/>] angegeben werden.
    Typ: URL.
    Kardinalität: 0 bis *.
    Die Eigenschaft ist EMPFOHLEN.

`contactEmail`
:   Dient der Angabe einer Kontakt-E-Mail-Adresse mit "mailto:"-Schema.
    Die Adresse soll die Kontaktaufnahme zu einer für die Körperschaft
    und idealerweise das parlamentarische Informationssystem zuständigen Stelle
    ermöglichen.
    Typ: E-Mail-Adresse inklusive "mailto:".
    Kardinalität: 0 bis 1.
    Die Eigenschaft ist EMPFOHLEN.

`contactName`
:   Name oder Bezeichnung der mit `contactEmail` erreichbaren Stelle.
    Typ: String.
    Kardinalität: 0 bis 1.
    Die Eigenschaft ist OPTIONAL.

`paper`
:   Drucksachen unter dieser Körperschaft als Liste unter einer eigenen URL.
    Vgl. [Objektlisten](#objektlisten).
    Typ: `oparl:Paper`.
    Kardinalität: 0 bis *.
    Die Eigenschaft ist ZWINGEND.

`member`
:   Personen in dieser Körperschaft als Liste unter einer eigenen URL.
    Vgl. [Objektlisten](#objektlisten).
    Typ: `oparl:Person`.
    Kardinalität: 0 bis *.
    Die Eigenschaft ist ZWINGEND.

`meeting`
:   Sitzungen dieser Körperschaft als Liste unter einer eigenen URL.
    Vgl. [Objektlisten](#objektlisten).
    Typ: `oparl:Meeting`.
    Kardinalität: 0 bis *.
    Die Eigenschaft ist ZWINGEND.

`organization`
:   Gruppierung in dieser Körperschaft als Liste unter einer eigenen URL.
    Vgl. [Objektlisten](#objektlisten).
    Typ: `oparl:Organization`.
    Kardinalität: 0 bis *.
    Die Eigenschaft ist ZWINGEND.

`keyword`
:   Schlagwort(e). Vgl. [Vokabulare zur Klassifizierung](#vokabulare_klassifizierung).
    Typ: `skos:Concept`.
    Kardinalität: 0 bis *.
    Die Eigenschaft ist OPTIONAL.

`allConcepts`
:   Alle Schlagworte und Begriffe, die von dieser Körperschaft verwendet werden.
    Diese Eigenschaft ist insbesondere dann
    wichtig, wenn Sortierungs-Reihenfolgen verwendet werden.
    Typ: `skos:Concept`.
    Kardinalität: 0 bis *.
    Die Eigenschaft ist OPTIONAL.

`created`
:   Datum/Uhrzeit der Erzeugung des Objekts.
    Typ: `xsd:DateTime`.
    Kardinalität: 0 bis 1.
    Die Eigenschaft ist EMPFOHLEN.

`lastModified`
:   Datum/Uhrzeit der letzten Bearbeitung des Objekts.
    Typ: `xsd:DateTime`.
    Kardinalität: 0 bis 1.
    Die Eigenschaft ist EMPFOHLEN.

TODO: Beispiel zu `allConcepts` einfügen.
