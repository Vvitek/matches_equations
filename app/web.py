from flask import Flask, render_template, request, session, flash
from random import choice
from lib.matches import check, solve, ALL_EQUATIONS, solve2#, COORDINATES, SIGNS2
app = Flask(__name__)
app.secret_key = "Strong enough"

@app.route('/', methods = ['POST', 'GET'])

def show_page():
    if request.method == 'POST':
        return("Correct" if(solve(session.get('equation'))==request.form['solution']) else "Incorrect") 
        #return("Correct" if(request.form['solution'] in solve2(session.get('equation'))) else "Incorrect")
    else:
        session['equation'] = choice(ALL_EQUATIONS)
        return render_template("home.html", equation = session.get('equation'), solution = solve(session.get('equation')))

if __name__ == "__main__":
    app.run(debug = True)
