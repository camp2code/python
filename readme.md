# KW 34 /2021 - Camp2Code 
GPS-Koordinaten Formatdefinitionen: https://www.gpskoordinaten.de/gps-koordinatensystem
GPS-Koordinaten Genauigkeit: https://wiki.openstreetmap.org/wiki/DE:Genauigkeit_von_Koordinaten


Regulärer Ausdruck: r"([+-]?\d{1,2}[\.|,]\d{4,7})"


Erklärung des regulären Ausdrucks:
(...) -> Muster in (...) gesucht
[+-]? -> '+' oder '- ' dürfen min. 0, max. 1 mal auftreten
\d{1,2} -> Eine oder zwei Ziffern
[\.|,] -> entweder '.' oder ','
\d{4,7} -> min. 4-stellige, max. 7-stellige Zahl -> siehe auch GPS-Koordinaten - Genauigkeit im Dezimalformat (link oben):
4 Nachkommastellen -> 11.1 m (1110 cm)
7 Nachkommastellen -> 1.1 cm
Wir suchen nach diesem Muster im Character-Haufen und holen uns daraus die ersten zwei Treffer.
1. Treffer - Breitengrad (latitude)
2. Treffer - Längengrad (longitude)

Erwartung an Daten: es werden gültige GPS-Koordinaten übergeben (+-1-2ZiffernTrenner4-7Nachkommastellen):
2 Treffer (matches) mit jeweils 1 Gruppe (group) (eine GPS-Koordinate) werden erwartet.
-> D.h. alle Treffer zurückgeben lassen
-> min. 2, ansonsten gerade Anzahl an Treffern
-> gerader Treffer (zB. 0, 2, 4) ist Breitengrad
-> ungerader Treffer (zB. 1, 3, 5) ist Längengrad
Strings zum Testen - 
Autostadt Wolfsburg: 52.43340396989421, 10.795691408498394
52.43340396989421, 10.795691408498394
52.4334039698942110.795691408498394
52.43340396989421,10.795691408498394
textvorher52.4334039698942110.795691408498394textnahcer
:sf#453409ü45#52.43340396989421 10.795691408498394:343dsyfvgsfdgs45
52.43340396989421,10.795691408498394

