Schema
======

Dieses Kapitel beschreibt das Schema von OParl. Das Schema bildet das
Datzenmodell der OParl-Architektur ab. Es definiert, welche Objekttypen
über eine OParl-API abgerufen werden können und welche Eigenschaften
diese Objekttypen haben dürfen und müssen. Darüber hinaus ist im Schema
auch festgelegt, in welcher Beziehung verschiedene Objekttypen zu
einander stehen.


Übergreifende Aspekte
---------------------

### Eindeutige Identifizierung von Objekten ###

Sämtliche Objekte, die über die Schnittstelle geladen werden können, sollen 
anhand einer einzigen Objekteigenschaft eindeutig identifizierbar sein. Die 
Objekteigenschaft, mit der dies erreicht wird, wird hier im folgenden - 
unabhängig vom tatsächlichen Namen der Eigenschaft - als "Schlüssel" 
bezeichnet.

Eindeutigkeit meint hier eine Einzigartigkeit innerhalb des 
Informationssystems und für den jeweiligen Objekttyp. Das bedeutet: zwei von 
einander unabhängige Ratsinformationssysteme für verschiedene 
Körperschaften dürfen sich überlappende Schlüssel nutzen. Innerhalb 
eines Systems dürfen zwei Objekte unterschiedlichen Typs (beispielsweise 
eine Person und ein Gremium) den selben Schlüssel nutzen. Jedoch MÜSSEN zwei 
Objekte des selben Typs innerhalb des selben Systems grundsätzlich 
verschiedene Schlüssel haben.

Schlüssel-Eigenschaften werden grundsätzlich als Unicode-Zeichenkette 
übergeben. Sie können daher gleichermaßen aus 
numerischen wie alphanumerischen Werten befüllt werden.

Es wird grundsätzlich vorausgesetzt, dass Schlüssel unveränderlich sind. 
Ändert sich der Schlüssel eines Objekts nach der Erzeugung, werden Nutzer 
der Schnittstelle annehmen, dass es sich nicht mehr um das selbe Objekt 
handelt.


### Objekteigenschaften ###

Die nachfolgend beschriebenen Eigenschaften der Objekttypen sind, wenn nicht 
anders angegeben, verpflichtend. Das bedeutet: Bei jedem von der 
Schnittstelle ausgelieferten Objekt muss diese Eigenschaften definiert sein. 
Optionale Eigenschaften sind entsprechend gekennzeichnet.

Eigenschaften werden deutschsprachig und englischsprachig benannt. Die 
deutschsprachige Benennung dient der bestmöglichen Verständlichkeit im 
Kontext dieses Dokuments, während die Schnittstelle aus Gründen der 
Zugänglichkeit für möglichst viele Entwickler mit englischsprachigen 
Begriffen arbeiten soll.


### Zu den Beziehungen ###

Bei der Beschreibung von Beziehungen zwischen Objekten wird zu diesem 
Zeitpunkt nicht berücksichtigt, ob eine Beziehung zwischen zwei Objekten A 
und B am Objekt A oder am Objekt B definiert wird. So spielt es bislang keine 
Rolle, ob einem Gremium mehrere Personen zugeordnet werden oder einer Person 
mehrere Gremien zugewiesen werden. Das Augenmerkt liegt hier nur auf der 
Tatsache, welche Beziehung existieren können und was diese Beziehungen 
aussagen sollen.


