Als de website (tijdelijk) niet online staat, kun je deze zelf lokaal draaien op jouw computer. Dit betekent dat de website alleen op jouw eigen apparaat te zien is, via een zogenoemde localhost.

Je hoeft hiervoor alleen maar een paar stappen te volgen om de code van de website te downloaden en uit te voeren.

# Windows

1. Installeer Python

    Check eerst of je python hebt geinstalleerd:  
    Open een terminal: druk op `WIN + R`, typ `cmd`, en druk op Enter.  
    Typ/plak deze opdracht in het terminalvenster en druk op Enter:  
    `python --version`  
    Als je een versie ziet staan iets als (`Python 3.??.?`), kun je verder gaan naar stap 2. Anders moet je Python even installeren:

    Ga naar de officiële Python-downloadpagina: <https://www.python.org/downloads/>  
    Download de nieuwste versie van Python voor Windows.  
    Tijdens het installeren, vink het vakje aan met "Add Python to PATH" onderaan het installatiescherm.  
    Klik daarna op Install Now en volg de stappen tot het klaar is.

2. Installeer Git

    Open een terminal: druk op `WIN + R`, typ `cmd`, en druk op Enter.  
    Typ/plak deze opdracht in het terminalvenster en druk op Enter:  
    `winget install --id Git.Git -e --source winget`  
    Dit installeert Git, waarmee je de code van de website kunt downloaden van GitHub.

3. Download de websitecode

    Typ/plak in dezelfde terminal het volgende commando om de code op te halen:  
    `git clone https://github.com/Gijs6/CKVsite.git CKV_site_Gijs`

4. Ga naar de projectmap

    Typ/plak in dezelfde terminal het volgende commando om naar de projectmap te gaan:  
    `cd CKV_site_Gijs`

5. Installeer bibilotheken

    Typ/plak in dezelfde terminal het volgende commando om alle externe biblotheken te installeren:  
    `pip install -r requirements.txt` (mocht dat niet werken, probeer dan `python -m pip install -r requirements.txt`)

6. Start de website

    Typ/plak in dezelfde terminal het volgende commando om de pythonapplicatie te starten:  
    `python main.py`

Laat de terminal open staan. Open daarna je browser en ga naar: <http://localhost:5000>

Je ziet nu de website draaien op jouw computer!

# macOS

1. Installeer Python

    Check eerst of je python hebt geinstalleerd:  
    Open een terminal: druk op `CMD + Spatiebalk` en typ `Terminal`. Druk op Enter. (of zoek gewoon terminal in je Finder ofzo)  
    Typ/plak deze opdracht in het terminalvenster en druk op Enter:  
    `python3 --version`  
    Als je een versie ziet staan iets als (`Python 3.??.?`), kun je verder gaan naar stap 2. Anders moet je Python even installeren:

    Ga naar de officiële Python-downloadpagina: <https://www.python.org/downloads/>  
    Klik op de knop onder "Download the latest version"  
    Open de installer bestand en volg de instructies.

2. Installeer Git

    Open een terminal: druk op `CMD + Spatiebalk` en typ `Terminal`. Druk op Enter. (of zoek gewoon terminal in je Finder ofzo)  
    Typ/plak deze opdracht in het terminalvenster en druk op Enter:  
    `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`  
    Dit installeert Homebrew, waarmee je Git kunt gaan installeren.  

    Typ/plak in dezelfde terminal het volgende commando om Git te installeren:  
    `brew install git`

3. Download de websitecode

    Typ/plak in dezelfde terminal het volgende commando om de code op te halen:  
    `git clone https://github.com/Gijs6/CKVsite.git CKV_site_Gijs`

4. Ga naar de projectmap

    Typ/plak in dezelfde terminal het volgende commando om naar de projectmap te gaan:  
    `cd CKV_site_Gijs`

5. Installeer bibilotheken

    Typ/plak in dezelfde terminal het volgende commando om alle externe biblotheken te installeren:  
    `pip3 install -r requirements.txt` (mocht dat niet werken, probeer dan `python3 -m pip install -r requirements.txt`)

6. Start de website

    Typ/plak in dezelfde terminal het volgende commando om de pythonapplicatie te starten:  
    `python3 main.py`

Laat de terminal open staan. Open daarna je browser en ga naar: <http://localhost:5000>

Je ziet nu de website draaien op jouw computer!

# Linux

Als je Linux gebruikt mag ik hopen dat je wel weet hoe je een repo moet clonen.
