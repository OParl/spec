OParlPaper (Drucksache)
-----------------------

Eine Drucksache bildet Mitteilungen, Antworten auf Anfragen, 
Beschlussvorlagen, Anfragen, Anträge und weitere Vorlagen ab. Jede Drucksache 
erhält eine eindeutige Kennung.

Die Drucksache hat im Informationsmodell eine hervorgehobene Bedeutung. Im 
Fall eines Antrags kann mit einer einzigen Drucksache ein über Monate oder 
Jahre dauernder politischer Entscheidungsprozess verbunden sein. In dem 
Zusammenhang entstehen üblicherweise weitere Drucksachen.

Drucksachen spielen in der schriftlichen wie mündlichen Kommunikation eine 
besondere Rolle, da in vielen Texten auf bestimmte Drucksachen Bezug genommen 
wird. Hierbei kommen in Ratsinformationssystemen unveränderliche Kennungen 
der Drucksachen zum Einsatz.

![Objekttyp Drucksache](images/datenmodell_drucksache.png)

Jede Drucksache ist über die Eigenschaft "Typ" als eine der folgenden Arten 
von Drucksachen gekennzeichnet:

* **Beschlussvorlage**: Entscheidungsvorschlag der Verwaltung
* **Antrag**: Entscheidungsvorschlag einer Fraktionen bzw. mehrerer 
Fraktionen oder einer/mehrerer Einzelperson/en
* **Anfrage**: Frage(n) einer oder mehrerer Fraktion oder Einzelpersonen an 
die Verwaltung
* **Mitteilung/Stellungnahme der Verwaltung**: Eine Information der 
Verwaltung an einzelne oder mehrere Gremien. Darunter fallen nicht 
Beantwortungen von Anfragen.
* **Beantwortung einer Anfrage**: Antwort der Verwaltung auf (mündliche oder 
schriftliche) Anfragen


### Eigenschaften ###

Schlüssel (`id`)
:   Die Kennung einer Drucksache muss für die jeweilige Körperschaft 
    eindeutig sein. Sie kann sowohl Ziffern als auch Buchstaben enthalten. 
    Einige Systeme (z.B. Köln) verwenden besondere Trennzeichen wie "/", um 
    eine Jahreszahl von einer laufenden Nummer abzutrennen. Weiterhin werden 
    mancherorts führende Nullen verwendet.
Datum (`date`)
:   Datum der Veröffentlichung
Typ (`type`)
:   Art der Drucksache (Erläuterung siehe oben)
Zuletzt geändert (`last_modified`)
:   Datum und Uhrzeit der letzten Änderung

### Beziehungen ###
* Es muss genau ein **Hauptdokument** (Objekttyp "Dokument") referenziert 
werden.
* Es können beliebig viele weitere Dokumente referenziert werden, die als 
nachgeordnete **Anlagen** zur Drucksache verstanden werden.
* Die Drucksache ist beliebig vielen Gremien zuzuordnen, in denen diese
beraten wird.
* Drucksachen können **Urhebern** zugewiesen werden. Im Fall von Mitteilungen 
der Verwaltung ist dies oft der Oberbürgermeister. Bei Anträgen oder Anfragen 
können Organisationen oder Einzelpersonen referenziert werden. Es können 
stets mehrere Uhrheber verknüpft werden.
* Es können beliebig viele **Orte** (siehe Objekttyp "Ort") referenziert 
werden, die im Inhalt der Drucksache behandelt werden. Beispiel: 
Beschlussvorlage zur Freigabe von Mitteln für die Sanierung eines 
Sportplatzes, wobei der Ort die Lage des Sportplatzes genau beschreibt.
* Drucksachen können auf andere Drucksachen referenzieren. Diese Verweise 
können verschiedene semantische Beziehungen ausdrücken. So kann eine 
Drucksache auf eine übergeordnete oder eine oder mehrere untergeordnete 
Drucksachen verweisen. Beim Drucksachen-Typ "Beantwortung einer Anfrage" ist 
die Drucksache zu referenzieren, die die ursprüngliche **Anfrage** 
beinhaltet. Denkbar sind auch Verweise auf frühere Drucksachen zum selben 
Thema. Zu klären ist, wie die verschiedenen möglichen Beziehungen formell 
ausgedrückt werden.
* Drucksachen können zu beliebig vielen Tagesordnungspunkten in Beziehung 
stehen, um die **Beratungsfolge** einer Drucksache abzubilden. Hierbei kann 
die Beziehung jeweils mit einer Zuständigkeit versehen sein, die noch 
näher zu bestimmen ist (TODO).

### Beispiel ###

~~~~~  {#paper_ex1 .json}
{
    "id": "1234/2012",
    "date": "2013-01-04",
    "type": "Beantwortung einer Anfrage",
    "related_papers": [
        "0768/2012"
    ],
    "main_document": "3000.pdf",
    "attachments": [
        "3002.pdf",
        "3003.pdf"
    ],
    "locations": [
    	{
	        "description": "Theodor-Heuss-Ring 1",
	        "lat": 7.148,
	        "lon": 50.023
    	}
    ],
    "committees": ["STA"],
    "creators": [
        {
            "typ": "Organisation",
            "id": "2000"
        },
        {
            "typ": "Person",
            "id": "1000"
        }
    ],
    "consultations": [
        {
            "meeting": "3271",
            "agendaitem": "3.1.2",
            "role": "Federführende Beratung"
        }
    ],
    "last_modified": "2013-01-08T12:05:27+01:00"
}
~~~~~


