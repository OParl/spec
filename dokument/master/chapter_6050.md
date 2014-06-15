Benannte und anonyme Objekte  {#benannte_anonyme_objekte}
----------------------------

Die JSON-LD-Spezifikation unterscheidet zwischen benannten und anonymen
Objekten. Da die Unterscheidung auch für OParl von Bedeutung ist, wird
sie hier genauer erläutert.

### Benannte Objekte  {#benannte_objekte}

Benannte Objekte sind innerhalb einer JSON-LD-Ausgabe diejenigen Objekte,
die durch eine eigene URL identifiziert werden. Als Beispiel dient ein
fiktives Objekt, das ein Client über die URL

    https://oparl.example.org/bodies/0/committees/1

abruft:

~~~~~  {#benanntanonym_ex1 .json}
{
    "@id": "https://oparl.example.org/bodies/0/committees/1",
    "@type": "http://oparl.org/schema/1.0/committee",
    "name": "Hauptausschuss"
}
~~~~~

Das Objekt enthält eine Eigenschaft `@id` mit der URL des Objekts
als Wert.

Das benannte Objekt kann über seine URL sowohl eindeutig identifiziert
als auch direkt abgerufen werden.

### Anonyme Objekte (Blank Nodes) {#anonyme_objekte}

Im Gegensatz dazu können Objekte existieren, die keine eigene URL haben.
Solche Objekte werden über die Werte von Eigenschaften anderer Objekte
ausgegeben.

Ein Beispiel dafür ist die Eigenschaft `location` innerhalb einer
Drucksache (`oparl:Paper):

~~~~~  {#benanntanonym_ex2 .json}
{
    "@context": "https://oparl.example.org/Pfad/zum/Kontext/oparl.jsonld",
    "@type": "oparl:Paper",
    "@id": "https://oparl.example.org/paper/749",
    "body": "beispielris:bodies/1",
    "name": "Antwort auf Anfrage 1200/2014",
    "reference": "1234/2014",
    "location": [
        {
            "description": "Theodor-Heuss-Ring 1",
            "geometry": "POINT(7.148  50.023)"
        }
    ],
    ...
}
~~~~~

Die Eigenschaft `location` ist eine Liste mit einem oder mehreren
Objekten vom Typ `oparl:Location`. Diese Objekte spiegeln wieder, mit welchen
Orten sich eine Drucksache befasst.

Die einzelnen `location`-Objekte innerhalb der Liste haben keine
`@id`-Eigenschaft, daher handelt es sich dabei um anonyme Objekte,
auch *Blank Nodes* genannt. Diese Objekte können nicht einzeln, sondern
nur im Kontext verbundener Objekte, wie hier im Beispiel im Kontext einer
Drucksache, abgerufen werden.

Wenn solche Blank Nodes im Semantic Web verwendet werden, dann führen sie
zu erheblichen Problemen. Sandro Hawke (W3C) hat diese so zusammengefasst:

    In general, blank nodes are a convenience for the content
    provider and a burden on the content consumer. Higher quality
    data feeds use fewer blank nodes, or none. Instead, they have
    a clear concept of identity and service for every entity in 
    their data.

    If someone in the middle tries to convert (Skolemize) blank 
    nodes, it’s a large burden on them. Specifically, they should
    provide web service for those new URIs, and if they get updated
    data from their sources, they’re going to have a very hard
    [perhaps impossible] time understanding what really changed.
^[Zitiert nach
<http://richard.cyganiak.de/blog/2011/03/blank-nodes-considered-harmful/>]

Ein Ziel bei der Entwicklung der Spezifikation war es, möglichst wenige
Blank Nodes zu erzeugen. Zukünftige Versionen können hier sicherlich noch einen
weiteren Beitrag leisten.
