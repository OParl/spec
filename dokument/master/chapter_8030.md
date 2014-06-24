oparl:System (System)   {#oparl_system}
--------------------

Der Objekttyp `oparl:System` bildet grundlegende Informationen zum
parlamentarischen Informationssystem ab. Das Objekt repräsentiert
das technische System, unabhängig von der Frage, welche Körperschaften
auf diesem System vertreten sind.

### Beispiel ###

Ein Kontext:

~~~~~  {#system_ex_context .json}
{
    "@language": "de",
    "beispielris": "https://oparl.beispielris.de/",
    "oparl": "http://oparl.org/specs/1.0/schema/",
    "dc": "http://purl.org/dc/terms/",
    "foaf": "http://xmlns.com/foaf/0.1/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",

    "name": {
        "@id": "skos:prefLabel",
        "@type": "@id"
    },
    "contactEmail": {
        "@id": "foaf:mbox",
        "@type": "@id"
    },
    "oparlVersion": {
        "@id": "oparl:oparlVersion",
        "@type": "@id"
    },
    "website": {
        "@id": "oparl:website",
        "@type": "@id"
    },
    "contactEmail": {
        "@id": "foaf:mbox",
        "@type": "@id"
    },
    "contactName": {
        "@id": "oparl:contactName",
        "@type": "xsd:string"
    },
    "vendor": {
        "@id": "oparl:vendor",
        "@type": "@id"
    },
    "product": {
        "@id": "oparl:product",
        "@type": "@id"
    },
    "body": {
        "@id": "oparl:body",
        "@type": "@id"
    },
    "newObjects": {
        "@id": "oparl:newObjects",
        "@type": "@id"
    },
    "updatedObjects": {
        "@id": "oparl:updatedObjects",
        "@type": "@id"
    },  
    "removedObjects": {
        "@id": "oparl:removedObjects",
        "@type": "@id"
    },  
}
~~~~~

Und das System-Objekt in kompakter Form unter Verwendung des Kontexts:

~~~~~  {#system_ex2 .json}
{
    "@context": "TODO",
    "@type": "oparl:System",
    "@id": "beispielris:",
    "oparlVersion": "beispielris:specs/1.0/",
    "name": "Beispiel-System",
    "website": "http://www.example.org/",
    "contactEmail": "mailto:info@example.org",
    "contactName": "Allgemeiner OParl Kontakt",
    "vendor": "http://example-software.com/",
    "product": "http://example-software.com/oparl-server/",
    "body": "beispielris:bodies/",
    "newObjects": "beispielris:new_objects/",
    "updatedObjects": "beispielris:updated_objects/",
    "removedObjects": "beispielris:removed_objects"
}
~~~~~

### Anmerkungen ###

Auf jedem OParl-Server MUSS ein Objekt vom Typ `oparl:System` vorgehalten
werden. Es DARF nur ein einziges solches Objekt je Server existieren.

Für Clients ist das `oparl:System` Objekt ein geeigneter Einstiegspunkt,
um grundlegende Informationen über das System zu bekommen und die URLs
zum Zugriff auf andere Informationen in Erfahrung zu bringen.

Die URL des `oparl:System`-Objekts MUSS per Definition identisch mit
der URL des API-Endpunkts des Servers sein.

### Eigenschaften

`oparlVersion`
:   Die URL der OParl-Spezifikation, die von diesem Server unterstützt 
    wird. Der Wert MUSS die URL `http://oparl.org/specs/1.0/` sein.
    Typ: URL
    ZWINGEND.

`body`
:   Liste der URLs der [`oparl:Body`](#oparl_body)-Objekte, also der 
    Körperschaften, die auf dem System vorliegen. Alternativ kann statt 
    einer Liste eine einzelne URL zum Abruf der Liste angeboten werden.
    Typ: URL
    ZWINGEND.

`name`
:   Nutzerfreundlicher Name für das System, mit dessen Hilfe Nutzer das
    System erkennen und von anderen unterscheiden können.
    Typ: String
    EMPFOHLEN.

`contactEmail`
:   E-Mail-Adresse für Anfragen zur OParl-API. Die Angabe einer E-Mail-Adresse dient sowohl Nutzerinnen
    wie auch Entwicklerinnen von Clients zur Kontaktaufnahme mit dem
    Betreiber.
    Typ: E-Mail-Adresse inklusive "mailto:"
    EMPFOHLEN. 

`contactName`
:   Name des Ansprechpartners oder der Abteilung, die über die `contactEmail`
    erreicht werden kann.
    Typ: String.
    EMPFOHLEN. 

`newObjects`
:   URL des Feeds ["Neue Objekte"](#feed_neue_objekte).
    Typ: URL
    EMPFOHLEN.

`updatedObjects`
:   URL des Feeds ["Geänderte Objekte"](#feed_geaenderte_objekte).
    Typ: URL
    EMPFOHLEN.

`removedObjects`
:   URL des Feeds ["Entfernte Objekte"](#feed_entfernte_objekte).
    Typ: URL
    EMPFOHLEN.

`website`
:   URL zur WWW-Oberfläche des parlamentarischen Informationssystems.
    Typ: URL
    OPTIONAL.

`vendor`
:   Software-Anbieter, von dem die OParl-Server-Software stammt.
    Typ: URL
    OPTIONAL.

`product`
:   Informationen zu der auf dem System genutzten OParl-Server-Software.
    Typ: URL
    OPTIONAL.
