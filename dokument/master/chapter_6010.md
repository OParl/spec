Designprinzipien
----------------

### Aufbauend auf der gängigen Praxis

Grundlage für die Erarbeitung der OParl-Spezifikation in der vorliegenden Version
ist eine Analyse der aktuell (2012 bis 2014) in Deutschland befindlichen
Ratsinformationssysteme und ihrer Nutzung. Erklärtes Ziel für diese Version ist es,
mit möglichst geringem Entwicklungsaufwand auf Seite der Softwareanbieter und 
Migrationsaufwand auf Seite der Betreiber zu einer Bereitstellung von parlamentarischen 
Informationen über eine OParl API zu gelangen. Hierbei war es von entscheidender 
Bedeutung, dass sich die Informationsmodelle der einschlägigen Softwareprodukte stark
ähneln. Für die OParl-Spezifikation wurde sozusagen ein Datenmodell als "gemeinsamer Nenner"
auf Basis der gängigen Praxis beschrieben.

### Verbesserungen gegenüber dem Status Quo wo möglich

Dort, wo es dem Ziel der einfachen Implementierbarkeit und der einfachen Migration
nicht im Weg steht, erlauben sich die Autoren dieser Spezifikation, auch Funktionen
aufzunehmen, die noch nicht als gängige Praxis im Bereich der Ratsinformationssysteme
bezeichnet werden können oder welche nur von einzelnen Systemen unterstützt werden.
Solche Funktionen sind dann so integriert, dass sie nicht als zwingende Anforderung
gelten.

Ein Beispiel für eine derartige Funktion ist die Abbildung von Geodaten im Kontext von
Drucksachen (`oparl:Paper`), um beispielsweise die Lage eines Bauvorhabens, das in
einer Beschlussvorlage behandelt wird, zu beschreiben. Zwar ist den Autoren nur ein
einziges Ratsinformationssystem^[Das System BoRis der Stadt Bonn
<http://www2.bonn.de/bo_ris/ris_sql/agm_index.asp>] in Deutschland bekannt, das 
Geoinformationen - und zwar in Form von Punktdaten, also einer Kombination aus 
Längen- und Breitengradangaben - mit Dokumenten verknüpft. Der Vorteil dieser
Funktion ist jedoch anhand zahlreicher Anwendungsszenarien belegbar. Somit ist der
vorliegenden OParl-Spezifikation die Möglichkeit beschrieben, beliebige Geodaten-Objekte
entsprechend der GeoJSON Spezifikation^[GeoJSON <http://geojson.org/>] einzubetten.
Die Angabe eines einzelnen Punktes ist dabei nur ein einfacher Sonderfall. Die
Spezifikation erlaubt auch die Kodierung von mehreren Objekten, die Punkte, Linien
oder Polygone repräsentieren können. Vgl. dazu `oparl:Location`.

Auch die Ausgabe einer Nur-Text-Version im Kontext des Dokuments (`oparl:Document`),
das den barrierefreien Zugriff auf Inhalte oder Indexierung für Volltextsuchfunktionen
deutlich vereinfacht, ist eine Möglichkeit, die in der gängigen Praxis noch nicht zu
finden ist. Ebenso die Möglichkeit, Beziehungen zwischen einzelnen Dokumenten
herzustellen, um so von einem Dokument zu anderen Dokumenten mit identischem Inhalt,
aber in anderen technischen Formaten zu verweisen, etwa von einer ODT-Datei zu einer
PDF-Version.

### RESTful

### Selbstbeschreibungsfähigkeit

### Erweiterbarkeit

### Browseability/Verlinkung
