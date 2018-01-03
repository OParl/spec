Cross-Origin Resource Sharing (CORS)  {#cors}
------------------------------------

Wenn Webbrowser mittels Skript auf JSON-Ressourcen zugreifen sollen
unterliegen diese Zugriffe üblicherweise einer _Same-Origin-Policy_ (SOP).
Das heißt, eine Anfrage ist nur an den Server zulässig, der auch das
initiierende Skript ausgeliefert hat. Anfragen an andere Server werden
vom Browser blockiert. Diese Einschränkung dient im Allgemeinen
der Sicherheit von Webbrowsern.^[vgl. Wikipedia: Same-Origin-Policy <https://de.wikipedia.org/wiki/Same-Origin-Policy>]

Um die Daten von OParl-Servern auch im Kontext von Webanwendungen
flexibel nutzen zu können, ist die Überwindung der SOP nötig. Hierzu dient
_Cross-Origin Resource Sharing_ (CORS)^[Cross Origin Resource Sharing -
W3C Recommendation 16. Januar 2014: <http://www.w3.org/TR/cors/>]. Mittels CORS
kann ein Server mitteilen, dass bestimmte von ihm ausgelieferte Ressourcen
auch innerhalb von Webapplikationen genutzt werden dürfen, die nicht vom selben Server ausgeliefert werden. Technisch wird dies durch Ausgabe
zusätzlicher HTTP-Header erreicht.

OParl-Server **müssen** für jegliche Anfrage, die mit der Ausgabe von JSON-Daten
beantwortet wird (das sind alle Anfragen außer [Dateizugriffe](#dateizugriff))
den folgenden HTTP-Antwort-Header senden:

    Access-Control-Allow-Origin: *

Der HTTP-Antwort-Header `Access-Control-Allow-Methods` **sollte** darüber hinaus
**nicht** gesetzt sein, oder **muss** die Methode `GET` beinhalten.

Entwicklerinnen von Webanwendungen sollten sich darüber bewusst sein, dass
durch die direkte Einbindung von Skripten Dritter in ihre Anwendungen mögliche
Sicherheitsrisiken entstehen. Für den Fall, dass ein OParl-Server, etwa in
Folge einer Manipulation, Schadcode ausliefert, könnte dieser unmittelbar
von Skripten im Browser ausgeführt werden.
