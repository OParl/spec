oparl:LegislativeTerm {#oparl_legislative_term}
---------------------

Wahlperioden

Englische Übersetzungen sind "legislative term" und "electoral term".
Beide betonen unterschiedliche Aspekte von Wahlperioden
die mehr oder weniger ausgeprägt sein können.

### Beispiel ###

Ein Kontext:

~~~~~  {#legislative_term_ex1 .json}
{
    "name": {
        "@id": "oparl:name",
        "@type": "xsd:string"
    },
    "startDate": {
        "@id": "schorg:startDate",
        "@type": "xsd:dateTime"
    },
    "endDate": {
        "@id": "schorg:endDate",
        "@type": "xsd:dateTime"
    }   
}
~~~~~


~~~~~  {#legislative_term_ex2 .json}
{
    "@context": {
        TODO: `schema:validFrom` und `schema:validThrough` verwenden
    },
    "@id": "beispielris:term/21",
    "@type": "oparl:LegislativeTerm",
    "name": "21. Wahlperiode",
    "startDate": "2010-12-03T16:30:00+01:00",
    "endDate":  "2013-12-03T16:30:00+01:00"
}
~~~~~

### Eigenschaften

`name`
:   Name der Wahlperiode.
    Typ: `xsd:string`.
    Kardinalität: 1.
    ZWINGEND.

`startDate`
:   Der erste Tag der Wahlperiode.
    Typ: `xsd:date`.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.

`endDate`
:   Der letzte Tag der Wahlperiode.
    Typ: `xsd:date`.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.

