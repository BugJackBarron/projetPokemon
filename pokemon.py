from flask import Flask, render_template, request, url_for
import sqlite3

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def homepage():
        con = sqlite3.connect('static/pokemon.db')
        curs = con.cursor()
        requ = """ SELECT DISTINCT type1
FROM Pokemon
ORDER BY type1;"""
        curs.execute(requ)
        rows = curs.fetchall()
        typeList = []
        for r in rows :
            typeList.append(r[0])
        
        return render_template('homepage.html', message = '', typeList = typeList)

    @app.route('/singlePokemon/')
    @app.route('/singlePokemon/<name>')
    def singlePokemon(name=''):        
        return render_template('singlePokemon.html', name=name)
    
    @app.route('/searchUnique',methods = ['POST', 'GET'])
    def searchUnique() :
        if request.method == 'POST' :
            if request.form.get('nom') :
                pokeName = request.form['nom'].capitalize()
                conn = sqlite3.connect('static/pokemon.db')
                curs = conn.cursor()
                requ = f""" SELECT * FROM Pokemon WHERE name='{pokeName}'"""
                curs.execute(requ)
                pokeData = curs.fetchone()
                conn.close()
                if pokeData==None :                    
                    return render_template('homepage.html', message = 'Pokemon inconnu')
                num, nom, type1, type2, total, hp, attack, defense, sp_attack, sp_defense, speed, generation, legendary = pokeData
                return  render_template('singlePokemon.html',
                                        nom = nom,
                                        type1 =type1,
                                        type2 = type2,
                                        total = total,
                                        hp = hp,
                                        attack = attack,
                                        defense = defense,
                                        sp_attack = sp_attack,
                                        sp_defense = sp_defense,
                                        speed = speed,
                                        generation = generation,
                                        legendary = legendary)
            
    @app.route('/searchMultiple', methods=['GET', 'POST'])
    def searchMultiple() :
        if request.method == 'POST' :
            if request.form.get('type1') :
                type1 = request.form.get('type1')
                req = f""" SELECT name, generation, legendary FROM Pokemon WHERE type1 = '{type1.capitalize()}'"""
                if request.form.get('type2') :
                    req += f"""AND type2 = '{request.form.get('type2').capitalize()}'"""
                req+= "ORDER BY name ASC"
                print(req)
                conn = sqlite3.connect('static/pokemon.db')
                curs = conn.cursor()
                curs.execute(req)
                return   render_template('multiplePokemon.html', listePokemon = curs.fetchall())   
        return 'Toto'

    return app

    

if __name__=="__main__" :
    app=create_app()
    app.run(debug=True)