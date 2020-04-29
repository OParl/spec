## Gelöschte Objekte {#geloeschte-objekte}

In OParl **dürfen** Objekte **nicht** einfach gelöscht werden, sodass unter
der betreffenden URL kein gültiges Objekt ausgeliefert wird. Stattdessen
 wird ein sogenanntes _soft delete_ verwendet.

Hintergrund ist, dass OParl-Clients bei der Aktualisierung ihres
 Datenbestandes, z.B. mit den [Filtern](#filter) `modified_since` bzw.
 `created_since`, erfahren können müssen, welche Objekte gelöscht wurden.

Dies wird durch die folgenden Regeln gewährleistet.

Wenn ein Objekt gelöscht wird,

* **muss** das Objekt das zusätzliche Attribut `deleted` mit dem Wert
`true` bekommen
* **muss** das Attribut `modified` auf den Zeitpunkt der Löschung setzen
* **müssen** die Attribute `id`, `type` und `created` erhalten bleiben
* **dürfen** alle weiteren Attribute entfernt werden

Als HTTP-Statuscode **muss** weiterhin 200 verwendet werden.

Neu in OParl 1.1: Die Objekte _LegislativeTerm_, _Membership_, _AgendaItem_ und
_Consultation_ dürfen nicht mehr einfach gelöscht werden. Um Kompatibilität zu
OParl 1.0 zu gewährleisten muss weiterhin der Wert `modified` aller Objekte
aktualisiert werden, in die dieses Objekt eingebettet war.

### Depublizierung von Objekten

Da es sich bei OParl um eine Schnittstelle für öffentliche Daten handelt werden
depublizierte Objekte im Sinne der Schnittstelle gelöscht und **sollen** wie oben
behandelt werden.
