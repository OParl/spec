Nutzungsszenarien  {#nutzungsszenarien}
=================

Die nachfolgenden Nutzungsszenarien dienen dazu, die Architektur und die
Anwendungsmöglichkeiten anhand konkreter Beispiele zu verdeutlichen. Sie
erheben keinen Anspruch auf Vollständigkeit.

Überblick der Szenarien:

1. Mobile Client-Anwendung
2. Integration in Web-Portal
3. Meta-Suche
4. Forschungsprojekt Themen- und Sprachanalyse

## Szenario 1: Mobile Client-Anwendung {#szenario_mobile_client}

Eine [Client](#client)-Anwendung für mobile Endgeräte wie Smartphones und Tablets,
nachfolgend "App" genannt, könnte das Ziel verfolgen, Nutzern unterwegs
sowie abseits vom Desktop-PC auf die Gegebenheiten mobiler Endgeräte optimierten
Lesezugriff auf Dokumente aus parlamentarischen Informationssystemen
zu bieten. Die möglichen Kontexte und Nutzungsmotivationen sind vielfältig:

* Teilnehmer einer Sitzung greifen während der Sitzung auf die Einladung
  dieser Sitzung und die zur Tagesordnung der Sitzung gehörenden
  Drucksachen zu, außerdem auf die Protokolle vorheriger Sitzungen.

* Eine Redakteurin der Lokalpresse geht unterwegs die Themen der nächsten
  Sitzungen bestimmter Gremien, für die sie sich besonders interessiert,
  durch.

* Eine Gruppe von Studierenden erkundet zusammen mit ihrem Dozenten die
  lokalpolitischen Aktivitäten des Viertels rund um ihre Hochschule. Dazu
  nutzen sie die GPS-Lokalisierung ihrer Smartphones in Verbindung mit den
  Geodaten, die an vielen Drucksachen des lokalen RIS zu finden sind. Direkt
  vor Ort an einer Baustelle öffnen sie Beschlüsse, Pläne und Eingaben aus
  dem Planfeststellungsverfahren, die dieser Baustelle voran gegangen sind.

Zur Realisierung derartiger Szenarien können die Fähigkeiten von OParl-kompatiblen
Servern mit den besonderen Eigenschaften der mobilen Endgeräte verknüpft werden.

Smartphones und Tablets verfügen beispielsweise, je nach Aufenthaltsort, über
sehr unterschiedlich gute Internetanbindung. In einem Büro oder zuhause können
Nutzer über ein WLAN Daten mit hoher Bandbreite austauschen, in Mobilfunknetzen
vor allem außerhalb der Ballungsgebiete jedoch sinken die Bandbreiten deutlich.
Einige Tablets werden sogar ohne Möglichkeit zur Mobilfunk-Datenübertragung
genutzt. In solchen Fällen kann ein [Cache](#cache) auf dem Endgerät dazu
dienen, Inhalte vorzuhalten, die dann auch bei langsamer oder fehlender
Internetverbindung zur Verfügung stehen. Sobald dann wieder eine Verbindung
mit hoher Bandbreite bereit steht, kann die App im Hintergrund, entweder über die 
[Feeds](#feeds) der OParl API oder über den einzelnen Abruf von Objekten, die 
gecachten Inhalte aktualisieren.

Eine Stärke eines mobilen Clients ist auch die Möglichkeit der Personalisierung,
also der Anpassung auf die Bedürfnisse und Interessen der Nutzerin oder des Nutzers.
Es wäre beispielsweise denkbar, dass eine Nutzerin die parlamentarischen Informationssysteme,
für die sie sich interessiert, dauerhaft in der App einrichtet und eine Favoritenliste
der Gremien, die ihre bevorzugten Themengebiete behandeln, hinterlegt. Die App
könnte aufgrund dieser Favoritenliste eigenständig über die API nach neuen
Sitzungsterminen, Tagesordnungspunkten, Drucksachen und Dokumente suchen. Taucht
dabei ein neues Objekt auf, wird die Nutzerin darüber benachrichtigt. Sie kann dann
beispielsweise entscheiden, Dokumente direkt zu öffnen oder für den späteren 
Offline-Zugriff zu speichern.

Einem derartigen Szenario kommt das Graph-orientierte Datenmodell der OParl-API
entgegen. Ausgehend von einer Sitzung eines bestimmten Gremiums beispielsweise
ist es damit einfach möglich, die in Verbindung stehenden Mitglieder des Gremiums,
Teilnehmer der Sitzung, Tagesordnungspunkte der Sitzung oder Drucksachen zu den
Tagesordnungspunkten und letztlich Dokumente zu Drucksachen und Sitzung abzurufen.

Für die Nutzer einer mobilen Client-Anwendung könnte es sich als besonders hilfreich
erweisen, wenn Dokumente auf dem Server in verschiedenen Formaten zur Verfügung
gestellt werden. Denn nicht jedes Endgerät mit kleinem Bildschirm bietet eine
nutzerfreundliche Möglichkeit, beispielsweise Dokumente im weit verbreiteten PDF-Format 
darzustellen. Hier könnte schon der Entwickler der mobilen App Mechanismen vorsehen,
die, sofern vorhanden, besser geeignete Formate wie z. B. HTML abrufen.

Neben dem kleinen Display kann für einige mobile Endgeräte auch die im Vergleich zu
einem zeitgemäßen Desktop-PC geringere CPU-Leistung eine Einschränkung darstellen.
Solchen Geräten kommt es besonders entgegen, wenn der Server zu allen Dokumenten auch
den reinen Textinhalt abrufbar macht, der dann beispielsweise für eine Volltextsuche
auf dem Endgerät indexiert werden kann. So wiederum kann auf dem Client eine
Suchfunktion realisiert werden, welche die OParl-API selbst nicht zur Verfügung
stellt.

Eine solche Suchfunktion kann auch über die reine Volltextsuche
und über die Suche mittels Text- oder Spracheingabe hinaus gehen. Denn ein Client
könnte von einem [Server](#server)-System, das Drucksachen mit Geoinformationen
anbietet, diese abrufen und räumlich indexieren. Anhand der Position des Geräts,
die mittels GPS genau bestimmt werden kann, könnte so der lokale Cache nach
Objekten in der Umgebung durchsucht werden. Das Ergebnis könnte auf einer Karte
dargestellt oder in einer Ergebnisliste angezeigt werden, die z. B. nach Distanz zum
Objekt sortiert werden kann.

## Szenario 2: Integration in Web-Portal  {#szenario_web_portal}

Portallösungen bieten den Betreibern die Möglichkeit, Inhalte auf einer einheitlichen
Weboberfläche zu veröffentlichen, die aus verschiedensten Quellen und Plattformen
bereitgestellt werden. Inhalte werden dabei häufig als sogenannte "Portlets" in
Seiten integriert.

Ein Beispiel für die Realisierung eines solchen Integrations-Ansatzes wäre eine Kommune,
die für ihre allgemeine Website eine Portallösung einsetzt und hier auch Inhalte aus
dem kommunalen Ratsinformationssystem einspeisen und darstellen möchte. Die Inhalte könnten
als Module mit anderen Inhalten, beispielsweise aus einem Web Content Management System
(WCMS), gemeinsam auf einer Seite dargestellt werden.

Eine Seite über den Gemeinderat beispielsweise könnte durch ein Portlet ergänzt
werden, in dem die nächsten Sitzungstermine des Gemeinderats aufgelistet werden. Eine
Pressemeldung über ein bestimmtes Bauvorhaben, in dem ein Beschluss erwähnt wird,
könnte direkt ein Portlet mit einer Detailansicht der entsprechenden Drucksache
einbinden.

Die Portlets, die von einem Portalserver zur Verfügung gestellt werden, stellen damit
im Sinne der OParl-Architektur Clients dar. Je nach Performanz und Anforderungen im
Einzelfall könnten diese Client mit eigenen Caches arbeiten oder aber direkt auf den
jeweiligen OParl-Server zugreifen. 

Vorteil einer solchen Einbindung, also der kontextbezogenen Darstellung von parlamentarischen
Informationen im Gegensatz zu einem monolitischen parlamentarischen Informationssystem
könnte sein, dass Nutzer in einer gewohnten und akzeptierten Oberfläche jeweils die
relevanten Informationen erhalten, ohne sich an die ungewohnte Umgebung eines parlamentarischen
Informationssystems gewöhnen zu müssen.

Die denkbaren Szenarien einer solchen Integration beschränken sich nicht auf
anonyme Nutzer von öffentlichen Websites. In einem authentifizierten Umfeld wie beispielsweise
einem kommunalen Intranet oder Extranet lassen sich weitere Arten von Portlets und damit
Mehrwerte für die Nutzer realisieren. So könnte beispielsweise eine eingeloggte Nutzerin eine
personalisierte Liste der Sitzungstermine, zu der sie eingeladen ist, angezeigt bekommen.

Die Standardisierung durch OParl sorgt im Rahmen der Portal-Szenarios dazu, dass Portlets,
die für ein bestimmtes parlamentarisches Informationssystem entwickelt wurden, leichter auf
andere Systeme – auch verschiedener Anbieter – ausgeweitet werden können, sofern diese ebenfalls
OParl-konform sind. Dies ermöglicht es beispielsweise verschiedenen Kommunen,
bei der Entwicklung von Portlets zusammenzuarbeiten und ihre Ergebnisse auszutauschen. Denkbar
sind auch Portlet-Entwicklungen als Open-Source-Projekte.

## Szenario 3: Meta-Suche  {#szenario_meta_suche}

Die Ermöglichung einer nutzerfreundlichen Suche, die damit verbundene Indexierung von
verschiedensten Dokumenteninhalten und die Kategorisierung von Inhalten kann eine
sowohl konzeptionell als auch technisch anspruchsvolle Aufgabe sein. Auch im Hinblick
auf die Server-Ressourcen sind damit nennenswerte Aufwände verbunden. Andererseits
liegt auf der Hand, dass die effiziente Arbeit mit großen Informationsmengen nach
intelligenten Möglichkeiten der Einschränkung von Informationsmengen auf jeweils
im Anwendungsfall relevante Treffer verlangt. Beispiel wäre ein Nutzer, der sich für
alle Dokumente zum Thema Kreisverkehre interessiert. Die OParl-Spezifikation sieht
keine Methoden vor, wie die Ausgabe des Servers schon bei der Anfrage von Dokumenten
derart beschränkt werden können. Damit ist die Realisation von Such- und Filtermechanismen
im OParl-Umfeld eine Aufgabe, die bis auf weiteres lediglich auf Seite der Clients
angeboten werden kann.

Angelehnt an das seit den Anfängen des Webs etablierte Modell der externen Web-Suchmaschine
sind spezielle Suchmaschinen für OParl-konforme parlamentarische Informationssysteme
denkbar. Diese können auch von dritten, beispielsweise zivilgesellschaftlichen
Organisationen betrieben werden, die nicht Betreiber des Server-Systems sind. Solche
Plattformen treten gegenüber dem OParl-Server als Client auf und rufen bestimmte oder
sämtliche Informationen, die das System bereit hält, ab. Vorbild sind die Robots oder
Spider von Web-Suchmaschinen. Die abgerufenen Informationen können dann indexiert
und je nach Anforderungen für eine gezielte Suche weiterverarbeitet werden.

Dieses Modell ist grundsätzlich nicht auf einzelne OParl-Server oder einzelne
Körperschaften beschränkt. Vielmehr könnte der Betreiber einer solchen Suchmaschine
sich entschließen, die Informationen aus mehreren OParl-konformen Systemen zu indexieren.
Nutzern könnte entweder angeboten werden, die Suche auf bestimmte Körperschaften,
beispielsweise auf eine bestimmte Kommune, zu beschränken, oder ohne Beschränkung über
alle angebotenen Körperschaften zu suchen.^[Daher der Begriff Meta-Suche]

Daraus ergeben sich vielfältige Anwendungsszenarien, die hier beispielhaft
beschrieben werden:

* Eine Mitarbeiterin eines regionalen Zweckverbands hat die Aufgabe, Ratsvorgänge in den
Mitgliedskommunen mit Relevanz für die Aufgaben des Verbandes im Blick zu behalten. Sie
nutzt dafür ein regionales Internetportal, in dem die Inhalte der OParl-konformen 
parlamentarischen Informationssysteme der Mitgliedskommunen durchsuchbar sind.
Um die Suche zu vereinfachen, hat sie einzelne Schlagwörter abonniert, zu denen sie 
automatisch über neue Vorgänge informiert wird.

* Ein Einwohner eines Ballungsraums will sich über aktuelle Vorgänge rund um seine
Mietwohnung in Stadt A, sein Gartengrundstück in einer Kleingartenkolonie in der
Nachbarstadt B und seinen Arbeitsplatz in Stadt C auf dem Laufenden halten. Dazu abonniert
er im regionalen Meta-Such-Portal parlamentarische Vorgänge mit räumlichem Bezug zu diesen
drei Standorten und wird so automatisch über neue Aktivitäten informiert, die Relevanz
für ihn haben könnten.

* Eine Landespolitikerin möchte einfacher über die politischen Aktivitäten ihrer
Parteikollegen in den Rathäusern des Bundeslandes informiert werden. Dazu nutzt sie ein
Internetportal, in dem die Informationen aus den parlamentarischen Informationssystemen 
mit OParl-Schnittstelle im Land zusammengeführt werden. Dort hat sie sich Abonnements 
zu einzelnen Lokalpolitikern eingerichtet und wird automatisch über ihre Teilnahme an 
Gremiensitzungen und die Themen dieser Sitzungen informiert.

## Szenario 4: Forschungsprojekt Themen- und Sprachanalyse {#szenario_forschung}

In einem Forschungsprojekt sollen Pro- und Contra-Argumentationen bei Ratsdiskussionen zum
Ausbau von Stromtrassen identifiziert werden. Über die Analyse in mehreren Gebietskörperschaften
sollen die gefundenen Argumentationen zu wiederkehrenden Mustern verdichtet werden und festgestellt
werden, wie diese Muster regional abweichen.

Dazu nutzen die Mitarbeitenden des Forschungsprojektes die OParl-Schnittstellen der
parlamentarischen Informationssysteme aller Kommunen entlang der geplanten überregionalen
Trassen. Über diese einheitlichen Schnittstellen können sie insbesondere die relevanten
Wortprotokolle abrufen und zum Beispiel in einem Werkzeug zur qualitativen
Datenanalyse lokal verarbeiten. Im Ergebnis ließe sich auch erkennen, wie ähnlich oder
wie unterschiedlich die Argumente in rhetorischer Hinsicht vorgetragen werden.
