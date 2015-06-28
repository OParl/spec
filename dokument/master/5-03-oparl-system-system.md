oparl:System (System)   {#oparl_system}
--------------------

**Namespace-URL:** `http://oparl.org/schema/1.0/System`

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
    "body": "https://oparl.example.org/bodies/",
    "name": "Beispiel-System",
    "contactEmail": "mailto:info@example.org",
    "contactName": "Allgemeiner OParl Kontakt",
    "newObjects": "https://oparl.example.org/new_objects/",
    "updatedObjects": "https://oparl.example.org/updated_objects/",
    "removedObjects": "https://oparl.example.org/removed_objects",
    "website": "http://www.example.org/",
    "vendor": "http://example-software.com/",
    "product": "http://example-software.com/oparl-server/"
}
~~~~~


### Eigenschaften

**`oparlVersion`**

-------------   -------------------------------------------------------
Beschreibung:   Die URL der OParl-Spezifikation, die von diesem Server
                unterstützt wird. Aktuell kommt hier nur ein Wert in
                Frage. Mit zukünftigen OParl-Versionen kommen weitere
                mögliche URLs hinzu.
Status:         _ZWINGEND_
Typ:            URL
Wert:           `http://oparl.org/specs/1.0/`
-------------   -------------------------------------------------------

**`body`**

-------------   -------------------------------------------------------
Beschreibung:   Liste der Körperschaften (`oparl:Body`-Objekte), die
                auf dem System existieren.
Status:         _ZWINGEND_
Typ:            Array mit Objekt-URLs oder URL zum Listenabruf
Siehe auch:     [`oparl:Body`](#oparl_body), [Objektlisten](#objektlisten)
-------------   -------------------------------------------------------

**`name`**

-------------   -------------------------------------------------------
Beschreibung:   Nutzerfreundlicher Name für das System, mit dessen
                Hilfe Nutzerinnen und Nutzer das System erkennen und
                von anderen unterscheiden können.
Status:         _EMPFOHLEN_
Typ:            String
Wert:           `http://oparl.org/specs/1.0/`
-------------   -------------------------------------------------------

**`contactEmail`**

-------------   -------------------------------------------------------
Beschreibung:   E-Mail-Adresse für Anfragen zur OParl-API. Die Angabe
                einer E-Mail-Adresse dient sowohl NutzerInnen wie auch
                Entwicklerinnen von Clients zur Kontaktaufnahme mit dem
                Betreiber.
Status:         _EMPFOHLEN_
Typ:            String im Format `foaf:mbox`
-------------   -------------------------------------------------------

**`contactName`**

-------------   -------------------------------------------------------
Beschreibung:   Name der Ansprechpartnerin bzw. des Ansprechpartners
                oder der Abteilung, die über die in `contactEmail`
                angegebene Adresse erreicht werden kann.
Status:         _EMPFOHLEN_
Typ:            String
-------------   -------------------------------------------------------


**`newObjects`**

-------------   -------------------------------------------------------
Beschreibung:   URL des Feeds "Neue Objekte".
Status:         _EMPFOHLEN_
Typ:            URL
Siehe auch:     [Feeds](#feeds), [Neue Objekte](#feed_neue_objekte)
-------------   -------------------------------------------------------

**`updatedObjects`**

-------------   -------------------------------------------------------
Beschreibung:   URL des Feeds "Geänderte Objekte".
Status:         _EMPFOHLEN_
Typ:            URL
Siehe auch:     [Feeds](#feeds), [Geänderte Objekte](#feed_geaenderte_objekte)
-------------   -------------------------------------------------------

**`removedObjects`**

-------------   -------------------------------------------------------
Beschreibung:   URL des Feeds "Entfernte Objekte".
Status:         _EMPFOHLEN_
Typ:            URL
Siehe auch:     [Feeds](#feeds), [Entfernte Objekte](#feed_entfernte_objekte)
-------------   -------------------------------------------------------

**`website`**

-------------   -------------------------------------------------------
Beschreibung:   URL der Website des parlamentarischen
                Informationssystems
Status:         _OPTIONAL_
Typ:            URL
-------------   -------------------------------------------------------

**`vendor`**

-------------   -------------------------------------------------------
Beschreibung:   URL der Website des Software-Anbieters, von dem die
                OParl-Server-Software stammt.
Status:         _OPTIONAL_
Typ:            URL
-------------   -------------------------------------------------------

**`product`**

-------------   -------------------------------------------------------
Beschreibung:   URL zu Informationen über die auf dem System genutzte
                OParl-Server-Software
Status:         _OPTIONAL_
Typ:            URL
-------------   -------------------------------------------------------
