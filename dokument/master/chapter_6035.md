URLs
====

Den URLs (für "Uniform Resource Locators", auch URI für "Uniform Resource Identifier")
kommt bei einer OParl-konformen API eine besondere Bedeutung zu und es werden eine 
Reihe von Anforderungen an die Verarbeitung von URLs gestellt.

Die grundsätzliche Funktionsweise von URLs ist in RFC3986 beschrieben^[<http://tools.ietf.org/html/rfc3986>].

Der Aufbau einer beispielhaften URL mit den Bezeichnungen, wie sie in diesem Dokument
Verwendung finden:

    http://refserv.oparl.org/bodies/0/committees/4/members/?skip=234
    \__/   \_______________/\_____________________________/ \______/
     |         |                  |                           |
    Schema    Host               Pfad                        Query-String

### URL-Kanonisierung

Absicht ist, dass jedes benannte Objekt, das ein Server über eine OParl-API anbietet, über genau
eine URL identifizierbar und abrufbar ist. Diese Vereinheitlichung der URL nennen
wir Kanonisierung.

Die Kanonisierung ist entscheidend, um erkennen zu können, ob zwei URLs das selbe
Objekt repräsentieren. Sind zwei URLs identisch, sollen Clients daraus ableiten können,
dass diese das selbe Objekt repräsentieren. Sind zwei URLs unterschiedlich, soll
im Umkehrschluss die Annahme gelten, dass sie zwei verschiedene Objekte repräsentieren.

Der OParl-konforme Server MUSS für jedes benannte Objekt eine kanonische URL bestimmen können.

Die URL-Kanonisierung betrifft sämtliche Bestandteile der URL. Entsprechend beginnt diese
schon beim **Schema** und bei der Entscheidung durch den Betreiber, ob eine OParl-API regulär
über HTTP oder über HTTPS erreichbar sein soll (vgl. [HTTP und HTTPS]).

Der **Host**-Teil der URL wird ebenfalls durch die Konfiguration des Betreibers festgelegt.
Obwohl technisch auch die Verwendung einer IP-Adresse (z.B. "123.123.123.123") möglich wäre,
SOLL der Betreiber einen mit Bedacht gewählten Host-Namen einsetzen. Die Vorteile dieser Lösung
gegenüber der Verwendung einer IP-Adresse sind vielfältig:

* NutzerInnen können Host-Namen lesen und interpretieren
* In Kombination mit der richtigen Domain (oder Subdomain) kann der Hostname
  kommunizieren, wer der Betreiber ist.
* Host-Namen können zwischen verschiedenen technischen Systemen (bzw. von IP-Adresse zu IP-Adresse)
  migriert werden, was hilft, die Langlebigkeit der URLs zu gewährleisten

Eine URL wie

    http://oparl.ratsinformation.stadt-koeln.de/

kommuniziert beispielsweise direkt die Zugehörigkeit zur Stadt Köln als Betreiber des Systems. Die
Bezeichnung "ratsinformation" in der Subdomain zeigt den Zweck des Systems allgemein verständlich an.
Der Host-Name "oparl.ratsinformation.stadt-koeln.de" deutet an, dass diese URL zu einer 
OParl-Schnittstelle zu diesem System gehört.

Um die Kanonisierung zu gewährleisten, sind vom Betreiber alle notwendigen Faktoren auszuschließen,
die dazu führen können, dass eine Ressource neben der kanonischen URL noch über andere URLs
abrufbar ist. Diese Faktoren könnten sein:

* Der selbe Server antwortet nicht nur über den kanonischen Host-Namen, sondern auch noch über andere
  Host-Namen. Das könnte zum Beispiel der Fall sein, wenn der Host-Name als CNAME für einen anderen
  Namen konfiguriert wurde oder wenn ein DNS A-Record für die IP-Adresse des Servers existiert.

* Der Server ist neben dem Host-Namen auch über die IP-Adresse erreichbar.

* Zusätzliche Domains, die einen A-Record auf den selben Server besitzen

Zu der oben gezeigten kanonischen Beispiel-URL http://oparl.ratsinformation.stadt-koeln.de/ wären eine Reihe von nicht-kanonischen URL-Varianten denkbar, die technischen auf den selben Server führen könnten:

* http://83.123.89.102/
* http://oparl.ratsinformation.stadtkoeln.de/
* http://risserv.stadt-koeln.de/

Falls es aus technischen Gründen nicht möglich ist, den Zugang auf das OParl-System über nicht-kanonische
URLs zu unterbinden, SOLL eine entsprechende HTTP-Anfrage mit einer Weiterleitung auf die entsprechende 
kanonische URL beantwortet werden. Dabei ist der HTTP-Status-Code 301 zu verwenden.

Server-Implementierern wird empfohlen, hierfür den Host-Header der HTTP-Anfrage auszuwerten und mit
der konfigurierten Einstellung für den kanonischen Hostnamen des Systems abzugleichen.

### Langlebigkeit

Weiterhin ist es Absicht, dass URLs von
Objekten langlebig sind, so dass sie, wenn sie einmal verbreitet wurden, langfristig
zur Abfrage des dazugehörigen Objekts verwendet werden können.

### Empfehlungen für langlebige IRIs/URIs/URLs

- Hinweise und evtl. Auszüge aus
  - http://www.w3.org/Provider/Style/URI.html
  - https://joinup.ec.europa.eu/sites/default/files/D7.1.3%20-%20Study%20on%20persistent%20URIs.pdf

### Empfehlungen für eindeutige URLs

- Vermeidung von Duplicate Content durch Fehlkonfiguration
- z.B.: verschiedene CNAMES mit der selben IP-Adresse
- z.B.: Aufruf über http://www.example.com und http://example.com
- z.B.: Direkter Aufruf über IP-Adresse http://1.2.3.4/
- URL-Parameter in definierter Reihenfolge verwenden
- Groß- und Kleinschreibung unterscheiden
