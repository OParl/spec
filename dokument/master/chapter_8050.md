oparl:Committee (Gremium)
------------------------

Das Gremium ist ein Personenkreis, üblicherweise von gewählten und/oder 
ernannten Mitgliedern. Beispiele hierfür sind der Stadtrat, Kreisrat, 
Gemeinderat, Ausschüsse und Bezirksvertretungen. Gremien halten Sitzungen 
ab, zu denen die Gremien-Mitglieder eingeladen werden.

![Objekttyp Committee](images/datenmodell_gremium.png)


### Eigenschaften ###

Schlüssel (`id`)
:   Zur eindeutigen Identifizierung des Gremiums im Kontext einer bestimmten 
    Körperschaft. In der Praxis kommen sowohl numerische IDs als auch 
    Namenskürzel (Beispiel: "STA" für den Stadtentwicklungsausschuss) vor. 
    Beides sollte hier Verwendung finden können.
Name (`name`)
:   Der Name des Gremiums. Beispiele: "Rat", "Hauptausschuss", 
    "Bezirksvertretung 1 (Innenstadt)"
Kurzname (`short_name`)
:   _Optional_. Eine zur Anzeige bestimmte, kürzere Form des Namens.
Zuletzt geändert (`last_modified`)
:   Datum und Uhrzeit der letzten Änderung


### Beziehungen ###

* Objekte vom Typ `oparl:Person` referenzieren auf Gremien, um die 
Mitgliedschaft/Zugehörigkeit einer Person im/zum Gremium zu kennzeichnen.
Diese Beziehung ist datiert. Das bedeutet, sie hat einen Anfangszeitpunkt und
ggf. einen Endzeitpunkt.
* Objekte vom Typ "Drucksache" verweisen auf Gremien. Beispielsweise wird 
eine Anfrage oder ein Antrag dem Rat und/oder einer bestimmten Bezirksvertretung 
zugeordnet. Details zu dieser Beziehung werden unter "Drucksache" erläutert.
* Das Gremium verweist auf die Körperschaft, zu der das Gremium gehört.

### Beispiel ###

~~~~~  {#committee_ex1 .json}
{
    "id": "7",
    "name": "Finanzausschuss",
    "short_name": "FA",
    "body": "1",
    "last_modified": "2012-08-16T14:05:27+02:00"
}
~~~~~

