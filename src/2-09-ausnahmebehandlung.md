## Ausnahmebehandlung  {#ausnahmebehandlung}

Wenn ein Server eine Anfrage eine Anfrage nicht bearbeiten kann, z.B. weil die
URL ungültig ist oder das angefragte Objekt nicht existiert, dann SOLLTE er
mit dem entsprechenden HTTP-Statuscode antworten.

Ein Client kann nicht vorraussetzen, dass im Fall einer Ausnahme noch weitere
verwertbare Informationen wie ein Fehlermeldung gesendet werden.
