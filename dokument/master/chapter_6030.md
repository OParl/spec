HTTP und HTTPS
--------------

OParl-Server und -Client kommunizieren miteinander über das HTTP-Protokoll.

Hierbei SOLL eine verschlüsselte Variante des Protokolls, auch HTTPS 
genannt, zum Einsatz kommen, alternativ kann jedoch auch unverschlüsseltes
HTTP verwendet werden. Welche Verschlüsselungstechnologie im Fall von
HTTPS gewählt wird, obliegt dem Betreiber bzw. Server-Implementierer.

Die Wahl des unverschlüsselten oder verschlüsselten HTTP-Zugriffs hat
Auswirkung auf die im System verwendeten URLs. Wie im Kapitel [URLs](#urls)
beschrieben, verfolgt diese Spezifikation die Festlegung auf genau eine 
"kanonische" URL je Ressource (URL-Kanonisierung).

Bei unverschlüsseltem Zugriff wird allen URLs, die auf das betreffende System
zeigen, das Schema "http://" voran gestellt, beim verschlüsselten Zugriff
stattdessen "https://".

Es ist daher ZWINGEND, dass der Server-Betreiber sich zur URL-Kanonisierung 
für nur eine von beiden Varianten entscheidet. Beantwortet das System regulär
Anfragen über HTTPS mit der Auslieferung von Objekten etc., dann MUSS das System
bei Anfragen an die entsprechenden URLs ohne "https://" Schema mit einer 
Weiterleitung antworten (HTTP Status-Code 301).

Gleiches gilt umgekehrt: beantwortet das System regulär Anfragen über
unverschlüsseltes HTTP, dann MÜSSEN Anfragen auf die entsprechenden URLs mit
"https://"-Schema mit einer HTTP-Weiterleitung (HTTP Status-Code 301) beantwortet
werden.
