Objektlisten  {#objektlisten}
------------

Über die OParl-API können entweder einzelne (benannte) Objekte,
beispielsweise eine bestimmte Drucksache, oder Listen von Objekten,
etwa die Liste aller Sitzungen einer Körperschaft, abgefragt werden.

Fragt ein Client eine Liste von Objekten an, hat der Server mehrere
Möglichkeiten, diese Anfrage zu beantworten.

In jedem Fall werden die einzelnen Objekte, die Bestandteile der
Liste sind (wie z.B. die einzelnen Drucksachen) durch die URL
des jeweiligen Objekts repräsentiert. Objektlisten sind also 
tatsächlich immer Listen von URLs.

### Vollständige Listenausgabe

In der einfachsten Form gibt der Server die Liste als Objekt 
mit nur einer einzigen Eigenschaft `items` aus. Der Wert dieser 
Eigenschaft ist die **vollständige Liste** der URLs aller 
in der Liste enthaltenen Objekte.

Diese einfachste Form der Antwort eignet sich nur für Listen mit
einer begrenzten Anzahl von Einträgen, wie beispielsweise die
Liste der Mitglieder einer Organisation.

Beispiel:

~~~~~  {#objektlisten_ex1 .json}
{
	"items": [
		"http://refserv.oparl.org/bodies/0/papers/2",
		"http://refserv.oparl.org/bodies/0/papers/5",
		"http://refserv.oparl.org/bodies/0/papers/7",
	]
}
~~~~~

### Paginierung  {#paginierung}

Für den Abruf von Listen mit vielen Elementen ist eine Blätterfunktion,
(Paginierung) vorgesehen. Darunter verstehen wir die Aufteilung einer Liste
in kleinere Teilstücke, die wir hier als Listenseiten bezeichnen.
Jede Listenseite wird vom Client jeweils mit einer eigenen API-Anfrage
abgerufen. Das dient dazu, die bei der jeweiligen Anfrage übertragenen
Datenmengen zu begrenzen und damit Antwortzeiten und Systemressourcen
sowohl beim Server als auch beim Client zu schonen.

Die Entscheidung, ob eine Seite teilweise und daher mit Paginierung
ausgegeben wird, liegt allein beim Server. Bei Listen mit mehr als 100
Einträgen ist dies EMPFOHLEN. Die Zahl der Einträge, die der
Server dabei je Listenseite ausliefert, SOLL dabei maximal 100 betragen.
Die Anzahl der Einträge (Obergrenze) MUSS auf allen Listenseiten der selben
Liste konstant gehalten werden, sofern nicht (beispielsweise auf der letzten
Listenseite) weniger Listeneinträge vorhanden sind.

Das nachstehende Beispiel zeigt, wie dem Client die URL zum
"Blättern", also zum Aufruf der jeweils nächsten Listenseite,
angeboten wird.


~~~~~  {#objektlisten_ex2 .json}
{
	"items": [
		"http://refserv.oparl.org/bodies/0/papers/2",
		"http://refserv.oparl.org/bodies/0/papers/5",
		"http://refserv.oparl.org/bodies/0/papers/7",
	],
	"nextPage": "http://refserv.oparl.org/bodies/0/papers/?skip=7",
	"count": 118
}
~~~~~

Wie oben zu sehen, enthält das Beispiel-Objekt nun eine zusätzliche 
Eigenschaft `nextPage`. Der Wert dieser Eigenschaft ist eine URL, die
dem Client dazu dient, die weiteren Einträge der Liste abzurufen.

Die Eigenschaft `count` DARF bei Listen grundsätzlich ausgegeben werden
und SOLL bei mehrseitigen Listen ausgegeben werden. Ihr Wert ist eine
Zahl und gibt an, wie viele Einträge die vollständige Liste aller Objekte
enthält.

Ruft der Client die unter `nextPage` angegebene URL auf, erhält er
wiederum ein Listenobjekt. Dieses Objekt MUSS, sofern noch immer mehr
Listeneinträge vorhanden sind, als ausgegeben wurden, wiederum die `nextPage`
Eigenschaft mit einer URL enthalten. Um alle Einträge einer Liste zu
erfassen, folgt der Client also jeweils der URL, die in der `nextpage`
Eigenschaft angegeben ist.

![Paginierung: Schematische Darstellung](images/pagination01.png)

Server-Implementierer entscheiden selbst, wie die `nextPage`-URL
aufgebaut ist und tragen damit selbst Verantwortung für die Funktionsweise
der Paginierung. Bei der Entscheidung für eine Form der Implementierung
sind weitere Anforderungen zu berücksichtigen:

* Es ist davon auszugehen, dass Clients für den gesamten Abruf aller
  Seiten einer Liste längere Zeit benötigen. In der Zwischenzeit kann sich
  der Inhalt der Liste bereits ändern, etwa durch das Hinzukommen neuer
  Einträge. Die Paginierung ist so zu implementieren, dass sich das
  Hinzukommen oder Entfernen von Einträgen möglichst nicht auf einen Client
  auswirkt, der aktuell die Liste paginiert, um alle Einträge abzurufen.

Eine ungünstige (unstabile) Form der Implementierung soll hier mit Hilfe einer
SQL-Abfrage illustriert werden. Gegeben sei eine Tabelle `example`, die einen 
numerischen Primärschlüssel `id` enthält. Nehmen wir an, die erste Seite der 
Liste wird mit der Abfrage

~~~~~  {#objektlisten_ex3 .sql}
SELECT * FROM example ORDER BY id LIMIT 10 OFFSET 0
~~~~~

abgerufen und würde 10 Datensätze mit den `id`s 1 bis 10 zurück liefern. Dann wird
die zweite Seite mit der Abfrage

~~~~~  {#objektlisten_ex4 .sql}
SELECT * FROM example ORDER BY id LIMIT 10 OFFSET 10
~~~~~

abgerufen. Sofern sich an der Tabelle zwischen den beiden Abfragen nichts
geändert hat, liefert die zweite Abfrage Datensätze mit `id` > 10 aus. Sollte
zwischen den beiden Abfragen jedoch beispielsweise der Datensätze mit der `id` 1
gelöscht worden sein, liefert die zweite Abfrage Datensätze mit `id` > 9. In
diesem Fall würde dies nur dazu führen, dass ein Datensatz (`id` = 10) zweimal
ausgegeben wird. Bei ungünstigeren Konstellationen wäre auch denkbar, dass
eine instabile Paginierung bewirkt, dass einzelne Datensätze beim Paginieren
übergangen werden.

Besser wäre es, bei der Paginierung die Eintragsgrenze, bei der eine Listenseite
beginnen soll, explizit zu benennen. Wurden auf der ersten
Listenseite die Datensätze mit den `id`s 1 bis 10 ausgegeben, so könnte der
Folgeaufruf, um beim SQL-Beispiel zu bleiben, so aussehen:

~~~~~  {#objektlisten_ex5 .sql}
SELECT * FROM example WHERE id > 10 ORDER BY id LIMIT 10
~~~~~

TODO: Bestimmte Listen können mit Einschränkung auf einen Datumsbereich
abgefragt werden. Mehr dazu in https://github.com/OParl/specs/issues/30
Fraglich ist, ob das in diesem Kapitel behandelt werden sollte oder in
einem anderen.

### Listen als Eigenschaften von Objekten

TODO: Listen können auch als Werte von Objekteigenschaften auftreten. 
Hierbei gibt es keine Paginierung, sondern es müssen alle URLs aufgelistet werden.
Das ist auszuformulieren und mit Beispielen zu zeigen.
