## Eigenschaften mit Verwendung in mehreren Objekttypen {#eigenschaften-mit-verwendung-in-mehreren-objekttypen}

### `id` {#eigenschaft-id}

Die Eigenschaft `id` enthält den eindeutigen Bezeichner des Objekts, nämlich seine URL.
Dies ist ein **zwingendes** Merkmal für jedes Objekt.

### `type` {#eigenschaft-type}

Objekttypenangabe des Objekts, **zwingend** für jedes Objekt. Der Wert ist
eine Namespace-URL. Für die OParl-Objekttypen sind die folgenden URLs
definiert:

Typ (kurz)               | Namespace-URL
-------------------------|-------------------------------------------
`oparl:AgendaItem`       |https://schema.oparl.org/1.0/AgendaItem
`oparl:Body`             |https://schema.oparl.org/1.0/Body
`oparl:Consultation`     |https://schema.oparl.org/1.0/Consultation
`oparl:File`             |https://schema.oparl.org/1.0/File
`oparl:LegislativeTerm`  |https://schema.oparl.org/1.0/LegislativeTerm
`oparl:Location`         |https://schema.oparl.org/1.0/Location
`oparl:Meeting`          |https://schema.oparl.org/1.0/Meeting
`oparl:Membership`       |https://schema.oparl.org/1.0/Membership
`oparl:Organization`     |https://schema.oparl.org/1.0/Organization
`oparl:Paper`            |https://schema.oparl.org/1.0/Paper
`oparl:Person`           |https://schema.oparl.org/1.0/Person
`oparl:System`           |https://schema.oparl.org/1.0/System

### `name` und `shortName` {#eigenschaft-name-shortname}

Beide Eigenschaften können bei vielen Objekttypen genutzt werden um den
Namen des Objekts anzugeben. Üblicherweise ist `name` eine Pflichteigenschaft
für den ausgeschriebenen offiziellen Namen, während `shortName` optional
angegeben werden kann. Dies ist dann zu empfehlen, wenn zu einem Namen eine
kurze bzw. kompakte und eine längere, aber weniger nutzerfreundliche Variante
existieren. So ist "Innenministerium" die Kurzform des offiziellen
"Bundesministerium des Inneren".

### `license` {#eigenschaft_license}

Mit `license` wird angegeben, unter welcher Lizenz die Daten des jeweiligen
Objekts stehen. ^[Verzeichnisse für Lizenz-URLs sind unter anderem unter
<http://licenses.opendefinition.org/> und
<https://github.com/fraunhoferfokus/ogd-metadata/blob/master/lizenzen/deutschland.json>
zu finden. Allgemeine Informationen zur Lizensierung von Open Data finden sich auch
im Open Data Handbook der Open Knowledge Foundation unter
<http://opendatahandbook.org/de/how-to-open-up-data/apply-an-open-license.html>.]

Wird `license` im `oparl:System`-Objekt oder am `oparl:Body`-Objekt verwendet,
dann bedeutet das, dass alle Objekte dieses Systems bzw. der Körperschaft
unter der angegebenen Lizenz veröffentlicht werden, sofern nicht das
einzelne Objekt eine anders lautende Lizenz-URL angibt. Es wird **empfohlen**,
die Lizenzinformation sofern möglich global am `oparl:System` Objekt mitzuteilen
und auf redundante Informationen zu verzichten.

### `created` {#eigenschaft-created}

Datum und Uhrzeit der Erstellung des jeweiligen Objekts.

Diese Eigenschaft **muss** in allen Objekttypen angegeben werden, die nicht
in anderen Objekten intern ausgegeben werden.

### `modified` {#eigenschaft-modified}

Diese Eigenschaft kennzeichnet stets Datum und Uhrzeit der letzten Änderung des
jeweiligen Objekts.

Diese Eigenschaft **muss** - genau wie `created` - in allen Objekttypen angegeben
werden, die nicht in anderen Objekten intern ausgegeben werden.

Es ist **zwingend**, dass bei jeder Änderung eines Objekts der Wert dieses
Attributs auf die zu diesem Zeitpunkt aktuelle Uhrzeit gesetzt wird, da ein
Client in der Regel seinen Datenbestand nur auf Basis dieses Attributs
verlustfrei aktualisieren kann.

### `keyword` {#eigenschaft-keyword}

Die Eigenschaft `keyword` dient der optionalen Kategorisierung eines Objekts.

### `web` {#eigenschaft-web}

Gibt die URL einer Website an, die das Objekt im Browser darstellt. Das
ist z.B. die HTML-Ansicht eines parlamentarischen Informationssystems.

### `deleted` {#eigenschaft-deleted}

Falls das Objekt gelöscht wurde, muss dieses gemäß Kapitel 2.8 das Attribut
`deleted: true` bekommen.
