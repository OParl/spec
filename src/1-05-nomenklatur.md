## Nomenklatur {#nomenklatur}

### Zwingende, empfohlene und optionale Anforderungen  {#muss_sollte_darf}

Diese Spezifikation nutzt **müssen**, **können** und **sollten**
in einer eindeutig definierten Art und Weise. Diese ist angelehnt an die
Definitionen der Begriffe MUST, SHOULD und MAY (bzw. MUST NOT, SHOULD NOT und
MAY NOT) aus RFC2119.^[RFC2119 <http://tools.ietf.org/html/rfc2119>]

Die Bedeutung im Einzelnen:

**müssen**/**muss** bzw. **zwingend**:

:   Die Erfüllung einer so gekennzeichneten Anforderung ist zwingend erforderlich.

    Die Entsprechung in RFC2119 lautet "MUST", "REQUIRED" oder "SHALL".

**nicht dürfen**/**darf nicht**:

:   Dieses Stichwort kennzeichnet ein absolutes Verbot.

    Die Entsprechung in RFC2119 lautet "MUST NOT" oder "SHALL NOT".

**sollten**/**sollte** bzw. **empfohlen**:

:   Mit dem Wort **sollten** bzw. **sollte** sind empfohlene Anforderungen gekennzeichnet,
    die von jeder Implementierung erfüllt werden sollten. Eine Nichterfüllung
    ist als Nachteil zu verstehen, beispielsweise weil die Nutzerfreundlichkeit
    dadurch Einbußen erleidet, und sollte daher sorgfältig abgewogen werden.

    Die Entsprechung in RFC2119 lautet "SHOULD" oder "RECOMMENDED".

**sollten nicht**/**sollte nicht** bzw. **nicht empfohlen**:

:   Diese Formulierung wird verwendet, wenn unter gewissen Umständen Gründe
    existieren können, die ein bestimmtes Verhalten akzeptabel oder sogar
    nützlich erscheinen lassen, jedoch die Auswirkung des Verhaltens vor
    einer entsprechenden Implementierung verstanden und abgewogen werden
    sollten.

    Die Entsprechung in RFC2119 lautet "SHOULD NOT" oder "NOT RECOMMENDED".

**dürfen**/**darf** bzw. **optional**:

:   Mit dem Wort **dürfen** bzw. **darf** oder **optional** sind optionale Bestandteile
    gekennzeichnet. Ein Anbieter könnte sich entscheiden, den entsprechenden
    Bestandteil aufgrund besonderer Kundenanforderungen zu unterstützen,
    während andere diesen Bestandteil ignorieren könnten. Implementierer von
    Clients oder Servern **dürfen** in solchen Fällen **nicht** davon ausgehen, dass der
    jeweilige Kommunikationspartner den entsprechenden, optionalen Anteil
    unterstützt.

    Die Entsprechung in RFC2119 lautet "MAY".


### Geschlechterspezifische Begrifflichkeiten {#geschlechterspezifische-begrifflichkeiten}

Um bei Begriffen wie Nutzer, Anwender, Betreiber etc. die sonst übliche Dominanz
der männlichen Variante zu vermeiden, werden in diesem Dokument
männliche und weibliche Varianten gemischt. Gemeint sind in allen Fällen
Personen jeglichen Geschlechts.


### Codebeispiele {#codebeispiele}

Die in diesem Dokument aufgeführten Codebeispiele dienen der Veranschaulichung
der beschriebenen Prinzipien. Es handelt sich um frei erfundene Daten.

Codebeispiele erheben insbesondere bei JSON-Code nicht den Anspruch auf
syntaktische Korrektheit und Vollständigkeit. Dementsprechend können in
Codebeispielen Auslassungen vorkommen, die mit `...` gekennzeichnet werden.


### Namespace-Präfixe für Objekt- und Datentypen {#namespace-praefixe-fuer-objekt-und-datentypen}

Bei der Erwähnung von Objekttypen, die in dieser Spezifikation beschrieben
werden, wird in der Regel ein Präfix `oparl:` vor den Namen gesetzt, z. B.
"oparl:Organization". Damit soll verdeutlicht werden, dass der Objekttyp
innerhalb der OParl-Spezifikation gemeint ist.

Das Präfix `oparl:` steht hierbei für die folgende Namespace-URL:

    https://schema.oparl.org/1.1/

Dadurch kann eine Typenangabe wie `oparl:Organization` eindeutig in die
folgende URL übersetzt werden:

    https://schema.oparl.org/1.1/Organization
