import csv, sqlite3

con = sqlite3.connect('pokemon.db')

    


with open('pokemon.csv', newline='', encoding='utf8') as csvfile:
    reader = csv.reader(csvfile)
    curseur=con.cursor()
    curseur.execute("""DROP TABLE IF EXISTS Pokemon""")
    curseur.execute("""
    CREATE TABLE IF NOT EXISTS Pokemon (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT,
    type1 TEXT,
    type2 TEXT,
    total INTEGER,
    hp INTEGER,
    attack INTEGER,
    defense INTEGER,
    sp_attack INTEGER,
    sp_defense INTEGER,
    speed INTEGER,
    generation INTEGER,
    legendary BOOLEAN)
    """)
    for line in list(reader)[1:] :
        print(line)
        req = f"""
    INSERT INTO Pokemon (name, type1, type2, total, hp,
    attack, defense,sp_attack, sp_defense, speed, generation, legendary
    ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?);
        """
        curseur.execute(req,line[1:] )
con.commit()
con.close()
        
