<p align="center">
  <img src="https://github.com/FelixSpuehler/Hackathon-Beratungsdschungel/blob/master/Follow_Me.jpg" alt="Follow Me", width="300" height="300"/>
</p> 

# Hackathon-Beratungsdschungel

Studierendenservice, Fachberatung, Career Service, Schreibwerkstatt und Co. - Hochschulen und Universitäten bieten ihren Studierenden vielfältige Unterstützung und Service für (fast) alle Lebenslagen. Doch wie behält man da den Überblick? Oftmals ist es für die Studierenden nicht leicht, den richtigen Weg durch den “Beratungsdschungel” zu finden und zu wissen, an welche Service- oder Beratungsstelle man sich mit welchem Anliegen wendet.
Abhilfe schafft der “Beratungslotse”, eine von uns entwickelte Website, die eine gezielte Auffindbarkeit des passenden Beratungsangebots unterstützt. Für die Umsetzung wird ein Prototyp basierend auf Google Sheets, einem selbst geschriebenen Importprogramm und Google Forms entwickelt.


## Anleitung zum Erstellen eines GoogleForm-Dokuments
1. Der Entscheidungsbaum im .csv-Format muss vorliegen. Dazu kann z.B. eine Excel-Tabelle angelegt werden, die die Spalten "ID", "Typ", "Titel", "Frage/Text", "Antwort" und "Ziel-ID" enthält und anschließend als csv-Datei exportiert wird. Ein Beispiel für eine solche Tabelle ist hier aufgeführt und findet sich auch unter [data](https://github.com/FelixSpuehler/Hackathon-Beratungsdschungel/data/).


| ID | Typ | Titel | Formulierung (Frage / Text) | Antwort | ZielID
| -------- | -------- | -------- | -------- | -------- | -------- |
| 1     | Frage     | Herzlich Willkommen!     |  Hast du bereits ein genaues Thema? | Ja | 4 |
| 1     | Frage     | Herzlich Willkommen!     |  Hast du bereits ein genaues Thema? | Nein | 3 |
| 2   | ...     | ...     |  ...  | ... | ... |

**!** Folgende Bedingungen sollten für die csv-Datei erfüllt sein:
- Typ sollte nur 'Frage' oder 'Text' enthalten.
- Unter Titel wird das Thema der Frage / des Textes angegeben.
- Formulierung enthält die eigentliche Frage bzw. den Text, der den Nutzern angezeigt werden soll.
- Die ZielID von Text-Knoten sollte leer gelassen werden bzw. wird ignoriert, da sie als Endknoten des Entscheidungsbaums betrachtet werden.
- Pro Antwort sollte eine Zeile gefüllt werden, um die entsprechende Weiterleitung auf die nächste Seite/Frage zu gewährleisten.

2. In der Datei src/main.py müssen folgende Variablen angeben werden:
    - csv_file (Name der csv-Datei des Entscheidungsbaumes)
    - project_title (Titel des Projekts, der auf der Website erscheint. Default: "Beratungslotse - Follow Me!")
    - gs_file (Name der Output-Datei)
    
3. Anschließend muss das Programm (src/main.py) ausgeführt werden. Dies erstellt eine Datei mit dem Namen <gs_file>.gs

4. Diese Datei muss nun bei Google Apps Script kompiliert werden. Dazu auf der Website [Google Script](https://script.google.com) ein neues Projekt anlegen und dort den Inhalt der <gs_file>.gs Datei einfügen. Das Kompilieren dieses Google Apps Scripts erstellt ein Google Forms Formular, welches den Beratungslotsen darstellt. Nun kann der Beratungslotse Studierenden durch die Einbettung in eine Website oder das Versenden des Linkes bereitgestellt werden.
