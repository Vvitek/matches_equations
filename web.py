from flask import Flask, render_template, request, session, flash
from random import choice
from matches import check, solve, ALL_EQUATIONS#, COORDINATES, SIGNS2
app = Flask(__name__)
app.secret_key = "Strong enough"

@app.route('/home', methods = ['POST', 'GET'])

def show_page():
    if request.method == 'POST':
        jsdata = request.form['javascript_data']
        return("Correct" if(solve(session.get('equation'))==request.form['solution']) else "Incorrect") 
    else:
        session['equation'] = choice(ALL_EQUATIONS)
        return render_template("home.html", equation = session.get('equation'))

if __name__ == "__main__":
    app.run(debug = True)
