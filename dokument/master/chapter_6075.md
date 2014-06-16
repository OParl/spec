Daten Dump / bulk download
--------------------------

Als Alternative zu dem eher fein-granularen Zugriff auf einzelne
OParl-Objekte kann es sinnvoll sein, wenn alle Objekte in einem Vorgang
abgerufen werden können. Gründe dafür können sein:

* z. B. für Auswertungen wird ein großer Teil aller Objekte benötigt
* Anzahl erforderlicher http-Zugriffe sinkt drastisch
* die Last auf dem Server (z. B. für Datenbank) kann reduziert werden

Für die Implementierung gibt es mehrere Anforderungen:
* weitgehende Nutzung ohnehin bereits in OParl genutzter Techniken
* Verwendung etablierter Vokabulare

Bei Betrachtung der OParl-Daten als Tripel geht es hier um eine Abfrage
nach allen Objekten, deren Subjekt, Prädikat und Objekt nicht eingeschränkt
ist.
~~~~~
https://oparl.example.org/ldf?subject=&predicate=&object=
~~~~~

Zum Vergleich: Bei einer Abfrage von [Objektlisten](#objektlisten) sind
Subjekt und Prädikat durch die Abfrage festgelegt, nur das Objekt ist variabel.

Für die Spezifikation des Formats der downloadbaren Dateien wird also
auf das Objektlisten-Format zurückgegriffen.

Wenn das Ergebnis dieser Abfrage in eine Datei geschrieben und als solche zum
Download angeboten wird, dann kann und soll auf [Paginierung](#paginierung)
in dieser Datei jedoch verzichtet werden, da diesei Daten nur stören würden.

TODO: Beispiel und Besonderheiten
TODO: SOLL-Anforderung

In dieser Version von OParl werden keine Festlegungen getroffen, wie
ein Client über die URLs der downloadbaren Dateien informiert wird.
In Frage kommen aber z. B. Links, die auf HTML-Seiten plaziert werden.

