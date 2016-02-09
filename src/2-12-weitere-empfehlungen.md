## Weitere Empfehlungen {#weitere-empfehlungen}

* Ein Server SOLLTE die Verwendung von Kompression gemäß dem HTTP-Standard
unterstützen.

* Ein Server SOLLTE auch "Conditional GET" unterstüzen, insbesondere
`If-Modified-Since` und `If-None-Match`.

* Für den Dateiabruf wird die Ausgabe der HTTP-Header `Last-Modified`,
`Content-Length` und `ETag` EMPFOHLEN.

* Bei gelöschten Dateien SOLLTE der HTTP-Statuscode `410` verwendet werden.
