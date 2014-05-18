Content Negotiation  {#content_negotiation}
-------------------

Das Prinzip _Content Negotiation_ wird in RFC2295^[RFC2295:
<http://tools.ietf.org/html/rfc2295>] beschrieben und bedeutet, dass
WWW-Server eine Ressource in verschiedenen Formaten bereithalten
können und Clients die Möglichkeit haben, eine Vorliebe für ein
bestimmtes Format zu übermitteln. Auch die HTTP-1.1-Spezifikation^[
RFC2616: <http://tools.ietf.org/html/rfc2616>] schließt Content
Negotiation ein.

Die Idee hinter Content Negotiation ist, dass ein Client die von ihm
akzeptierten Repräsentationen im `Accept`-Header der HTTP-Anfrage mitsendet,
damit der Server gemäß Spezifikation die am besten passende und von ihm
unterstützte Repräsentation an den Client ausliefert.

Grundanforderung der vorliegenden Spezifikation an OParl Clients ist,
dass sie bei jeder Anfrage an einen OParl-Server einen Accept-Header
mit dem Mime-Type `application/ld+json` senden MÜSSEN, es sei denn,
es handelt sich um einen [Dateizugriff](#dateizugriff).

Im Kontext von OParl soll durch Unterstützung von Content Negotiation
ermöglicht werden, dass die URLs von OParl-Objekten auch von WWW-Clients
aufgerufen werden können, die nicht unmittelbar in Kenntnis der
OParl-Spezifikation entwickelt wurden.

Ein Beispiel für einen solchen  Client wäre ein üblicher Browser. Ruft
dieser die URL einer Drucksache (OParl-Objekttyp `oparl:Paper`) auf, 
sendet er entweder keinen `Accept`-Header oder aber einen solchen,
der eine Bevorzugung von Inhaltstypen wie HTML angibt.

Der Server DARF nun, da kein Accept-Header mit dem Typ `application/ld+json`
gesendet wurde, dem Client eine alternative Version der Information über die
Drucksache ausliefern, beispielsweise eine HTML-Ansicht.

Ein Server DARF eine alternative Inhaltsform auch in Form einer
HTTP-Weiterleitung anbieten.

### httpRange-14

Im Zusammenhang von Content Negotiation soll als Exkurs auf ein für Linked Data
relevantes Detail hingewiesen werden, das in Fachkreisen _httpRange-14_ genannt wird.
Dabei geht es um das im folgenden beschriebenePhänomen.

Wenn man in einem üblichen Web-Browser diese URL aufruft:

    <http://dbpedia.org/resource/John_Doe_(musician)>

dann erfolgt eine Weiterleitung auf diese URL:

    <http://dbpedia.org/page/John_Doe_(musician)>

Dabei identifiziert die erste URL den abstrakten Begriff des Musikers,
während die zweite eine Repräsentation dieses Begriffs identifiziert.
Ein anderer HTTP-Client, der statt HTML-Seiten z.B. JSON-LD bevorzugt,
würde bei Zugriff auf die erste URL wiederum zu einer anderen URL
weiter geleitet:

    <http://dbpedia.org/data/John_Doe_(musician).jsonld>

Dabei handelt es sich um eine Repräsentation des Musikers in Form von
JSON-LD.

Diese drei Links sind nicht nur verschieden, sondern haben unterschiedliche
Bedeutungen. Eine Angabe z.B. der zweiten URL (HTML-Seite) oder der dritten
URL (JSON-LD) kann von Clients generell nicht verwendet werden, um auf
einfache Weise zu den anderen beiden URLs zu gelangen. Deshalb soll bei
Linked Data der erste Link, also der des abstrakten Begriffs angegeben
werden. Der Zugriff auf diesen Link wird "Dereferenzierung" genannt. Von
dem ersten Link gelangt man zu den beiden anderen mittels Content
Negotiation.

So kann der Server beim Zugriff eines Client auf

    <https://dbpedia.org/resource/John_Doe_(musician)>

z.B. entweder diese URL sowie HTML-Inhalt liefern

    <https://dbpedia.org/page/John_Doe_(musician)>

oder aber diese URL mit JSON-LD als Inhalt

    <https://dbpedia.org/data/John_Doe_(musician).jsonld>

Die Entscheidung darüber, welche der URLs und welche der Inhaltsformate
der Server liefert, wird zwischen Client und Server mittels Content
Negotiation ausgehandelt.

Das Phänomen verdeutlicht zum einen, dass URLs im Kontext von Linked Data
eine wichtige Bedeutung haben und außerdem, dass es auch vom aufrufenden
Client abhängen kann, bei welcher URL eine bestimmte Anfrage letztlich "landet".
