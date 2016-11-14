from flask import Flask, render_template, request
import datetime
from random import randrange
app = Flask(__name__)
#Numero oculto de endevina
hidden = randrange(1,99)

@app.route("/")
def main():
    return render_template('main.html')

from flask import render_template

@app.route('/calendario')
def calendario(name=None):
	contador = 1;
	today = datetime.date.today().day
	return render_template('calendario.html', dias=[today])

@app.route('/sudoku')
def sudoku(name=None):
	contador = 1;
	return render_template('sudoku.html', numeros={31:3,54:2,80:8})

@app.route('/endevina', methods=['GET', 'POST'])
def endevina():
	msg = "No has introducido un numero";
	global hidden
	print hidden
	if request.method == "POST":
		numero = request.form["number"]
		numero = int(numero)
		if hidden == numero:
			msg = 'Felicidades, has acertado el numero, otro numero es generado'
			hidden = randrange(1,99)
			print hidden
		else:
			if(hidden>numero):
				msg = 'El numero es mayor'
			else:
				msg = 'El numero es menor'
	
	return render_template('endevina.html', mensaje = msg)


if __name__ == "__main__":
    app.run()
