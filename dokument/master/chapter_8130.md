oparl:Location (Ort)
-------------------

Dieser Objekttyp dient dazu, einen Ortsbezug einer Drucksache formal 
abzubilden. Ortsangaben können sowohl aus Textinformationen bestehen 
(beispielsweise der Name einer Straße/eines Platzes oder eine genaue 
Adresse) als auch aus Geodaten.

OParl sieht die Angabe von Geodaten in Anlehnung an die 
GeoJSON-Spezifikation [13] vor. Die GeoJSON-Spezifikation erlaubt die 
Abbildung von vielen unterschiedlichen Geometrien wie Punkten, Pfaden und 
Polygonen. Während GeoJSON zu jedem Geodaten-Objekt auch die Speicherung
zusätzlicher Metadaten ermöglicht, beschränkt sich OParl ledliglich auf das
`geometry`-Attribut in GeoJSON. Sämtliche Geo-Koordinatenangaben werden in
in OParl im WGS-84-System [11] erwartet.

### Eigenschaften ###

Textanabe (`description`)
:   _Optional._ Textliche Beschreibung eines Orts, z.B. in Form einer Adresse
Koordinaten (`geometry`)
:   _Optional._ GeoJSON geometry Objekt
Zuletzt geändert (`last_modified`)
:   Datum und Uhrzeit der letzten Änderung


### Beziehungen ###
* Orte können mit Drucksachen in Verbindung stehen.

~~~~~  {#location_ex1 .json}
{
    "description": "Honschaftsstraße 312, 51061 Köln",
    "geometry": {
        "type": "Point",
        "coordinates": [7.03291, 50.98249]
    },
    "last_modified": "2013-02-14T14:05:27+01:00"
}
~~~~~
