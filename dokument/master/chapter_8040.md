OParlBody (Körperschaft)
------------------------

Die Körperschaft erlaubt es, den Betreiber bzw. Eigentümer des
Informationssystems wie zum Beispiel einen Landkreis, eine bestimmte 
Gemeinde oder einen bestimmten Stadtbezirk in Form eines Datenobjekts 
abzubilden.

Viele RIS werden nur genau eine Instanz dieses Typs „beherbergen“. Einige 
Systeme werden jedoch für mehrere Mandanten betrieben, wobei die Mandanten 
verschiedene Körperschaften repräsentieren (z.B. "Verbandsgemeinde 
Ulmen" und "Stadt Ulmen".)

![Objekttyp Körperschaft](images/datenmodell_koerperschaft.png)

### Eindeutige Identifizierung ###

Die Körperschaft hat eine innerhalb des Systems eindeutige ID.

Darüber hinaus werden verschiedene Möglichkeiten geboten, die Körperschaft
semantisch zu repräsentieren.

Handelt es sich beim Betreiber des Systems um eine Gebietskörperschaft
(Landkreis, Kommune etc.), soll für die eindeutige Identifizierung der 
Regionalschlüssel[1] verwendet werden.

Darüber hinaus soll zusätzlich, sofern vorhanden, die eindeutige Kennung
der Körperschaft aus der GND[12] verwendet werden.

Als dritte Möglichkeit, die Körperschaft zu identifizieren, kann eine 
aussagekräftigen URL, unter der weitere Informationen zur Körperschaft zu 
finden sind, genannt werden.

Sämtliche hier genannten Methoden zur Identifizierung können kombiniert
werden.

### Eigenschaften ###

Schlüssel (`id`)
:   Zur eindeutigen Identifizierung der Körperschaft im System
Name (`name`)
:   Der Name der Körperschaft, z.B. "Stadt Köln"
Regionalschlüssel (`regionalschluessel`)
:   _Optional_. Regionalschlüssel der Gebietskörperschaft, z.B. 
    "053150000000". Muss grundsätzlich 12-stellig angegeben werden.
GND URL (`gnd_url`)
:   _Optional_. URL des Eintrags in der GND, z.B.
    "http://d-nb.info/gnd/2015732-0"
URL (`url`)
:   _Optional_. URL der Homepage oder einer vergleichbaren Seite
    mit Informationen über die Körperschaft, z.B. "http://www.stadt-koeln.de/"
Lizenz (`license_url`)
:   _Optional_. URL der Lizenz, unter der die Daten, die über die API
    abgerufen werden können, stehen.
Betreiber-Kontakt (`operator_contact`)
:   _Optional_. Kontaktinformationen für die direkte Kontaktaufnahme zum
    Betreiber der API.

### Beziehungen ###

* Objekte vom Typ "Organisation" sind zwingend genau einer 
Körperschaft zugeordnet. So wird beispielseise eine SPD in Köln von 
einer SPD in Leverkusen unterschieden.
* Objekte vom Typ "Gremium" sind zwingend genau einer Körperschaft 
zugeordnet. Damit wird der "Rat" einer bestimmten Kommune von den 
gleichnamigen Gremien anderer Kommunen abgegrenzt.


### Beispiel ###

~~~~~  {#body_ex1 .json}
{
    "id": "1",
    "name": "Stadt Köln",
    "regionalschluessel": "053150000000",
    "gnd_url": "http://d-nb.info/gnd/2015732-0",
    "url": "http://www.stadt-koeln.de/",
    "operator_contact": "Tel. +49 221-221-5432, E-Mail: ris-api@stadt-koeln.de",
    "license_url": "http://opendatacommons.org/licenses/odbl/1.0/"
}
~~~~~

