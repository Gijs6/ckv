from flask import Flask, render_template, url_for, redirect, send_from_directory
import json


app = Flask(__name__)



# Redirecters

@app.route("/")
def redirecthome():
    return redirect(url_for('home')), 301


@app.route('/<path:path>')
def redirecter(path):
    if path in ["favicon", "security", "robots"]:
        return redirect(f"/{path}")
    elif not path.startswith("gijsckv"):
        return redirect(f"/gijsckv/{path}")
    return render_template("ckv404.html", e="Error redirecting"), 404



# File stuff

@app.route('/favicon.ico')
@app.route('/favicon')
def favicon():
    return send_from_directory('static', "favs/cirkels.ico", mimetype='image/vnd.microsoft.icon')

@app.route("/.well-known/security.txt")
def securitytxt():
    return send_from_directory('static', "security.txt", mimetype="text/plain")

@app.route("/security.txt")
def securitytxtredirect():
    return redirect(url_for('securitytxt')), 301

@app.route("/robots")
@app.route("/robots.txt")
def robots():
    return send_from_directory("static", "robots.txt", mimetype="text/plain")



# Pages

@app.route("/gijsckv")
def home():
    with open("/data/paglijst.json", "r") as file:
        paglijst = json.load(file)
    return render_template("ckvhome.html", pagdata=paglijst)

@app.route("/gijsckv/over-mij")
def over_mij():
    return render_template("ckvovermij.html")

@app.route("/gijsckv/introductielessen")
def introductie():
    return render_template("ckvintro.html")

@app.route("/gijsckv/eigen-initiatieven")
def eigen_initiatieven():
    return render_template("ckvei.html")

@app.route("/gijsckv/blok-1")
def blok1():
    return render_template("ckvb1.html")

@app.route("/gijsckv/blok-2")
def blok2():
    return render_template("ckvb2.html")

@app.route("/gijsckv/blok-3")
def blok3():
    return render_template("ckvb3.html")

@app.route("/gijsckv/blok-4")
def blok4():
    return render_template("ckvb4.html")

@app.route("/gijsckv/colofon")
def colofon():
    return render_template("ckvcolofon.html")



# Error pages

@app.errorhandler(404)
def not_found(e):
    return render_template("ckv404.html", e=e), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('ckv500.html', e=e), 500
