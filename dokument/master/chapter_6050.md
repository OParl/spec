Benannte und anonyme Objekte
----------------------------

Die JSON-LD-Spezifikation unterscheidet zwischen benannten und anonymen
Objekten. Da die Unterscheidung auch für OParl von Bedeutung ist, wird
sie hier genauer erläutert.

### Benannte Objekte

Benannte Objekte sind innerhalb einer JSON-LD-Ausgabe diejenigen Objekte,
die durch eine eigene URL identifiziert werden. Als Beispiel dient ein
fiktives Objekt, das ein Client über die URL

    http://refserv.oparl.org/bodies/0/committees/1

abruft:

~~~~~  {#benanntanonym_ex1 .json}
{
    "@id": "http://refserv.oparl.org/bodies/0/committees/1",
    "@type": "http://oparl.org/schema/1.0/committee",
    "name": "Hauptausschuss"
}
~~~~~

Das Objekt enthält eine Eigenschaft `@id` mit der URL des Objekts
als Wert.

Das benannte Objekt kann über seine URL sowohl eindeutig identifiziert
als auch direkt abgerufen werden.

### Anonyme Objekte (Blank Nodes)

Im Gegensatz dazu können Objekte existieren, die keine eigene URL haben.
Ein Beispiel dafür findet sich in der Beratungsfolge einer Drucksache.

Das nachfolgende Beispiel zeigt eine Drucksache, deren Beratungsfolge
über die Eigenschaft `consultations` kodiert ist.

TODO: Nachstehendes Beispiel und Text dazu auf stimmiges Paper Objekt
umschreiben.

~~~~~  {#benanntanonym_ex2 .json}
{
    "@id": "http://refserv.oparl.org/bodies/0/papers/456",
    "@type": "http://oparl.org/schema/1.0/paper",
    "title": "Beschlussvorlage zur Jugendförderung",
    "consultations": [
    	{
    		"@type": "http://oparl.org/schema/1.0/consultation",
    		"committee": "http://refserv.oparl.org/bodies/0/committees/1",
    		"meeting": "http://refserv.oparl.org/bodies/0/committees/1/meetings/123",
    		"agendaitem": "7.2.4",
    		"authoritative": false
    	},
    	{
    		...
    	}
    ]
}
~~~~~

Die Eigenschaft `consultations` ist eine Liste mit einem oder mehreren
Objekten vom Typ `consultation`. Diese Objekte spiegeln wieder, in welchen 
Sitzungen die vorliegende Drucksache beraten wurde bzw. wird.

Die einzelnen `consultation`-Objekte haben keine `@id`-Eigenschaft, daher
handelt es sich dabei um anonyme Objekte, auch *Blank Nodes* genannt. Diese
Objekte können nicht einzeln, sondern nur im Kontext verbundener Objekte, wie
hier im Beispiel im Kontext einer Drucksache, abgerufen werden.

TODO: Weitere Objekttypen nennen, in denen Blank Nodes vorkommen.
