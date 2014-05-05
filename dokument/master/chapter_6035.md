URLs bzw. IRIs
----

Internationalized Resource Identifier (IRI) sind die internationalisierte Form der Uniform Resource Identifier (URI). Diese sind in RFC 3987 spezifiziert (http://tools.ietf.org/html/rfc3987). In der OParl-Spezifikation sind grundsätzlich auch dann IRIs gemeint, wenn wie folgt die Bezeichnungen URI oder URL verwendet werden. Dies soll der Lesbarkeit dienen, auch wenn es technisch nicht ganz korrekt ist.

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


Um bereits an dieser Stelle das Entstehen von Missverständnissen zu vermeiden sei darauf hingewiesen, dass insbesondere
auch der enthaltene Pfad nur ein Beipiel ist. Der Aufbau der Pfade wird in OParl nicht festgelegt.

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

Zu der kanonischen Beispiel-URL http://oparl.ratsinformation.stadt-koeln.de/ wären eine Reihe von nicht-kanonischen URL-Varianten denkbar, die technischen auf den selben Server führen könnten:

* http://83.123.89.102/
* http://oparl.ratsinformation.stadtkoeln.de/
* http://risserv.stadt-koeln.de/

Falls es aus technischen Gründen nicht möglich ist, den Zugang auf das OParl-System über nicht-kanonische
URLs zu unterbinden, SOLL eine entsprechende HTTP-Anfrage mit einer Weiterleitung auf die entsprechende 
kanonische URL beantwortet werden. Dabei ist der HTTP-Status-Code 301 zu verwenden.

Server-Implementierern wird empfohlen, hierfür den Host-Header der HTTP-Anfrage auszuwerten und mit
der konfigurierten Einstellung für den kanonischen Hostnamen des Systems abzugleichen.

Beim **Pfad**-Bestandteil der URL MÜSSEN Server-Implementierer darüber hinaus beachten, dass
nur jeweils eine Schreibweise als die kanonische Schreibweise gelten kann. Dazu gehört auch
die Groß- und Kleinschreibung, die Anzahl von Schrägstrichen als Pfad-Trennzeichen, die Anzahl
von führenden Nullen vor numerischen URL-Bestandteilen und vieles mehr.

Die Kanonisierung umfasst auch den **Query-String**-Bestandteil der URL. Wie auch beim Pfad, gilt hier,
dass für jeden Parameter und jeden Wert im Query-String nur eine kanonische Schreibweise gelten MUSS.

Darüber hinaus SOLL der Server-Implementierer darauf achten, bei Verwendung von Query-String-Parametern
diese in URLs immer nach dem selben Prinzip zu sortieren. Ein Beispiel: die beiden URLs

    http://oparl.meinris.de/members?body=1&committee=2
    http://oparl.meinris.de/members?committee=2&body=1

unterscheiden sich lediglich in der Reihenfolge der Query-String-Parameter. Da sie jedoch nicht
identisch sind, müssen Clients annehmen, dass beide URLs verschiedene Objekte repräsentieren. In der
Konsequenz kann es zu vermeidbarer Ressourcennutzugn sowohl auf Client- als auch auf Serverseite kommen.

### Langlebigkeit

Weiterhin ist es Absicht, dass URLs von Objekten langlebig sind, so dass sie, wenn sie einmal 
verbreitet wurden, langfristig zur Abfrage des dazugehörigen Objekts verwendet werden können.

Um dies zu gewährleisten, wird den **Betreibern** empfohlen, die Wahl der Domain, eventuell der
Subdomain und letztlich des Host-Namens sorgfältig auf seine längerfristige Verwendbarkeit abzuwägen.

**Server-Implementierer** SOLLEN darüber hinaus dafür sorgen, dass der Pfad-Bestandteil der URLs
die Langlebigkeit der URLs unterstützt. Es gelten die folgenden Empfehlungen, die jedoch keinen
Anspruch auf Vollständigkeit erheben:

* **Veränderliche Objekt-Eigenschaften nicht als URL-Bestandteil nutzen.** In URLs sollten nur Eigenschaften
  des Objekts aufgenommen werden, die keinen Veränderungen unterliegen. Ändert sich beispielsweise
  die Kennung einer Drucksache im Verlauf ihrer Existenz, dann scheidet sie für die Bildung
  der URL aus.

* **Technische Eigenschaften der Implementierung verbergen.** Ist ein OParl-Server beispielsweise in PHP
  implementiert, sollte dies nicht dazu führen, dass im Pfad ein Bestandteil wie "oparl.php/" erscheint.
  Erfahrungsgemäß überdauern solche URLs nur kurz.

Weitere Empfehlungen für langlebige URLs liefern Tim Berners-Lee^[Berners-Lee, Tim: Cool URIs don't change. <http://www.w3.org/Provider/Style/URI.html>] sowie die Europäische Kommission^[Study on persistent URIs, with identification of 
best practices and recommendations on the topic for the MSs and the EC. (PDF) <http://goo.gl/JaTq6Z>]. TODO: goo.gl URL expandieren
