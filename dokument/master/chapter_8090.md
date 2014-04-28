oparl:AgendaItem (Tagesordnungspunkt)  {#oparl_agendaitem}
------------------------------------

Der Tagesordnungspunkt wird für eine bestimmte Sitzung angelegt, erhält eine 
(innerhalb dieser Sitzung eindeutige) Nummer und einen Titel (Betreff). Nach 
der Sitzung wird dem Tagesordnungspunkt außerdem ein Ergebnis angehängt. 
Unter Umständen kann dem Tagesordnungspunkt ein bestimmter Beschlusstext 
beigefügt sein.

Überlicherweise haben Sitzungen mehrere Tagesordnungspunkte.

### Eigenschaften ###

Nummer (`identifier`)
:   Beispiel: "1.2.3". Diese Nummer gibt an, in welcher Reihenfolge die 
    Tagesordnungspunkte einer Sitzung normalerweise behandelt werden. Im 
    Kontext einer Sitzung ist diese Nummer eindeutig.
Öffentlich (`public`)
:   Kennzeichnet, ob der Tagesordnungspunkt in öffentlicher Sitzung 
    behandelt wird. Kann die Werte `true` (öffentlich) oder `false` annehmen.
Titel (`title`)
:   Das Thema des Tagesordnungspunktes
Ergebnis (`result`)
:   _Optional_. Kategorische Information darüber, welches Ergebnis die Beratung des
    Tagesordnungspunktes gebracht hat. In der Praxis sind hier Kategorien wie
     "Unverändert beschlossen", "Geändert beschlossen", "Endgültig abgelehnt",
     "Zur Kenntnis genommen", "Ohne Votum in nachfolgende Gremien überwiesen"
     und weitere zu erwarten.
Ergebnis Details (`result_details`)
:   _Optional_. Ermöglicht die Angabe zusätzlicher Textinformationen zum 
    Ergebnis, zum Beispiel im Fall der Verweisung an ein anderes Gremium die
    Angabe, an welches Gremium verwiesen wurde.
Beschlusstext (`resolution_text`)
:   _Optional_. Falls in diesem Tagesordnungspunkt ein Beschluss gefasst 
    wurde, kann der Text hier hinterlegt werden. Das ist besonders dann in der 
    Praxis relevant, wenn der gefasste Beschluss (z.B. durch Änderungsantrag) 
    von der Beschlussvorlage abweicht.
Zuletzt geändert (`last_modified`)
:   Datum und Uhrzeit der letzten Änderung

#### Anmerkungen ####

* Einige Systeme vergeben zu Tagesordnungspunkten intern unveränderliche, 
numerische IDs. Es ist unklar, ob es zusätzlichen Nutzen bringt, derartige 
IDs, neben den Nummern, in den Standard zu übernehmen. Dies würde vermutlich 
nur Sinn ergeben, wenn es als Pflichtfeld gelten könnte.
* Teil der Beratungen über einheitliche Nomenklatur im Standard sollte sein,
eine Vereinheitlichung der Werte für die Eigenschaft `result` zu diskutieren.

### Beziehungen ###

* Jeder Tagesordnungspunkt gehört zu genau einem `oparl:Meeting`.
* Der Tagesordnungspunkt kann auf eine Drucksache verweisen, die im Rahmen
dieses Tagesordnungspunkt beraten werden soll.
* Es können `oparl:Person` Objekte referenziert werden, die während der Abstimmung zu diesem Tagesordnungspunkt *nicht* anwesend waren.

### Beispiel in kompakter Form ###

~~~~~  {#agendaitem_ex1 .json}
{
    "@context": "https://oparl.beispielris.de/Pfad/zum/Kontext/oparl.jsonld"
    "@type": "oparl:AgendaItem",
    "@id": "http://oparl.beispielris.de/agendaitem/3271",
    "identifier": "3.1.2",
    "public": true,
    "title": "Gemeinschaftsgrundschule Hornschaftsstraße/Höhenhaus. Hier: Anfrage von Herrn Philippi",
    "result": "Geändert beschlossen",
    "resolution_text": "Der Beschluss weicht wie folgt vom Antrag ab: ...",
    "people_absent": [
        "beispielris:people/1002",
        "beispielris:people/1003"
    ],
    "last_modified": "2012-08-16T14:05:27+02:00"
}
~~~~~


