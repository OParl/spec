Content Negotiation  {#content_negotiation}
-------------------

Server im World Wide Web können bestimmte Ressourcen entsprechend 
RFC2295^[RFC2295: <http://tools.ietf.org/html/rfc2295>] in verschiedenen Formaten
vorhalten. Clients haben die Möglichkeit, mittels HTTP-Header schon in
der Anfrage eine Vorliebe für ein bestimmtes Format zu übermitteln.

Der Vorgang der Content Negotiation ist u.a. in http://de.wikipedia.org/wiki/Content_Negotiation erklärt. Content Negotiation ist Bestandteil der HTTP 1.1 Spezifikation. Siehe RFC 2616 (http://tools.ietf.org/html/rfc2616).

Die Idee hinter Content Negotiation ist, dass ein Client die von ihm akzeptierten Repräsentationen im `Accept`-Header des Requests mitgibt, damit der Server gemäß Spezifikation die am besten passende und von ihm unterstützte Repräsentation an den Client ausliefert. 

Eine Schwierigkeit ergibt sich, dass auch `*/*` ein valider `Accept`-Header und bedeutet soviel wie "ich nehme alles". Eine Webanwendung würde dann üblicherweise HTML ausgeben, da es die Standard Repräsentation einer Webanwendung ist. Im Falle einer API, die standardmäßig mit JSON-LD arbeitet, würde eventuell `application/ld+json` als Antwort erwartet. Der Server weiss in diesem Fall aufgrund der fehlenden Information durch den Client nicht, was dieser tatsächlich wünscht. Die OParl-Spezifikation kann in diesem Fall für den Server auch nicht zwingend `application/ld+json` vorgeben, da es durchaus sinnvoll sein kann, wenn unter einer URL *sowohl* OParl-Daten z.B. über ein Gremium abrufbar sind als auch eine HTML-Seite mit Informationen über dieses Gremium.

OParl-Clients MÜSSEN den Accept-Header verwenden und darin mindestens `application/ld+json` als akzeptiertes Format angeben.

Ein Server KANN Content Negotiation über einen Redirect auf eine andere URL umsetzen, oder einfach die entsprechende Repräsentation ohne Redirect ausgeben. Beides ist für OParl zulässig. Der OParl-Server MUSS NICHT Content-Negotiation per Redirect unterstützen, aber OParl-Clients MÜSSEN dies.

### httpRange-14

In dem Zusammenhang sei informell auf ein für Linked Data relevantes Detail hingewiesen - auf welches man gelegentlich unter dem Kürzel `httpRange-14 stößt. Wenn man in einem üblichen Web-Browser diesen bereits an anderer Stelle erwähnten Link eingibt und aufruft:

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

Die Entscheidung darüber, welche der URLs und welche der Inhaltsformate der Server liefert, wird zwischen Client und Server mittels Content Negotiation ausgehandelt.
