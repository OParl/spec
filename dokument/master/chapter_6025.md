Content Negotiation  {#content_negotiation}
-------------------

Server im World Wide Web können bestimmte Ressourcen entsprechend 
RFC2295^[RFC2295: <http://tools.ietf.org/html/rfc2295>] in verschiedenen Formaten
vorhalten. Clients haben die Möglichkeit, mittels HTTP-Header schon in
der Anfrage eine Vorliebe für ein bestimmtes Format zu übermitteln.

TODO: Hier muss eine Beschreibung folgen, was mit Content Negotiation erreicht werden
soll und wie genau die Anforderungen lauten (vgl. Issue #105).

TODO: Der nachstehende Text muss noch sauber formuliert werden.

Auf ein für Linked Data wichtiges Detail sei hier hingewiesen. Wenn man in einem üblichen Web-Browser
diesen oben angegebenen Link eingibt und aufruft:

    https://dbpedia.org/resource/John_Doe_(musician)

dann sieht man anschliessend bei der Anzeige der HTML-Seite diesen Link im Adressfeld:

    https://dbpedia.org/page/John_Doe_(musician)

Dabei identifiziert der erste Link den abstrakten Begriff des Musikers, während der
zweite Link eine Repräsentation dieses Begriffs identifiziert. Ein anderer http-Client, der
statt HTML-Seiten z.B. JSON-LD bevorzugt, würde bei Zugriff auf den ersten Link statt der
HTML-Seite den Inhalt dieser URL erhalten:

    https://dbpedia.org/data/John_Doe_(musician).jsonld

Dabei handelt es sich um eine Repräsentation des Musikers in Form von JSON-LD.

Diese drei Links sind nicht nur verschieden, sondern haben unterschiedliche Bedeutungen. Eine Angabe z.B. der zweiten URL (HTML-Seite) oder der dritten URL (JSON-LD) kann von Clients generell nicht verwendet werden, um auf einfache Weise zu den anderen beiden URLs zu gelangen. Deshalb soll bei Linked Data der erste Link, also der des abstrakten Begriffs angegeben werden. Der Zugriff auf diesen Link wird "Dereferenzierung" genannt. Von dem ersten Link gelangt man zu den beiden anderen mittels "Content Negotiation".

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
