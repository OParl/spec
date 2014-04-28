oparl:AgendaItem (Tagesordnungspunkt)  {#oparl_agendaitem}
------------------------------------

Tagesordnungspunkte sind die Bestandteile von Sitzungen (`oparl:Meeting`).
Jeder Tagesordnungspunkt widmet sich inhaltlich einem bestimmten Thema,
wozu in der Regel auch die Beratung bestimmter Drucksachen gehört.

Ein Beispiel in kompakter Form:

~~~~~  {#agendaitem_ex1 .json}
{
    "@context": "https://oparl.beispielris.de/Pfad/zum/Kontext/oparl.jsonld"
    "@type": "oparl:AgendaItem",
    "@id": "http://oparl.beispielris.de/agendaitem/3271",
    "meeting": "http://oparl.beispielris.de/meetings/281",
    "name": "Satzungsänderung für Ausschreibungen",
    "public": true,
    "consultations": [
        "http://oparl.beispielris.de/consultations/1034"
    ],
    "result": "http://oparl.org/vocab/decided_modified",
    "resolutionText": "Der Beschluss weicht wie folgt vom Antrag ab: ...",
    "absentParticipants": [
        "http://oparl.beispielris.de/people/75"
    ],
    "last_modified": "2012-08-16T14:05:27+02:00"
}
~~~~~

### Eigenschaften ###

`meeting`
:   URL der Sitzung (`oparl:Meeting`), dem der Tagesordnungspunkt zugeordnet ist.
    Die Eigenschaft ist ZWINGEND.

`name`
:   Das Thema des Tagesordnungspunktes.
    Die Eigenschaft ist ZWINGEND.

`public`
:   Kennzeichnet, ob der Tagesordnungspunkt zur Behandlung in öffentlicher Sitzung 
    vorgesehen ist/war. Es wird ein Wahrheitswert (`true` oder `false`) erwartet.
    Die Eigenschaft ist EMPFOHLEN.

`consultations`
:   Liste der URLs der Beratungen (oparl:Consultation), die diesem Tagesordnungspunkt
    zugewiesen sind, oder alternativ die URL zum Abruf dieser Liste.
    Die Eigenschaft ist ZWINGEND. Sofern diesem Tagesordnungspunkt keine Beratungen
    zugewiesen sind, bleibt die Liste ohne Einträge.

`result`
:   Kategorische Information darüber, welches Ergebnis die Beratung des
    Tagesordnungspunktes erbracht hat. In der Praxis sind hier Kategorien wie
    "Unverändert beschlossen", "Geändert beschlossen", "Endgültig abgelehnt",
    "Zur Kenntnis genommen", "Ohne Votum in nachfolgende Gremien überwiesen"
    und weitere zu erwarten.
    Alternativ können, sobald dieses zur Verfügung steht, URLs aus einem OParl
    Vokabular verwendet werden, wie im Beispiel oben zu sehen. Diese dienen dazu,
    Kategorien über Systemgrenzen hinweg maschinenlesbar zu vereinheitlichen.
    Die Eigenschaft ist EMPFOHLEN.

`resolutionText`
:   Falls in diesem Tagesordnungspunkt ein Beschluss gefasst 
    wurde, kann der Text hier hinterlegt werden. Das ist besonders dann in der 
    Praxis relevant, wenn der gefasste Beschluss (z.B. durch Änderungsantrag) 
    von der Beschlussvorlage abweicht.
    Diese Eigenschaft ist OPTIONAL.

`created`
:   Erzeugungsdatum und -zeit des Objekts. EMPFOHLEN.

`lastModified`
:   Datum und Uhrzeit der letzten Änderung. EMPFOHLEN.
