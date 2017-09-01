from flask import Flask, render_template, request
from random import choice
from matches import check, solve
app = Flask(__name__)

@app.route('/home', methods = ['POST', 'GET'])

def show_page():
    equation = equation if 'equation'in locals() else choice(open('examples.tsv', 'r').read().split('\t'))
    if request.method == 'POST':
        solution = request.form['solution']
        return "Correct" if(solve(equation)==solution) else solve(equation) 
    else:
        return render_template("home.html", equation = equation)

if __name__ == "__main__":
    app.run(debug = True)
