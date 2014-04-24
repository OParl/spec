Eigenschaften mit Verwendung in mehreren Objekttypen
----------------------------------------------------

TODO: Sauber ausformulieren

Für Datum und Zeit werden die in XML Schema festgelegten Typen verwendet (was nicht bedeutet, dass in OParl XML verwendet wird).

Für ein Datum wird http://www.w3.org/TR/xmlschema-2/#date verwendet und für eine Zeit http://www.w3.org/TR/xmlschema-2/#dateTime. Dabei wird ein Datum (ein Tag ohne Uhrzeit) ohne Zeitzone und ein Datum mit Zeit mit Zeitzone angegeben, denn nur damit ist die Uhrzeit weltweit eindeutig ohne zusätzlich auf den Ort einer Sitzung o.ä. Bezug nehmen zu müssen.

Diese Spezifikationen stützen sich auf RFC 3339 (http://www.ietf.org/rfc/rfc3339.txt) und RFC 3339 wiederum auf ISO 8601.

Im JSON-LD Kontext von OParl ist der Präfix 'xsd' so spezifiziert, dass Datums- und Zeittyp durch 'xsd:date' bzw. 'xsd:dateTime' abgekürzt werden können.

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

