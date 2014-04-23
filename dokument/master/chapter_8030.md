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
    "oparlVersion": "http://oparl.org/specs/1.0/",
    "name": "Beispiel-System",
    "wwwUrl": "http://www.beispielris.de/",
    "contactEmail": "mailto:info@beispielris.de",
    "contactName": "Allgemeiner OParl Kontakt",
    "vendor": "http://example-software.com/",
    "product": "http://example-software.com/oparl-server/",
    "license": "http://creativecommons.org/licenses/by/4.0/",
    "bodies": "http://beispielris.de/bodies/",
    "newObjects": "http://beispielris.de/new_objects/",
    "updatedObjects": "http://beispielris.de/updated_objects/",
    "removedObjects": "http://beispielris.de/removed_objects"
}
~~~~~

Auf jedem OParl Server MUSS ein Objekt vom Typ `oparl:System` vorgehalten
werden. Es DARF nur ein einziges solches Objekt je Server existieren.

Für Clients ist das `oparl:System` Objekt ein geeigneter Einstiegspunkt,
um grundlegende Informationen über das Sytem zu bekommen und die URLs
zum Zugriff auf andere Informationen in Erfahrung zu bringen.

Die URL des `oparl:System` Objekts MUSS per Definition identisch mit
der URL des API-Endpunkts des Servers sein.

### Well-Known URIs

TODO: eventuell in eigenen Abschnitt oder eigenes Kapitel auslagern.

Es gibt eine standardisierte Technik, mit der ein Einstiegspunkt in die OParl-Daten angegeben werden kann: "Well-Known URIs". Dieser kann dann maschinell gefunden werden. Diese Technik wurde durch die IETF und das W3C standardisiert.

Die Spezifikation von "Well-Known URIs" durch die IETF ist:

Defining Well-Known Uniform Resource Identifiers (URIs)
http://tools.ietf.org/html/rfc5785

Eine Liste der Well-Known URIs wird von der IANA verwaltet:

Well-Known URIs
http://www.iana.org/assignments/well-known-uris/well-known-uris.xhtml

Für OParl sind gegenwärtig nur "Well-Known URIs" für Beschreibungen von Datasets gemäß dem "Vocabulary of Interlinked Datasets" (VoID) relevant.

BEISPIEL:

Wenn ein RIS unter der Domain "example.com" betrieben wird, dann sieht der "Well-Known URI" so aus (der enthaltene "." ist _kein_ Schreibfehler):

https://example.com/.well-known/void

Forwarding ist erlaubt.

Siehe dazu auch:

Describing Linked Datasets with the VoID Vocabulary
W3C Interest Group Note 03 March 2011
http://www.w3.org/TR/void/#well-known

Die über derartige URIs dereferenzierbaren Dokumente sind hier spezifiziert:
http://www.w3.org/TR/void/#void-file

BEISPIEL:

Bei einem http GET Request auf https://example.com/.well-known/void mit Angabe des bevorzugten MIME-Type "application/ld+json" antwortet das System mit dem URI https://example.com/.well-known/void.jsonld unter welchem dieses JSON-LD Dokument abrufbar ist:

TODO: Beispiele für JSON-LD und exemplarisch auch für HTML.

### Eigenschaften

`oparlVersion`
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

`contactEmail`
:   E-Mail-Adresse für Anfragen zur OParl-API. Diese Eigenschaft wird 
    EMPFOHLEN. Die Angabe einer E-Mail-Adresse dient sowohl NutzerInnen
    wie auch EntwicklerInnen von Clients zur Kontaktaufnahme mit dem
    Betreiber. 

`contactName`
:   Name des Ansprechpartners oder der Abteilung, die über die `contact_email`
    erreicht werden kann. Die Eigenschaft ist EMPFOHLEN. Typ: Zeichenkette.

`license`
:   URL der Lizenz, die für die Daten, die über diese API abgerufen werden
    können, gilt, sofern nicht am einzelnen Objekt anders angegeben.
    Die Eigenschaft ist EMPFOHLEN.

`newObjects`
:   URL des Feeds ["Neue Objekte"](#feed_neue_objekte). Die Eigenschaft ist 
    EMPFOHLEN.

`updatedObjects`
:   URL des Feeds ["Geänderte Objekte"](#feed_geaenderte_objekte). Die 
    Eigenschaft ist EMPFOHLEN.

`removedObjects`
:   URL des Feeds ["Entfernte Objekte"](#feed_entfernte_objekte). Die 
    Eigenschaft ist EMPFOHLEN.

`wwwUrl`
:   URL zur WWW-Oberfläche des parlamentarischen Informationssystem.
    Diese Eigenschaft ist OPTIONAL.

`vendor`
:   URL des Software-Anbieters, von dem die OParl-Server-Software stammt.
    Diese Eigenschaft ist OPTIONAL.

`product`
:   URL mit Informationen zu der auf dem System genutzten OParl-Server-Software.
    Diese Eigenschaft ist OPTIONAL.
