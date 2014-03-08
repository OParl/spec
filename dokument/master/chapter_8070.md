oparl:Organisation (Organisation)
--------------------------------

Organisationen sind üblicherweise Parteien bzw. Fraktionen, denen die 
Personen angehören können.

![Objekttyp Organisation](images/datenmodell_organisation.png)

### Eigenschaften ###

Schlüssel (`id`)
:   Zur eindeutigen Kennzeichnung einer Organisation innerhalb des 
    Systems
Name (`name`)
:   Der gebräuchliche Name der Organisation, z.B. "SPD" oder "DIE LINKE".
Zuletzt geändert (`last_modified`)
:   Datum und Uhrzeit der letzten Änderung

#### Anmerkungen ####

* Unklar ist bislang, ob Organisationen in der Praxis eher Fraktionen 
("SPD-Fraktion im Kölner Rat", "SPD-Fraktion in Köln-Innenstadt") abbilden 
oder ob eher Ortsverbände von Parteien ("SPD Köln") gemeint sein werden. 
Einblicke, wie gängige Systeme dies handhaben, sollten evtl. gesammelt und 
berücksichtigt werden.

### Beziehungen ###

* Jede `oparl:Organisation` gehört zu einer Körperschaft.
* Personen können Organisationen angehören (*datiert*).

### Beispiel ###

~~~~~  {#organisation_ex1 .json}
{
    "id": "15",
    "name": "SPD",
    "body": "1",
    "last_modified": "2012-08-16T14:05:27+02:00"
}
~~~~~

