oparl:AgendaItem (Tagesordnungspunkt)  {#oparl_agendaitem}
-------------------------------------

Tagesordnungspunkte sind die Bestandteile von Sitzungen (`oparl:Meeting`).
Jeder Tagesordnungspunkt widmet sich inhaltlich einem bestimmten Thema,
wozu in der Regel auch die Beratung bestimmter Drucksachen gehört.

Ein Beispiel in kompakter Form:

~~~~~  {#agendaitem_ex1 .json}
{
    "@context": "https://oparl.beispielris.de/Pfad/zum/Kontext/oparl.jsonld",
    "@type": "oparl:AgendaItem",
    "@id": "https://oparl.beispielris.de/agendaitem/3271",
    "meeting": "beispielris:meeting/281",
    "number": "10.1",
    "name": "Satzungsänderung für Ausschreibungen",
    "public": true,
    "consultation": [
        "beispielris:consultation/1034",
        "beispielris:consultation/1235"
    ],
    "result": "besipielris:vocab/decided_modified",
    "resolutionText": "Der Beschluss weicht wie folgt vom Antrag ab: ...",
    "absentParticipant": [
        "beispielris:person/75"
    ],
    "paper": "beispielris:paper/2812",
    "modified": "2012-08-16T14:05:27+02:00"
}
~~~~~

### Eigenschaften ###

`meeting`
:   Sitzung, der der Tagesordnungspunkt zugeordnet ist.
    Typ: `oparl:Meeting`.
    Kardinalität: 1.
    ZWINGEND.

`number`
:   Nummer des Tagesordnungspunktes. Eine beliebige Zeichenkette, wie z. B. "10.", "10.1", "C", "c)" o. ä.
    Die Reihenfolge wird nicht dadurch, sondern durch die Reihenfolge der TOPs im `agendaItem`-Attribut von `oparl:Meeting` festgelegt.
    Typ: Zeichenkette.
    Kardinalität: 0 bis 1.
    OPTIONAL.

`name`
:   Das Thema des Tagesordnungspunktes.
    Typ: String.
    ZWINGEND.

`public`
:   Kennzeichnet, ob der Tagesordnungspunkt zur Behandlung in öffentlicher Sitzung 
    vorgesehen ist/war. Es wird ein Wahrheitswert (`true` oder `false`) erwartet.
    Typ: Boolean.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.

`consultation`
:   Beratung, die diesem Tagesordnungspunkt zugewiesen ist.
    Typ: `oparl:Consultation`.
    Kardinalität: 1.
    EMPFOHLEN.

`result`
:   Kategorische Information darüber, welches Ergebnis die Beratung des
    Tagesordnungspunktes erbracht hat, in der Bedeutung etwa
    "Unverändert beschlossen" oder "Geändert beschlossen". Mehr zur
    Funktionsweise dieses Attributs unter [Vokabulare zur Klassifizierung](#vokabulare_klassifizierung).
    Typ: `skos:Concept`.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.

`resolutionText`
:   Falls in diesem Tagesordnungspunkt ein Beschluss gefasst 
    wurde, kann der Text hier angegeben werden. Das ist besonders dann in der 
    Praxis relevant, wenn der gefasste Beschluss (z. B. durch Änderungsantrag) 
    von der Beschlussvorlage abweicht. Der Text kann als Zeichenkette oder auch als Dokument angegeben werden.
    Typ: Datentyp `xsd:string` | `oparl:Document`.
    FRAGE: Dies ist noch nicht optimal. Gibt es Redundanz? Weitere Eigenschaft notwendig oder sinnvoll?
    Kardinalität: 0 bis 2.
    OPTIONAL.

`paper`
:   Drucksache. Zwar kann auch das `oparl:Meeting` darauf verweisen, aber hier
    sind solche Verweise in der Regel präziser, da Drucksachen regelmäßig nur
    für einen TOP relevant sind und nicht für alle TOPs.
    Typ: `oparl:Paper`.
    OPTIONAL.
    FRAGE: Ist das nicht eine Doppelung mit `consultation`?

`auxiliaryDocument`
:   Dateianhang zum Tagesordnungspunkt.
    Typ: `oparl:Document`.
    Kardinalität: 0 bis *.
    OPTIONAL.

`keyword`
:   Vgl. [Vokabulare zur Klassifizierung](#vokabulare_klassifizierung).
    Typ: `skos:Concept`.
    Kardinalität: 0 bis *.
    OPTIONAL.

`created`
:   Erzeugungsdatum und -zeit des Objekts.
    Typ: Datentyp `xsd:dateTime`.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.

`modified`
:   Datum und Uhrzeit der letzten Änderung.
    Typ: Datentyp `xsd:dateTime`.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.

`absentParticipant`
:   Person(en), die bei der Behandlung dieses Tagesordnungspunkts nicht
    anwesend war(en).
    Typ: `oparl:Person`.
    Kardinalität: 0 bis *.
    OPTIONAL.
