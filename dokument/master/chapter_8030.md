oparl:System (System)   {#oparl_system}
--------------------

Der Objekttyp `oparl:System` bildet grundlegende Informationen zum
parlamentarischen Informationssystem ab. Das Objekt repräsentiert
das technische System, unabhängig von der Frage, welche Körperschaften
auf diesem System vertreten sind.

Auf jedem OParl-Server MUSS ein Objekt vom Typ `oparl:System` vorgehalten
werden. Es DARF nur ein einziges solches Objekt je Server existieren.

Für Clients ist das `oparl:System` Objekt ein geeigneter Einstiegspunkt,
um grundlegende Informationen über das System zu bekommen und die URLs
zum Zugriff auf andere Informationen in Erfahrung zu bringen.

Die URL des `oparl:System`-Objekts MUSS per Definition identisch mit
der URL des API-Endpunkts des Servers sein.

**Beispiel**

~~~~~  {#system_ex2 .json}
{
    "id": "https://oparl.example.org/",
    "type": "http://oparl.org/schema/1.0/System",
    "oparlVersion": "http://oparl.org/specs/1.0/",
    "name": "Beispiel-System",
    "website": "http://www.example.org/",
    "contactEmail": "mailto:info@example.org",
    "contactName": "Allgemeiner OParl Kontakt",
    "vendor": "http://example-software.com/",
    "product": "http://example-software.com/oparl-server/",
    "body": "https://oparl.example.org/bodies/",
    "newObjects": "https://oparl.example.org/new_objects/",
    "updatedObjects": "https://oparl.example.org/updated_objects/",
    "removedObjects": "https://oparl.example.org/removed_objects"
}
~~~~~


### Eigenschaften

`oparlVersion`
:   Die URL der OParl-Spezifikation, die von diesem Server unterstützt 
    wird. Der Wert MUSS die URL `http://oparl.org/specs/1.0/` sein.
    Typ: URL.
    Kardinalität: 1.
    ZWINGEND.

`body`
:   Liste der URLs der [`oparl:Body`](#oparl_body)-Objekte, also der 
    Körperschaften, die auf dem System vorliegen. Alternativ kann statt 
    einer Liste eine einzelne URL zum Abruf der Liste angeboten werden.
    Typ: URL des `oparl:Body` Objekts
    Kardinalität: 1.
    ZWINGEND.

`name`
:   Nutzerfreundlicher Name für das System, mit dessen Hilfe Nutzer das
    System erkennen und von anderen unterscheiden können.
    Typ: String.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.

`contactEmail`
:   E-Mail-Adresse für Anfragen zur OParl-API. Die Angabe einer E-Mail-Adresse dient sowohl Nutzerinnen
    wie auch Entwicklerinnen von Clients zur Kontaktaufnahme mit dem
    Betreiber.
    Typ: String im Format `foaf:mbox`
    Kardinalität: 0 bis 1.
    EMPFOHLEN. 

`contactName`
:   Name des Ansprechpartners oder der Abteilung, die über die `contactEmail`
    erreicht werden kann.
    Typ: String.
    Kardinalität: 0 bis 1.
    EMPFOHLEN. 

`newObjects`
:   URL des Feeds ["Neue Objekte"](#feed_neue_objekte).
    Typ: URL.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.

`updatedObjects`
:   URL des Feeds ["Geänderte Objekte"](#feed_geaenderte_objekte).
    Typ: URL.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.

`removedObjects`
:   URL des Feeds ["Entfernte Objekte"](#feed_entfernte_objekte).
    Typ: URL.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.

`website`
:   URL zur WWW-Oberfläche des parlamentarischen Informationssystems.
    Typ: URL.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`vendor`
:   Software-Anbieter, von dem die OParl-Server-Software stammt.
    Typ: URL.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`product`
:   Informationen zu der auf dem System genutzten OParl-Server-Software.
    Typ: URL.
    Kardinalität: 0 bis 1.
    OPTIONAL.
