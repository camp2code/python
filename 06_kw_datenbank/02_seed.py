import csv, os


""" 
- baut verbindung zu *.csv auf
- liest die daten ein
- baut verbindung zu datenbank auf
- fuegt die gelesenen daten in die datenbank ein
- ggf. ausgeben was eingefuegt wurde
- baut verbindung zu datenbank ab
- baut verbindung zu *.csv ab
"""
# verbindung zu fahrzeuge.csv aufbauen:
aktuelles_verzeichnis = os.path
print(aktuelles_verzeichnis)
dateipfad_fahrzeug_csv = aktuelles_verzeichnis + './fahrzeuge.csv'
# url_fahrtenbuch_csv = 'https://github.com/bellmann-engineering/python-basic-to-advanced/blob/08ccd81ed3749b5fb5bf499a3b72463e4c71c9c1/files-data-and-oop/fahrtenbuecher/H-EL-99.csv'
# inhalt_fahrzeug_csv = urllib.request.urlopen(url_fahrzeug_csv,  allow_redirects=True)

with open(dateipfad_fahrzeug_csv) as datei_inhalt_fahrzeug_csv:
    for each_line in datei_inhalt_fahrzeug_csv.readlines(): # fileiterator holen...
        print(each_line) # mit iterator die datei zeilenweise iterieren


#         with open(filename) as f:
# for line in f.readlines():
# process(line)
