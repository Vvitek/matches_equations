from flask import Flask, render_template, request, session, flash, jsonify
from random import choice
from lib.matches import solve, ALL_EQUATIONS

app = Flask(__name__)
app.secret_key = "Strong enough"

@app.route('/', methods = ['POST', 'GET'])

def show_page():
    session['equation'] = choice(ALL_EQUATIONS)
    return render_template("home.html", equation = session.get('equation'), solution = solve(session.get('equation')))

@app.route('/solution', methods = ['GET'])
def check_solution():
    return(jsonify(solve(session['equation'])))

@app.route('/equation', methods = ['GET'])
def return_solution():
    session['equation'] = choice(ALL_EQUATIONS)
    return(session['equation'])

if __name__ == "__main__":
    app.run(debug = True)
