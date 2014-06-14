Ausnahmebehandlung  {#ausnahmebehandlung}
------------------

Nicht immer kann ein Server die Anfrage eines Clients erfolgreich, also im Sinne
der Anfrage, behandeln und eine entsprechende Antwort liefern. Beispiele für solche
Ausnahmefälle könnten sein (ohne Anspruch auf Vollständigkeit):

* Eine angefragte Ressource existiert nicht

* Der Client nutzt eine nicht unterstützte HTTP-Methode, z. B. `POST`

* Der Client nutzt einen nicht interpretierbaren URL-Parameter

Die HTTP-1.1-Spezifikation sieht für derartige und weitere Ausnahmefälle
zahlreiche spezifische Status-Codes vor, die hier nicht wiederholt werden
sollen. Verallgemeinernd lautet die Anforderung an jeden OParl-Server,
dass diese Ausnahmen mit den entsprechenden HTTP-Status-Codes beantworten
SOLLEN. Damit wird Client-Entwicklern die Möglichkeit gegeben, diese Fälle
entsprechend zu behandeln.

Clients DÜRFEN darüber hinaus nicht davon ausgehen, dass mit der HTTP-Antwort
im Fall einer Ausnahme noch weitere verwertbare Informationen wie z. B. eine
Fehlermeldung gesendet werden.
