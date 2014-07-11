Objektlisten  {#objektlisten}
------------

Generell kommt es beim Aufruf eines einzelnen Objekts in vielen
Fällen vor, dass eine Reihe von Objekten referenziert wird, die
mit dem aktuellen Objekt in Beziehung stehen. Für einzelne
Eigenschaften ist es nur erlaubt, genau ein verbundenes Objekt
zu referenziert (unter "Schema" gekennzeichnet mit einer "Kardinalität"
von höchstens 1). Andere Eigenschaften erlauben die Verknüpfung einer
beliebigen Anzahl von anderen Objekten. Ein Beispiel dafür liefert der
Objekttyp `oparl:System`, der über die Eigenschaft `body` auf sämtliche
Objekte vom Typ `oparl:Body` (Körperschaften) des Systems zeigt.

Dieses Kapitel beschreibt, wie solche Listen von verknüpften Objekten
ausgegeben werden und welche Möglichkeiten dabei Server und Clients haben,
um diese Ausgabe zu beeinflussen. Dabei werden die folgenden Konzepte
behandelt:

* Interne und externe Ausgabe von Listen
* Kompakte und vollständige Form
* Paginierung
* Sortierung
* Filter

### Interne und externe Ausgabe von Listen {#objektlisten_internextern}

Das folgende Beispiel zeigt eine Möglichkeit, wie die Eigenschaft `body`
ausgegeben werden kann. Dabei handelt es sich um eine *interne*,
also die Ausgabe der Listenelemente direkt im eigentlich abgerufenen Objekt.

~~~~~  {#objektlisten_ex1 .json}
{
    "id": "https://oparl.example.org/",
    "type": "http://oparl.org/schema/1.0/System",
    "body": [
        "https://oparl.example.org/bodies/1",
        "https://oparl.example.org/bodies/2",
        "https://oparl.example.org/bodies/3"
    ],
    ...
}
~~~~~

Wie oben zu sehen ist, ist der Wert der Eigenschaft `body` in diesem Fall ein
Array. Die Einträge des Arrays sind URLs. Es handelt sich dabei um die URLs
aller Objekte vom Typ `oparl:Body`, die mit dem gezeigten `oparl:System`
Objekt in Beziehung stehen.

Eine alternative Möglichkeit für die Ausgabe derselben Information
ist die *externe* Listenausgabe. Mit dieser Form der Ausgabe sieht das
oben gezeigte Objekt nun so aus:

~~~~~  {#objektlisten_ex2 .json}
{
    "id": "https://oparl.example.org/",
    "type": "http://oparl.org/schema/1.0/System",
    "body": "https://oparl.example.org/bodies/",
    ...
}
~~~~~

In diesem Fall ist der Wert der Eigenschaft `body` kein Array, sondern
eine URL. Diese URL kann vom Client genutzt werden, um die entsprechende
Liste mit Objekten aufzurufen. Wie die entsprechende Ausgabe des Servers
aussieht, wird weiter unten beschrieben.

Diese beiden Mechanismen sind grundsätzlich immer anwendbar, wenn eine
Mehrzahl von Objekten mit einem Objekt verknüpft ist, unabhängig von der
Art des verknüpfenden oder des verknüpften Objekts.

Die Entscheidung, ob eine Liste intern, also im Kontext eines einzelnen
Objekts, oder extern, also über eine eigene URL ausgegeben wird, obliegt
allein dem Server. Bei der Abwägung durch den Server sollte dieser 
berücksichtigen:

1. Die interne Listenausgabe eignet sich für kleine Listen mit wenigen
   Elementen.

2. Die externe Listenausgabe eignet sich für längere Listen, da hier
   auch Paginierung und Filterung möglich sind.

3. Die externe Listenausgabe ermöglicht über die Ausgabe einer URL
   hinaus auch die Ausgabe vollständiger Objekte.

Mehr zu 2. und 3. ist den folgenden Abschnitten zu entnehmen. 

Die externe Listenausgabe wird explizit EMPFOHLEN in den folgenden Fällen:

* Eine Liste wächst mit der Zeit, wie z.B. die Liste aller Drucksachen
  einer Körperschaft.

* Es handelt sich um Listen von Objekten des Typs `oparl:Paper` (Drucksache)
  oder `oparl:Meeting`

* Es handelt sich bei der Liste um einen [Feed](#feeds).

Server DÜRFEN in den URLs für die externe Ausgabe von Listen NICHT den
reservierten URL-Parameter `listformat` verwenden. Server MÜSSEN in den
URLs für den Listenaufruf stets die URL zum Abruf der *kompakten Form*
ausgeben. Die Unterscheidung zwischen *kompakter* und *vollständiger*
Form wird nachfolgend beschrieben.


### Kompakte und vollständige Form (`listformat`) {#objektlisten_listformat}

Wie im vorangehenden Abschnitt beschrieben, gibt es die Möglichkeit,
Listen von Objekten über eine eigene URL zugänglich zu machen (*externe
Listenausgabe*). Bei dieser externen Ausgabe gibt es zwei verschiedene
Ausgabeformate, die sich durch den Umfang der Informationen unterscheiden,
die je Objekt ausgegeben werden:

* **Kompakte Form**: Hier wird je Eintrag nur die URL des Objekts
  ausgegeben.

* **Vollständige Form**: Hier wird jedes Objekt in der Liste vollständig
  ausgegeben. Was genau "vollständig" bedeutet, wird nachstehend näher
  beschrieben.

Die Entscheidung, ob die kompakte oder die vollständige Form
ausgegeben wird, obliegt dem Client. Dieser aktiviert die vollständige
Ausgabe über den URL-Parameter `listformat`. Ist dieser Parameter nicht
gesetzt, MUSS der Server die kompakte Form ausgeben. Ist der Parameter
auf den Wert `complete` gesetzt, MUSS der Server die vollständige Form
ausgeben.

Hat beispielsweise der Server zum externen Aufruf der Liste die URL

    https://oparl.example.org/bodies/1/papers/

ausgegeben, ist unter dieser grundsätzlich die kompakte Form zu erwarten.
Der Client kann diese URL so erweitern, um die vollständige Form
anzufordern:

    https://oparl.example.org/bodies/1/papers/?listformat=complete

Das folgende Beispiel zeigt, wie die Ausgabe der kompakten Form in einem
einfachen Fall aussehen kann:

~~~~~  {#objektlisten_ex3 .json}
{
    "items": [
        "https://oparl.example.org/bodies/0/papers/2",
        "https://oparl.example.org/bodies/0/papers/5",
        "https://oparl.example.org/bodies/0/papers/7"
    ]
}
~~~~~

Die grundlegende Syntax ist für die externe Listenausgabe identisch,
unabhängig davon, ob die kompakte oder vollständige Form ausgegeben wird:
Der Server gibt ein JSON-Objekt aus, das eine Eigenschaft `items` enthält.
Diese Eigenschaft hat den Typ `Array`.

Die vollständige Form ist so definiert, dass darin jedes Objekt mit allen
von OParl für diesen Typ definierten Eigenschaften ausgegeben werden MUSS,
die auch beim individuellen Aufruf des jeweiligen Objekts ausgegeben werden.

Das nachfolgende Beispiel zeigt dies verkürzt, analog zur oben gezeigten Liste:

~~~~~  {#objektlisten_ex3 .json}
{
    "items": [
        {
            "id": "https://oparl.example.org/bodies/0/papers/2",
            "type": "http://oparl.org/schema/1.0/Paper",
            "body": "https://oparl.example.org/bodies/0",
            "name": "Antwort auf Anfrage 1200/2014",
            "publishedDate": "2014-04-04T16:42:02+02:00",
            "paperType": "Beantwortung einer Anfrage",
            "mainDocument": "https://oparl.example.org/documents/925",
            "originator": [
                "https://oparl.example.org/organization/2000"
            ]
        },
        {
            "id": "https://oparl.example.org/bodies/0/papers/5",
            "type": "http://oparl.org/schema/1.0/Paper",
            "body": "https://oparl.example.org/bodies/0",
            "name": "Mitteilung der Verwaltung",
            "publishedDate": "2014-06-01T12:24:18+02:00",
            "paperType": "Mitteilung",
            "mainDocument": "https://oparl.example.org/documents/2758",
            "originator": [
                "https://oparl.example.org/people/1000"
            ]
        },
        ...
    ]
}
~~~~~

Wie zu sehen ist, hat die Eigenschaft `items` als Wert nun ein Array mit
JSON-Objekten.

Die Anforderung der vollständigen Form wirkt sich *nicht rekursiv* aus.
Die einzelnen JSON-Objekte können ihrerseits wieder Eigenschaften
haben, die auf mehrere Objekte verweisen. Diese Eigenschaften sind von der
Anforderung der vollständigen Listenausgabe durch den Client nicht betroffen.
Hier obliegt es wieder dem Server, zwischen der internen und der externen
Listenausgabe (siehe oben) zu wählen. Bei der internen Listenausgabe ist ohnehin
nur die kompakte Form (Ausgabe von URLs), wie oben im Beispiel gezeigt, erlaubt.

Die Sortierreihenfolge der ausgegebenen Einträge SOLL unabhängig
von der Ausgabe der kompakten oder vollständigen Form identisch sein.

Die vollständige Listenausgabe SOLL nur für Listen verwendet
werden, die bis zu 100 Einträge umfassen. Links zu solch kurzen Listen
wir jedoch in OParl-Objekten in der Regel nicht enthalten.


### Paginierung  {#paginierung}

Für die externe Listenausgabe von Listen mit vielen Elementen ist eine Blätterfunktion
(Paginierung) vorgesehen. Damit ist die Aufteilung einer Liste
in kleinere Teilstücke gemeint, die wir als *Listenseiten* bezeichnen.
Jede Listenseite wird vom Client jeweils mit einer eigenen API-Anfrage
abgerufen. Das dient dazu, die bei der jeweiligen Anfrage übertragenen
Datenmengen und Antwortzeiten zu begrenzen und Systemressourcen
sowohl beim Server als auch beim Client zu schonen.

Die Entscheidung, ob eine Seite teilweise und daher mit Paginierung
ausgegeben wird, liegt allein beim Server. Bei Listen mit mehr als 100
Einträgen ist dies EMPFOHLEN.

Der Server gibt für eine Liste, bei der die Paginierung aktiv ist, d. h.
nicht alle Listenelemente ausgegeben wurde, zusätzliche Eigenschaften aus.
Das nachfolgende Beispiel zeigt dies für den Anfang einer paginierten Liste:

~~~~~  {#objektlisten_ex4 .json}
{
    "items": [
        "https://oparl.example.org/bodies/0/papers/2",
        "https://oparl.example.org/bodies/0/papers/5",
        "https://oparl.example.org/bodies/0/papers/7",
        ...
    ],
    "itemsPerPage": 100,
    "nextPage": "https://oparl.example.org/bodies/0/papers/?skip_id=495"
}
~~~~~

Über die ZWINGEND bei Paginierung ausgegebene Eigenschaft `itemsPerPage`
kommuniziert der Server, wie viele Einträge pro Listenseite
ausgegeben werden. Die Zahl der Einträge, die der
Server dabei je Listenseite ausliefert, SOLL dabei mindestens 10 und
maximal 100 betragen. Der Wert von `itemsPerPage` MUSS auf allen
Listenseiten derselben Liste einheitlich sein. Nur bei Ausgabe der
letzten Listenseite DARF der Server weniger Einträge ausgeben, als
von `itemsPerPage` angegeben.

Weiterhin wird bei Paginierung über eine Eigenschaft `nextPage` eine
URL zum Abruf der jeweils nächsten Listenseite ausgegeben. Die
Beschaffenheit der URL bestimmt der Server frei, das obige Beispiel
ist in keiner Form bindend.

Es ergibt sich eine typische Abfolge, wie Clients bei Bedarf
mit mehreren Anfragen ganze Objektlisten vom Server abrufen:

1. Der Server stellt eine URL für eine Liste zur Verfügung.

2. Der Client ruft diese URL der Liste auf.

3. Der Server antwortet mit einer verkürzten Listenausgabe und 
   gibt mittels `nextPage`-Eigenschaft die URL für den
   Abruf der nächsten Listenseite an.

4. Der Client ruft die URL für die nächste Listenseite auf.

Die Punkte 3 und 4 können sich nun so oft wiederholen, bis
die letzte Listenseite erreicht ist.

5. Der Server liefert die letzte Listenseite ohne
   `nextPage`-Eigenschaft aus.

Zusätzlich zur für die Paginierung ZWINGENDEN Eigenschaft
`nextPage`, die lediglich auf der letzten Listenseite entfällt,
können Server OPTIONAL weitere URLs zum Abruf bestimmter
Listenseiten anbieten:

Erste Listenseite (Eigenschaft `firstPage`):
:   Sofern die aktuell abgerufene Listenseite nicht den Anfang der
    Liste wiedergibt, KANN der Server diese Eigenschaft ausgeben,
    deren Wert die URL zum Abruf der *ersten* Listenseite ist.

Letzte Listenseite (Eigenschaft `lastPage`):
:   Sofern die aktuell abgerufene Listenseite nicht das Ende der
    Liste wiedergibt, KANN der Server diese Eigenschaft ausgeben,
    deren Wert die URL zum Abruf der *letzten* Listenseite ist.

Vorherige Listenseite (Eigenschaft `prevPage`):
:   Sofern die aktuell abgerufene Listenseite nicht den Anfang der
    Liste wiedergibt, KANN der Server diese Eigenschaft ausgeben,
    deren Wert die URL zum Abruf der *vorigen* Listenseite ist.

Damit eröffnet der Server dem Client zusätzliche Möglichkeiten,
die einzelnen Listenseiten abzurufen.

![Paginierung: Schematische Darstellung](images/pagination01.png)

Server-Implementierer entscheiden selbst, wie die URLs zum Abruf einzelner
Listenseiten aufgebaut sind und tragen damit selbst Verantwortung für die
Funktionsweise der Paginierung. Bei der Entscheidung für eine Form der
Implementierung sollten die folgenden Anforderungen von Clients
berücksichtigt werden:

* Es ist davon auszugehen, dass Clients für den gesamten Abruf aller
Seiten einer Liste längere Zeit benötigen. In der Zwischenzeit kann sich
der Inhalt der Liste bereits ändern, etwa durch das Hinzukommen neuer
Einträge. Die Paginierung ist idealerweise so zu implementieren, dass sich
das Hinzukommen oder Entfernen von Einträgen möglichst nicht auf einen Client
auswirkt, der aktuell die Liste paginiert, um alle Einträge abzurufen. Wir
bezeichnen dies als **stabile Paginierung**.

* Eine wesentliche Anforderung an Listen mit Paginierung ist, dass alle
Einträge der Liste in einer konsistenten Reihenfolge sortiert ausgegeben
werden MÜSSEN. Das bedeutet, dass die Sortierung beim Server im Idealfall
anhand einer eindeutigen und unveränderlichen Objekteigenschaft vorgenommen
wird. Hierfür eignen sich die Objekt-URLs, da sie genau diese beiden
Anforderungen erfüllen sollten.

Über die Sortierung hinaus können bei der Implementierung einer stabilen 
Paginierung auf Server-Seite weitere Überlegungen einbezogen werden.
Zur Verdeutlichung soll hier eine ungünstige (unstabile) Form der
Implementierung mit Hilfe einer SQL-Abfrage illustriert werden. Gegeben sei
eine Tabelle `example`, die einen 
numerischen Primärschlüssel `id` enthält. Nehmen wir an, die erste Seite der 
Liste wird mit der Abfrage

~~~~~  {#objektlisten_ex3 .sql}
SELECT * FROM example ORDER BY id LIMIT 10 OFFSET 0
~~~~~

abgerufen und würde 10 Datensätze mit den `id`s 1 bis 10 zurückliefern. Dann wird
die zweite Seite mit der Abfrage

~~~~~  {#objektlisten_ex4 .sql}
SELECT * FROM example ORDER BY id LIMIT 10 OFFSET 10
~~~~~

abgerufen. Sollte nach der ersten, aber vor der zweiten Abfrage beispielsweise 
der Datensatz mit der `id=1` gelöscht worden sein, liefert die zweite Abfrage
Datensätze mit `id` > 9. In diesem Fall würde dies nur dazu führen, dass ein
Datensatz (`id=10`) zweimal ausgegeben wird. Bei ungünstigeren Konstellationen
wäre auch denkbar, dass eine unstabile Paginierung bewirkt, dass einzelne 
Datensätze beim Paginieren übergangen werden. Je nach Bedeutung der fehlenden
Datensätze können solche Inkonsistenzen erhebliche Auswirkungen haben.

Besser wäre es, bei der Paginierung die Eintragsgrenze, bei der eine Listenseite
beginnen soll, explizit zu benennen. Wurden auf der ersten
Listenseite die Datensätze mit den IDs 1 bis 10 ausgegeben, so könnte der
Folgeaufruf, um beim SQL-Beispiel zu bleiben, so aussehen:

~~~~~  {#objektlisten_ex5 .sql}
SELECT * FROM example WHERE id > 10 ORDER BY id LIMIT 10
~~~~~

Die zuvor beschriebenen Anforderungen für die Paginierung von Listen
gelten auch unverändert, wenn der Umfang der Liste durch Abfrageparameter
vom Client eingeschränkt wurde.


### Sortierung

OParl definiert keine Möglichkeit für Clients, auf die Reihenfolge von Listeneinträgen
Einfluss zu nehmen. Von Servern wird die Einhaltung einiger grundlegender Anforderungen
erwartet, die teilweise bereits erwähnt wurden.

Server SOLLEN generell für eine **stabile Sortierung** von Listeneinträgen sorgen. Das
heißt, die Sortierung von Einträgen folgt einem konstanten Prinzip und ändert sich nicht von
Abfrage zu Abfrage. Eine Einfache Möglichkeit, dies Umzusetzen, wäre in vielen Fällen
die Sortierung von Objekten nach ihrer eindeutigen und unveränderlichen ID.


### Filter  {#filter}

Bei der *externen Listenausgabe* (siehe weiter oben) werden in Abhängigkeit vom ausgegebenen
Objekttyp bestimmte Möglichkeiten geboten, die Ausgabe von Listen auf eine
Teilmenge einzuschränken.

Hierfür sind die URL-Parameter `startdate` und `enddate` vorgesehen. Beide können vom Client
unabhängig voneinander gesetzt werden. Sie schränken die Objektmenge anhand auf einen
Zeitraum ein, der entweder einseitig oder beidseitig begrenzt ist. Die Einschränkung bezieht
sich auf ein Bezugsdatum, das vom Objekttyp abhängt.

Der Filter mittels `startdate` und `enddate` ist nur auf Listen mit den folgenden Objekttypen
anwendbar:

* `oparl:File`: Bezugsdatum ist hier die Eigenschaft `date` (Erstellungsdatum)
* `oparl:Meeting`: Bezugsdatum ist hier die Eigenschaft `start` (Startzeitpunkt der Sitzung)
* `oparl:Paper`: Bezugsdatum ist hier die Eigenschaft `publishedDate` (Veröffentlichungsdatum)

Für die genannten Objekttypen MUSS der Server bei externer Listenausgabe die beschriebenen
Filter unterstützen.

Die Filter werden vom Client aktiviert, indem der oder die gewünschte(n) URL-Parameter
der vom Server angegebenen URL für die Listenausgabe hinzugefügt werden. Lautet diese
URL für eine Liste von Drucksachen so,

    https://oparl.example.org/papers/

dann kann der Client die folgende URL bilden, um die Ausgabe der Liste auf Drucksachen
einzuschränken, die nach dem 1.1.2014 veröffentlicht wurden:

    https://oparl.example.org/papers/?startdate=2014-01-01T00%3A00%3A00%2B01%3A00

Der Server interpretiert die Angabe eines `startdate` so, dass das Bezugsdatum
aller ausgegebenen Objekte gleich oder größer dem im Parameter angegebenen Datum
sein muss. Der Parameter `enddate` ist entsprechend so zu interpretieren, dass
alle Bezugsdaten der ausgelieferten Objekte kleiner oder gleich dem angegebenen
Wert sein müssen.

Sind beide Parameter gesetzt, handelt es sich um eine Boolsche UND-Verknüpfung.
Der Server liefert entsprechend nur Objekte aus, deren Bezugsdatum größer/gleich
dem Wert von `startdate` und kleiner/gleich dem Wert von `enddate` ist.

Clients MÜSSEN die Werte von `startdate` und `enddate` im Format xsd:dateTime, also
mit Uhrzeit und Zeitzone, angeben (siehe dazu auch [Datums- und Zeitangaben](#datum_zeit))
und für eine entsprechende URL-Kodierung sorgen.
