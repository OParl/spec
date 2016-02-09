Dateizugriffe  {#dateizugriff}
-------------

Mit dem Begriff "Datei" sind im Sinne dieser Spezifikation alle Ressourcen
gemeint, die von einem OParl-Server zur Verfügung gestellt werden und
deren Metadaten über die JSON-API als [`oparl:File`](#entity-file)
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

Grundsätzlich gilt, dass jede Datei mittels HTTP-Anfrage unter Verwendung der
HTTP-Methode `GET` abrufbar sein MUSS.

Die URLs zum Abruf der einzelnen Datei stellt der Server dem Client in den
Daten des Metadaten-Objekts zur Verfügung. Details finden sich in der
Schema-Beschreibung zu [`oparl:File`](#file).

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

Der in diesem Header kommunizierte Dateiname ist als Vorschlag an die Nutzerin
zu verstehen, die Datei unter diesem Namen zu speichern. Entsprechend sind Abwägungen
bezüglich der Verständlichkeit, Leserlichkeit und Einzigartigkeit des Dateinamens,
aber auch in Hinblick auf den verwendeten Zeichenumfang zu berücksichtigen. Es
wird EMPFOHLEN, den Dateinamen ausschließlich aus dem ASCII-Zeichenvorrat zu bilden.

Im Unterschied zum Zugriff auf die Download-URL DARF der Server beim Zugriff auf die
Zugriffs-URL KEINEN `Content-Disposition` Header mit Parameter `attachment`
senden.
