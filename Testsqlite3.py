import sqlite3

connection= sqlite3.connect('test.db')

curseurr = connection.cursor()
curseurr.execute("""
DROP TABLE IF EXISTS Sport;
""")
curseurr.execute("""
CREATE TABLE Sport
(
    id_sport INTEGER PRIMARY KEY,
    nom_sport VARCHAR(30)
);
""")
curseurr.execute("""
INSERT INTO Sport
VALUES (1, 'ARCHERY'),
       (2, 'ATHLETICS'),
       (3, 'BADMINTON'),
       (4, 'BASKETBALL'),
       (5, 'BEACH VOLLEYBALL'),
       (6, 'BOXING'),
       (7, 'CANOE SLALOM'),
       (8, 'CANOE SPRINT'),
       (9, 'CYCLING BMX'),
       (10, 'CYCLING MOUNTAIN BIKE'),
       (11, 'CYCLING ROAD'),
       (12, 'CYCLING TRACK'),
       (13, 'DIVING'),
       (14, 'EQUESTRIAN'),
       (17, 'FENCING'),
       (18, 'FOOTBALL'),
       (19, 'GOLF'),
       (20, 'GYMNASTICS ARTISTIC'),
       (21, 'GYMNASTICS RHYTHMIC'),
       (22, 'HANDBALL'),
       (23, 'HOCKEY'),
       (24, 'JUDO'),
       (25, 'MODERN PENTATHLON'),
       (26, 'ROWING'),
       (27, 'RUGBY'),
       (28, 'SAILING'),
       (29, 'SHOOTING'),
       (30, 'SWIMMING'),
       (31, 'SYNCHRONIZED SWIMMING'),
       (32, 'TABLE TENNIS'),
       (33, 'TAEKWONDO'),
       (34, 'TENNIS'),
       (35, 'TRAMPOLINE'),
       (36, 'TRIATHLON'),
       (37, 'VOLLEYBALL'),
       (38, 'WATER POLO'),
       (39, 'WEIGHTLIFTING'),
       (40, 'WRESTLING');
""")
connection.commit()