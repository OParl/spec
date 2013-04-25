Zugriffsmethoden
================

In diesem Kapitel werden die Zugriffsmethoden der OParl-konformen 
Schnittstelle beschrieben.


Stichpunkte:

* Grundlage für den Zugriff auf die Schnittstelle ist das Hypertext Transfer 
Protocol (HTTP).
* Ausschließlich HTTP GET Methode
* Optional gzip Encoding und andere Kodierungen, wenn Client und Server dies 
unterstützen
* HTTP Last-Modified Header sowie Conditional GET sind bei Dateiabruf (Laden 
von Anhängen) zu unterstützen
* Das Protkoll ist zustandslos
* Authentifizierung wird nicht benötigt.