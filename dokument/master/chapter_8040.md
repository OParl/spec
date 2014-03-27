oparl:Body (Körperschaft)
------------------------

Dieser Objekttyp erlaubt es, eine Körperschaft abzbilden. Eine Körperschaft
kann beispielsweise eine Gemeinde, ein Landkreis oder ein Zweckverband sein.

Von einem funktionsfähigen Server wird erwartet, dass er mindestens
ein Objekt vom Typ `oparl:Body` bereit hält. Teilen sich mehrere Körperschaften
das selbe technische System, können auf demselben Server auch mehrere
Objekte vom Typ `oparl:Body` beherbergt werden.

Über die Zuordnung zu einem bestimmten `oparl:Body` Objekt zeigen andere
Objekte, wie beispielsweise Gremien oder Drucksachen, ihre Zugehörigkeit
zu einer bestimmten Körperschaft an.

Es werden mehrere Eigenschaften angeboten, die dazu dienen, die real
existierende Körperschaft, die von einem `oparl:Body` Objekt repräsentiert
wird, programmatisch auslesbar zu machen zu können. Insbesondere sind hier
die Eigenschaften `url`, `rgs` und `gnd_url` zu nennen.

### Eigenschaft `system`

Diese Eigenschaft ist ZWINGEND.

Mit dieser Eigenschaft wird das Objekt dem übergeordneten `oparl:System` Objekt zugeordnet. Wert MUSS der IRI des `oparl:System` Objekts sein.

### Eigenschaft `name`

Diese Eigenschaft ist ZWINGEND. Sie transportiert den gebräuchlichen Namen der Körperschaft.

### Eigenschaft `name_long`

Diese Eigenschaft ist OPTIONAL und kann bei Bedarf dazu verwendet werden, eine längere Form
des Namens der Körperschaft wieder zu geben, sofern dieser für die Eigenschaft `name` zu lang
ist.

### Eigenschaft `url`

Diese Eigenschaft ist EMPFOHLEN.

Mit dieser Eigenschaft SOLL die URL der offiziellen Website der Körperschaft
ausgegeben werden.

TODO: Beschreibung

### Eigenschaft `rgs`

Diese Eigenschaft ist EMPFOHLEN.

Handelt es sich bei der Körperschaft um eine Gebietskörperschaft
(Landkreis, Kommune etc.) in Deutschland, SOLL für die eindeutige
Identifizierung der amtliche Regionalschlüssel verwendet werden.^[Regionalschlüssel können im [Gemeindeverzeichnis (GV-ISys) des Statistischen Bundesamtes](https://www.destatis.de/DE/ZahlenFakten/LaenderRegionen/Regionales/Gemeindeverzeichnis/Gemeindeverzeichnis.html) eingesehen werden]
Dieser ist grundsätzlich zwölfstellig.

### Eigenschaft `gnd_url`

Diese Eigenschaft ist EMPFOHLEN.

Sofern die Körperschaft in der GND^[Gemeinsame Normdatei <http://www.dnb.de/gnd>] vertreten ist, SOLL diese Eigenschaft
als Wert die URL des Eintrags in der GND enthalten.

### Eigenschaft `contact`

Diese Eigenschaft ist EMPFOHLEN.

Über diese Eigenschafte SOLLEN Kontaktinformationen zu einer Stelle bereit
gestellt werden, die die inhaltliche Verantwortung für sämtliche zu dieser
Körperschaft gehörenden Inhalte im System trägt. Besonders wichtig ist diese
Angabe, wenn auf einem System mehrere Körperschaften vertreten sind und damit
auf der Ebene des `oparl:System` Objekts ein rein technischer Kontakt ausgegeben
wird, der nicht für inhaltliche Fragestellungen im Zuständigkeitsbereich der
jeweiligen Körperschaften kontaktiert werden sollte.

### Eigenschaft `papers`

Diese Eigenschaft ist ZWINGEND.

Wert dieser Eigenschaft ist die URL der API zum Aufruf einer Liste der
Drucksachen (Objekte vom Typ `oparl:Paper`) für diese Körperschaft.

### Eigenschaft `people`

Diese Eigenschaft ist ZWINGEND.

Wert dieser Eigenschaft ist die URL der API zum Aufruf einer Liste der
Personen (Objekte vom Typ `oparl:Person`) für diese Körperschaft.

### Eigenschaft `meetings`

Diese Eigenschaft ist ZWINGEND.

Wert dieser Eigenschaft ist die URL der API zum Aufruf einer Liste der
Sitzungen (Objekte vom Typ `oparl:Meeting`) für diese Körperschaft.

### Eigenschaft `committees`

Diese Eigenschaft ist ZWINGEND.

Wert dieser Eigenschaft ist die URL der API zum Aufruf einer Liste der
Gremien (Objekte vom Typ `oparl:Committee`) für diese Körperschaft.


### Beispiel

~~~~~  {#oparlbody_ex1 .json}
{
    "@id": "http://refserv.oparl.org/bodies/0",
    "@context": "http://oparl.org/schema/1.0/Body",
    "committees": "http://refserv.oparl.org/bodies/0/committees/",
    "contact": {
        "email": "ris@stadt-koeln.de",
        "name": "RIS-Betreuung"
    }, 
    "created": "2014-01-08T14:28:31.568+0100",
    "gnd_url": "http://d-nb.info/gnd/2015732-0",
    "last_modified": "2014-01-08T14:28:31.568+0100",
    "meetings": "http://refserv.oparl.org/bodies/0/meetings/",
    "name": "Stadt K\u00f6ln",
    "name_long": "Stadt K\u00f6ln, kreisfreie Stadt",
    "organisations": "http://refserv.oparl.org/bodies/0/organisations/",
    "papers": "http://refserv.oparl.org/bodies/0/papers/",
    "people": "http://refserv.oparl.org/bodies/0/people/",
    "rgs": "053150000000",
    "system": "http://refserv.oparl.org/",
    "url": "http://www.stadt-koeln.de/"
}
~~~~~

