oparl:Location (Ort)  {#oparl_location}
-------------------

Dieser Objekttyp dient dazu, den Ortsbezug einer Drucksache formal 
abzubilden. Ortsangaben können sowohl aus Textinformationen bestehen 
(beispielsweise dem Namen einer Straße/eines Platzes oder eine genaue 
Adresse) als auch aus Geodaten.

In der Praxis soll dies dazu dienen, den geografischen Bezug eines
politischen Vorgangs, wie zum Beispiel eines Bauvorhabens oder der 
Änderung eines Flächennutzungsplanes, maschinenlesbar nachvollziehbar
zu machen.

Dieser Objekttyp kann für Objekte im Kontext des Objekttyps
`oparl:Paper` verwendet werden.

Ein einfaches Beispiel - welches GeoJSON verwendet und deshalb nur der Illustration dient:

~~~~~  {#location_ex1 .json}
{
    ...
    "location": {
        "description": "Honschaftsstra\u00dfe 312, K\u00f6ln", // TODO: weshalb diese Kodierung?!
        "geometry": {
            "type": "Point",
            "coordinates": [7.03291, 50.98249]
        }
    },
    ...
}
~~~~~

In der JSON-LD Recommendation des W3C ist diese Passage zu finden:
~~~~~
List of lists in the form of list objects are not allowed in this version of JSON-LD. 
This decision was made due to the extreme amount of added complexity when 
processing lists of lists.
~~~~~

Das lässt sich nicht mit der Verwendung von GeoJSON vereinbaren, denn dort sind die Geometriedaten bei vielen
Objektarten in Form von verschachtelten Listen kodiert. Zwar gibt es eine Iniatitive zur Schaffung von GeoJSON-LD (siehe http://geojson.org/vocab und https://github.com/geojson/geojson-ld), diese Spezifikation hat bisher jedoch keinen verwendbaren Zustand erreicht, so dass sie nicht für OParl 1.0 verwendbar ist.

Statt GeoJSON oder GeoJSON-LD wird deshalb der semantisch gleichwertige und etablierte Standard "Well-Known Text" (WKT) verwendet (siehe http://en.wikipedia.org/wiki/Well-known_text).

WKT ist:
- präzise spezifiziert a) ISO/IEC 13249-3:2011 standard, "Information technology -- Database languages -- SQL multimedia and application packages -- Part 3: Spatial" (SQL/MM) b) "OpenGIS ® Implementation Standard for Geographic information - Simple feature access - Part 1: Common architecture"
- semantisch ebenso ausdrucksstark wie GeoJSON / GeoJSON-LD
- auch durch Linked Data Technik weitreichend unterstützt (GeoSPARQL, Apache Jena spatial extension)
- leicht von und nach GeoJSON konvertierbar (http://en.wikipedia.org/wiki/Well-known_text#APIs_that_provide_support)

TODO: neue Beispiele

Ein Kontext:

~~~~~
{
   "geometry":
   {
     "@type": "ogc:wktLiteral" 
   }
}
~~~~~

Und ein Beispiel unter Verwendung des Kontextes:

~~~~~  {#location_ex2 .json}
{
    // ...
    "location": {
        "description": "Honschaftsstra\u00dfe 312, K\u00f6ln",
        "geometry": "POINT (7.03291 50.98249)"
    },
    // ...
}
~~~~~

OParl sieht bei Angabe von Geodaten die Verwendung des  
GeoJSON-Formats^[GeoJSON Spezifikation 
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
:   Geodaten-Repräsentation des Orts. Diese Eigenschaft ist OPTIONAL. Ist diese Eigenschaft gesetzt, MUSS ihr Wert der Spezifikation von Well-Known Text (WKT) entsprechen.

### Weitere Beispiele

#### Ortsangabe mit Polygon-Objekt

~~~~~  {#location_ex3 .json}
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
