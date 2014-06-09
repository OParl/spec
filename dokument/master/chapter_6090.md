Content Negotiation  {#content_negotiation}
-------------------

Das Prinzip _Content Negotiation_ wurde bereits in RFC2295^[RFC2295:
<http://tools.ietf.org/html/rfc2295>] beschrieben und bedeutet, dass
WWW-Server eine Ressource in verschiedenen Formaten bereithalten
können und Clients die Möglichkeit haben, eine Vorliebe für ein
bestimmtes Format zu übermitteln. Auch die HTTP-1.1-Spezifikation^[RFC7231: <http://tools.ietf.org/html/rfc7231#section-3.4>] schließt Content
Negotiation ein.

Die Idee hinter Content Negotiation ist, dass ein Client die von ihm
akzeptierten Repräsentationen im `Accept`-Header der HTTP-Anfrage mitsendet,
damit der Server gemäß Spezifikation die am besten passende und von ihm
unterstützte Repräsentation an den Client ausliefert.

Grundanforderung der vorliegenden Spezifikation an OParl-Clients ist,
dass sie bei jeder Anfrage an einen OParl-Server einen Accept-Header
mit dem Mime-Type `application/ld+json` senden MÜSSEN, es sei denn,
es handelt sich um einen [Dateizugriff](#dateizugriff).

Im Kontext von OParl soll durch Unterstützung von Content Negotiation
ermöglicht werden, dass die URLs von OParl-Objekten auch von WWW-Clients
aufgerufen werden können, die nicht unmittelbar in Kenntnis der
OParl-Spezifikation entwickelt wurden.

Ein Beispiel für einen solchen Client wäre ein üblicher Browser. Ruft
dieser die URL einer Drucksache (OParl-Objekttyp `oparl:Paper`) auf, 
sendet er entweder keinen `Accept`-Header oder aber einen solchen,
der eine Bevorzugung von Inhaltstypen wie HTML angibt.

Der Server DARF nun, da kein Accept-Header mit dem Typ `application/ld+json`
gesendet wurde, dem Client eine alternative Version der Information über die
Drucksache ausliefern, beispielsweise eine HTML-Ansicht.

Ein Server DARF eine alternative Inhaltsform auch in Form einer
HTTP-Weiterleitung anbieten.
