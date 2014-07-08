Cross-Origin Resource Sharing (CORS)  {#cors}
------------------------------------

Wenn Webbrowser mittels Script auf JSON-Ressourcen zugreifen sollen,
unterliegen diese Zugriffe üblicherweise einer _Same-Origin-Policy_ (SOP).
Das heißt, eine Anfrage ist nur an den Server zulässig, der auch das
initiierende Script ausgeliefert hat. Anfragen an andere Server werden
vom Browser blockiert. Diese Einschränkung dient allgemein
der Sicherheit von Webbrowsern.^[vgl. Wikipedia: Same-Origin-Policy <https://de.wikipedia.org/wiki/Same-Origin-Policy>]

Um die Informationen von OParl-Servern auch im Kontext von Webanwendungen
flexibel nutzen zu können, ist die Überwindung der SOP nötig. Hierzu dient
_Cross-Origin Resource Sharing_ (CORS)^[Cross Origin Resource Sharing - 
W3C Recommendation 16. Januar 2014: <http://www.w3.org/TR/cors/>]. Mittels CORS
kann ein Server mitteilen, dass bestimmte von ihm ausgelieferte Ressourcen
auch innerhalb von Webapplikationen genutzt werden dürfen, die nicht von
demselben Server ausgeliefert werden. Technisch wird dies durch Ausgabe
zusätzlicher HTTP-Header erreicht.

OParl-Server SOLLEN für jegliche Anfrage, die mit der Ausgabe von JSON-Daten
beantwortet wird (das sind alle Anfragen außer [Dateizugriffe](#dateizugriff))
den folgenden HTTP-Antwort-Header senden:

    Access-Control-Allow-Origin: *

Der HTTP-Antwort-Header `Access-Control-Allow-Methods` SOLL darüber hinaus
entweder NICHT gesetzt sein oder die Methode `GET` beinhalten.

EntwicklerInnen von Webanwendungen sollten sich darüber bewusst sein, dass
durch die direkte Einbindung von Scripten dritter in ihre Anwendungen mögliche
Sicherheitsrisiken entstehen. Für den Fall, dass ein OParl-Server, etwa in
Folge einer Manipulation, Schadcode ausliefert, könnte dieser unmittelbar
von Scripten im Browser ausgeführt werden.
