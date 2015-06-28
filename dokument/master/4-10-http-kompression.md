HTTP-Kompression
----------------

Die zwischen Servern und Clients übertragenen Datenvolumen SOLLEN
mit Hilfe von Kompressionsverfahren reduziert werden, wenn sowohl
der Client als auch der Server dies unterstützen. Dabei kommt
das in HTTP 1.1^[RFC7231 Section 5.3.4:
<http://tools.ietf.org/html/rfc7231#section-5.3.4>]
beschriebene Verfahren zum Einsatz.

HTTP 1.1 stellt drei komprimierte Kodierungen vor, wobei die Liste
durch Registrierung neuer Verfahren bei der IANA erweitert werden
kann. Diese sind:

* gzip
* compress
* deflate

Server-Implementierer SOLLEN mindestens eines dieser drei Verfahren
unterstützen, wenn Clients dies mittels Accept-Encoding-Header
anfragen.

Die Verwendung von HTTP-Kompression ist grundsätzlich sowohl bei
JSON-Daten als auch bei Dateizugriffen möglich. Bei Dateizugriffen
sind die zu erwartenden Einsparungen beim Datenvolumen stark
abhängig vom jeweiligen Dateifomat. Bei bereits komprimierten Dateien
wie beispielsweise OpenOffice oder PDF lassen sich oft nur geringe
oder gar keine weiteren Ersparnisse erzielen. Daher DARF grundsätzlich
der Server in solchen Fällen eine unkomprimierte HTTP-Antwort senden,
auch wenn der Client ein unterstütztes Kompressionsverfahren angefragt
hat.
