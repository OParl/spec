Datenmodell
===========

Das Datenmodell soll die Bausteine für die später zu entwerfende Schnittstelle definieren. Im folgenden werden sozusagen die Objekttypen bzw. die Klassen beschrieben, auf die über eine spätere API zugegriffen werden kann.

Einige Objekte werden eine eindeutige Identifizierung (ID) benötigen, wobei „eindeutig“ auch eine Frage des Kontextes ist. In den wenigsten Fällen wird es notwendig sein, eine Objekt-Kennung weltweit eindeutig zu machen. Darüber hinaus wird zu entscheiden sein, ob IDs unveränderlich oder veränderlich sein sollen.


Gebietskörperschaft
-------------------

Die Gebietskörperschaft erlaubt es, Körperschaften wie einen bestimmten Landkreis, eine bestimmte Gemeinde oder einen bestimmten Stadtbezirk in Form eines Datenobjekts abzubilden.

Viele RIS werden nur genau eine Instanz dieses Typs „beherbergen“. Denkbar ist aber auch, dass Systeme für einen Verbund von mehreren Körperschaften betrieben werden.

![Abbildung: Gebietskörperschaft](images/01.png)

### Eindeutige Identifizierung ###

Zur Identifizierung des Objekts kann der Amtliche Gemeindeschlüssel (AGS[1]) verwendet werden, der für Deutschland alle Gemeinden, Landkreise, kreisfreien Städte etc. eindeutig erfasst.

Vorteil der Verwendung des AGS:

* Kompakte, einfache und einheitliche Schreibweise für jede Körperschaft.
* Der AGS wird von Behörden genutzt, ist anerkannt und auch in anderen Medien, z.B. der Wikipedia, verbreitet.

Nachteil des AGS:

* Führende Nullen machen den Schlüssel fehleranfällig. Bestimmte Systeme wie z.B. Excel könnten den Inhalt als Zahlenwert erkennen und die führenden Nullen automatisch verwerfen.

### Eigenschaften ###

Name
:   Der Name der Gebietskörperschaft, z.B. "Köln" oder "Stadt Köln".

### Beziehungen ###

* Objekte vom Typ "Organisation" sind zwingend genau einer Gebietskörperschaft zugeordnet. So wird beispielseise eine SPD in Köln von einer SPD in Leverkusen unterschieden.
* Objekte vom Typ "Gremium" sind zwingend einer genau einer Gebietskörperschaft zugeordnet. Damit wird der "Rat" einer bestimmten Kommune von den gleichnamigen Gremien anderer Kommunen abgegrenzt.

Gremium
-------

Das Gremium ist ein Personenkreis, üblicherweise von gewählten und/oder ernannten Mitgliedern. Beispiele hierfür sind der Stadtrat, Kreisrat, Gemeinderat, Ausschüsse und Bezirksvertretungen. Gremien halten Sitzungen ab, zu denen die Gremien-Mitglieder eingeladen werden.

### Eigenschaften ###

### Beziehungen ###


Person
------

Jede natürliche Person, die Mitglied eines Gremiums ist, ist als Person im Datenmodell eindeutig identifizierbar.

### Eigenschaften ###

### Beziehungen ###


Organisation
------------

Organisationen sind üblicherweise Parteien bzw. Fraktionen, denen die Personen angehören können.

### Eigenschaften ###

### Beziehungen ###


Sitzung
-------

Eine Sitzung ist die Versammlung der Mitglieder eines Gremiums zu einem bestimmten Zeitpunkt. Sitzungen können eine laufende Nummer haben., üblicherweise beginnend bei 1 zu Beginn einer Wahlperiode, haben.

Die geladenen Teilnehmer der Sitzung sind jeweils als „Person“ in entsprechender Form referenziert. Verschiedene Drucksachen (Einladung, Ergebnis- und Wortprotokoll) werden ebenfalls referenziert.


### Eigenschaften ###

### Beziehungen ###


Tagesordnungspunkt
------------------

Der Tagesordnungspunkt wird für eine bestimmte Sitzung angelegt, erhält eine (innerhalb dieser Sitzung eindeutige) Nummer und einen Titel (Betreff). Nach der Sitzung wird dem Tagesordnungspunkt außerdem ein Ergebnis angehängt. Falls abweichend von der ursprünglichen Beschlussvorlage (z.B. durch Berücksichtigung eines Änderungsantrags) kann ein bestimmter Beschlusstext zu Protokoll gegeben werden. Sofern das Abstimmungsergebnis nicht einstimmig ist, kann es durch mehrere referenzierende Stimmabgaben festgehalten werden.


### Eigenschaften ###

### Beziehungen ###


Stimmabgabe
-----------

Wie eine Person bzw. eine Fraktion zu einem Tagesordnungspunkt abgestimmt hat, wird durch eine Stimmabgabe festgehalten. Ganze Abstimmungsergebnisse bestehen überlicherweise aus mehreren Stimmabgaben. Jede Stimmabgabe gibt entweder die (einzelne) Stimme einer Peson wieder, in diesem Fall ist die Anzahl der Stimmen zwingend 1. Oder eine Stimmabgabe gibt das Abstimmungsverhalten einer ganzen Gruppe von Personen wieder. Dann ist die Anzahl der Stimmen anzugeben und statt einer Person eine Organisation (in der Regel die Fraktion) zu referenzieren.


### Eigenschaften ###

### Beziehungen ###


Drucksache
----------

Eine Drucksache bildet Mitteilungen, Antworten auf Anfragen, Beschlussvorlagen, Anfragen und Anträge ab. Jede Drucksache erhält eine eindeutige Kennung. Das Datum gibt an, wann die Drucksache erzeugt bzw. veröffentlicht wurde.

Die Drucksache verweist auf genau ein Hauptdokument. Darüber hinaus können beliebig viele Dokumente als Anhang referenziert werden.


### Eigenschaften ###

### Beziehungen ###


Dokument
--------

Ein Dokument hält die Daten und Metadaten einer Datei vor, beispielsweise einer PDF-Datei, eines RTF- oder Word-Dokuments. Wird von einem Word-Dokument eine PDF-Ableitung hinterlegt, ist diese Ableitung ebenfalls ein Dokument, das jedoch nicht als Master gekennzeichnet wird, sondern auf den entsprechenden Master verweist.


### Eigenschaften ###

### Beziehungen ###


Ort
---

Dieser Objekttyp dient dazu, einen Ortsbezug einer Drucksache formal abzubilden. Ortsangaben können sowohl aus Textinformationen bestehen (beispielsweise der Name einer Straße/eines Platzes oder eine genaue Adresse) oder aus einer Geo-Koordinatenangabe aus Längen- und Breitengrad.
