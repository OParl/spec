Designprinzipien
----------------

### Aufbauen auf gängiger Praxis

Grundlage für die Erarbeitung der OParl-Spezifikation in der vorliegenden Version
ist eine Analyse von aktuell (2012 bis 2014) in Deutschland etablierten
parlamentarischen Informationssystemen und ihrer Nutzung. Erklärtes Ziel für diese erste
Version ist es, mit möglichst geringem Entwicklungsaufwand auf Seite der Softwareanbieter und 
Migrationsaufwand auf Seite der Betreiber zu einer Bereitstellung von parlamentarischen 
Informationen über eine OParl-API zu gelangen. Hierbei war es von entscheidender 
Bedeutung, dass sich die Informationsmodelle der einschlägigen Softwareprodukte stark
ähneln. Für die OParl-Spezifikation wurde sozusagen ein Datenmodell als "gemeinsamer Nenner"
auf Basis der gängigen Praxis beschrieben.

### Verbesserung gegenüber dem Status Quo wo möglich

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
Funktion ist jedoch anhand zahlreicher Anwendungsszenarien belegbar. Somit ist der
vorliegenden OParl-Spezifikation die Möglichkeit beschrieben, Geodaten-Objekte
einzubetten.

Die Angabe eines einzelnen Punktes ist dabei nur ein einfacher Sonderfall. Die
Spezifikation erlaubt auch die Kodierung von mehreren Objekten, die Punkte, Linien
oder Polygone repräsentieren können. Vgl. dazu `oparl:Location`.

Auch die Ausgabe einer Nur-Text-Version im Kontext des Dokuments (`oparl:File`),
das den barrierefreien Zugriff auf Inhalte oder Indexierung für Volltextsuchfunktionen
deutlich vereinfacht, ist eine Möglichkeit, die in der gängigen Praxis noch nicht zu
finden ist. Ebenso die Möglichkeit, Beziehungen zwischen einzelnen Dokumenten
herzustellen, um so von einem Dokument zu anderen Dokumenten mit identischem Inhalt,
aber in anderen technischen Formaten zu verweisen, etwa von einer ODT-Datei zu einer
PDF-Version.

### RESTful  {#restful}

Die Bezeichnung "REST" (für "Representational State Transfer") wurde im Jahr 2000 von
Roy Fielding eingeführt^[Fielding, Roy: Architectural Styles and
the Design of Network-based Software Architectures,
<http://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm>]. Die Definition
von Fielding reicht sehr weit und berührt viele Details. In der Praxis wird der Begriff
häufig genutzt, um eine Schnittstelle zu beschreiben,

* die auf WWW-Technologie aufbaut, insbesondere dem HTTP-Protokoll
* die darauf beruht, dass mittels URL einzelne Ressourcen oder Zustände vom
  Client abgerufen werden können.
* die zustandslos ist. Das bedeutet, die Anfrage eines Clients an den Server enthält
  alle Informationen, die notwendig sind, um die Anfrage zu verarbeiten. Auf dem Server
  wird kein Speicher zur Verfügung gestellt, um beispielsweise den Zustand einer Session
  zu speichern.

Diese Prinzipien macht sich auch OParl zunutze. Damit gilt prinzipiell, dass eine 
OParl-konforme Server-Schnittstelle auch als "RESTful" gelten darf.

### Selbstbeschreibungsfähigkeit

Ausgaben des Servers sollten so beschaffen sein, dass sie für menschliche Nutzerinnen
weitgehend selbsterklärend sein können. Dies betrifft besonders die Benennung von
Objekten und Objekteigenschaften.

Aber auch für die maschinelle Verarbeitung der Daten durch Clients kann die
Selbstbeschreibung wichtig sein. Dies stellt allerdings erhöhte Anforderungen
an die verwendeten Datenformate, da dafür formalisierte semantische
Informationen enthalten sein müssen.

Um den Kreis der Entwicklerinnen und Entwickler, die mit einer OParl-API arbeiten
können, nicht unnötig einzuschränken, wird hierbei grundsätzlich auf englischsprachige
Begrifflichkeiten gesetzt.

### Erweiterbarkeit

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
sie nicht für die Aufgabe des Clients relevant sind.


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
bestimmten Objekt die anderen Objekte im System finden, indem er einfach den angebotenen
URLs folgt. Dieses Prinzip wird auch "Follow Your Nose"^[<http://patterns.dataincubator.org/book/follow-your-nose.html>] genannt.

### Schritte in Richtung Linked Data {#linked_data}

Der Begriff "Linked Data" steht für die Beschreibung von Daten in einer Form, die diese 
über ihren ursprünglichen Kontext hinaus verständlich macht.^[vgl. Bundesministerium 
des Innern (Herausg.): Open Government Data Deutschland, Seite 433f., 2012 
<http://www.bmi.bund.de/SharedDocs/Downloads/DE/Themen/OED_Verwaltung/ModerneVerwaltung/opengovernment.pdf>]

OParl unterstützt mit der vorliegenden Version 1.0 der Spezifikation die Anwendung
einiger Linked-Data-Prinzipien. Damit soll die automatisierte Verarbeitung
und Verknüpfung von Informationen aus parlamentarischen Informationnssystemen, auch über
deren Grenzen hinweg, erleichtert werden.

Ein grundlegender Baustein der Linked-Data-Unterstützung in OParl ist die Tatsache, dass
jedes Objekt durch eine URL identifiziert wird. So eignen sich OParl-Objekte für die
Verknüpfung durch externe Anwendungen.

Ein weiteres wesentliches Linked-Data-Konzept in OParl ist die Möglichkeit, externe Vokabulare
zur Klassifizierung von Objekten zu nutzen. So können beispielsweise Gruppierungen (d. h.
Objekte des Typs `oparl:Organization`) als Ausschuss oder als Fraktion klassifiziert werden,
wobei der Begriff "Ausschuss" oder "Fraktion" durch eine URL repräsentiert wird, die auf
ein Konzept in einem externen Vokabular zeigt. Weitere Informationen hierzu sind in
[Vokabulare zur Klassifizierung](#vokabulare_klassifizierung) beschrieben.
