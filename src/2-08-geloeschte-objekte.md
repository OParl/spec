## Gelöschte Objekte {#geloeschte-objekte}

Das Löschen der Objekte _oparl:System_, _oparl:Body_, _oparl:Organisation_, _oparl:Person_, _oparl:Meeting_,
_oparl:Paper_, _oparl:File_ und _oparl:Location_ muss in OParl gesondert vermerkt werden.
Es **darf** insbesondere **nicht** einfach gelöscht werden, so dass unter der
betreffenden URL kein gültiges Objekt ausgeliefert wird.

Hintergrund ist, dass alle OParl-Clients zeitnah erfahren können müssen,
wenn ein Objekt gelöscht wurde. Dies wird durch die folgenden Regeln
gewährleistet.

Wenn ein Objekt gelöscht wird,

* **muss** das Objekt das zusätzliche Attribut `deleted`: true bekommen
* **muss** das Attribut `modified` auf den Zeitpunkt der Löschung setzen
* **müssen** die Attribute `id`, `type` und `created` erhalten bleiben

Als HTTP-Statuscode **muss** weiterhin 200 verwendet werden.

Neu in OParl 1.1: Die Objekte _LegislativeTerm_, _Membership_, _AgendaItem_ und
_Consultation_ dürfen nicht mehr einfach gelöscht werden. Um Kompatibilität zu
OParl 1.0 zu gewährleisten muss weiterhin der Wert `modified` aller Objekte
aktualisiert werden, in die dieses Objekt eingebunden war.
