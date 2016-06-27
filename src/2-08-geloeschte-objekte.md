## Gelöschte Objekte {#geloeschte-objekte}

Das Löschen der Objekte _System_, _Body_, _Organisation_, _Person_, _Meeting_, _Paper_, _File_ und _Location_
muss in OParl gesondert vermerkt werden. Es **darf** insbesondere **nicht** einfach gelöscht werden,
so dass unter der betreffenden URL kein gültiges Objekt ausgeliefert wird.

Hintergrund ist, dass alle OParl-Clients zeitnah erfahren können müssen,
wenn ein Objekt gelöscht wurde. Dies wird durch die folgenden Regeln
gewährleistet.

Wenn ein Objekt gelöscht wird,

* **muss** das Objekt das zusätzliche Attribut `deleted`: true bekommen
* **muss** das Attribut `modified` auf den Zeitpunkt der Löschung setzen
* **müssen** die Attribute `id`, `type` und `created` erhalten bleiben

Als HTTP-Statuscode muss weiterhin 200 verwendet werden.

Die Objekte _LegislativeTerm_, _Membership_, _AgendaItem_ und _Consultation_ können dagegen einfach
gelöscht werden. Beim Löschen dieser Objekte muss allerdings der
Wert `modified` aller Objekte aktualisiert werden, in die dieses Objekt
eingebunden war.

Dies garantiert, dass das gelöschte Objekt beim Updaten eines Client-Datenbestandes
aktualisiert wird, falls der Client nur seit dem letzten Update aktualisierte Objekte abruft.
