oparl:System (System)   {#oparl_system}
--------------------

Der Objekttyp `oparl:System` bildet grundlegende Informationen zum
parlamentarischen Informationssystem ab. Das Objekt repräsentiert
das technische System, unabhängig von der Frage, welche Körperschaften
auf diesem System vertreten sind.

Ein Beispiel:

~~~~~  {#system_ex1 .json}
{
    "@type": "oparl:System",
    "@id": "http://beispielris.de/",
    "oparl_version": "http://oparl.org/specs/1.0/",
    "name": "Beispiel-System",
    "www_url": "http://www.beispielris.de/",
    "contact_email": "mailto:info@beispielris.de",
    "contact_name": "Allgemeiner OParl Kontakt",
    "vendor": "http://example-software.com/",
    "product": "http://example-software.com/oparl-server/",
    "license": "http://creativecommons.org/licenses/by/4.0/",
    "bodies": "http://beispielris.de/bodies/",
    "new_objects": "http://beispielris.de/new_objects/",
    "updated_objects": "http://beispielris.de/updated_objects/",
    "removed_objects": "http://beispielris.de/removed_objects"
}
~~~~~

Auf jedem OParl Server MUSS ein Objekt vom Typ `oparl:System` vorgehalten
werden. Es DARF nur ein einziges solches Objekt je Server existieren.

Für Clients ist das `oparl:System` Objekt ein geeigneter Einstiegspunkt,
um grundlegende Informationen über das Sytem zu bekommen und die URLs
zum Zugriff auf andere Informationen in Erfahrung zu bringen.

Die URL des `oparl:System` Objekts MUSS per Definition identisch mit
der URL des API-Endpunkts des Servers sein.

### Eigenschaften

`oparl_version`
:   Die URL der OParl-Spezifikation, die von diesem Server unterstützt 
    wird. Der Wert MUSS die URL `http://oparl.org/specs/1.0/` sein.
    Diese Eigenschaft ist ZWINGEND.

`bodies`
:   Liste der URLs der [`oparl:Body`](#oparl_body)-Objekte, also der 
    Körperschaften, die auf dem System vorliegen. Alternativ kann statt 
    einer Liste eine einzelne URL zum Abruf der Liste angeboten werden. 
    Die Eigenschaft ist ZWINGEND.

`name`
:   Nutzerfreundlicher Name für das System, mit dessen Hilfe Nutzer das
    System erkennen und von anderen unterscheiden können. Diese Eigenschaft
    wird EMPFOHLEN.

`contact_email`
:   E-Mail-Adresse für Anfragen zur OParl-API. Diese Eigenschaft wird 
    EMPFOHLEN. Die Angabe einer E-Mail-Adresse dient sowohl NutzerInnen
    wie auch EntwicklerInnen von Clients zur Kontaktaufnahme mit dem
    Betreiber. 

`contact_name`
:   Name des Ansprechpartners oder der Abteilung, die über die `contact_email`
    erreicht werden kann. Die Eigenschaft ist EMPFOHLEN. Typ: Zeichenkette.

`license`
:   URL der Lizenz, die für die Daten, die über diese API abgerufen werden
    können, gilt, sofern nicht am einzelnen Objekt anders angegeben.
    Die Eigenschaft ist EMPFOHLEN.

`new_objects`
:   URL des Feeds ["Neue Objekte"](#feed_neue_objekte). Die Eigenschaft ist 
    EMPFOHLEN.

`updated_objects`
:   URL des Feeds ["Geänderte Objekte"](#feed_geaenderte_objekte). Die 
    Eigenschaft ist EMPFOHLEN.

`removed_objects`
:   URL des Feeds ["Entfernte Objekte"](#feed_entfernte_objekte). Die 
    Eigenschaft ist EMPFOHLEN.

`www_url`
:   URL zur WWW-Oberfläche des parlamentarischen Informationssystem.
    Diese Eigenschaft ist OPTIONAL.

`vendor`
:   URL des Software-Anbieters, von dem die OParl-Server-Software stammt.
    Diese Eigenschaft ist OPTIONAL.

`product`
:   URL mit Informationen zu der auf dem System genutzten OParl-Server-Software.
    Diese Eigenschaft ist OPTIONAL.
