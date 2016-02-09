## HTTP und HTTPS {#http-und-https}

OParl-Server und -Client kommunizieren miteinander über das HTTP-Protokoll.
Der Zugriff MUSS zustandslos, also ohne Sessioninformationen (z.B. Cookies)
erfolgen.

Der Einsatz des verschlüsselten HTTPS wird Empfohlen. Bei Verwendung von HTTPS
wird allen URLs "https://" voran gestellt, ansonsten beginnen URLs mit
"http://".

Wie im Kapitel [URLs](#urls) beschrieben, verfolgt diese Spezifikation die
Festlegung auf genau eine "kanonische" URL je Ressource
(vgl. [URL-Kanonisierung](#url_kanonisierung)). Es ist daher ZWINGEND
notwendig, dass der Server-Betreiber sich entweder für HTTP oder für HTTPS
entscheidet. Es jedoch möglich, eine Weiterleitung (HTTP Status-Code 301)
einzurichten. Eine Weiterleitung von HTTPS auf HTTP wird NICHT EMPFOHLEN.
