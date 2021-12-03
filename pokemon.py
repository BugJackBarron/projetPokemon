from flask import Flask, render_template
import sqlite3

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def homepage():
        con = sqlite3.connect('pokemon.db')
        curs = con.cursor()
        requ = """ SELECT DISTINCT type1
FROM Pokemon
ORDER BY type1;"""
        curs.execute(requ)
        rows = curs.fetchall()
        typeList = ""
        for r in rows :
            typeList +=r[0]
        
        return render_template('homepage.html', typeList = typeList)

    @app.route('/singlePokemon/')
    @app.route('/singlePokemon/<name>')
    def singlePokemon(name=''):        
        return render_template('singlePokemon.html', name=name)

    return app

if __name__=="__main__" :
    app=create_app()
    app.run(debug=True)