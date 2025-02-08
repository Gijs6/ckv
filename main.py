from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/")
def index():
    with open("paglijst.json", "r") as file:
        paglijst = json.load(file)
    return render_template("ckvhome.html", pagdata=paglijst)

@app.route("/over-mij")
def over_mij():
    return render_template("ckvovermij.html")

@app.route("/introductielessen")
def introductie():
    return render_template("ckvintro.html")

@app.route("/eigen-initiatieven")
def eigen_initiatieven():
    return render_template("ckvei.html")

@app.route("/blok-1")
def blok1():
    return render_template("ckvb1.html")

@app.route("/blok-2")
def blok2():
    return render_template("ckvb2.html")

@app.route("/blok-3")
def blok3():
    return render_template("ckvb3.html")

@app.route("/blok-4")
def blok4():
    return render_template("ckvb4.html")


@app.errorhandler(404)
def not_found(e):
    return render_template("ckv404.html", e=e), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('ckv500.html', e=e), 500
