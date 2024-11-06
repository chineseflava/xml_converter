# xml_converter
A converter that converts format A to format B.
Run in a terminal from the current folder. 
Example "python .\xml_converter.py .\inputs\example1.txt"

Format A:
P|förnamn|efternamn
T|mobilnummer|fastnätsnummer
A|gata|stad|postnummer
F|namn|födelseår
P kan följas av T, A och F
F kan följas av T och A

Example: 
P|Victoria|Bernadotte
T|070-0101010|0459-123456
A|Haga Slott|Stockholm|101
F|Estelle|2012
A|Solliden|Öland|10002
F|Oscar|2016
T|0702-020202|02-202020
P|Joe|Biden
A|White House|Washington, D.C

Format B:
<people>
    <person>
        <firstname>Victoria</firstname>
        <lastname>Bernadotte</lastname>
    <address>
        <street>Haga Slott</street>
        ...
    </address>
    <phone>
        <mobile>070-0101010</mobile>
        ...
    </phone>
    <family>
        <name>Estelle</name>
        <born>2012</born>
        <address>...</address>
    </family>
    <family>...</family>
    </person>
    <person>...</person>
</people>

