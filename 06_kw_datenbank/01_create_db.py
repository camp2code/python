import sqlite3

# erstellt eine datenbank und gibt die verbindung zur erstellten datenbank zurueck.
# ./ -> relative pfadangabe, hier: db im selben verzeichnis anlegen wie skript
db_connection = sqlite3.connect("./fuhrpark.db")


# SQL-Anweisungen - generiere Tabellen 
# tabelle fahrzeug
sql_create_fahrzeug_tabelle = """CREATE TABLE IF NOT EXISTS fahrzeug (
        id    INTEGER,
        marke       varchar(50),
        kennzeichen varchar(10),
        fahrgestellnr TEXT,
        baujahr            INTEGER,
        erstzulassung INTEGER,
        PRIMARY KEY(id))"""

# tabelle 
# privat - boolean -> INTEGER -> 0 == false; 1 == true.
sql_create_fahrtenbuch_tabelle =  """CREATE TABLE IF NOT EXISTS fahrtenbuch (
        id INTEGER,
        kennzeichen varchar(10),
        datum INTEGER,
        startkm INTEGER,
        endkm INTEGER,
        startort TEXT,
        zielort TEXT,
        privat INTEGER,
        PRIMARY KEY(id))"""

# lege die die tabellen an
db_connection.execute(sql_create_fahrzeug_tabelle)
db_connection.execute(sql_create_fahrtenbuch_tabelle)


# schliesse die verbidung
db_connection.close