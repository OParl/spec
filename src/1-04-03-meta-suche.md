### Szenario 3: Meta-Suche  {#szenario_meta_suche}

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
sämtliche Informationen, die das System bereithält, ab. Vorbild sind die Robots oder
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
