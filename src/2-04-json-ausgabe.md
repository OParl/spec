## JSON-Ausgabe {#json-ausgabe}

Ein OParl-Server **muss** Objekte in Form von JSON ausgeben. Die Abkürzung JSON steht
für "JavaScript Object Notation". Das JSON-Format ist in
RFC4627^[RFC4627: <https://tools.ietf.org/html/rfc4627>] beschrieben.

Sämtliche JSON-Ausgabe **muss** in UTF-8 ohne Byte Order Mark (BOM) geschehen. Dies entspricht
RFC 7159 Section 8.1[^fn-rfc7159-81]. Gemäß RFC 7159 Section 7[^fn-rfc7159-7] **darf** UTF-8
String-Escaping verwendet werden. XML-/HTML-String-Escaping **darf nicht** verwendet werden.

Eine Syntaxübersicht und weitere Implementierungshinweise finden sich auf
[json.org](http://json.org/).

[^fn-rfc7159-7]: [RFC 7159 Section 7](https://tools.ietf.org/html/rfc7159#section-7)
[^fn-rfc7159-81]: [RFC 7159 Section 8.1](https://tools.ietf.org/html/rfc7159#section-8.1)

### In OParl verwendete Datentypen

In OParl werden alle in JSON definierten Dateitypen verwendet:

object:
:   Objects entsprechen der Definition des Objects in RFC 7159 Section 4

array:
:   Arrays entsprechen der Definition des Arrays in RFC 7159 Section 5

integer:
:   Integers entsprechen der Definition des Integer-Parts der Number aus RFC 7159 Section 6

boolean:
:   Booleans entsprechen der Definition von Boolean in RFC 7159 Section 3

string:
:   Strings entsprechen der Definition der Unicode-Strings aus RFC 7159 Section 7


In OParl werden verschiedene String-Typen verwendet. Wenn von diesen Typen gesprochen wird,
so wird automatisch ein JSON-String vorausgesetzt:

url:
:   Eine URL ist ein String, der entsprechend dem Kapitel zu [URLs](#urls) formatiert wurde.

url (Object):
:   Eine url mit in Klammern angehängtem Object beschreibt eine URL auf eben diesen Objekttypus.

date-time:
:   Ein date-time entspricht einem Datum und ggf. einer Uhrzeit, wie sie im folgenden Abschnitt beschrieben werden.

### Datums- und Zeitangaben  {#datum_zeit}

Für Datum und Zeit werden die im XML-Schema festgelegten Typen
date^[<http://www.w3.org/TR/xmlschema-2/#date>]
und <!--- Mind the Space ---!>
dateTime^[<http://www.w3.org/TR/xmlschema-2/#dateTime>]
verwendet (was nicht bedeutet, dass in OParl XML verwendet wird). Dabei wird
ein Datum (ein Tag ohne Uhrzeit) ohne Zeitzone und ein Datum mit Zeit mit
Zeitzone angegeben, denn nur damit ist die Uhrzeit weltweit eindeutig.

Beispiel: `1969-07-21T02:56:00+00:00`

Diese Spezifikationen stützen sich auf RFC 3339^[RFC3339:
<http://www.ietf.org/rfc/rfc3339.txt>] und RFC 3339 wiederum auf ISO 8601.

### `null`-Werte und leere Listen {#null-werte-und-leere-listen}

JSON erlaubt es grundsätzlich, Eigenschaften mit dem Wert `null` zu versehen.
Eigenschaften **sollten** nicht mit dem Wert `null` ausgegeben werden.
Obligatorische Eigenschaften **dürfen nicht** den Wert `null` haben.

Im Fall von Arrays erlaubt JSON grundsätzlich die Ausgabe von `[]` für leere
Arrays. Wie bei `null` wird auch hier **empfohlen**, auf die Ausgabe einer
Eigenschaft mit dem Wert `[]` zu verzichten. Bei obligatorischen Eigenschaften
**muss** jedoch eine leere Liste ausgegeben werden.
