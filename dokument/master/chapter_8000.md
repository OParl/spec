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

### Typen von Objekteigenschaften

JSON erlaubt grundsätzlich die Kodierung von Eigenschaften in den folgenden
verschiedenen Typen:

* Zeichenkette
* Zahle
* Wahrheitswert
* null
* Liste (Array)
* Objekt

Wenn nicht anders angegeben, wird eine Eigenschaft grundsätzlich als Zeichenkette
erwartet. Eventuelle Längenbeschränkungen oder Einschränkungen des Zeichenvorrats
werden gesondert erwähnt.

### null-Werte

JSON erlaubt es grundsätzlich, dass Eigenschaften den Wert `null` haben können.
Im Rahmen dieser Spezifikation DARF das jedoch nur bei Eigenschaften der Fall sein,
die als OPTIONAL oder EMPFOHLEN gekennzeichnet sind. ZWINGENDE Eigenschaften müssen
einen Wert ungleich `null` besitzen.

### Vererbung der Lizenzbedingung

- Jedes Objekt KANN die Eigenschaft "license" besitzen.
- Die genannte Lizenz bezieht sich auf das jeweilige Objekt und auf untergeordnete 
  Objekte, sofern diese keine license-Eigenschaft besitzen.
- Dazu muss die Vererbungshierarchie aufgezeigt werden.
- Empfohlene Minimalvariante: Nur eine license-Angabe auf Ebene von OParlSystem.
- Auf Ebene des OParlDocument bezieht sich die Eigenschaft sowohl auf die Metadaten als auch auf das Dokument selbst.
