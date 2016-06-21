## Gelöschte Objekte {#geloeschte-objekte}

Das Löschen der Objekte System, Body, Organisation, Person, Meeting, Paper, File und Location
muss in OParl gesondert vermerkt werden. Es **darf** insbesondere **nicht** einfach gelöscht werden,
so dass unter der betreffenden URL kein gültiges Objekt ausgeliefert wird.

Hintergrund ist, dass alle OParl-Clients zeitnah erfahren müssen,
wenn ein Objekt gelöscht wurde. Dies wird durch die folgenden Regeln
gewährleistet.

Wenn ein Objekt gelöscht wird,

* **muss** das Objekt das zusätzliche Attribut `deleted`: true bekommen
* **muss** das Attribut `modified` auf den Zeitpunkt der Löschung setzen
* **müssen** die Attribute `id`, `type` und `created` erhalten bleiben

Als HTTP-Statuscode muss weiterhin 200 verwendet werden.

Die Objekte LegislativeTerm, Membership, AgendaItem und Consultation können dagegen einfach
gelöscht werden. Beim Löschen dieser Objekte muss allerdings der Wert `modified` aller
Objekte aktualisiert werden, in der dieses Objekt eingebunden war.

Dies garantiert, dass das gelöschte Objekt beim Updaten eines Client-Datenbestandes
aktualisiert wird, wenn der Client nur seit dem letzten Update aktualisierte Objekte abruft.
