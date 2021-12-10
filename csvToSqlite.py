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
    imageName TEXT,
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
        if " "in line[1] :
            splited = line[1].split(" ")
            print(splited)
            for t in splited[1: ] :
                
                if len(t)>1 and t in splited[0] :
                    newl = splited[0].split(t)[-1]
                    name = newl+" "+" ".join(splited[1:])
                    imgname = "-".join(name.split(" "))
        else :
                name= line[1]
                imgname= line[1]
        req = f"""
    INSERT INTO Pokemon (name, imagename, type1, type2, total, hp,
    attack, defense,sp_attack, sp_defense, speed, generation, legendary
    ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?);
        """
        curseur.execute(req,[name.lower(),imgname.lower(), *line[2:]] )
con.commit()
con.close()
        
