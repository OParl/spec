Eigenschaften mit Verwendung in mehreren Objekttypen
----------------------------------------------------

### `@id`

Die Eigenschaft `@id` ist durch die JSON-LD-Spezifikation vorgegeben
und enthält einen eindeutigen Bezeichner des Objekts, nämlich seine URL.
Siehe dazu auch [Benannte Objekte](#benannte_objekte). Dies ist ein 
ZWINGENDES Merkmal für jedes Objekt.

### `@type`

Objekttypenangabe des Objekts im Sinne von JSON-LD. ZWINGEND für jedes Objekt.
Der Wert ist (in Verbindung mit dem JSON-LD-Kontext eines Objekts) eine URL,
unter der weitere Informationen über den Objekttyp angeboten werden KÖNNEN.

### `name` und `shortName`

Beide Eigenschaften können bei vielen Objekttypen genutzt werden, um den
Namen des Objekts anzugeben. Üblicherweise ist `name` eine Pflichteigenschaft
für den ausgeschriebenen offiziellen Namen, während `shortName` optional angegeben werden kann.
Dies ist dann zu empfehlen, wenn zu einem Namen eine kurze bzw. kompakte und eine
längere, aber weniger nutzerfreundliche Variante existieren. Ein Beispiel wäre
die offizielle Kurzform "CDU" für den offiziellen Parteinamen "Christlich Demokratische Union Deutschlands".

Die Werte von `name` und `shortName` SOLLEN nicht identisch sein.

### `license` {#eigenschaft_license}

Die Eigenschaft `license` erlaubt es, am jeweiligen Objekt die URL einer Lizenz
anzugeben. Damit wird gekennzeichnet, welche Lizenz der Veröffentlicher der
Daten für das jeweilige Objekt vergibt.^[Verzeichnisse für Lizenz-URLs sind
unter anderem unter <http://licenses.opendefinition.org/> und 
<https://github.com/fraunhoferfokus/ogd-metadata/blob/master/lizenzen/deutschland.json>
zu finden.]

Eine besondere Bedeutung hat die Eigenschaft `license`, wenn sie am `oparl:System` Objekt oder am `oparl:Body`
Objekt vergeben wird. Die hier angegebene Lizenzinformation sagt aus, dass alle
Objekte dieses Systems bzw. der Körperschaft unter der angegebenen Lizenz veröffentlicht werden, sofern
dies nicht am jeweiligen Objekt mit einer anders lautenden Lizenz-URL überschrieben
wird. Daher wird dringend EMPFOHLEN, die Lizenzinformation global am `oparl:System`
Objekt mitzuteilen und auf redundante Informationen zu verzichten.

An Objekten vom Typ `oparl:File` auftretend, bezieht sich die Lizenzinformation
nicht nur auf die strukturierten Metadaten, die über die API bezogen werden, sondern
auch auf den eigentlichen Inhalt der Datei(en), die über die angebotene(n) URL(s)
abgerufen werden können.

Lesenswert zum Thema Lizensierung von Linked Data ist auch er Abschnitt "Licenses,
Waivers and Norms for Data" im online zugänglichen Linked Data Book.^[Tom Heath, Christian Bizer: Linked Data: Evolving the Web into a Global Data Space (1st edition), <http://linkeddatabook.com/editions/1.0/#htoc48>]

### `created`

Datum und Uhrzeit der Erstellung des jeweiligen Objekts.

Datentyp: `xsd:dateTime`.

### `modified`

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
die im `modified` Zeitstempel widerspiegeln sollte.

Datentyp: `xsd:dateTime`.

### `keyword`

Die Eigenschaft `keyword` dient der Kategorisierung von Objekten und ist in
einer Vielzahl von Objekttypen zu diesem Zweck einsetzbar.

Mehr zur Funktionsweise dieser Eigenschaft wird im Abschnitt
[Vokabulare zur Klassifizierung](#vokabulare_klassifizierung) beschrieben.
