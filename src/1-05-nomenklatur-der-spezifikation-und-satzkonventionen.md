## Nomenklatur der Spezifikation und Satzkonventionen {#nomenklatur-der-spezifikation-und-satzkonventionen}

### Zwingende, empfohlene und optionale Anforderungen  {#muss_sollte_darf}

Dieses Spezifikationsdokument nutzt die Modalverben _müssen_, _können_ und _sollten_
in einer Art und Weise, die bestimmte Anforderungen unmissverständlich
in drei verschiedene Abstufungen einteilen lässt. Um ihre normative Bedeutung
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

SOLLTEN/SOLLTE bzw. EMPFOHLEN:

:   Mit dem Wort SOLLTEN bzw. SOLLTE sind empfohlene Anforderungen gekennzeichnet,
    die von jeder Implementierung erfüllt werden sollten. Eine Nichterfüllung
    ist als Nachteil zu verstehen, beispielsweise weil die Nutzerfreundlichkeit
    dadurch Einbußen erleidet, und sollte daher sorgfältig abgewogen werden.

    Die Entsprechung in RFC2119 lautet "SHOULD" oder "RECOMMENDED".

SOLLTEN NICHT/SOLLTE NICHT bzw. NICHT EMPFOHLEN:

:   Diese Formulierung wird verwendet, wenn unter gewissen Umständen Gründe
    existieren können, die ein bestimmtes Verhalten akzeptabel oder sogar
    nützlich erscheinen lassen, jedoch die Auswirkung des Verhaltens vor
    einer entsprechenden Implementierung verstanden und abgewogen werden
    sollten.

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


### Geschlechterspezifische Begrifflichkeiten {#geschlechterspezifische-begrifflichkeiten}

Um bei Begriffen wie Nutzer, Anwender, Betreiber etc. die sonst übliche Dominanz
der männlichen Variante zu vermeiden, werden in diesem Dokument
männliche oder weibliche Varianten gemischt. Es wird also beispielsweise mal
von einer Nutzerin gesprochen und mal von einem Nutzer. Gemeint sind
in allen Fällen Personen jeglichen Geschlechts.


### Codebeispiele {#codebeispiele}

Die in diesem Dokument aufgeführten Codebeispiele dienen der Veranschaulichung
der beschriebenen Prinzipien. Es handelt sich in der Regel um frei erfundene
Daten.

Codebeispiele erheben insbesondere bei JSON-Code nicht den Anspruch auf
syntaktische Korrektheit und Vollständigkeit. Dementsprechend können in Codebeispielen Auslassungen vorkommen, die mit `...` gekennzeichnet werden.


### Namespace-Präfixe für Objekt- und Datentypen {#namespace-praefixe-fuer-objekt-und-datentypen}

Bei der Erwähnung von Objekttypen, die in dieser Spezifikation beschrieben
werden, wird in der Regel ein Präfix `oparl:` vor den Namen gesetzt, z. B.
"oparl:Organization". Damit soll verdeutlicht werden, dass dieser Objekttyp
innerhalb der OParl-Spezifikation beschrieben wird.

Das Präfix `oparl:` steht hierbei für die folgende Namespace-URL:

    https://oparl.org/schema/1.0/

Dadurch kann eine Typenangabe wie `oparl:Organization` eindeutig in die
folgende URL übersetzt werden:

    https://oparl.org/schema/1.0/Organization
