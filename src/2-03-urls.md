## URLs {#urls}

![Aufbau einer URL](images/url.png)

Den URLs (für _Uniform Resource Locators_) kommt eine besondere Bedeutung zu
und es werden deshalb eine Reihe von Anforderungen an deren Aufbau und
Eigenschaften gestellt. Die allgemeine Funktionsweise von URLs ist in RFC 3986
beschrieben^[RFC 3986: <http://tools.ietf.org/html/rfc3986>].

Grundsätzlich **müssen** alle Zugriffe zustandslos erfolgen können, also ohne
Sessioninformationen wie Cookies. Das bedeutet, dass alle Informationen,
die zum Abrufen eines Objekts nötig sind, in der URL vorhanden sein müssen.

### URL-Kanonisierung {#url_kanonisierung}

Um Objekte eindeutig identifizieren zu können ist es notwendig, dass ein Server
für ein Objekt genau eine unveränderliche URL benutzt. Diese Festlegung auf
genaue eine eindeutige URL wird Kanonisierung genannt. Ein Server **muss**
deshalb für jedes seiner Objekte eine kanonische URL bestimmen können.

Es wird empfohlen keine IP-Adressen in URLs zu benutzen, sondern einen
mit Bedacht gewählten Hostnamen einzusetzen. Das ist vor allem im Hinblick
auf die Langlebigkeit der URLs wichtig.

Um die Kanonisierung zu gewährleisten **sollten** OParl-Server so konfiguriert
werden, dass sie nur über eine bestimmte Domain erreichbar sind. OParl-Server **sollten** dagegen möglichst **nicht** nur über eine IP-Addresse sowieso möglichst auch **nicht** über weitere, nicht kanonische URLs erreichbar sein.

Wenn ein Server auch durch eine nicht-kanonische URL erreichbar ist, dann
**sollte** eine entsprechende HTTP-Anfrage mit einer Weiterleitung auf die
entsprechende kanonische URL und HTTP-Status-Code 301 beantwortet werden.
Zur überprüfung kann z.B. der `Host`-Header einer HTTP-Anfrage verwendet werden.

Beim Pfad-Bestandteil der URL **müssen** Server-Implementierer darüber hinaus
beachten, dass zur kanonischen Schreibweise auch die Groß- und Kleinschreibung, die Anzahl von Schrägstrichen als Pfad-Trennzeichen und die Anzahl von führenden Nullen vor numerischen URL-Bestandteilen gehört.

Die Kanonisierung umfasst auch den Query-String-Bestandteil der URL. Wie auch
beim Pfad gilt, dass für jeden Parameter und jeden Wert im Query-String genau
eine kanonische Schreibweise gelten **muss**.

Darüber hinaus **sollte** der Server-Implementierer darauf achten, Query-String-Parameter
immer nach demselben Prinzip zu sortieren. Als Beispiel: Die beiden URLs

    https://oparl.example.org/members?body=1&committee=2
    https://oparl.example.org/members?committee=2&body=1

unterscheiden sich lediglich in der Reihenfolge der Query-String-Parameter. Da
sie jedoch nicht identisch sind, könnten Clients annehmen, dass beide URLs
verschiedene Objekte repräsentieren.

Clients **sollen** die vom Server gelieferten URLs bei Anzeige, Speicherung
und Weiterverarbeitung nicht verändern.

### HTTP und HTTPS {#http-und-https}

Der Einsatz des verschlüsselten HTTPS wird empfohlen. Bei Verwendung von HTTPS
wird allen URLs "https://" voran gestellt, ansonsten beginnen URLs mit
"http://".

Aus Gründen der URL-Kanonisierung ist es **zwingend** notwendig, dass ein
Server-Betreiber sich entweder für HTTP oder für HTTPS entscheidet.
Es jedoch möglich, eine Weiterleitung (HTTP Status-Code 301)
einzurichten. Eine Weiterleitung von HTTPS auf HTTP wird **nicht  empfohlen**.


### Langlebigkeit {#url_langlebigkeit}

Weiterhin sollen URLs langlebig sein, sodass sie möglichst lange zur Abfrage des
dazugehörigen Objekts verwendet werden können.

In URLs **sollten** deshalb nur Eigenschaften des Objekts aufgenommen werden,
die nicht verändert werden. Ändert sich beispielsweise die Kennung einer
Drucksache im Verlauf ihrer Existenz, dann scheidet sie für die Bildung
der URL aus.

Des weiteren sollen Eigenschaften der Implementierung nicht sichtbar sein.
Ist ein OParl-Server beispielsweise in PHP geschrieben, **sollte** dies
**nicht** dazu führen, dass im Pfad ein Bestandteil wie "oparl.php/" erscheint.

Weitere Empfehlungen für langlebige URLs liefern Tim Berners-Lee^[Berners-Lee, Tim: Cool URIs don't change. <http://www.w3.org/Provider/Style/URI.html>] sowie die Europäische Kommission^[Study on persistent URIs, with identification of
best practices and recommendations on the topic for the MSs and the EC. (PDF) <https://joinup.ec.europa.eu/sites/default/files/D7.1.3%20-%20Study%20on%20persistent%20URIs.pdf>].
