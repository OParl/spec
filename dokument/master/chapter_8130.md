oparl:Location (Ort)  {#oparl_location}
-------------------

Dieser Objekttyp dient dazu, den Ortsbezug einer Drucksache formal 
abzubilden. Ortsangaben können sowohl aus Textinformationen bestehen 
(beispielsweise dem Namen einer Straße/eines Platzes oder eine genaue 
Adresse) als auch aus Geodaten.

Dieser Objekttyp ist für anonyme Objekte im Kontext des Objekttyps
`oparl:Paper` zu verwenden.

Ein einfaches Beispiel:

~~~~~  {#location_ex1 .json}
{
    ...
    "location": {
        "description": "Honschaftsstra\u00dfe 312, K\u00f6ln",
        "geometry": {
            "type": "Point",
            "coordinates": [7.03291, 50.98249]
        }
    },
    ...
}
~~~~~

In der Praxis soll dies dazu dienen, den geografischen Bezug eines
politischen Vorgangs, wie zum Beispiel eines Bauvorhabens oder der 
Änderung eines Flächennutzungsplanes, maschinenlesbar nachvollziehbar
zu machen.

OParl sieht bei Angabe von Geodaten die Verwendung des  
GeoJSON-Formats^[GeoJSON Spazifikation 
<http://geojson.org/geojson-spec.html>] vor. GeoJSON erlaubt die 
Beschreibung von vielen unterschiedlichen Geometrien wie Punkten, Pfaden und 
Polygonen in JSON-Notation. Ein GeoJSON-Objekt kann auch mehrere Geometrien
umfassen, beispielsweise um damit mehrere Punkte oder Polygone zu umschreiben.

Gegenüber der GeoJSON-Spezifikation sieht OParl eine wichtige
Einschränkung vor: Für die Ausgabe über eine OParl API MÜSSEN sämtliche
Koordinatenangaben im System WGS84^[WGS84 steht für "World Geodetic System 1984",
es wird unter anderem auch vom Global Positioning System (GPS) verwendet.
In geografischen Informationssystemen ist für das System der EPSG-Code 4326 
geläufig.] angegeben werden, und zwar in Form von Zahlenwerten (Fließkommazahlen)
für Längen- und Breitengrad.

### Eigenschaften ###

`description`
:   Textliche Beschreibung eines Orts, z.B. in Form einer Adresse. Diese Eigenschaft ist EMPFOHLEN. Typ: Zeichenkette.

`geometry`
:   Geodaten-Repräsentation des Orts. Diese Eigenschaft ist OPTIONAL. Ist diese Eigenschaft gesetzt, MUSS ihr Wert ein valides GeoJSON-Objekt sein.

### Weitere Beispiele

#### Ortsangabe mit Polygon-Objekt

~~~~~  {#location_ex2 .json}
{
    "description": "Rechtes Rheinufer zwischen Deutzer
        Br\u00fccke und Hohenzollernbr\u00fccke",
    "type": "Polygon",
    "geometry": {
        "coordinates": [
            [
                [6.9681106, 50.9412137],
                [6.9690940, 50.9412137],
                [6.9692169, 50.9368270],
                [6.9681218, 50.9368270],
                [6.9681106, 50.9412137]
            ]
        ]
    }
}
~~~~~
