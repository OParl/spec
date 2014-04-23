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

Ein Beispiel:

~~~~~  {#oparlbody_ex1 .json}
{
    "@type": "http://oparl.org/schema/1.0/Body",
    "@id": "http://oparl.beispielris.de/bodies/0",
    "system": "http://oparl.beispielris.de/",
    "contactEmail": "mailto:ris@beispielstadt.de",
    "contactName": "RIS-Betreuung",
    "rgs": "053150000000",
    "sameAs": [
        "http://d-nb.info/gnd/2015732-0",
        "http://dbpedia.org/resource/Cologne"
    ],
    "name": "Stadt K\u00f6ln",
    "nameLong": "Stadt K\u00f6ln, kreisfreie Stadt",
    "wwwUrl": "http://www.beispielstadt.de/",
    "organizations": "http://oparl.beispielris.de/bodies/0/organisations/",
    "meetings": "http://oparl.beispielris.de/bodies/0/meetings/",
    "papers": "http://oparl.beispielris.de/bodies/0/papers/",
    "people": "http://oparl.beispielris.de/bodies/0/people/",
    "created": "2014-01-08T14:28:31.568+0100",
    "lastModified": "2014-01-08T14:28:31.568+0100"
}
~~~~~

Vom OParl-Server wird erwartet, dass er mindestens
ein Objekt vom Typ `oparl:Body` bereit hält. Teilen sich mehrere Körperschaften
das selbe technische System, können auf demselben Server auch mehrere
Objekte vom Typ `oparl:Body` beherbergt werden.

Über die Zuordnung zu einem bestimmten `oparl:Body` Objekt zeigen andere
Objekte, wie beispielsweise Gremien oder Drucksachen, ihre Zugehörigkeit
zu einer bestimmten Körperschaft und damit implizit zu einem bestimmten
Parlament an.

### Eigenschaften

`system`
:   URL des Objekts vom Typ `oparl:System` Objekts, zu dem dieses Objekt gehört. 
    Diese Eigenschaft ist ZWINGEND.

`name`
:   Gibt den gebräuchlichen Namen der Körperschaft an.
    Diese Eigenschaft ist ZWINGEND.

`nameLong`
:   Kann bei Bedarf dazu verwendet werden, eine längere Form des 
    Namens der Körperschaft anzugeben. Diese Eigenschaft ist OPTIONAL.

`wwwUrl`
:   Dient der Angabe der WWW-URL der Körperschaft.
    Diese Eigenschaft ist EMPFOHLEN.

`rgs`
:   Regionalschlüssel der Körperschaft als zwölfstellige Zeichenkette^[Regionalschlüssel können im [Gemeindeverzeichnis (GV-ISys) des Statistischen Bundesamtes](https://www.destatis.de/DE/ZahlenFakten/LaenderRegionen/Regionales/Gemeindeverzeichnis/Gemeindeverzeichnis.html) eingesehen werden].
    Diese Eigenschaft ist EMPFOHLEN.

`sameAs`
:   Dient der Angabe beliebig vieler zusätzlicher URLs, die die Körperschaft
    repräsentieren. Diese Eigenschaft ist EMPFOHLEN. Hier können Beispielsweise,
    sofern vorhanden, der entpsrechende Eintrag der Gemeinsamen Normdatei der Deutschen Nationalbibliothek^[Gemeinsame Normdatei <http://www.dnb.de/gnd>],
    der DBPedia^[DBPedia <http://www.dbpedia.org/>] oder der Wikipedia^[Wikipedia <http://de.wikipedia.org/>] angegeben werden.

`contactEmail`
:   Dient der Angabe einer Kontakt-E-Mail-Adresse mit "mailto:"-Schema. Diese Eigenschaft
    ist EMPFOHLEN. Die Adresse soll die Kontaktaufnahme zu einer für die Körperschaft
    und idealerweise das parlamentarische Informationssystem zuständigen Stelle
    ermöglichen.

`contactName`
:   Name oder Bezeichnung der mit `contactEmail` erreichbaren Stelle. OPTIONAL.

`papers`
:   URL, unter welcher die API die Liste aller Objekte vom Typ `oparl:Paper`,
    also die Drucksachen unter dieser Körperschaft ausgibt.
    Diese Eigenschaft ist ZWINGEND.

`people`
:   URL, unter welcher die API die Liste aller Objekte vom Typ `oparl:Person`,
    also die Personen unter dieser Körperschaft ausgibt.
    Diese Eigenschaft ist ZWINGEND.

`meetings`
:   URL, unter welcher die API die Liste aller Objekte vom Typ `oparl:Meeting`,
    also die Sitzungen dieser Körperschaft ausgibt.
    Diese Eigenschaft ist ZWINGEND.

`organizations`
:   URL, unter welcher die API die Liste aller Objekte vom Typ `oparl:Organization`,
    also die Gruppierungen dieser Körperschaft ausgibt.
    Diese Eigenschaft ist ZWINGEND.

`created`
:   Datum/Uhrzeit der Erzeugung des Objekts. EMPFOHLEN.

`lastModified`
:   Datum/Uhrzeit der letzten Bearbeitung des Objekts. EMPFOHLEN.
