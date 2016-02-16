## Eigenschaften mit Verwendung in mehreren Objekttypen {#eigenschaften-mit-verwendung-in-mehreren-objekttypen}

### `id` {#eigenschaft-id}

Die Eigenschaft `id` ist für jeden OParl-Objekttypen vorgegeben
und enthält den eindeutigen Bezeichner des Objekts, nämlich seine URL.
Dies ist ein **zwingendes** Merkmal für jedes Objekt.

### `type` {#eigenschaft-type}

Objekttypenangabe des Objekts, **zwingend** für jedes Objekt. Der Wert ist
eine Namespace-URL. Für die OParl-Objekttypen sind die folgenden URLs
definiert:

Typ (kurz)               | Namespace-URL
-------------------------|-------------------------------------------
`oparl:AgendaItem`       |https://oparl.org/schema/1.0/AgendaItem
`oparl:Body`             |https://oparl.org/schema/1.0/Body
`oparl:Consultation`     |https://oparl.org/schema/1.0/Consultation
`oparl:File`             |https://oparl.org/schema/1.0/File
`oparl:LegislativeTerm`  |https://oparl.org/schema/1.0/LegislativeTerm
`oparl:Location`         |https://oparl.org/schema/1.0/Location
`oparl:Meeting`          |https://oparl.org/schema/1.0/Meeting
`oparl:Membership`       |https://oparl.org/schema/1.0/Membership
`oparl:Organization`     |https://oparl.org/schema/1.0/Organization
`oparl:Paper`            |https://oparl.org/schema/1.0/Paper
`oparl:Person`           |https://oparl.org/schema/1.0/Person
`oparl:System`           |https://oparl.org/schema/1.0/System

### `name` und `shortName` {#eigenschaft-name-shortname}

Beide Eigenschaften können bei vielen Objekttypen genutzt werden, um den
Namen des Objekts anzugeben. Üblicherweise ist `name` eine Pflichteigenschaft
für den ausgeschriebenen offiziellen Namen, während `shortName` optional
angegeben werden kann. Dies ist dann zu empfehlen, wenn zu einem Namen eine
kurze bzw. kompakte und eine längere, aber weniger nutzerfreundliche Variante
existieren. Ein Beispiel wäre die Kurzform "CDU" für den offiziellen
Parteinamen "Christlich Demokratische Union Deutschlands".

### `license` {#eigenschaft_license}

Die Eigenschaft `license` erlaubt es, am jeweiligen Objekt die URL einer Lizenz
anzugeben. Damit wird gekennzeichnet, welche Lizenz der Veröffentlicher der
Daten für das jeweilige Objekt vergibt.^[Verzeichnisse für Lizenz-URLs sind
unter anderem unter <http://licenses.opendefinition.org/> und
<https://github.com/fraunhoferfokus/ogd-metadata/blob/master/lizenzen/deutschland.json>
zu finden. Allgemeine Informationen zur Lizensierung von Open Data finden sich auch
im Open Data Handbook der Open Knowledge Foundation unter
<http://opendatahandbook.org/de/how-to-open-up-data/apply-an-open-license.html>.]

Eine besondere Bedeutung hat die Eigenschaft `license`, wenn sie am `oparl:System` Objekt oder am `oparl:Body`
Objekt vergeben wird. Die hier angegebene Lizenzinformation sagt aus, dass alle
Objekte dieses Systems bzw. der Körperschaft unter der angegebenen Lizenz veröffentlicht werden, sofern
dies nicht am jeweiligen Objekt mit einer anders lautenden Lizenz-URL überschrieben
wird. Daher wird dringend **empfohlen**, die Lizenzinformation global am `oparl:System`
Objekt mitzuteilen und auf redundante Informationen zu verzichten.

An Objekten vom Typ `oparl:File` auftretend, bezieht sich die Lizenzinformation
nicht nur auf die strukturierten Metadaten, die über die API bezogen werden, sondern
auch auf den eigentlichen Inhalt der Datei(en), die über die angebotene(n) URL(s)
abgerufen werden können.

### `created` {#eigenschaft-created}

Datum und Uhrzeit der Erstellung des jeweiligen Objekts.

### `modified` {#eigenschaft-modified}

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

### `keyword` {#eigenschaft-keyword}

Die Eigenschaft `keyword` dient der optionalen Kategorisierung von Objekten und ist in einer Vielzahl von Objekttypen zu diesem Zweck einsetzbar.
