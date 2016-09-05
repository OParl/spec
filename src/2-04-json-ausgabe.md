## JSON-Ausgabe {#json-ausgabe}

Ein OParl-Server **muss** Objekte in Form von JSON ausgeben. Die Abkürzung JSON steht
für "JavaScript Object Notation". Das JSON-Format ist in
RFC 7159^[RFC 7159: <https://tools.ietf.org/html/rfc7159>] beschrieben.

Sämtliche JSON-Ausgabe **muss** in UTF-8 ohne Byte Order Mark (BOM) geschehen. Dies entspricht
RFC 7159 Section 8.1[^fn-rfc7159-81]. Gemäß RFC 7159 Section 7[^fn-rfc7159-7] **darf** UTF-8
String-Escaping verwendet werden. XML-/HTML-String-Escaping **darf nicht** verwendet werden.

Eine Syntaxübersicht und weitere Implementierungshinweise finden sich auf
[json.org](http://json.org/).

Es ist gestattet, weitere zur JSON-Ausgabe semantisch identische
Formate^[Zu semantischen identischen Formaten zählen u.a.: YAML, MessagePack, etc.]
anzubieten. Da diese jedoch nicht Bestandteil der Spezifikation sind,
**sollten** sich Clients nicht auf deren Vorhandensein verlassen.

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
:   Eine URL ist ein String, der entsprechend des [URL-Kapitels](#urls) formatiert wurde.

url (Object):
:   Eine URL mit in Klammern angehängtem Objektname beschreibt eine URL auf eben diesen Objekttypus.

date:
:   Entspricht einem Datum ohne Uhrzeit und ohne Zeitzone, wie sie im folgenden Abschnitt beschrieben werden.

date-time:
:   Entspricht einem Datum und einer Uhrzeit mit Zeitzone, wie sie im folgenden Abschnitt beschrieben werden.

### Datums- und Zeitangaben  {#datum_zeit}

Für Datums- und Zeitangaben werden die in ISO 8601 beschriebenen Formate verwendet.
Ein Datum (date) **muss** muss also die Form `yyyy-mm-dd` besitzen und ein
Zeitpunkt (date-time) **muss** in der Form `yyyy-mm-ddThh:mm:ss+hh:mm` angegeben werden.

Beispiel für ein Datum: `1969-07-21`

Beispiel für einen Zeitpunkt: `1969-07-21T02:56:00+00:00`.

### `null`-Werte und leere Listen {#null-werte-und-leere-listen}

JSON erlaubt es grundsätzlich, Eigenschaften mit dem Wert `null` zu versehen.
Eigenschaften **sollten** nicht mit dem Wert `null` ausgegeben werden, wenn zu
einer Eigenschaft keine Daten vorliegen. Obligatorische Eigenschaften
**dürfen nicht** den Wert `null` haben.

Im Fall von Arrays erlaubt JSON grundsätzlich die Ausgabe von `[]` für leere
Arrays. Wie bei `null` wird auch hier **empfohlen**, auf die Ausgabe einer
Eigenschaft mit dem Wert `[]` zu verzichten, wenn zu einer Eigenschaft keine Daten
vorliegen. Bei obligatorischen Eigenschaften **muss** jedoch eine leere Liste
ausgegeben werden.
