HTTP und HTTPS
--------------

OParl-Server und -Client kommunizieren miteinander über das HTTP-Protokoll.

Hierbei SOLL eine verschlüsselte Variante des Protokolls, HTTPS,
zum Einsatz kommen. Dabei werden auch die URLs verschlüsselt,
deren Kenntnis möglicherweise Rückschlüsse auf Interessen von Nutzer
ermöglicht. Alternativ kann jedoch auch unverschlüsseltes
HTTP verwendet werden. Welche Verschlüsselungstechnologie im Fall von
HTTPS gewählt wird, obliegt dem Betreiber bzw. Server-Implementierer.

Die Wahl des unverschlüsselten oder verschlüsselten HTTP-Zugriffs hat
Auswirkung auf die im System verwendeten URLs. Wie im Kapitel [URLs](#urls)
beschrieben, verfolgt diese Spezifikation die Festlegung auf genau eine 
"kanonische" URL je Ressource (vgl. [URL-Kanonisierung](#url_kanonisierung)).

Bei unverschlüsseltem Zugriff wird allen URLs, die auf das betreffende System
zeigen, das Schema "http://" voran gestellt, beim verschlüsselten Zugriff
stattdessen "https://".

Es ist daher ZWINGEND, dass der Server-Betreiber sich zur URL-Kanonisierung 
für nur eine von beiden Varianten entscheidet. Beantwortet das System regulär
Anfragen über HTTPS mit der Auslieferung von Objekten etc., dann gilt für
Anfragen an die entsprechende unverschlüsselte URL ZWINGEND:

* unter der URL ist kein Webserver erreichbar, oder

* der Server unter der URL beantwortet die Anfrage mit einer Weiterleitung
  an die HTTPS-URL (HTTP Status-Code 301)

Gleiches gilt umgekehrt: hat sich der Betreiber generell für den Betrieb des
OParl-Servers über unverschlüsseltes HTTP entscheiden, dann MUSS für die
entsprechenden HTTPS-URLs eine der beiden folgenden Möglichkeiten gelten:

* Entweder ist unter den entsprechenden HTTPS-URLs kein Webserver erreichbar

* oder Anfragen an die HTTPS-URLs werden mit Redirects auf die entsprechenden
  HTTP-URLs beantwortet (FRAGE: ist das ein sinnvolles Szenario?).
