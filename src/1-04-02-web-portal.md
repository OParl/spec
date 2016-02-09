### Szenario 2: Integration in Web-Portal  {#szenario_web_portal}

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
