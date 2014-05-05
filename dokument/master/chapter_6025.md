Content Negotiation
-------------------

Im Abschnitt Designprinzipien wurde bereits erwähnt, dass die "Dereferenzierung" mittels Content Negotiation erfolgt.

So kann der Server beim Zugriff eines Client auf

https://dbpedia.org/resource/John_Doe_(musician)

z.B. entweder diese URL sowie HTML-Inhalt liefern

https://dbpedia.org/page/John_Doe_(musician)

oder aber diese URL mit JSON-LD als Inhalt

https://dbpedia.org/data/John_Doe_(musician).jsonld

Die Entscheidung darüber, welche der URLs und welche der Inhaltsformate der Server liefert, wird zwischen Client und Server
mittels Content Negotiation ausgehandelt.

Der Vorgang ist u.a. in http://de.wikipedia.org/wiki/Content_Negotiation erklärt. Content Negotiation ist Bestandteil der HTTP 1.1 Spezifikation. Siehe RFC 2616 (http://tools.ietf.org/html/rfc2616).

Wichtig ist, dass Client und Server die Möglichkeit haben, das Format auszuhandeln. Deshalb müssen in OParl-Daten 
format-unspezifische URLs angegeben werden, bei dem Musiker John Doe ist das die erste der oben angegebenen URLs und nicht
die letzte.
