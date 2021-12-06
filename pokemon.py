from flask import Flask, render_template, request, url_for, redirect, flash
import sqlite3

def create_app():
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

    @app.route('/')
    def homepage(message=""):
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
        requ = """ SELECT DISTINCT generation
FROM Pokemon
ORDER BY generation;"""
        curs.execute(requ)
        rows = curs.fetchall()
        genList = []
        for r in rows :
            genList.append(r[0])
            
        
        return render_template('homepage.html', message = message, typeList = typeList, genList=genList)

    @app.route('/singlePokemon/')
    @app.route('/singlePokemon/<name>')
    def singlePokemon(name=''):        
        return render_template('singlePokemon.html', name=name)
    
    @app.route('/searchUnique',methods = ['POST', 'GET'])
    @app.route('/searchUnique/<name>')
    def searchUnique(name="") :
        print(f"Le nom : {name}")
        if name =="" :
            if request.method == 'POST' :
                if request.form.get('nom') :
                    pokeName = request.form['nom'].capitalize()
            else :
                if request.args.get('name') :
                    pokeName = request.args['name'].capitalize()
                else :
                    flash("Erreur dans la recherche")
                    return redirect(url_for('homepage'))
        else :            
            pokeName = name        
        conn = sqlite3.connect('static/pokemon.db')
        curs = conn.cursor()
        requ = f""" SELECT * FROM Pokemon WHERE name='{pokeName}'"""
        curs.execute(requ)
        pokeData = curs.fetchone()
        conn.close()
        if pokeData==None :
            flash('Pokemon Inconnu')
            return redirect(url_for('homepage'))
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
            type1 = request.form.get('type1')
            print(str(type1))
            type2 = request.form.get('type2')
            gen = request.form.get('gen')
            legendary = request.form.get('legendary')
            req = f""" SELECT name, generation, legendary FROM Pokemon WHERE """
            conditions=[]
            if request.form.get('type1') :               
                conditions.append(f"""type1 = '{type1.capitalize()}'""")
            if request.form.get('type2') :               
                conditions.append(f"""type2 = '{type2.capitalize()}'""")
            if request.form.get('gen') :               
                conditions.append(f"""generation = '{gen}'""")
            if request.form.get('legendary') :               
                conditions.append(f"""legendary = '{legendary}'""")
            req+= " AND ".join(conditions)    
            req+= " ORDER BY name ASC"            
            conn = sqlite3.connect('static/pokemon.db')
            curs = conn.cursor()
            curs.execute(req)
            listePokemon = curs.fetchall()
            conn.close()            
            if  len(listePokemon) != 0 :
                return render_template('multiplePokemon.html', listePokemon = listePokemon, type1=type1, type2=type2, gen=gen, legendary=legendary)
        flash('Aucun Pokemon ne correspond aux critères')
        return redirect(url_for('homepage'))
    return app

    

if __name__=="__main__" :
    app=create_app()
    app.run(debug=True)