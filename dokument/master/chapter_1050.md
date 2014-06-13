Nomenklatur der Spezifikation und Satzkonventionen
--------------------------------------------------

### Zwingende, empfohlene und optionale Anforderungen  {#muss_soll_darf}

Dieses Spezifikationsdokument nutzt die Modalverben _müssen_, _können_ und _sollen_
in einer Art und Weise, die bestimmte Anforderungen möglichst unmissverständlich
in drei verschiedene Abstufung einteilen lässt. Um ihre normative Bedeutung
zu unterstreichen, werden diese Wörter grundsätzlich in Großbuchstaben gesetzt.

Diese Konvention ist angelehnt an die Definitionen der Begriffe MUST, SHOULD und
MAY (bzw. MUST NOT, SHOULD NOT und MAY NOT) aus
RFC2119.^[RFC2119 <http://tools.ietf.org/html/rfc2119>]

Die Bedeutung im Einzelnen:

MÜSSEN/MUSS bzw. ZWINGEND:

:   Die Erfüllung einer Anforderung, die explizit vom Modalverb MÜSSEN bzw.
    MUSS Gebrauch macht, ist zwingend erforderlich.

    Die Entsprechung in RFC2119 lautet "MUST", "REQUIRED" oder "SHALL".

NICHT DÜRFEN/DARF NICHT:

:   Dieses Stichwort kennzeichnet ein absolutes Verbot.
    
    Die Entsprechung in RFC2119 lautet "MUST NOT" oder "SHALL NOT".

SOLLEN/SOLL bzw. EMPFOHLEN:

:   Mit dem Wort SOLLEN bzw. SOLL sind empfohlene Anforderungen gekennzeichnet, 
    die von jeder Implementierung erfüllt werden sollen. Eine Nichterfüllung
    ist als Nachteil zu verstehen, beispielsweise weil die Nutzerfreundlichkeit
    dadurch Einbußen erleidet, und sollte daher sorgfältig abgewogen werden.

    Die Entsprechung in RFC2119 lautet "SHOULD" oder "RECOMMENDED".

NICHT SOLLEN/SOLL NICHT bzw. NICHT EMPFOHLEN:

:   Diese Formulierung wird verwendet, wenn unter gewissen Umständen Gründe
    existieren können, die ein bestimmtes Verhalten akzeptabel oder sogar 
    nützlich erscheinen lassen, jedoch die Auswirkung des Verhaltens vor
    einer entsprechenden Implementierung verstanden und abgewogen werden
    sollen.

    Die Entsprechung in RFC2119 lautet "SHOULD NOT" oder "NOT RECOMMENDED".

DÜRFEN/DARF bzw. OPTIONAL:

:   Mit dem Wort DÜRFEN bzw. DARF oder OPTIONAL sind optionale Bestandteile
    gekennzeichnet. Ein Anbieter könnte sich entscheiden, den entsprechenden
    Bestandteil aufgrund besonderer Kundenanforderungen zu unterstützen,
    während andere diesen Bestandteil ignorieren könnten. Implementierer von
    Clients oder Servern DÜRFEN in solchen Fällen NICHT davon ausgehen, dass der
    jeweilige Kommunikationspartner den entsprechenden, optionalen Anteil
    unterstützt.

    Die Entsprechung in RFC2119 lautet "MAY" oder "OPTIONAL".


### Geschlechterspezifische Begrifflichkeiten

Um bei Begriffen wie Nutzer, Anwender, Betreiber etc. die sonst übliche Dominanz
der männlichen Variante zu vermeiden, werden in diesem Dokument
männliche oder weibliche Varianten gemischt. Es wird also beispielsweise mal
von einer Nutzerin gesprochen und mal von einem Nutzer. Alternativ kommt auch die
Kurzform _NutzerInnen_ für _Nutzerinnen und Nutzer_ zum Einsatz. Gemeint sind
selbstverständlich in allen Fällen immer weibliche wie auch männliche Personen.

### Codebeispiele

Die in diesem Dokument aufgeführten Codebeispiele dienen der Veranschaulichung
der beschriebenen Prinzipien. Es handelt sich in der Regel um frei erfundene
Daten.

Codebeispiele erheben insbesondere bei JSON-Code nicht den Anspruch auf
hundertprozentige syntaktische Korrektheit. Insbesondere können in Codebeispielen
Auslassungen vorkommen, die mit `...` gekennzeichnet werden.
