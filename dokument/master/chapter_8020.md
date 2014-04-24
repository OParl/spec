Eigenschaften mit Verwendung in mehreren Objekttypen
----------------------------------------------------

### `@id`

URL des Objekts und eindeutiges Identifikationsmerkmal. Siehe dazu auch "Benannte Objekte".
Dies ist ein ZWINGENDES Merkmal für jedes Objekt.

### `@type`

Objekttypenangabe des Objekts. ZWINGEND für jedes Objekt.

### `name` und `nameLong`

Beide Eigenschaften können bei vielen Objekttypen genutzt werden, um den nutzerfreundlichen
Namen des Objekts anzugeben. Üblicherweise ist `name` eine Pflichteigenschaft, während
nameLong optional angegeben werden kann. Dies ist dann zu empfehlen, wenn zu einem Namen
eine kurze bzw. kompakte und eine längere, aber weniger nutzerfreundliche Variante
existieren. Ein Beispiel wäre die Kurzform "CDU" für den Parteinamen "Christlich Demokratische
Union Deutschlands".

In keinem Fall sollten die Werte von `name` und `nameLong` identische sein.

### `license`

Die Eigenschaft `license` erlaubt es, am jeweiligen Objekt die URL einer Lizenz
anzugeben. Damit wird gekennzeichnet, welche Lizenz der Veröffentlicher der
Daten für das jeweilige Objekt vergibt.

Eine besondere Bedeutung hat die Eigenschaft `license`, wenn sie am `oparl:System`
Objekt vergeben wird. Die hier angegebene Lizenzinformation sagt aus, dass alle
Objekte dieses Systems unter der angegebenen Lizenz veröffentlicht werden, sofern
dies nicht am jeweiligen Objekt mit einer anders lautenden Lizenz-URL überschrieben
wird. Daher wird dringend EMPFOHLEN, die Lizenzinformation global am `oparl:System`
Objekt mitzuteilen und auf redundante Informationen zu verzichten.

Auf Objekte vom Typ `oparl:Document` bezogen bezieht sich die Lizenzinformation
nicht nur auf die strukturierten Metadaten, die über die API bezogen werden, sondern
auch auf den eigentlichen Inhalt der Dateien, die über die angebotene(n) URL(s)
abgerufen werden können.

### `created`

Datum und Uhrzeit der Erstellung des jeweiligen Objekts.

### `lastModified`

Diese Eigenschaft kennzeichnet stets Datum und Uhrzeit der letzten Änderung des
jeweiligen Objekts.

In Einzelfällen unterliegt die Frage, was als Änderung eines Objekts bezeichnet werden
kann, einem gewissen Interpretationsspielraum. Beispielsweise ist zu entscheiden,
ob eine Gruppierung (`oparl:Organization`) als geändert gilt, wenn ein neues Mitglied 
hinzugefügt wurde.

Diese Frage sollte aus Sicht des OParl-Clients beantwortet werden. Wenn beispielsweise
eine Gruppierung vom Server grundsätzlich mit der Liste der URLs aller Mitglieder ausgegeben
wird, umfasst das Objekt aus Sicht des Clients eben auch die Liste der Mitglieder. In diesem
Fall wäre eine Veränderung der Liste der Mitglieder als Änderung des Objekts zu verstehen,
die im `lastModified` Zeitstempel wiederspiegeln sollte.

