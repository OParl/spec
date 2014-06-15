Zukunftssicherheit
------------------

Wie unter [Designprinzipien](#designprinzipien) beschrieben, ist diese
erste Version der OParl-Spezifikation bereits im Wesentlichen von den
Zielen der einfachen Implementierbarkeit und Migration geleitet.

Der Aufwand, den die Betreiber von parlamentarischen Informationssystemen
bei der Bereitstellung von OParl-konformen Schnittstellen betreiben, soll
auch bei der zukünftigen Weiterentwicklung dieser Spezifikation
berücksichtigt werden. Ebenso soll den Entwicklern von Client-Software
zukünftig entgegen kommen, dass ihre bestehenden Clients auch mit Servern
kommunizieren können, die eine neuere Version der OParl-Spezifikation
unterstützen. Dieser Wunsch ist bereits im Designprinzip [Erweiterbarkeit](#erweiterbarkeit)
ausformuliert.

Mit anderen Worten: die Autoren der OParl-Spezifikation beabsichtigen
größtmögliche Zukunftssicherheit und zukünftige Abwärtskompatibilität.
Dieses Ziel wird in Zukunft natürlich abgewägt werden müssen mit
dem Wunsch, sich an Veränderungen und neue Erkenntnisse anzupassen. Eine
Garantie für Zukunftssicherheit kann insofern niemand aussprechen.

Ein fiktives Szenario soll verdeutlichen, dass es zweckmäßig ist, schon
beim Betrieb eines OParl 1.0 Servers die zukünftige Entwicklung im Blick
zu haben:

* Die Kommune *Beispielstadt* betreibt ihren OParl-1.0-Server unter
  der URL `https://oparl.example.org/1.0/`.

* Verschiedene Clients, die für OParl Version 1.0 entwickelt wurden, kommen
  bei Nutzerinnen und Nutzern, die sich für den Stadtrat in Beispielstadt
  intressieren, zum Einsatz. Jeder Client-Nutzer hat dazu lediglich die 
  URL `https://oparl.example.org/1.0/` des OParl-Servers in der Client-Konfiguration
  hinterlegt.

* Die OParl-Spezifikation wird aktualisiert, es erscheint
  Version 1.1. Das Schema enthält Erweiterungen gegenüber Version 1.0,
  jedes gültige Objekt aus Version 1.0 behält jedoch auch weiterhin seine
  Gültigkeit. Und Objekte, die nach Version 1.1 gültig sind, sind auch
  für Clients gültig, die für Version 1.0 entwickelt wurden.

* Die Firma, die den OParl-Server von Beispielstadt entwickelt hat,
  liefert ein Update.

* Der OParl-Server von Beispielstadt ist nun über eine neue URL
  `https://oparl.example.org/1.1/` zu erreichen.
  Alle Anfragen an `https://oparl.example.org/1.0/...`
  werden auf die entsprechende URL unter `https://oparl.example.org/1.1/` mit
  HTTP-Redirects und Status-Code 301 weiter geleitet.

* Die Nutzer der Clients, die mit dem OParl-Server von Beispielstadt
  arbeiten, können weiter arbeiten wie bisher. Sie erhalten vom Client
  höchstens einmalig eine Information, dass sich die Server-URL geändert hat.

* Einzelne Client-Nutzerinnen werden von den Anbietern ihrer Clients darauf
  aufmerksam gemacht, dass eine neue Version ihres Produkts für eine neue
  OParl-Version zur Verfügung steht. Mit dieser Version könnten die Nutzer
  in den Genuss der Vorteile von OParl-Version 1.1 kommen.

* Nach einiger Zeit erscheint eine neue Version 2.0 der OParl-Spezifikation.
  Hier haben sich größere Änderungen ergeben. Das Schema ist nicht kompatibel
  mit dem von Version 1.0 und 1.1. Clients, die für eine Version 1.* entwickelt
  wurden, werden nicht sinnvoll mit einem Server der Version 2 kommunizieren können.

* Der Server-Entwickler bietet das entsprechende Produkt zu OParl-Version 2 an,
  Beispielstadt entschließt sich zum Einsatz der neuen Version. Da das Server-Produkt
  gleichzeitig OParl 1.* und OParl 2.0 bedienen kann, kann Beispielstadt gleichzeitig
  einen Endpunkt für 1.1 und einen für 2.0 betreiben. Die URL des neuen Endpunkts
  lautet `https://oparl.example.org/2.0/`.

Das Szenario verdeutlicht, wie insbesondere zwei Aspekte für eine möglichst
sanfte Migration zwischen den OParl-Versionen sorgen können:

1. Dedizierte API-Endpunkt-URLs für jede OParl-Version

2. HTTP-Weiterleitungen auf die neue URL, sofern diese kompatibel mit der alten ist,
   erspart den Parallelbetrieb von zwei ähnlichen Endpunkten und kommuniziert
   den Clients automatisch den Endpunkt der neuen Version

Zu der Art, wie die OParl-Version sich auf die Endpunkt-URL auswirkt, will diese
Spezifikation keine Vorgaben machen. Die Pfad-Elemente im obigen Szenario sind
Vorschläge, aber in keiner Weise bindend.

Die praktische Umsetzung von HTTP-Weiterleitungen ist besonders dann einfach,
wenn die restlichen URL-Bestandteile identisch bleiben. In diesem Fall
können Server mit einer einfachen Regel von jeglicher vorherigen auf jegliche neue
URL weiterleiten.
