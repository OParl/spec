OParlSystem (System)
--------------------

Der Objekttyp `oparl:System` bildet grundlegende Informationen zum
parlamentarischen Informationssystem ab. Das Objekt repräsentiert
das technische System, unabhängig von der Frage, welche Körperschaften
auf diesem System vertreten sind.

Auf jedem OParl Server MUSS ein Objekt vom Typ `oparl:System` vorgehalten
werden. Es DARF nur ein einziges solches Objekt je Server existieren.

Für Clients ist das `oparl:System` Objekt ein geeigneter Einstiegspunkt,
um grundlegende Informationen über das Sytem zu bekommen und die URLs
zum Zugriff auf andere Informationen in Erfahrung zu bringen.

Die URL (IRI) des `oparl:System` Objekts MUSS per Definition identisch mit
der URL des API-Endpunkts des Servers sein.

### Eigenschaft `oparl_version`

Diese Eigenschaft ist ZWINGEND.

URL der Version der OParl-Spezifikation, die von diesem System unterstützt wird.
So lange es nur die Version 1.0 der OParl-Spezifikation gibt, MUSS der Wert dieser
Eigenschaft `http://oparl.org/specs/1.0/` sein.

Sofern zukünftig weitere Versionen der Spezifikation vorliegen, können Clients damit
in Erfahrung bringen, welches Schema, welche Eigenschaften und Methoden auf Seite des
Servers vorausgesetzt werden können.

### Eigenschaft `bodies`

Diese Eigenschaft ist ZWINGEND.

Über diese URL sind alle `oparl:Body` Objekte, also die im System geführten Körperschaften, als Liste abrufbar.

TODO: Verweis auf `oparl:Body` einfügen

### Eigenschaft `name`

Diese Eigenschaft wird EMPFOHLEN.

Diese Eigenschaft dient dazu, einen nutzerfreundlichen Namen zu kommunizieren, mit dem
NutzerInnen das System wiedererkennen und von anderen unterscheiden können.

### Eigenschaft `contact`

Diese Eigenschaft wird EMPFOHLEN.

Die Eigenschaft dient dazu, NutzerInnen bzw. EntwicklerInnen von Clients die Kontaktaufnahme
mit dem Betreiber des Systems zu ermöglichen. Es wird EMPFOHLEN, hier die Kontaktdaten
eines technischen Ansprechpartners bzw. einer allgemeinen Kontaktstelle auszugeben, über die
Anfragen verschiedener Art an die richtige Kontaktperson umgeleitet werden können.

Der Wert dieser Eigenschaft MUSS ein Objekt vom Typ `oparl:Contact` sein.

TODO: Verweis auf `oparl:Contact` einfügen.

### Eigenschaft `license`

Diese Eigenschaft wird EMPFOHLEN.

Die Eigenschaft dient dazu, darüber zu informieren, unter welcher Lizenz die Daten
des aktuell angezeigten Objekts stehen. Zur Vererbung dieser Eigenschaft siehe
(TODO: Verweis auf Abschnitt zur Lizenz-Vererbung einfügen).

Der Wert dieser Eigenschaft sollte nach Möglichkeit eine URL sein, unter der genau die
entsprechende Lizenz abgerufen werden kann.

### Eigenschaft `new_objects`

Diese Eigenschaft ist EMPFOHLEN.

Mit dieser Eigenschaft wird die URL des Feeds für neu hinzugekommene Objekte ausgegeben.

TODO: Verweis auf Feeds > Neue Objekte

### Eigenschaft `updated_objects`

Diese Eigenschaft ist EMPFOHLEN.

Mit dieser Eigenschaft wird die URL des Feeds für geänderte Objekte ausgegeben.

TODO: Verweis auf Feeds > Geänderte Objekte

### Eigenschaft `removed_objects`

Diese Eigenschaft ist EMPFOHLEN.

Mit dieser Eigenschaft wird die URL des Feeds für entfernte Objekte ausgegeben.

TODO: Verweis auf Feeds > Entfernte Objekte

### Eigenschaft `info_url`

Diese Eigenschaft ist OPTIONAL.

Diese Eigenschaft dient dazu, eine zusätzliche URL zu einer
WWW-Seite mit zusätzlichen Informationen zum System anzubieten. So könnten NutzerInnen
beispielsweise auf eine Web-Oberfläche eines parlamentarischen Informationssystems
geführt werden.

### Eigenschaft `vendor_url`

Diese Eigenschaft ist OPTIONAL.

Diese Eigenschaft dient dazu, über eine URL den Hersteller des Server-Systems zu komunizieren.
Die URL sollt nach Möglichkeit zu einer WWW-Seite mit weiteren Informationen zum Hersteller führen.

### Eigenschaft `product_url`

Diese Eigenschaft ist OPTIONAL.

Diese Eigenschaft dient dazu, über eine URL mitzuteilen, welches Softwareprodukt
das Server-System bereitstellt. Die URL soll nach Möglichkeit zu einer WWW-Seite
mit weiteren Informationen zum Produkt führen.



### Beispiel

~~~~~  {#OParlSystem_ex1 .json}
{
    "@id": "http://refserv.oparl.org/",
    "@context": "http://oparl.org/schema/1.0/OParlSystem",
    "oparl_version": "http://oparl.org/specs/1.0/",
    "name": "OParl Reference Server",
    "info_url": "https://github.com/OParl/reference-server",
    "contact": {
        "email": "info@oparl.org",
        "name": "Common OParl contact"
    }, 
    "vendor_url": "http://oparl.org/",
    "product_url": "https://github.com/OParl/reference-server",
    "license": "http://creativecommons.org/licenses/by/4.0/",
    "bodies": "http://refserv.oparl.org/bodies/",
    "new_objects": "http://refserv.oparl.org/feeds/new/",
    "updated_objects": "http://refserv.oparl.org/feeds/updated/",
    "removed_objects": "http://refserv.oparl.org/feeds/removed/"
}
~~~~~
