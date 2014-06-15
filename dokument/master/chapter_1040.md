Zukunft von OParl
-----------------

Die vorliegende Version 1.0 der OParl-Spezifikation erhebt keineswegs den Anspruch,
ein aktuell und für die ferne Zukunft vollständige Lösung alle Problemstellungen
rund um die Veröffentlichung parlamentarischer Informationen zu sein. Viele Funktionen,
die denkbar und bestimmt sinnvoll wären, sind aus verschiedensten Gründen in dieser
Version noch nicht berücksichtigt. Einige der Gründe, die dazu führten, ein Thema
nicht auszuspezifizieren, waren:

* Zu wenig detaillierte Anforderungen aus der Praxis
* Zu großer Arbeitsaufwand für die Spezifikations-Entwicklung
* Hohe Aufwände bei den Server-Implementierern

Zu den Themen, die in zukünftigen Versionen adressiert werden können, zählen:

* Loslösung von der kommunalen Ebene: Es ist möglich, dass OParl mit nur geringfügigen
  Änderungen oder Erweiterungen auch für die Ebene von Bundesländern (Landtage) oder
  des Bundes (Bundestag, Bundesrat) nutzbar wäre.

* Flexible Abfragemöglichkeiten für Objekte: Aufgrund der unklaren Anforderungslage
  sowie dem Bestreben möglichst wenige spezielle Lösungen nur für OParl zu schaffen
  sind in Version 1.0 nur sehr beschränkte Möglichkeiten vorgesehen, Listen von
  Drucksachen etc. nach bestimmten Kriterien einzuschränken. Zukünftig könnten
  hier weitere Möglichkeiten definiert werden, bis hin zur Suche nach Stichworten
  in Volltexten. Ein möglicher Ansatz hierfür wäre die Verwendung von Linked Data
  Fragements^[http://linkeddatafragments.org/]. Diese ermöglichen Clients mächtige
  Abfragen, ohne dabei zu übermäßiger Last auf Serverseite zu führen.

* Detaillierte Wiedergabe von Abstimmungen: Das Thema ist vom Datenmodell/Schema
  der vorliegenden Version noch nicht abgedeckt, da es vielerorts nicht üblich ist,
  Abstimmungen über die Fraktionsebene genau zu erfassen. Zukünftig könnte es ein
  Ziel sein, das Abstimmungsverhalten einzelner Parlamentarier und Fraktionen genau
  zu dokumentieren.

* Strukturierte Protokolle: Während Protokolle in der Praxis in der Regel als
  unstrukturierte Fließtexte angelegt werden, könnte eine Strukturierung der Inhalte
  die Nachvollziehbarkeit des parlamentarischen Geschehens deutlich verbessern.

* Vokabular für Drucksachentypen: In der Praxis wird eine Vielzahl von Drucksachentypen
  genutzt. Um eine Vergleichbarkeit, beispielsweise zwischen Anträgen, innerhalb der
  Parlamente zu schaffen, könnte zukünftig eine Erweiterung des OParl-Vokabulars
  im Sinne von Linked Data angestrebt werden.^[Das gesagte lässt sich auch auf viele
  andere Informationen, nicht nur auf Drucksachen, anwenden.]

* Weitere externe Standards, insbesondere zu Paginierung:
  Teile der Spezifikation beziehen sich auf technische
  Anforderungen die nicht nur für OParl relevant sind. Das betrifft insbesondere die
  Paginierung-Mechanismen. Idealerweise sollte OParl hierfür externe Standards verwenden.
  Deshalb werden entsprechende Standardisierungsvorhaben wie Linked Data Platform
  Paging^[https://dvcs.w3.org/hg/ldpwg/raw-file/default/ldp-paging.html] des W3C
  und das Hydra Core Vocabulary^[http://hydra-cg.com/spec/latest/core/#collections]
  beobachtet.

* Schreibender Zugriff: Denkbar ist auch, dass OParl von der derzeitigen Ausrichtung
  auf den reinen lesenden Informationszugriff um die Möglichkeit, Inhalte anzulegen,
  zu verändern und zu entfernen sowie um das Konzept von authentifizierten Nutzern
  erweitert wird.

* Internationalisierung: Es gibt in sehr vielen Ländern Gebietskörperschaften mit 
  politischen Gremien, deren Prozesse ähnlich strukturiert sind, wie diejenigen in 
  Deutschland. Auch dort besteht Bedarf an standardisierten Vokabularen zur 
  Veröffentlichung parlamentarischer Informationen. Deshalb sind – teilweise noch 
  vor OParl – auch weitere entsprechende Initiativen entstanden.^[Vgl. dazu 
  beispielsweise <http://popoloproject.com/>, TODO: UK, KB Niederlande,
  Italienisches Parlament: <http://data.camera.it/data/en/>] Eine
  Zusammenarbeit mit derartigen Initiativen mit dem Ziel der Wiederverwendung von
  Arbeitsergebnissen ist vorstellbar. Auch aus diesem Grund wurde bereits in OParl 
  1.0 die Möglichkeit der Verwendung mit anderen Sprachen und Mehrsprachigkeit
  eingebaut.

* IT-Planungsrat: Dieser kann die Verbindlichkeit von Standards wie OParl für
  Deutschland beschliessen. Der "Vertrag über die Errichtung des IT-Planungsrats 
  und über die Grundlagen der Zusammenarbeit beim Einsatz der Informationstechnologie
  in den Verwaltungen von Bund und Ländern – Vertrag zur Ausführung von Artikel 91c 
  GG"^[http://www.it-planungsrat.de/SharedDocs/Downloads/DE/ITPlanungsrat/Staatsvertrag/Staatsvertrag.html]
  enthält in § 3 Absatz 2 diese Aussage: "Beschlüsse über Standards im Sinne des
  Absatz 1 werden vom IT-Planungsrat ... gefasst, soweit dies zum 
  bund-länderübergreifenden Datenaustausch oder zur Vereinheitlichung des 
  Datenaustauschs der öffentlichen Verwaltung mit Bürgern und Wirtschaft notwendig 
  ist."

Generell gilt auch für OParl: "Completion is a state that a good specification never
reaches before it's irrelevant."^[OGCWG - Lessons Learned: <http://www.w3.org/community/oilgaschem/wiki/OGCWG_-_Lessons_Learned>] - Ian Hickson

