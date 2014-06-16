Dateizugriff  {#dateizugriff}
------------

Mit dem Begriff "Datei" sind im Sinne dieser Spezifikation alle Ressourcen
gemeint, die von einem OParl-Server zur Verfügung gestellt werden und
deren Metadaten über die JSON-API als [`oparl:File`](#oparl_document) 
abgerufen werden können. Es handelt sich dabei beispielsweise um Textdokumente 
im PDF-Format, Abbildungen im JPEG- oder PNG-Format etc., die wesentliche 
Inhalte der parlamentarischen Informationen im OParl-System ausmachen.

In Bezug auf die Datenvolumen, die der Verkehr zwischen OParl-Servern und -Clients
ausmacht, kommt dem Dateizugriff eine besondere Bedeutung zu. Daher formuliert
OParl diesbezüglich einige Anforderungen, die helfen sollen, unnötigen
Datentransfer zu vermeiden.

Detail zu sämtlichen angesprochenen Mechanismen sind in den verschiedenen Teilen der 
HTTP-1.1-Spezifikation^[vgl. <http://tools.ietf.org/html/rfc7230>,
<http://tools.ietf.org/html/rfc7231>, <http://tools.ietf.org/html/rfc7232>]
zu finden.

### GET und HEAD Anfragen

Grundsätzlich gilt, dass jede Datei mittels HTTP-Anfrage unter Verwendung der
HTTP-Methode `GET` abrufbar sein MUSS. Um Clients zusätzlich die Überprüfung
einer Datei zu ermöglichen, MUSS vom Server außerdem die HTTP-Methode `HEAD`
unterstützt werden. Gemäß HTTP-Spezifikation gibt der Server in diesem Fall nur
die Antwort-Header, nicht aber den eigentlichen Inhalt der angefragten Ressource,
aus.

Die URLs zum Abruf der einzelnen Datei (wahlweise mittels GET oder HEAD) stellt
der Server dem Client in den Daten des Metadaten-Objekts zur Verfügung.
Details finden sich in der Schema-Beschreibung zu [`oparl:File`](#oparl_document).

### Allgemeiner Zugriff und expliziter Download

Mit der im `oparl:File` ZWINGEND anzugebenden Eigenschaft `accessUrl` liefert der
Server dem Client eine URL, die wir hier nachfolgend als *Zugriffs-URL* bezeichnen.
Diese URL dient dem allgemeinen Zugriff auf die Datei. Wie der Client dem Endnutzer
diesen Zugriff genau ermöglicht, ist nicht Sache der OParl-Spezifikation.

Im Unterschied dazu KANN der Server dem Client in der Eigenschaft `downloadUrl`
eine weitere URL anbieten, hier *Download-URL* genannt. Diese dient im Gegensatz 
zur Zugriffs-URL speziell zum Herunterladen und Speichern der Datei in einem 
Dateisystem des Endnutzers. Bei Zugriff auf die Download-URL MUSS der Server in der
HTTP-Antwort einen `Content-Disposition` Header senden.^[vgl. RFC2138
<http://www.ietf.org/rfc/rfc2183>] Dieser Header MUSS als ersten Parameter den
Typ `attachment` sowie den `filename`-Parameter mit dem Namen der Datei enthalten.

Beispiel:

    Content-Disposition: attachment; filename="2014-08-22 Rat Wortprotokoll.pdf"

FRAGE: Sind in Dateinamen sinnvoll?

Der in diesem Header kommunizierte Dateiname ist als Vorschlag an die Nutzerin
zu verstehen, die Datei unter diesem Namen zu speichern. Entsprechend sind Abwägungen
bezüglich der Verständlichkeit, Leserlichkeit und Einzigartigkeit des Dateinamens,
aber auch in Hinblick auf den verwendeten Zeichenumfang zu berücksichtigen. Es
wird EMPFOHLEN, den Dateinamen ausschließlich aus dem ASCII-Zeichenvorrat zu bilden.
FRAGE: Ist die Beschränkung auf ASCII und damit der Verzicht z.B. auf Umlaute
erforderlich?

Im Unterschied zum Zugriff auf die Download-URL DARF der Server beim Zugriff auf die
Zugriffs-URL KEINEN `Content-Disposition` Header mit Parameter `attachment`
senden.

### Obligatorische und empfohlene Header

Ziel ist, dem Client möglichst flexible Möglichkeiten zu geben, einen Cache zu
überprüfen bzw. zu aktualisieren und vermeidbare Anfragen einer Ressource zu
vermeiden. Um dies zu unterstützen, können laut HTTP-Spezifikationen unterschiedliche
Header zum Einsatz kommen.

Die Auslieferung eines `Last-Modified`-Headers gilt für alle OParl-Server beim
Zugriff auf eine Datei-URL, sei es Download- oder Zugriffs-URL, als ZWINGEND.

Darüber hinaus EMPFEHLEN wir, bei Anfrage einer Datei die folgenden
Header auszuliefern:

* `Content-Length`: Die Größe des Dateiinhalts
* `ETag`: Entity Tag

### Conditional GET

Unter einem "Conditional GET" versteht man im HTTP-Kontext die Möglichkeit des
Clients, die Anfrage einer Ressource mit einer Bedingung zu verknüpfen. Der Server
beantwortet die Anfrage nur dann mit einer vollständigen HTTP-Antwort, wenn die
Bedingung erfüllt ist. Andernfalls enthält die Anfrage lediglich den Header; der 
HTTP Status-Code SOLL in diesem Fall "304" lauten (für "nicht geändert"). Dies
dient der Schonung von Ressourcen.

Für einen OParl-Server wird EMPFOHLEN, die nachstehenden Varianten des
Conditional GET zu unterstützen:

* `If-Modified-Since`: Der Client sendet mit der Anfrage als Bedingung ein
  Datum. Nur wenn die angefragte Datei zuletzt *nach* diesem Datum geändert
  wurde, wird der Dateiinhalt mit der Antwort ausgeliefert.

* `If-None-Match`: Erlaubt die Formulierung der Bedingung anhand eines
  Entity-Tags.

### Zustandsloser Dateizugriff

Die Anforderung, dass die OParl-API zustandslos arbeitet (vgl. [RESTful]{#restful}),
hat ZWINGEND auch für den Abruf von Dateien zu gelten. Es DÜRFEN daher keine
Session-spezifischen URLs oder Ähnliches für den Dateizugriff gebildet werden.

Damit wird erreicht, dass Clients die Zugriffs-URLs aus dem `oparl:File` für
längere Zeit speichern bzw. cachen können.

### Weiterleitungen

Es ist im Rahmen dieser Spezifikation problemlos möglich, die Anfrage an eine
Datei-URL mit einer HTTP-Weiterleitung zu beantworten, um dem Client eine
andere URL zum Zugriff mitzuteilen.

In diesem Fall wird dringend EMPFOHLEN, die Unterscheidung der Bedeutung der
HTTP-Status-Codes `301` und `307` zu beachten.

* `301` SOLL verwendet werden, wenn die vom Client angefragte URL auch zukünftig
  nicht mehr gültig sein wird. Clients erhalten damit das Signal, die bisherige
  URL zu verwerfen und zukünftig die neue, vom Server in der Antwort mitgeteilte
  zu verwenden.

* `307` SOLL verwendet werden, wenn die vom Client genutzte URL nur temporär auf
  eine bestimmte andere URL weiter leitet. Clients werden so aufgefordert, die
  vorhandene URL auch bei zukünftigen Anfragen zu nutzen.

### Entfernte Dateien

Beim Zugriff auf eine Datei, die zuvor einmal abrufbar war, es inzwischen jedoch
nicht mehr ist, SOLL die HTTP-Antwort des Servers den spezifischen Status-Code
`410` tragen.
