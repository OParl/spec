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
    "meeting": "beispielris:meetings/281",
    "number": "10.1",
    "name": "Satzungsänderung für Ausschreibungen",
    "public": true,
    "consultations": [
        "beispielris:consultations/1034",
        "beispielris:consultations/1235"
    ],
    "result": "besipielris:vocab/decided_modified",
    "resolutionText": "Der Beschluss weicht wie folgt vom Antrag ab: ...",
    "absentParticipants": [
        "beispielris:people/75"
    ],
    "paper": "beispielris:paper/2812",
    "last_modified": "2012-08-16T14:05:27+02:00"
}
~~~~~

### Eigenschaften ###

`meeting`
:   URL der Sitzung (`oparl:Meeting`), dem der Tagesordnungspunkt zugeordnet ist.
    ZWINGEND.

`number`
:   Nummer des Tagesordnungspunktes. Eine beliebige Zeichenkette, wie z.B. "10.", "10.1", "C", "c)" o.ä.
    Die Reihenfolge wird dadurch nicht festgelegt, sondern durch die Reihenfolge der TOPs im `agendaItem`-Attribut
    von  `oparl:Meeting`
    OPTIONAL
`name`
:   Das Thema des Tagesordnungspunktes.
    ZWINGEND.

`public`
:   Kennzeichnet, ob der Tagesordnungspunkt zur Behandlung in öffentlicher Sitzung 
    vorgesehen ist/war. Es wird ein Wahrheitswert (`true` oder `false`) erwartet.
    EMPFOHLEN.

`consultations`
:   Liste der URLs der Beratungen (oparl:Consultation), die diesem Tagesordnungspunkt
    zugewiesen sind, oder alternativ die URL zum Abruf dieser Liste.
    Die Eigenschaft ist ZWINGEND. Sofern diesem Tagesordnungspunkt keine Beratungen
    zugewiesen sind, bleibt die Liste ohne Einträge.

`result`
:   Kategorische Information darüber, welches Ergebnis die Beratung des
    Tagesordnungspunktes erbracht hat. Es wird zu einem Objekt verlinkt, welches ein `skos:prefLabel`-Attribut
    mit einer Zeichenkette hat. In der Praxis sind hier Kategorien wie
    "Unverändert beschlossen", "Geändert beschlossen", "Endgültig abgelehnt",
    "Zur Kenntnis genommen", "Ohne Votum in nachfolgende Gremien überwiesen"
    und weitere zu erwarten.
    Alternativ können, sobald dieses zur Verfügung steht, URLs aus einem OParl
    Vokabular verwendet werden, wie im Beispiel oben zu sehen. Diese dienen dazu,
    Kategorien über Systemgrenzen hinweg maschinenlesbar zu vereinheitlichen.
    EMPFOHLEN

`resolutionText`
:   Falls in diesem Tagesordnungspunkt ein Beschluss gefasst 
    wurde, kann der Text hier hinterlegt werden. Das ist besonders dann in der 
    Praxis relevant, wenn der gefasste Beschluss (z.B. durch Änderungsantrag) 
    von der Beschlussvorlage abweicht.
    OPTIONAL.

`paper`
:   `oparl:Paper`. Zwar kann auch das `oparl:Meeting` darauf verweisen, aber hier sind solche Verweise in der
    Regel präziser, da sich Drucksachen regelmäßig für einen TOP relevant sind und nicht für alle TOPs.
    OPTIONAL

`auxiliaryDocument`
:  `oparl:Document` zum TOP.
    OPTIONAL

`created`
:   Erzeugungsdatum und -zeit des Objekts.
    EMPFOHLEN

`lastModified`
:   Datum und Uhrzeit der letzten Änderung.
    EMPFOHLEN
