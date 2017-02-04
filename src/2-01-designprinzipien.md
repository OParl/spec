## Designprinzipien {#designprinzipien}

### Aufbauen auf gängiger Praxis {#aufbauen-auf-gaengiger-praxis}

Grundlage für die Erarbeitung der OParl-Spezifikation in der vorliegenden Version
ist eine Analyse von aktuell (2012 bis 2016) in Deutschland etablierten
parlamentarischen Informationssystemen und ihrer Nutzung. Erklärtes Ziel für diese erste
Version ist es, mit möglichst geringem Entwicklungsaufwand auf Seite der Softwareanbieter und
ebenso geringem Migrationsaufwand auf Seite der Betreiber zu einer Bereitstellung von parlamentarischen
Informationen über eine OParl-API zu gelangen. Hierbei war es von entscheidender
Bedeutung, dass sich die Informationsmodelle der einschlägigen Softwareprodukte stark
ähneln. Für die OParl-Spezifikation wurde sozusagen ein Datenmodell als "gemeinsamer Nenner"
auf Basis der gängigen Praxis konstruiert.

### Verbesserung gegenüber dem Status Quo wo möglich {#verbesserung-gegenueber-status-quo}

Dort, wo es dem Ziel der einfachen Implementierbarkeit und der einfachen Migration
nicht im Weg steht, erlauben sich die Autoren dieser Spezifikation, auch Funktionen
aufzunehmen, die noch nicht als gängige Praxis im Bereich der Ratsinformationssysteme
bezeichnet werden können oder welche nur von einzelnen Systemen unterstützt werden.
Solche Funktionen sind dann so integriert, dass sie nicht als zwingende Anforderung
gelten.

Ein Beispiel für eine derartige Funktion ist die Abbildung von Geodaten im Kontext von
Drucksachen (`oparl:Paper`), um beispielsweise die Lage eines Bauvorhabens, das in
einer Beschlussvorlage behandelt wird, zu beschreiben. Zwar ist den Autoren nur ein
einziges parlamentarisches Informationssystem^[Das Ratsinformationssystem BoRis, eine
Eigenentwicklung der Stadt Bonn <http://www2.bonn.de/bo_ris/ris_sql/agm_index.asp>]
in Deutschland bekannt, das
Geoinformationen – und zwar in Form von Punktdaten, also einer Kombination aus
Längen- und Breitengradangaben – mit Dokumenten verknüpft. Der Vorteil dieser
Funktion ist jedoch anhand zahlreicher Anwendungsszenarien, wie z.B. dem Bauinformationssystem "Bürger baut Stadt"^[bürgerbautstadt, <http://www.buergerbautstadt.de>], belegbar. Somit ist in der
vorliegenden OParl-Spezifikation die Möglichkeit beschrieben, Geodaten-Objekte
einzubetten.

Die Angabe eines einzelnen Punktes ist dabei der einfachste Fall. Die
Spezifikation erlaubt auch die Kodierung von mehreren Objekten, die Punkte,
Linien oder Polygone repräsentieren können. Vgl. dazu `oparl:Location`.

Auch die Ausgabe einer Nur-Text-Version im Kontext der Datei (`oparl:File`),
das den barrierefreien Zugriff auf Inhalte oder Indexierung für Volltextsuchfunktionen
deutlich vereinfacht, ist eine Möglichkeit, die in der gängigen Praxis noch nicht zu
finden ist. Ebenso die Möglichkeit, Beziehungen zwischen einzelnen Dateien
herzustellen, um so z.B. von einer Datei zu anderen Dateien mit identischem
Inhalt, aber in anderen technischen Formaten zu verweisen, etwa von einer
ODT-Datei zu einer PDF-Version.

### Selbstbeschreibungsfähigkeit {#selbstbeschreibungsfaehigkeit}

Ausgaben des Servers sollten so beschaffen sein, dass sie für menschliche Nutzerinnen
weitgehend selbsterklärend sein können. Dies betrifft besonders die Benennung von
Objekten und Objekteigenschaften.

Um den Kreis der Entwicklerinnen und Entwickler, die mit einer OParl-API
arbeiten können, nicht unnötig einzuschränken, wird hierbei grundsätzlich und
soweit sinnvoll auf englischsprachige Begrifflichkeiten gesetzt.

### Erweiterbarkeit {#erweiterbarkeit}

Implementierer sollen in der Lage sein, über eine OParl-konforme Schnittstelle auch
solche Informationen auszugeben, die nicht im Rahmen des OParl-Schemas abgebildet werden
können. Dies bedeutet zum einen, dass ein System Objekttypen unterstützen und ausliefern
darf, die nicht (oder noch nicht) im OParl-Schema beschrieben sind. Das bedeutet auch,
dass Objekttypen so um eigene Eigenschaften erweitert werden können, die nicht im OParl
Schema beschrieben sind.

Ein weiterer Aspekt betrifft die Abwärtskompatibilität, also die Kompatibilität von
OParl-Clients mit zukünftigen Schnittstellen. So können beispielsweise zukünftige Erweiterungen
des OParl-Schemas, etwa um neue Objekttypen, genauso durchgeführt werden, wie die Erweiterungen
um herstellerspezifische Objekttypen. Ein Client muss diese Anteile nicht auswerten, sofern
sie nicht für die Aufgabe des Clients relevant sind. Es bedeutet im Umkehrschluss allerdings auch, dass ein Client
nicht fehlschlagen darf, falls derartige Erweiterungen vorhanden sind.


### Browseability/Verlinkung {#browseability_verlinkung}

Klassische Webservice-Schnittstellen erfordern von den Entwicklern vollständige Kenntnis
der angebotenen Einstiegspunkte und Zugriffsmethoden, gepaart mit sämtlichen unterstützten
URL-Parametern, um den vollen Funktionsumfang der Schnittstelle ausschöpfen zu können.

Parlamentarische Informationen sind weitgehend in Form von Graphen aufgebaut. Das bedeutet, dass
Objekte häufig mit einer Vielzahl anderer Objekte verknüpft sind. So ist eine Person
beispielsweise Mitglied in mehreren Gremien, das Gremium hat mehrere Sitzungen abgehalten
und zu diesen Sitzungen gibt es jeweils zahlreiche Drucksachen, die ihrerseits wieder
zahlreiche Dokumente enthalten.

Eine OParl-Schnittstelle gibt jedem einzelnen Objekt eine eindeutige Adresse, eine URL.
Somit kann die Schnittstelle den Verweis von einem Objekt, beispielsweise einem Gremium,
auf ein anderes Objekt, etwa ein Mitglied des Gremiums, dadurch ausgeben, dass im Kontext
des Gremiums die URL des Mitglieds ausgeben wird. Der Client kann somit ausgehend von einem
bestimmten Objekt die zugehörigen Objekte im System finden, indem er einfach den angebotenen
URLs folgt. Dieses Prinzip wird auch "Follow Your Nose"^[<http://patterns.dataincubator.org/book/follow-your-nose.html>] genannt.
