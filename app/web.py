from flask import Flask, render_template, request, session, flash
from random import choice
from lib.matches import solve, ALL_EQUATIONS

app = Flask(__name__)
app.secret_key = "Strong enough"

@app.route('/', methods = ['POST', 'GET'])

def show_page():
    if request.method == 'POST':
        return("Correct" if(request.form['solution'] in solve(session.get('equation'))) else "Incorrect")
    else:
        session['equation'] = choice(ALL_EQUATIONS)
        return render_template("home.html", equation = session.get('equation'), solution = solve(session.get('equation')))

@app.route('/solution', methods = ['POST'])

def check_solution():
    return render_template("home.html", equation = session.get('equation'), solution = solve(session.get('equation')))

    #return(solve(session['equation']))


if __name__ == "__main__":
    app.run(debug = True)
