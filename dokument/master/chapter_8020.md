Attribute mit Verwendung in mehreren Objekttypen
------------------------------------------------

Für Datum und Zeit werden die in XML Schema festgelegten Typen verwendet (was nicht bedeutet, dass in OParl XML verwendet wird).

Für ein Datum wird http://www.w3.org/TR/xmlschema-2/#date verwendet und für eine Zeit http://www.w3.org/TR/xmlschema-2/#dateTime. Dabei wird ein Datum (ein Tag ohne Uhrzeit) ohne Zeitzone und ein Datum mit Zeit mit Zeitzone angegeben, denn nur damit ist die Uhrzeit weltweit eindeutig ohne zusätzlich auf den Ort einer Sitzung o.ä. Bezug nehmen zu müssen.

Diese Spezifikationen stützen sich auf RFC 3339 (http://www.ietf.org/rfc/rfc3339.txt) und RFC 3339 wiederum auf ISO 8601.

Im JSON-LD Kontext von OParl ist der Präfix 'xsd' so spezifiziert, dass Datums- und Zeittyp durch 'xsd:date' bzw. 'xsd:dateTime' abgekürzt werden können.

TODO: BEISPIELE



