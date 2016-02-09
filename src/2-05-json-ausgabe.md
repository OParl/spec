## JSON-Ausgabe {#json-ausgabe}

Ein OParl-Server MUSS Objekte in Form von JSON ausgeben. Die Abkürzung JSON steht
für "JavaScript Object Notation". Das JSON-Format ist in
RFC4627^[RFC4627: <https://tools.ietf.org/html/rfc4627>] beschrieben. 

Sämtliche JSON-Ausgabe MUSS in UTF-8 ohne Byte Order Mark (BOM) geschehen. Dies entspricht
RFC 7159 Section 8.1[^fn-rfc7159-81]. Gemäß RFC 7159 Section 7[^fn-rfc7159-7] DARF UTF-8
String-Escaping verwendet werden. XML-/HTML-String-Escaping DARF NICHT verwendet werden.

Eine Syntaxübersicht und weitere Implementierungshinweise finden sich auf 
[json.org](http://json.org/).

[^fn-rfc7159-7]: [RFC 7159 Section 7](https://tools.ietf.org/html/rfc7159#section-7)
[^fn-rfc7159-81]: [RFC 7159 Section 8.1](https://tools.ietf.org/html/rfc7159#section-8.1)
