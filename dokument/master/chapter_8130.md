oparl:Location (Ort)  {#oparl_location}
--------------------

Dieser Objekttyp dient dazu, den Ortsbezug einer Drucksache formal 
abzubilden. Ortsangaben können sowohl aus Textinformationen bestehen 
(beispielsweise dem Namen einer Straße/eines Platzes oder eine genaue 
Adresse) als auch aus Geodaten. Ortsangaben sind auch nicht auf einzelne
Positionen beschränkt, sondern können eine Vielzahl von Positionen,
Flächen, Strecken etc. abdecken.

In der Praxis soll dies dazu dienen, den geografischen Bezug eines
politischen Vorgangs, wie zum Beispiel eines Bauvorhabens oder der 
Änderung eines Flächennutzungsplanes, maschinenlesbar nachvollziehbar
zu machen.

Dieser Objekttyp kann für Objekte im Kontext des Objekttyps
`oparl:Paper` verwendet werden.

OParl sieht bei Angabe von Geodaten ZWINGEND die Verwendung des  
Well-Known-Text-Formats (WKT) der Simple Feature Access Spezifikation^[Simple
Feature Access Spezifikation: <http://www.opengeospatial.org/standards/sfa>]
vor. WKT erlaubt die Beschreibung von unterschiedlichen Geometrien wie
Punkten (`Point`), Pfaden (`LineString`), Polygonen (`Polygon`) und viele andere
mehr.

Zum Zeitpunkt der Erstellung der vorliegenden Spezifikation ist Version 1.2.1
der Simple-Feature-Access-Spezifikation aktuell. OParl stellt keine Anforderungen
daran, welche Version von Simple-Feature-Access bei der Ausgabe von WKT zu
unterstützen ist.

Für die Ausgabe über eine OParl-API MÜSSEN sämtliche Koordinatenangaben solcher
Geodaten im System WGS84^[WGS84 steht für "World Geodetic System 1984",
es wird unter anderem auch vom Global Positioning System (GPS) verwendet.
In geografischen Informationssystemen ist für das System der EPSG-Code 4326 
geläufig.] angegeben werden, und zwar in Form von Zahlenwerten (Fließkommazahlen)
für Längen- und Breitengrad.

**Beispiele**

Ein einfaches Objekt mit Punktkordinate:

~~~~~  {#location_ex1 .json}
{
    "id": "https://oparl.example.org/locations/29856",
    "type": "http://oparl.org/schema/1.0/Location",
    "description": "Honschaftsstraße 312, Köln",
    "geometry": "POINT (7.03291 50.98249)"
}
~~~~~

Ortsangabe mit Polygon-Objekt:

~~~~~  {#location_ex2 .json}
{
    "id": "https://oparl.example.org/locations/29856",
    "type": "http://oparl.org/schema/1.0/Location",
    "description": "Rechtes Rheinufer zwischen Deutzer
        Brücke und Hohenzollernbrücke",
    "geometry": "POLYGON ((
                6.9681106 50.9412137,
                6.9690940 50.9412137,
                6.9692169 50.9368270,
                6.9681218 50.9368270,
                6.9681106 50.9412137))"
}
~~~~~


### Eigenschaften ###

`description`
:   Textliche Beschreibung eines Orts, z. B. in Form einer Adresse.
    Typ: String.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.

`geometry`
:   Geodaten-Repräsentation des Orts. Ist diese Eigenschaft gesetzt,
    MUSS ihr Wert der Spezifikation von Well-Known Text (WKT) entsprechen.
    Typ: String.
    Kardinalität: 0 bis 1.
    EMPFOHLEN.

`keyword`
:   Schlagworte mit `skos:prefLabel`. Vgl. dazu [Vokabulare zur Klassifizierung](#vokabulare_klassifizierung).
    Typ: Array mit Strings oder URLs zu `skos:Concept` Objekten.
    Kardinalität: 0 bis *.
    OPTIONAL.
