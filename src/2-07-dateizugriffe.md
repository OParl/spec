Dateizugriffe  {#dateizugriff}
-------------

Mit dem Begriff "Datei" sind im Sinne dieser Spezifikation alle Ressourcen
gemeint, die von einem OParl-Server zur Verfügung gestellt werden und
deren Metadaten über die JSON-API als [`oparl:File`](#entity-file)
abgerufen werden können. Es handelt sich dabei beispielsweise um Textdokumente
im PDF-Format oder Abbildungen im JPEG- oder PNG-Format.

Jede Datei **muss** dabei mit einer HTTP-GET-Anfrage abrufbar sein.

### Empfehlungen für Dateizugriffe

* Ein Server **sollte** die Verwendung von Kompression gemäß dem HTTP-Standard
unterstützen.

* Ein Server **sollte** "Conditional GET", insbesondere
`If-Modified-Since` und `If-None-Match` sowie "Chunked GET" unterstützen.

* Die Ausgabe der HTTP-Header `Last-Modified`, `Content-Length` und `ETag` ist
**empfohlen**.

* Bei gelöschten Dateien **sollte** der HTTP-Statuscode `410` verwendet werden.

### Allgemeiner Zugriff und expliziter Download

Mit der im `oparl:File` **zwingend** anzugebenden Eigenschaft `accessUrl` liefert
der Server dem Client eine URL, die dem allgemeinen Zugriff auf die Datei dient.
Beim Zugriff auf dieser URL **darf** der Server **nicht** den `Content-Disposition`-Header
mit dem Parameter `attachment` senden. ^[vgl. RFC2138<http://www.ietf.org/rfc/rfc2183>]

Es wird daher **empfohlen**, zusätzlich eine Eigenschaft `downloadUrl` anzubieten. Beim
Zugriff auf die Download-URL **muss** der Server in der HTTP-Antwort einen
`Content-Disposition`-Header senden, der als ersten Parameter den
Typ `attachment` enthält und mit dem `filename`-Parameter den Namen der Datei
angibt.

Beispiel:

    Content-Disposition: attachment; filename="2014-08-22 Rat Wortprotokoll.pdf"
