## Ausnahmebehandlung {#ausnahmebehandlung}

Wenn ein Server eine Anfrage nicht bearbeiten kann, z.B. weil die
URL ungültig ist oder das angefragte Objekt nicht existiert, dann **sollte** er
mit dem entsprechenden HTTP-Statuscode antworten.

Ein Server **sollte** in diesem Fall ein Objekt ausgeben, das die folgenden
3 Attribute enthält:

 * `type`: Enthält als Wert die URL `https://schema.oparl.org/1.0/Error`
 * `message`: Eine Fehlermeldung, die zur Anzeige für einen Nutzer
 gedacht ist. Die Fehlermeldung sollte deshalb in der Sprache der durch die
 Schnittstelle ausgelieferten Inhalte verfasst sein
 * `debug`: Zusätzliche Informationen über den Fehler

 Wenn ein Server ein solches Objekt ausgibt, dann **muss** er dazu einen
 HTTP-Statuscode senden, der einen Fehler anzeigt.

 Ein Client **darf nicht** voraussetzen, dass er im Fall eines Fehlers
 verwertbare Informationen wie das oben beschriebene Fehlerobjekt erhält.
