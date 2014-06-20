oparl:AgendaItem (Tagesordnungspunkt)  {#oparl_agendaitem}
-------------------------------------

Tagesordnungspunkte sind die Bestandteile von Sitzungen (`oparl:Meeting`).
Jeder Tagesordnungspunkt widmet sich inhaltlich einem bestimmten Thema,
wozu in der Regel auch die Beratung bestimmter Drucksachen gehört.

### Beispiel ###

Zunächst ein Kontext:

~~~~~
{   
    "meeting":  {
        "@id": "oparl:meeting",
        "@type": "@id"
    },
    "number": {
        "@id": "oparl:number"
    },
    "name": {
        "@id": "rdfs:label",
        "@type": "xsd:string"
    },
    "public": "xsd:boolean",
    "consultation":  {
        "@id": "oparl:consultation",
        "@type": "@id"
    },
    "result":  {
        "@id": "oparl:result",
        "@type": "@id"
    },
    "resolution": {
        "@id": "oparl:resolution",
        "@type": ["@id", "xsd:string"],
        "TODO": "Geht so leider nicht. Issue #212"
    }
    "paper":  {
        "@id": "oparl:paper",
        "@type": "@id"
    },
    "modified": {
        "@id": "dc:modified",
        "@type": "xsd:dateTime"
    }   
}
~~~~~


~~~~~  {#agendaitem_ex1 .json}
{
    "@context": "https://oparl.example.org/Pfad/zum/Kontext/oparl.jsonld",
    "@type": "oparl:AgendaItem",
    "@id": "beispielris:agendaitem/3271",
    "meeting": "beispielris:meeting/281",
    "number": "10.1",
    "name": "Satzungsänderung für Ausschreibungen",
    "public": true,
    "consultation": "beispielris:consultation/1034",
    "result": "beispielris:vocab/decided_modified",
    "resolution": "Der Beschluss weicht wie folgt vom Antrag ab: ...",
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
:   Gliederungs-"Nummer" des Tagesordnungspunktes. Eine beliebige Zeichenkette, wie z. B. "10.", "10.1", "C", "c)" o. ä.
    Die Reihenfolge wird nicht dadurch, sondern durch die Reihenfolge der TOPs im `agendaItem`-Attribut von `oparl:Meeting` festgelegt.
    Typ: String.
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
    Kardinalität: 0 bis 1.
    FRAGE: Wirklich immer nur maximal 1 ?
    EMPFOHLEN.

`result`
:   Kategorische Information darüber, welches Ergebnis die Beratung des
    Tagesordnungspunktes erbracht hat, in der Bedeutung etwa
    "Unverändert beschlossen" oder "Geändert beschlossen". Mehr zur
    Funktionsweise dieses Attributs unter [Vokabulare zur Klassifizierung](#vokabulare_klassifizierung).
    Typ: `skos:Concept`.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.

`resolution`
:   Falls in diesem Tagesordnungspunkt ein Beschluss gefasst
    wurde, kann hier ein Text oder Dokument angegeben werden. Das ist besonders dann in der
    Praxis relevant, wenn der gefasste Beschluss (z. B. durch Änderungsantrag)
    von der Beschlussvorlage abweicht.
    TODO: Issue #212
    Typ: `oparl:File` | Datentyp `xsd:string`.
    Kardinalität: 0 bis 1.
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
    Typ: `oparl:File`.
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
    DEPRECATED issue #213.
