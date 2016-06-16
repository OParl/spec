## Gelöschte Objekte {#geloeschte-objekte}

Wenn ein Objekt gelöscht wird, so muss das Objekt in OParl gesondert vermerkt
werden. Es **darf** insbesondere **nicht** einfach gelöscht werden,
so dass unter der betreffenden URL kein gültiges Objekt ausgeliefert wird.

Hintergrund ist, dass alle OParl-Clients zeitnah erfahren müssen,
wenn ein Objekt gelöscht wurde. Dies wird durch die folgenden Regeln
gewährleistet.

Wenn ein Objekt gelöscht wird,

* **muss** das Objekt das zusätzliche Attribut `deleted`: true bekommen
* **muss** das Attribut `modified` auf den Zeitpunkt der Löschung setzen
* **müssen** die Attribute `id`, `type` und `created` erhalten bleiben

Dies gilt nur für Hauptobjekte und globale Subobjekte (d.h. System, Body, Organisation, Person,
Meeting, Paper, File, Location). D.h. Subobjekte (LegislativeTerm, Membership, AgendaItem, Consultation)
benötigen nicht das Attribut `deleted`, sondern können einfach gelöscht werden. Beim Löschen einer
der Subobjekte muss allerdings der Wert `modified` des dazugehörigen Hauptobjektes aktualisiert werden.
Als HTTP-Statuscode muss weiterhin 200 verwendet werden.

Dies garantiert, dass das gelöschte Objekt beim Updaten eines Client-Datenbestandes
aktualisiert wird, wenn der client nur seit dem letzten Update aktualisierte Objekte abruft.
