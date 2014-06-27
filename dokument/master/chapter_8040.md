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

Vom OParl-Server wird erwartet, dass er mindestens
ein Objekt vom Typ `oparl:Body` bereit hält. Teilen sich mehrere Körperschaften
das selbe technische System, können auf demselben Server auch mehrere
Objekte vom Typ `oparl:Body` beherbergt werden.

Über die Zuordnung zu einem bestimmten `oparl:Body`-Objekt zeigen andere
Objekte, wie beispielsweise Gremien oder Drucksachen, ihre Zugehörigkeit
zu einer bestimmten Körperschaft und damit implizit zu einem bestimmten
Parlament an.

**Beispiel**

~~~~~  {#oparlbody_ex1 .json}
{
    "id": "https://oparl.example.org/body/0",
    "type": "http://oparl.org/schema/1.0/Body",
    "system": "https://oparl.example.org/",
    "contactEmail": "mailto:ris@beispielstadt.de",
    "contactName": "RIS-Betreuung",
    "rgs": "053150000000",
    "equivalentBody": [
        "http://d-nb.info/gnd/2015732-0",
        "http://dbpedia.org/resource/Cologne"
    ],
    "shortName": "Stadt Köln",
    "name": {
        "de": "Stadt Köln, kreisfreie Stadt",
        "en": "City of Cologne"
    },
    "website": "http://www.beispielstadt.de/",
    "license": "http://creativecommons.org/licenses/by/4.0/",
    "licenseValidSince": "2014-01-01",
    "organization": "https://oparl.example.org/body/0/organizations/",
    "meeting": "https://oparl.example.org/body/0/meetings/",
    "paper": "https://oparl.example.org/body/0/papers/",
    "member": "https://oparl.example.org/body/0/people/",
    "legislativeTerm": "https://oparl.example.org/body/0/terms/",
    "classification": "https://oparl.example.org/vocab/landkreis",
    "created": "2014-01-08T14:28:31.568+0100",
    "modified": "2014-01-08T14:28:31.568+0100"
}
~~~~~


### Eigenschaften

`system`
:   System, zu dem dieses Objekt gehört.
    Typ: URL des `oparl:System` Objekts.
    Kardinalität: 1.
    ZWINGEND.

`shortName`
:   Kurzer Name der Körperschaft.
    Typ: Datentyp `xsd:string`.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.

`name`
:   Der offizielle lange Name der Körperschaft.
    Typ: Datentyp `xsd:string`.
    Kardinalität: 1.
    ZWINGEND.

`website`
:   Allgemeine Website der Körperschaft.
    Typ: URL.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.

`license`
:   Lizenz, die für die Daten, die über diese API abgerufen werden
    können, gilt, sofern nicht am einzelnen Objekt anders angegeben.
    Siehe dazu auch die übergreifende Beschreibung zur Eigenschaft
    [`license`](#eigenschaft_license).
    Typ: URL.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.

`licenseValidSince`
:   Zeitpunkt, seit dem die unter `license` angegebene Lizenz gilt.
    Vorsicht bei Änderungen der Lizenz die zu restriktiveren Bedingungen führen.
    Typ: `xsd:Date`.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.

`rgs`
:   Regionalschlüssel der Körperschaft als zwölfstellige Zeichenkette^[Regionalschlüssel können im [Gemeindeverzeichnis (GV-ISys) des Statistischen Bundesamtes](https://www.destatis.de/DE/ZahlenFakten/LaenderRegionen/Regionales/Gemeindeverzeichnis/Gemeindeverzeichnis.html) eingesehen werden].
    Typ: String.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.

`equivalentBody`
:   Dient der Angabe beliebig vieler zusätzlicher URLs, die die selbe Körperschaft
    repräsentieren. Hier können beispielsweise,
    sofern vorhanden, der entsprechende Eintrag der Gemeinsamen Normdatei der Deutschen Nationalbibliothek^[Gemeinsame Normdatei <http://www.dnb.de/gnd>],
    der DBPedia^[DBPedia <http://www.dbpedia.org/>] oder der Wikipedia^[Wikipedia <http://de.wikipedia.org/>] angegeben werden.
    Typ: Array mit URLs.
    Kardinalität: 0 bis *.
    EMPFOHLEN.

`contactEmail`
:   Dient der Angabe einer Kontakt-E-Mail-Adresse mit "mailto:"-Schema.
    Die Adresse soll die Kontaktaufnahme zu einer für die Körperschaft
    und idealerweise das parlamentarische Informationssystem zuständigen Stelle
    ermöglichen.
    Typ: E-Mail-Adresse inklusive "mailto:".
    Kardinalität: 0 bis 1.
    EMPFOHLEN.

`contactName`
:   Name oder Bezeichnung der mit `contactEmail` erreichbaren Stelle.
    Typ: String.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`paper`
:   Drucksacheen unter dieser Körperschaft. Vgl. [Objektlisten](#objektlisten).
    Typ: Liste von `oparl:Paper` Objekten.
    Kardinalität: 0 bis *.
    ZWINGEND.

`member`
:   Personen in dieser Körperschaft. Vgl. [Objektlisten](#objektlisten).
    Typ: Liste von `oparl:Person` Objekten.
    Kardinalität: 0 bis *.
    ZWINGEND.

`meeting`
:   Sitzungen dieser Körperschaft. Vgl. [Objektlisten](#objektlisten).
    Typ: Liste von `oparl:Meeting` Objekten.
    Kardinalität: 0 bis *.
    ZWINGEND.

`organization`
:   Gruppierungen in dieser Körperschaft. Vgl. [Objektlisten](#objektlisten).
    Typ: Liste von `oparl:Organization` Objekten.
    Kardinalität: 0 bis *.
    ZWINGEND.

`legislativeTerm`
:   Wahlperioden in dieser Körperschaft. Vgl. [Objektlisten](#objektlisten).
    Typ: Liste von `oparl:LegislativeTerm` Objekten.
    Kardinalität: 0 bis *.
    EMPFOHLEN.

`keyword`
:   Schlagwort(e). Vgl. [Vokabulare zur Klassifizierung](#vokabulare_klassifizierung).
    Typ: Array mit Strings oder URLs zu `skos:Concept` Objekten.
    Kardinalität: 0 bis *.
    OPTIONAL.

`created`
:   Datum/Uhrzeit der Erzeugung des Objekts.
    Typ: `xsd:dateTime`.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.

`modified`
:   Datum/Uhrzeit der letzten Bearbeitung des Objekts.
    Typ: `xsd:dateTime`.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.
