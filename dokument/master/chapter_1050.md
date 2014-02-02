Nomenklatur der Spezifikation und Satzkonventionen
--------------------------------------------------

### MÜSSEN, SOLLEN und KÖNNEN bzw. ZWINGEND, EMPFOHLEN und OPTIONAL

Dieses Spezifikationsdokument nutzt die Modalverben müssen, können und sollen
in einer Art und Weise, die bestimmte Anforderungen möglichst unmissverständlich
in drei verschiedene Abstufung einteilen lässt. Um ihre normative Bedeutung
zu unterstreichen, werden diese Wörter grundsätzlich in Großbuchstaben gesetzt.

Diese Konvention ist angelehnt an die Definitionen der Begriffe MUST, SHOULD und
MAY (bzw. MUST NOT, SHOULD NOT und MAY NOT) aus RFC2119[^1].

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


### Besondere Hervorhebungen und Satzkonventionen

[^1]: RFC2119: [http://tools.ietf.org/html/rfc2119](http://tools.ietf.org/html/rfc2119)
