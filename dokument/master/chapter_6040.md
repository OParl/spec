Serialisierung mittels JSON-LD und JSONP
----------------------------------------

### JSON

- Siehe RFC4627
- Generelle Terminologie übernehmen (JSON-Objekt, Array, String, Number, true/false, null)

### JSON-LD

- JSON-LD: http://www.w3.org/TR/json-ld/
- Einschränkungen von OParl gegenüber JSON-LD
- Schlüssel in einem JSON-LD-Objekt müssen einzigartig sein.
- Unterscheidung von Groß- und Kleinschreibung
- Benannte Objekte (URL als Schlüssel)
- Anonyme Objekte (Blank Nodes)
- Mime Type application/ld+json
- Verweis auf http://www.bmi.bund.de/SharedDocs/Downloads/DE/Themen/OED_Verwaltung/ModerneVerwaltung/opengovernment.pdf?__blob=publicationFile
- Siehe https://github.com/OParl/specs/issues/77

### JSONP

- TODO: Spezifikation finden/verlinken. (RFC gibt es nicht)
- https://github.com/OParl/specs/issues/67
- Zeichenvorrat für callback-Parameter beschränken auf [a-zA-Z0-9] aus Sicherheitsgründen
